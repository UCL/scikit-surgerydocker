# Base python image
FROM python:3.6

# Set the working directory to /src in the container
WORKDIR /src

# COPY everything from project directory in repo to /project directory in the docker image
COPY ./src/ .

# To use Python version 3 for execution
ENTRYPOINT ["python3"]

# To run app.py application by python3
CMD [ "app.py" ]
