# scikit-surgerydocker
This repo describes with a simple example how to use docker to containerize your project/algorithm. Another related project [scikit-surgerychallange](https://github.com/UCL/scikit-surgerychallenge) could be used to host an algorithm challange after containerizing the project/algorithm according to this repository.  

## Step 1: Running the project before dockerization

Clone the repository
```
git clone git@github.com:UCL/scikit-surgerydocker.git
```
To run the python application directly
```
cd scikit-surgerydocker
python3 app.py
```
On execution the python program will (1) read the text file `inputfile.txt` from provided `scikit-surgerydocker/input` directory, (2) append more lines to the existing text and (3) store the whole text in a newly created file `outputfile.txt` in `scikit-surgerydocker/output` directory provided in the project. You can check the `outputfile.txt`

```
cd scikit-surgerydocker/output
cat outputfile.txt
```


## Step 2: Containerise this application

Now before containerization of your package, first you need to know about few import terms.    
`docker host:` The term refers to the machine on which docker is installed. E.g. in my case my Mac machine is my docker host.    
`docker image:` The term docker image have everything defined which we want in out container. It is just like a Class in Object Oriented Programming which defines what properties and behaviours an object of the class will have.
`guest machine / docker container:` This is the container which is created from the docker image. It is just like a Object in Object Oriented Programming which contains all the properties and behaviours that are defined in a class.
`Docker Engine:` This is the docker software that you must INSTALL and ENABLE/RUN on your `docker host` to run any docker command. You can install `Docker Engine` by following this [link](https://docs.docker.com/desktop/).

### Create a Docker image
To create a docker image, you will need a file called `Dockerfile`. It contains the specifications e.g. What Python version you want to run your python application with etc. Please read the `Dockerfile` in the repo for further information.

The directory structure after the cloning the project: 

![Directory Structure](./images/directory-structure.png)

Run the following command to create the image by the name `my-project`. You can your image any thing you want.   
**Note:** The following command will only work if you are in the same directory where the `Dockerfile` is stored. In our case `Dockerfile` is in the root directory of the repo.
```
cd scikit-surgerydocker
docker build . -t my-project
```
Run the following command to check that your docker image is created.
This command will show all the docker images you have on your docker host including the newly created `my-project` Docker image.
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










