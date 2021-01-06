# Program execution from image

After you have containerize your python application, you would like to run it :) The following command will create a new `container` from image `my-project`. 
```
cd scikit-surgerydocker/project/
docker run -v "$PWD/input:/project/input" -v "$PWD/output:/project/output" my-project
```

In the above command,      
`my-project` is the image name.     
`-v "$PWD/input:/project/input"` This parameter will mount the `scikit-surgerydocker/project/input` directory from docker host to `/project/input` directory in the container to make the input file availabe to our python `app.py` when executed in the container.      
`-v "$PWD/output:/project/output"` This will mount the `scikit-surgerydocker/project/output` directory from docker host to `/project/output` directory in the container. So when the `app.py` application on execution write to `/project/output` in the container, we will automatically get it on docker host in `scikit-surgerydocker/project/output` because of the mount.

**NOTE:** The docker container will exit after doing its process of reading from a file and writing to a file.
To verify that the container was created from the image and completed its job. You can run the command
```
docker ps -a
```