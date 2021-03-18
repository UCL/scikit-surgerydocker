# Dockerizing a GPU program:
This is a hands on demo tutorial, showing how scikit-surgerydocker package could be used to dockerize the Python application.
In this demo we are dockerizing [stereo-recon-example](https://weisslab.cs.ucl.ac.uk/ThomasDowrick/stereo-recon-example) program that needs a GPU on the host computer (computer running docker) and Nvidia Driver installed.

## About stereo-recon-example program:
The program is modified code of [keras-flask-deploy-webapp](https://github.com/mtobeiyf/keras-flask-deploy-webapp) to make it work with the PSMNet model, and predict disparity maps from left/right images.

## Preliminary requirements:
Before starting make sure that you meet the software and hardware requirement.
### Software Requirements:
#### On Linux
On Linux, the software you need are.
##### Docker
To install Docker on Linux check [here](https://docs.docker.com/get-docker/).   
##### NVIDIA driver 
You must have NVIDIA driver installed on the host machine according to the GPU model on your computer. To find the compatible NVIDIA and GPU click [here](https://www.nvidia.co.uk/Download/index.aspx?lang=en-uk).
##### NVIDIA Container runtime
The nvidia-container-runtime is an open-source tool that is needed by docker to use the hosts machine GPU. Run the following command to check whether nvidia-container-runtime is installed.
```
nvidia-container-cli info
```
If it is not installed then download and install it from [here](https://github.com/NVIDIA/nvidia-container-runtime).    

#### On Windows and Mac
Sharing GPU of host computer with docker is not possible on Windows and Mac till now. Therefore, this example will not work on Windows and Mac.

### Hardware Requirements:
Make sure that GPU is available on the Computer running docker.


## Step 0: Prepare the docker host
Docker host is the machine on which the docker is installed. To run the GPU program in docker you need to install [nvidia-container-runtime](https://nvidia.github.io/nvidia-container-runtime/). 
The steps for debian based distribution are
```
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

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
Since this application needs data from front-end (web interface) therefore no need of specifying input data here. So no action needed here.

## Step 4: Containerize the application

To containerise the project a `Dockerfile` is provided in the scikit-surgerydocker. The Dockerfile uses `nvidia/cuda:11.1.1-devel-ubuntu18.04` i.e. Ubuntu 18.04 as base operating system along with Nvidia and Cuda software. On the base image Python 3.6.9 and pip 3 is installed. The pip utility is used to install the packages required by the app and mentioned in the requirements.txt. Please read the `Dockerfile` in the repo for further information. Feel free to modify the `Dockerfile` according to your environment.

This particular example needs `ffmpeg, libsm6, libxext6` libraries installed in the Ubuntu 18.04, so you can install them in the image by adding the following line in `# OS level dependencies` section of the Dockerfile.
```
# Open the Dockerfile stored in scikit-surgerydocker
cd scikit-surgerydocker
nano Dockerfile

# Uncomment the following line (remove # at the start of the line.)
RUN apt-get install ffmpeg libsm6 libxext6 -y

# Save the changes and exit.
```

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

The newly created `my-project-2` image will have the Python version "3.6.9" specified in the `Dockerfile` and the dependencies installed and finally the source code.

## Step 5: Execution of image

After you have containerized your Python application, you can run it on your computer for testing before sharing with others.


The following command will create a new `container` from image `my-project-2`.

```
cd scikit-surgerydocker
docker run -p 5000:5000 --gpus all my-project-2 
```

In the above command,  
`my-project-2` is the docker image name.     

`-p 5000:5000` will expose port 5000 inside the container to port 5000 of the docker host.

`--gpus all` will use all the installed physical gpus used for running the application.

**NOTE:** The docker container will exit after running the app.py script. It is normal for docker to stop the conainer automatically after executing the job.

## Step 6: Access the front-end

If everything is working then after executing the command in step 5 the application should up and running. To access the application front-end, open the browser and go to address http://127.0.0.1:5000
