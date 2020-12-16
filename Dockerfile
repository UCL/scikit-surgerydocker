# Base python image
FROM python:3.6

# COPY everything from current directory to /project directory in the docker image
COPY ./project /

# Make /project directory in the image and cd into it when it runs as container
WORKDIR /project

# To use Python version 3 for execution
ENTRYPOINT ["python3"]

# To run app.py application by python3
CMD [ "app.py" ]

