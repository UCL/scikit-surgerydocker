# How to containerize the application

To create a docker image, you will need a file called `Dockerfile`. It contains the specifications e.g. What Python version you want to run your python application with etc. Please read the `Dockerfile` in the repo for further information.

The directory structure after cloning the project: 

<!-- ![Directory Structure](./images/directory-structure.png) -->
```bash
scikit-surgerydocker
├── output
├── Dockerfile
├── input
│   └── inputfile.txt
├── CONTRIBUTING.md
├── app.py
└── README.md   
```
Run the following command to create the image by the name `my-project`. You can your image any thing you want.   
**Note:** The following command will only work if you are in the same directory where the `Dockerfile` is saved. In our case `Dockerfile` is in the root directory of the repo.
```
cd scikit-surgerydocker
docker build . -t my-project
```
Run the following command to check that your docker image is created.
This command will show all the docker images you have on your docker host including the newly created `my-project` Docker image.
```
docker images
```
The newly created `my-project` image will have the Python version you specified in `Dockerfile` and the dependencies installed (if any) and finally the source code.