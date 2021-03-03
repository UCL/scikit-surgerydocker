FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3.6
RUN apt-get install -y python3-pip && pip3 install --upgrade pip
RUN apt install -y ffmpeg
RUN apt install -y libsm6
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /usr/program/src
CMD ["python3", "app.py"]
