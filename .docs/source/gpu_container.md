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
git clone https://weisslab.cs.ucl.ac.uk/ThomasDowrick/stereo-recon-example.git
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
