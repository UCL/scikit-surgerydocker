# Base python image
FROM nvidia/cuda:11.1.1-devel-ubuntu18.04

# To uninstall default python 3.8 and install python 3.6

RUN apt-get update && \
    apt-get install -y python3.6

# To install pip
RUN apt-get install -y python3-pip && \
    pip3 install --upgrade pip

# OS level dependencies
# RUN apt-get install ffmpeg libsm6 libxext6 -y

# Set the working directory to /src in the container
WORKDIR /usr/program

# Copy the requirements.txt to the image
COPY src/requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# COPY everything from project directory in repo to /project directory in the docker image
COPY . .

# To use Python version 3 for execution
# ENTRYPOINT ["python3"]

# To change directory to src
WORKDIR /usr/program/src

# To run app.py application by python3
CMD ["python3", "app.py"]
