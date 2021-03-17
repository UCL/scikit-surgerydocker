# Dockerizing a CPU program:
This is a hands on demo tutorial, showing how scikit-surgerydocker package could be used to dockerize the Python application.
In this demo we are dockerizing [cpu-ex](https://github.com/UCL/cpu-ex) program. 

## About cpu-ex program:
The cpu-ex is short for CPU-Example. It is called CPU-ex because it utilizes CPU for program execution. Check the repo [cpu-ex](https://github.com/UCL/cpu-ex) for more details. The cpu-ex is mimicing how a real world algorithm/program will perform on execution i.e. 

1. Read the input file `input_file.txt` from the `cpu-ex/input_data` directory
1. Process it (Append more lines to the existing text in this case).
1. Store the output in newly created file `output_file.txt` in `cpu-ex/output_data`.

## Preliminary requirements:
Before starting make sure that you meet the software and hardware requirement.

### Software Requirements:
#### Windows:
On Windows operating system, you need to have
##### Docker
Docker is a free software. To download, install, configure and test it on windows check [here](https://hub.docker.com/editions/community/docker-ce-desktop-windows).
##### Gitbash
Gitbash is another free lightweight tool that provides a BASH emulation to run git from the command line. To download gitbash for windows click [here](https://gitforwindows.org/).

#### Linux and Mac:
On both Linux and Mac, all you need is docker installed and running.
##### Docker
To install Docker on Linux check [here](https://docs.docker.com/get-docker/).   
To install Docker on Mac check [here](https://docs.docker.com/docker-for-mac/install/)


### Hardware Requirements:
There is no specific hardware requirement to run this example.


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
git clone https://github.com/UCL/cpu-ex.git
```
Now the temp directory will have the following structure
```
temp
├── cpu-ex
│   ├── docs
│   │   └── source
│   ├── input
│   ├── src
│   └── tests
│       └── data
└── scikit-surgerydocker
    ├── input_data
    ├── output_data
    └── src
```

## Step 2: Copy the code
Second step is to copy the application/algorithm code from your project (cpu-ex) to scikit-surgerydocker
```
cp -r cpu-ex/src/* scikit-surgerydocker/src/
```

## Step 3: Copy the input data
Third step is to copy the input data to `scikit-surgerydocker/input_data` directory. In cpu-ex project the input data is stored in `cpu-ex/input_data` directory. 
```
cp -r cpu-ex/input_data/* scikit-surgerydocker/input_data/
```

## Step 4: Containerize the application

To containerise the project a `Dockerfile` is provided in the scikit-surgerydocker. It contains the specifications required for standard Python 3.6 application e.g. the specific Python version needed to run the program and any dependant packages needed to run the application. Please read the `Dockerfile` in the repo for further information. Feel free to modify the `Dockerfile` according to your environment.

Run the following command to create a docker image with the name `my-project`.    

**Note:** The following command will only work if you are in the directory where the `Dockerfile` is saved. In our case `Dockerfile` is in the `scikit-surgerydocker/' root directory.   

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

The newly created `my-project` image will have Ubuntu 18.04 as base operating system. It will be able to identify and use the installed Nvidia driver on host machine. It will also have CUDA version 11.1.1 available to use. Beside the basic software Python 3.6 is installed in the image to execute the example application. It will also have any packages mentioned in the requirements.txt that are required by the example application to run properly.

## Step 5: Execution of image

After you have containerized your Python application, you can run it on your computer for testing before sharing with others.
In the example we know that the input data is stored in `scikit-surgerydocker/input_data` and the program will write results to `scikit-surgerydocker/output_data`. 

The following command will create a new `container` from image `my-project`.

```
# On Linux/Mac
cd scikit-surgerydocker
docker run -v "$PWD/input_data:/usr/program/input_data" -v "$PWD/output_data:/usr/program/output_data" my-project

# On Windows (using gitbash)
cd scikit-surgerydocker
docker run -v "/$PWD/input_data:/usr/program/input_data" -v "/$PWD/output_data:/usr/program/output_data" my-project
```

In the above command,  
`my-project` is the docker image name.  
`-v "$PWD/input_data:/usr/program/input_data"` This parameter will mount the `scikit-surgerydocker/input_data` directory from docker host to `/usr/program/input_data` directory in the container to make the input file availabe to our python `app.py` when executed in the container.  
`-v "$PWD/output_data:/usr/program/output_data"`. This will mount the `scikit-surgerydocker/output_data` directory from docker host to `/usr/program/output_data` directory in the container. So the `app.py` application on execution will write to `/usr/program/output_data` in the container and we will automatically get it on docker host in `scikit-surgerydocker/output_data` because of the mount.

**NOTE:** The docker container will exit after running the app.py script. It is normal for docker to stop the conainer automatically after executing the job.

## Step 6: Verifying container

You can verify the newly created container by running the following command on docker host.

```
docker ps -a
```

Check the status column, which should show `Exited`, as the container exits after the script has been run. In our case, its job was to read text from input file and append text with it and write to output file.


# Step 7: Checking the output

To verify the processing performed in the container after executing the above run command. On docker host

```
cd scikit-surgerydocker/
cd output_data
cat output_file.txt
```

