# Program execution from image

After you have containerize your python application, you would like to run it :) The following command will create a new `container` from image `my-project`. 
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