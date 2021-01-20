# Base python image
FROM python:3.6

# Set the working directory to /src in the container
WORKDIR /

# Copy the requirements.txt to the image
COPY src/requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# COPY everything from project directory in repo to /project directory in the docker image
COPY . .

# To use Python version 3 for execution
ENTRYPOINT ["python3"]

# To run app.py application by python3
CMD [ "app.py" ]
