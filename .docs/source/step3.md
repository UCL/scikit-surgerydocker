# Program execution from image

After you have containerized your Python application, you can run it on your computer for testing before sharing with others.
In the example we know that the input data is stored in `scikit-surgerydocker/input_data` and the program will write results to `scikit-surgerydocker/output_data`. 

The following command will create a new `container` from image `my-project`.

```
cd scikit-surgerydocker
docker run -v "$PWD/input_data:/project/input_data" -v "$PWD/output_data:/project/output_data" my-project
```

In the above command,  
`my-project` is the docker image name.  
`-v "$PWD/input_data:/project/input_data"` This parameter will mount the `scikit-surgerydocker/input_data` directory from docker host to `/project/input_data` directory in the container to make the input file availabe to our python `app.py` when executed in the container.  
`-v "$PWD/output_data:/project/output_data"`. This will mount the `scikit-surgerydocker/project/output` directory from docker host to `/project/output_data` directory in the container. So the `app.py` application on execution will write to `/project/output_data` in the container, we will automatically get it on docker host in `scikit-surgerydocker/project/output_data` because of the mount.

**NOTE:** The docker container will exit after running the app.py script. It is normal for docker to stop the conainer automatically after executing the job.
