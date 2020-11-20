# scikit-surgerydocker
This repo describes with a simple example how to use docker to containerise your project/algorithm 

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
On execution it will add a new text file to the output folder. 


## Step 2: Containerise this application

Now before containerization of your package, first you need to know about few import terms.    
`docker host:` This is the machine on which docker is installed. E.g. in my case my mac     
`docker image:` The image will have everything defined that we want in out container. Just like Class in Object Oriented Programming.
`guest machine / docker container:` This is the container which will be created from docker image. Just like Object/Instance of a class in Object Oriented Programming.
`Docker Engine:` This is the docker software that you must INSTALL and ENABLE/RUN on your machine to run any docker command.

### Create a Docker image
To create a docker image, you will need a file `Dockerfile`. It contains the specifications e.g. what Python version you want to used etc.
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
`-v "$PWD/input:/project/input"` This will mount the `scikit-surgerydocker/input` directory to `/project/input` directory in the container to make the input file availabe to our python `app.py` when run in the container.
`-v "$PWD/output:/project/output"` This will mount the `scikit-surgerydocker/output` directory to `/project/output` directory in the container. So when the app.py application write to `/project/output` in the container, we will automatically get it on docker host in `scikit-surgerydocker/output`

### Checking the output
To verify the processing performed in the container after executing the above command. On docker host
```
cd scikit-surgerydocker
cd output
cat file.txt
```










