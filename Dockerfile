# Base python image
FROM nvidia/cuda:11.0-base

# To install python
RUN apt-get update && \
    apt-get install python3

# To install pip
RUN apt-get install -y python-pip && \
    pip install --upgrade pip

# Set the working directory to /src in the container
WORKDIR /

# Update the system

# To copy requirements.txt 
COPY ./src/requirements.txt .

# To install dependencies
RUN pip install -r requirements.txt

# COPY everything from project directory in repo to /project directory in the docker image
COPY . .

# To use Python version 3 for execution
ENTRYPOINT ["python3"]

# To change directory to src
RUN cd /src

# To run app.py application by python3
CMD [ "app.py" ]
