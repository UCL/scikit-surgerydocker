Docker Advance Commands
============================

The following are the intermediate level commands that are needed to work with Docker. Open the terminal and run the commands.

Port Mapping
------------
To open port on the container and map it to the port on dockerhost. Run the command

.. code:: bash

    docker run -d -p 5000:80 nginx

where

- :code:`-d` is used to run the container in backgroud.
- :code:`-p` is used for port mapping.
- :code:`5000:80` means map port 80 of nginx container to port 5000 on dockerhost.

To verify the service open browser and go to the address `localhost:5000` 



Limit RAM
-------------------
To specify maximum memory for a container

.. code:: bash

    docker run -d -p 5001:80 --memory=1g nginx
    # To find the container ID or name
    docker ps 
    # To find the resource utilization of the container
    docker stats <container_name or container_ID>


Limit CPU
-------------------
To specify limit on maximum cpu utilization of a container

.. code:: bash

    docker run -d -p 5002:80 --cpus="1.0" nginx

Limit GPU
---------
To specify specific number of gpus for a container. E.g. to assign only 1 GPU

.. Note:: 
    On computers not having a GPU the following command will give an error.

.. code:: bash

    docker run -it --rm --gpus="1" ubuntu nvidia-smi


Volume Mapping
--------------

To keep the data of container persistant (keeping the data even when the container is deleted),



.. code:: bash

    mkdir web
    echo "Hello World " > web/index.html
    docker run -v "$PWD/web:/usr/share/nginx/html" -d -p 5005:80 nginx

    # On windows in gitbash
    mkdir web
    echo "Hello World " > web/index.html
    # Note the extra / before $PWD to make it work in windows.
    docker run -v "/$PWD/web:/usr/share/nginx/html" -d -p 5005:80 nginx



- :code:`-v` is used for volumen mapping.
- :code:`$PWD/web:/usr/share/nginx/html` means map :code:`web` directory in the present working directory ($PWD) to /usr/share/nginx/html directory in the container. 

Now check the website "localhost:5005" from your computer.


Now data and web server are loosely coupled and even if the container is deleted you can spin another container and mount the existing data.


Inspect command
---------------
To find the details of a container like port, mount volume etc. You can run the command

.. code:: bash

    docker inspect <container_ID/Container_name>

