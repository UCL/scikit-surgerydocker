# Dockerizing a CPU program:
This is a hands on demo tutorial, showing how scikit-surgerydocker package could be used to dockerize a Python application.
In this demo we are dockerizing [cpu-ex](https://github.com/UCL/cpu-ex) program. 

## About cpu-ex program:
The cpu-ex is short for CPU-Example. It is called CPU-ex because it utilizes only CPU for program execution. Check the repo [cpu-ex](https://github.com/UCL/cpu-ex) for more details. The cpu-ex is emulating how a real world algorithm/program will perform on execution i.e. 

1. Create required environment by installing dependencies
1. Start program execution
1. Read input file `input_file.txt` from `cpu-ex/input_data` directory
1. Process it (Append more lines to the existing text in this case).
1. Store the output in newly created file `output_file.txt` in `cpu-ex/output_data`.

## Preliminary requirements:
Before starting make sure that you meet the software and hardware requirement.

### Software Requirements:
#### Windows:
On Windows operating system, you need to have the following: 
##### Docker
Docker is a free software. To download, install, configure and test it on windows check [here](https://hub.docker.com/editions/community/docker-ce-desktop-windows).
##### Gitbash
Gitbash is another free lightweight tool that provides a BASH emulation to run git from the command line. To download Gitbash for Windows click [here](https://gitforwindows.org/).

#### Linux and Mac:
On both Linux and Mac, all you need is docker installed and running.
##### Docker
To install Docker on Linux check [here](https://docs.docker.com/get-docker/).   
To install, configure and start Docker on Mac check [here](https://docs.docker.com/docker-for-mac/install/). 


### Hardware Requirements:
There is no specific hardware requirement to run this example. If Docker and Gitbash are installed then any standard computer should run this example.


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
To clone the project `cpu-ex` to containerize:
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

To containerize the project a `Dockerfile` is provided in the scikit-surgerydocker. It contains the specifications required for standard Python 3.6 application e.g. the specific Python version needed to run the program and any dependant packages needed to run the application. Please read the `Dockerfile` in the scikit-surgerydocker repo for further information. Feel free to modify the `Dockerfile` according to your environment.

Run the following command to create a docker image with the name `my-project`.    

**Note:** The following command will only work if you are in the directory where the `Dockerfile` exists. In our case `Dockerfile` is in the `scikit-surgerydocker/' root directory of the project.   

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

The newly created `my-project` image will have Ubuntu 18.04 as base operating system. It will be able to identify and use the installed Nvidia driver on host machine. It will also have CUDA version 11.1.1 available to use. Python 3.6 is installed in the image to execute the example application. It will also have any packages mentioned in the requirements.txt that are required by the example application to run properly.

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
`-v "$PWD/input_data:/usr/program/input_data"` This parameter will mount the `scikit-surgerydocker/input_data` directory from docker host to `/usr/program/input_data` directory in the container to make the input file available to our python `app.py` when executed in the container.  
`-v "$PWD/output_data:/usr/program/output_data"`. This will mount the `scikit-surgerydocker/output_data` directory from docker host to `/usr/program/output_data` directory in the container. So the `app.py` application on execution will write to `/usr/program/output_data` in the container and we will automatically get it on docker host in `scikit-surgerydocker/output_data` because of the mount.

**NOTE:** The docker container will exit after running the app.py script. It is normal for docker to stop the container automatically after executing the job.

## Step 6: Verifying container

You can verify the newly created container by running the following command on docker host.

```
docker ps -a
```

Check the status column, which is now in status `Exited`, as the container exits after the script has been run. In our case, its job was to read text from input file and append text with it and write to an output file.

## Step 7: Checking the output

To verify the processing performed in the container after executing the above run command. On docker host

```
cd scikit-surgerydocker/
cd output_data
cat output_file.txt
```

## Step 8: Upload image to dockerhub
To share the newly created docker image `my-project` we could make use of free service dockerhub. Following are the steps to upload the docker image to to dockerhub.

### Compress image:
The following command will create a compressed `.tar` file of the image in the current directory by the name `my-project.tar`.
```
docker save my-project > my-project.tar
```

### Upload to dockerhub

One of the docker registries where you can upload your created and compressed image `my-project.tar` is [docker hub](https://hub.docker.com/). You need to have an account on the dockerhub. To sign up to docker hub visit [here](https://hub.docker.com/signup).

1. Create a free account on docker hub.
2. Login to docker hub account online.
3. Create a repository
   1. Give a name, better to give same name as image name e.g. `my-project` in our case.
   2. Give a description
   3. Click Create.
4. Now on docker host login to your docker hub account from terminal by the following command and providing the password when requested.

```
# There are multiple ways to provide the password. I am using the environment variable one.
# First you need to create an environment variable and assign your password 
MY_PASSWORD="give_your_password"

# Now run the following command to login to docker hub from terminal
echo "$MY_PASSWORD" | docker login --username <username> --password-stdin
```

5. Now you need to tag your image with your docker hub login name.
   1. To tag the image, you need to know the image name
   2. After finding the ID you can tag the image

```
# To find the image name list all the images
docker images

# To tag the image with your docker hub login name
docker tag my-project yourdockerhubaccount/my-project
```

6. Now you can upload the tagged image to docker hub. It will take time in uploading depending on the size of the image.

```
docker push yourgithubusername/my-project:latest
```

Now you can verify the image online in your dockerhub account.

## Step 9: Clean the environment (Optional)

To delete all the containers and images on the computer to free-up space run the following commands.

**NOTE:** The following commands will delete all the images and containers so if you have any existing images or containers that you do not want to delete then do not run these commands.

To delete all the containers
```
docker rm -f $(docker ps -a -q)
```

To delete all the images 
```
docker rmi -f $(docker images -a -q)
```