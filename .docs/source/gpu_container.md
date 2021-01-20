# Dockerizing a GPU program:
This is a hands on demo tutorial, showing how scikit-surgerydocker package could be used to dockerize the Python application.
In this demo we are dockerizing [stereo-recon-example](https://weisslab.cs.ucl.ac.uk/ThomasDowrick/stereo-recon-example) program.

## About stereo-recon-example program:
[stereo-recon-example](https://weisslab.cs.ucl.ac.uk/ThomasDowrick/stereo-recon-example) is modifed code of https://github.com/mtobeiyf/keras-flask-deploy-webapp to work
with the PSMNet model, and predict disparity maps from left/right images.


## Step1: Clone the projects
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
temp
├── scikit-surgerydocker
│   ├── input_data
│   ├── output_data
│   └── src
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
Now copy the application from `stereo-recon-example/` in the `scikit-surgerydocker/src` directory. 
```
cp -r stereo-recon-example/* scikit-surgerydocker/src/
```

## Step 3: Containerize the application

To containerise the project a `Dockerfile` is provided in the scikit-surgerydocker. It contains the specifications required for standard Python 3.6 application e.g. the specific Python version needed to run the program and any dependant packages needed to run the application. Please read the `Dockerfile` in the repo for further information. Feel free to modify the `Dockerfile` according to your environment.

Run the following command to create a docker image with the name `my-project`.  
**Note:** The following command will only work if you are in the directory where the `Dockerfile` is saved. In our case `Dockerfile` is in the `scikit-surgerydocker/' root directory.
**Note:** Please also make sure that [Docker](https://docs.docker.com/engine/) is installed and docker engine is running before executing the following command.

```
cd scikit-surgerydocker
docker build -t my-project .
```