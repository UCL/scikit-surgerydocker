# scikit-surgerydocker
This repo describes with a simple example how to use docker to containerise your project/algorithm. Another relate project scikit-surgerychallange could be used to host an algorithm challange after containerizing the project/algorithm according to this repository.  

## Step 1: Running without Docker

Clone the repository
```
git clone git@github.com:UCL/scikit-surgerydocker.git
```
To run the python code
```
cd scikit-surgerydocker
python app.py
```
On execution the python program will (1) read the text file from provided input directory, (2) append more lines to the existing text and (3) store the whole text in a newly created file in output folder provided in the project. 
```
cd scikit-surgerydocker/output
cat file.txt
```


## Step 2: Containerise this application

Now before containerization of your package, first you need to know about few import terms.    
`docker host:` This is the machine on which docker is installed. E.g. in my case my mac     
`docker image:` The image will have everything defined that we want in out container. Just like Class in Object Oriented Programming.
`guest machine / docker container:` This is the container which will be created from docker image. Just like Object/Instance of a class in Object Oriented Programming.
`Docker Engine:` This is the docker software that you must INSTALL and ENABLE/RUN on your machine to run any docker command.

### Create a Docker image
To create a docker image, you will need a file called `Dockerfile`. It contains the specifications e.g. what Python version you want to run your python application with.
The directory structure should be like this 

![Directory Structure](./images/directory-structure.png)


Run the following command to create the image by the name `my-project`
```
cd scikit-surgerydocker
docker build . -t my-project
```
Run the following command to check that your docker image is created.
This command will show all the docker images you have on your docker host.
```
docker images
```

### Running the created image
After you have containerize your python application, you would like to run it :)
```
cd scikit-surgerydocker
docker run \
    -v "$PWD/input:/project/input" 
    -v "$PWD/output:/project/output" 
    my-project
```
In the above command,      
`my-project` is the image name.     
`-v "$PWD/input:/project/input"` This parameter will mount the `scikit-surgerydocker/input` directory from docker host to `/project/input` directory in the container to make the input file availabe to our python `app.py` when executed in the container.      
`-v "$PWD/output:/project/output"` This will mount the `scikit-surgerydocker/output` directory from docker host to `/project/output` directory in the container. So when the `app.py` application on execution write to `/project/output` in the container, we will automatically get it on docker host in `scikit-surgerydocker/output` because of the mount.

### Checking the output
To verify the processing performed in the container after executing the above run command. On docker host
```
cd scikit-surgerydocker
cd output
cat file.txt
```

### Step 3 how to package your image for sharing
If you would like to submit your docker image containing your Python application to a challange then two common ways are

#### 3.1 Compress the image and upload it to cloud drive
```
# You dont need to be in scikit-surgerydocker directory. 
# The following command will work from any where

docker save my-project:team1 > my-project-team1.tar
```
This command will create the tar file of the image in the current directory by the name `my-project-team1.tar`.   

Now you can upload this tar file to the cloud drive (Google drive, Drop box, One drive etc) and you can share it with any one you want.

#### 3.2 Upload it docker hub










