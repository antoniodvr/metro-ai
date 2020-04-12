<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/antoniodvr/metro-ai">
    <img src="images/logo.png" alt="Logo" width="96" height="96">
  </a>

  <h3 align="center">metro-ai</h3>

  <p align="center">
    A simple Object Detection API with OpenCV and YOLO v3 using a pre-trained model.
    <a href="https://github.com/antoniodvr/metro-ai/blob/master/README.md">
    <br />
    <strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#usage">View Usage</a>
    ·
    <a href="https://github.com/antoniodvr/metro-ai/issues">Report Bug</a>
    ·
    <a href="https://github.com/antoniodvr/metro-ai/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

A simple Object Detection API with OpenCV and YOLO v3 using a pre-trained model.

### Built With

* [Python](https://www.python.org/) 
* [pip](https://pip.pypa.io/en/stable/)



<!-- USAGE EXAMPLES -->
## Usage

Download YOLO v3:
```shell script
cd metro-ai/yolo
wget https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg?raw=true
wget https://github.com/pjreddie/darknet/blob/master/data/coco.names?raw=true
wget https://pjreddie.com/media/files/yolov3.weights
```

### As a library

```shell script
python metro-ai.py
```

### As a Docker container

```shell script
docker-compose up -d
```

### Make a prediction

Request: 
```shell script
curl.exe -X POST -F image=@human-dog.jpg http://localhost:5000/model/predict -v                    2028-09-14 04:00:00             3161
```

Response:
```json
{
    "network_execution_time": 2640,
    "predictions": [
        {
            "confidence": 0.9997827410697937,
            "detection_box": [
                0.20972222222222223,
                0.21458333333333332,
                0.8486111111111111,
                0.56875
            ],
            "label": "person",
            "label_id": 0
        },
        {
            "confidence": 0.9979773163795471,
            "detection_box": [
                0.5902777777777778,
                0.48125,
                0.8416666666666667,
                0.8041666666666667
            ],
            "label": "dog",
            "label_id": 16
        },
        {
            "confidence": 0.8539056777954102,
            "detection_box": [
                0.47638888888888886,
                0.45416666666666666,
                0.5083333333333333,
                0.5666666666666667
            ],
            "label": "frisbee",
            "label_id": 29
        }
    ]
}
```



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/antoniodvr/metro-ai/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Antonio Di Virgilio - [@antoniodvr](https://linkedin.com/in/antoniodvr)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/antoniodvr/metro-ai.svg?style=flat-square
[contributors-url]: https://github.com/antoniodvr/metro-ai/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/antoniodvr/metro-ai.svg?style=flat-square
[forks-url]: https://github.com/antoniodvr/metro-ai/network/members
[stars-shield]: https://img.shields.io/github/stars/antoniodvr/metro-ai.svg?style=flat-square
[stars-url]: https://github.com/antoniodvr/metro-ai/stargazers
[issues-shield]: https://img.shields.io/github/issues/antoniodvr/metro-ai.svg?style=flat-square
[issues-url]: https://github.com/antoniodvr/metro-ai/issues
[license-shield]: https://img.shields.io/github/license/antoniodvr/metro-ai.svg?style=flat-square
[license-url]: https://github.com/antoniodvr/metro-ai/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/antoniodvr
