# Base python image
FROM nvidia/cuda:11.0-base

# To install python
RUN apt-get update && \
    apt-get install -y build-essential checkinstall && \
    apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev 

RUN apt-get install -y wget

RUN cd /usr/src && \
    wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz && \
    tar xzf Python-3.6.9.tgz && \
    cd Python-3.6.9 && \
    ./configure --enable-optimizations && \
    make altinstall

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
