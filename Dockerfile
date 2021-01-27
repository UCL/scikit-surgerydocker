# Base python image
FROM nvidia/cuda:11.0-base

# To install python
RUN apt-get install software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.6

# To install pip
RUN apt-get install -y python3-pip && \
    pip3 install --upgrade pip

# Set the working directory to /src in the container
WORKDIR /

# Copy the requirements.txt to the image
COPY src/requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# COPY everything from project directory in repo to /project directory in the docker image
COPY . .

# To use Python version 3 for execution
# ENTRYPOINT ["python3"]

# To change directory to src
RUN cd /src

# To run app.py application by python3
CMD ["python3", "app.py"]
