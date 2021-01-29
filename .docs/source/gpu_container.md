# Dockerizing a GPU program:
This is a hands on demo tutorial, showing how scikit-surgerydocker package could be used to dockerize the Python application.
In this demo we are dockerizing [stereo-recon-example](https://weisslab.cs.ucl.ac.uk/ThomasDowrick/stereo-recon-example) program.

## About stereo-recon-example program:

## Step 1: Clone the projects
First step is to clone both the projects.

It is recommended to create a new directory.
```
# Make temp directory
mkdir temp
# Change directory to temp
cd temp
```
To clone scikit-surgerydocker:
```
git clone https://github.com/UCL/scikit-surgerydocker.git
```
To clone the project to containerise:
```
git clone --recursive https://weisslab.cs.ucl.ac.uk/ThomasDowrick/stereo-recon-example
```
Now the temp directory will have the following structure
```
.
├── scikit-surgerydocker
|   ├── input_data
|   ├── output_data
|   └── src
└── stereo-recon-example
    ├── PSMNet
    │   ├── dataloader
    │   ├── dataset
    │   ├── models
    │   ├── trained_models
    │   └── utils
    ├── data
    │   └── synthetic
    │       └── calib
    ├── static
    └── templates
```
## Step 2: Copy the code
Second step is to copy the application/algorithm code from your project (stereo-recon-example) to scikit-surgerydocker
```
cp -r stereo-recon-example/* scikit-surgerydocker/src/
```
## Step 3: Copy the input data
Since this application needs data from front-end therefore no need of specifying input data here. So no action needed here.

## Step 4: Containerize the application

To containerise the project a `Dockerfile` is provided in the scikit-surgerydocker. It contains the specifications required for standard Python 3.6 application i.e. the specific Python version needed to run the program and any dependant packages needed to run the application. Please read the `Dockerfile` in the repo for further information. Feel free to modify the `Dockerfile` according to your environment.

Run the following command to create a docker image with the name `my-project-2`.  
**Note:** The following command will only work if you are in the directory where the `Dockerfile` is saved. In our case `Dockerfile` is in the `scikit-surgerydocker/' root directory.
**Note:** Please also make sure that [Docker](https://docs.docker.com/engine/) is installed and docker engine is running before executing the following command.

```
cd scikit-surgerydocker
docker build -t my-project-2 .
```

**Note:** Dont forget the trailing . (dot) at the end of the above command.

Run the following command to check that your docker image is created.
This command will show all the docker images you have on your docker host including the newly created `my-project-2` Docker image.

```
docker images
```

The newly created `my-project-2` image will have the Python version "3.6" specified in the `Dockerfile` and the dependencies installed (if any) and finally the source code.

## Step 5: Execution of image

After you have containerized your Python application, you can run it on your computer for testing before sharing with others.


The following command will create a new `container` from image `my-project-2`.

```
cd scikit-surgerydocker
docker run -p 5000:5000 --gpus all my-project-2 
```

In the above command,  
`my-project` is the docker image name.  
`-v "$PWD/input_data:/input_data"` This parameter will mount the `scikit-surgerydocker/input_data` directory from docker host to `/input_data` directory in the container to make the input file availabe to our python `app.py` when executed in the container.  
`-v "$PWD/output_data:/output_data"`. This will mount the `scikit-surgerydocker/output_data` directory from docker host to `/output_data` directory in the container. So the `app.py` application on execution will write to `/output_data` in the container, we will automatically get it on docker host in `scikit-surgerydocker/output_data` because of the mount.

**NOTE:** The docker container will exit after running the app.py script. It is normal for docker to stop the conainer automatically after executing the job.