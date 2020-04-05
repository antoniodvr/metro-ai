FROM ubuntu:18.04
ENV NETWORK_FOLDER=./yolo
COPY . /app
WORKDIR /app
RUN apt-get update -y && apt-get install -y python3-pip python3-dev libsm6 libxext6 libxrender-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]