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

.. code:: bash

    docker run -it --rm --gpus="1" ubuntu nvidia-smi


Volume Mapping
--------------

To keep the data of container persistant (keeping the data even when the container is deleted),
Run the command

.. code:: bash

    docker run -v  "$PWD/web:/usr/share/nginx/html" nginx

- :code:`-v` is used for volumen mapping.
- :code:`$PWD/web:/usr/share/nginx/html` means map `web` directory in the present working directory (PWD) to /usr/share/nginx/html directory in the container. 

Now you can keep the web code in the docker host (local computer) and run it inside the container. e.g.

.. code:: bash

    mkdir web
    echo "Hello World" > web/index.html
    docker run -d -v "$PWD/web:/usr/share/nginx/html" -p 6666:80 nginx

Now check the website "localhost:5005" from your computer.


Inspect command
---------------
To find the details of a container like port, mount volume etc. You can run the command

.. code:: bash

    docker inspect <container_ID/Container_name>

