import os
import io
import time

import cv2
import numpy as np
from PIL import Image
from flask import Flask, request, Response, json
from werkzeug.exceptions import HTTPException


app = Flask(__name__)


class NetworkNotConfigured(HTTPException):
    code = 500
    name = 'NetworkNotConfigured'
    description = 'Network is not configured.'


def load_network(network_folder):
    """
    Load the Yolo network from disk.
    https://pjreddie.com/media/files/yolov3.weights
    https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg
    :param network_folder: folder where network files are stored
    """

    # Derive file paths and check existance
    labels_path = os.path.sep.join([network_folder, "coco.names"])
    if not os.path.isfile(labels_path):
        app.logger.error("NetworkError: Labels file \"{}\" not found.".format(labels_path))
        raise NetworkNotConfigured("Network is not configured")

    weights_path = os.path.sep.join([network_folder, "yolov3.weights"])
    if not os.path.isfile(weights_path):
        app.logger.error("NetworkError: Weights file \"{}\" not found.".format(weights_path))
        raise NetworkNotConfigured("Network is not configured")

    config_path = os.path.sep.join([network_folder, "yolov3.cfg"])
    if not os.path.isfile(config_path):
        app.logger.error("NetworkError: Configuration file \"{}\" not found.".format(config_path))
        raise NetworkNotConfigured("Network is not configured")

    # load YOLO object detector trained on COCO dataset (80 classes)
    # and determine only the *output* layer names that we need from YOLO
    # Network storend in Darknet format
    app.logger.info("loading YOLO from disk...")
    labels = open(labels_path).read().strip().split("\n")
    network = cv2.dnn.readNetFromDarknet(config_path, weights_path)
    names = network.getLayerNames()
    names = [names[i[0] - 1] for i in network.getUnconnectedOutLayers()]
    return network, names, labels


def execute_network(image, network, layernames):
    """
    Pull frame through the network
    :type image: RGB array
    :type network: object containing Yolo network
    :type layernames: array of layer names
    """

    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    start = time.time()
    network.setInput(blob)
    outputs = network.forward(layernames)
    network_execution_time = int((time.time() - start) * 1000)
    app.logger.info("YOLO  took      : %2.1f sec" % network_execution_time)
    return network_execution_time, outputs


def get_predictions(layer_outputs, threshold, img_width, img_height, labels):
    """
    Determine the objects as found by the network. Found objects are filtered
    on threshold.
    """

    # initialize our lists of prediction
    predictions = []

    for output in layer_outputs:
        # loop over each of the detections
        for detection in output:
            # extract the class ID and confidence (i.e., probability) of the current object detection
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # filter out weak predictions by ensuring the detected probability is greater than the minimum probability
            if confidence >= threshold:
                # scale the bounding box coordinates back relative to the size of the image
                box = detection[0:4] * np.array([img_width, img_height, img_width, img_height])
                (center_x, center_y, width, height) = box.astype("int")

                # use the center (x, y)-coordinates to derive the top left corner of the bounding box
                top_x = int(center_x - (width / 2))
                top_y = int(center_y - (height / 2))

                predictions.append(
                    {
                        'label_id': int(class_id),
                        'label': labels[class_id],
                        'confidence': float(confidence),
                        'detection_box': [int(top_x), int(top_y), int(width), int(height)]
                    }
                )

    return predictions


@app.route('/model/predict', methods=['POST'])
def predict():
    image = request.files["image"].read()

    threshold = 0.3
    if 'threshold' in request.args:
        threshold = float(request.args.get('threshold'))

    image = Image.open(io.BytesIO(image))
    frame = np.array(image).copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    (frame_height, frame_width) = frame.shape[:2]

    # Load the trained network
    network_folder = os.getenv('NETWORK_FOLDER', './yolo')
    (net, ln, labels) = load_network(network_folder)

    # Feed frame to network
    network_execution_time, layer_outputs = execute_network(frame, net, ln)

    # Obtain detected objects, including cof levels and bounding boxes
    predictions = get_predictions(layer_outputs, threshold, frame_width, frame_height, labels)

    response = {'network_execution_time': network_execution_time, 'predictions': predictions}
    return Response(response=json.dumps(response), status=200, mimetype="application/json")


@app.errorhandler(NetworkNotConfigured)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "name": e.name,
        "description": e.description
    })
    response.content_type = "application/json"
    return response


# start flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



