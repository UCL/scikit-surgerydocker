# Base python image
FROM python:3.6


# Make /project directory in the image and cd into it when it runs as container
WORKDIR /project

# COPY everything from current directory to /project directory in the docker image
COPY app.py /project

# To run the application when the container is created
ENTRYPOINT ["python3", "app.py"]

