# Containerize the application

To containerise the project a `Dockerfile` is provided in the scikit-surgerydocker. It contains the specifications required for your application e.g. the specific Python version needed to run the program and any dependant packages needed to run the application. Please read the `Dockerfile` in the repo for further information.

Run the following command to create a docker image with the name `my-project`.  
**Note:** The following command will only work if you are in the directory where the `Dockerfile` is saved. In our case `Dockerfile` is in the `scikit-surgerydocker' root directory.
**Note:** Please also make sure that [Docker](https://docs.docker.com/engine/) is installed and docker engine is running before executing the following command.

```
cd scikit-surgerydocker
docker build -t my-project .
```

**Note:** Dont forget the trailing . (dot) at the end of the above command.

Run the following command to check that your docker image is created.
This command will show all the docker images you have on your docker host including the newly created `my-project` Docker image.

```
docker images
```

The newly created `my-project` image will have the Python version "3.6" specified in the `Dockerfile` and the dependencies installed (if any) and finally the source code.
