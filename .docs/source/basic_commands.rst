Docker Basic Commands
=====================

The following are the most common commands that are needed to work with Docker. Open the terminal and run the commands.

.. Note::

   If you have installed docker on local computer then make sure docker service is running before executing any command.

Docker Version
^^^^^^^^^^^^^^
To find the version of installed docker client and docker server:

.. code:: bash

    docker version


Download image
^^^^^^^^^^^^^^
To download/pull an image from the default registry (docherhub).

.. code:: bash

    docker pull <image name>
    # e.g.
    docker pull hello-world
    # or
    docker pull busybox


Runing Container
^^^^^^^^^^^^^^^^
The run command is the combination of two commands :code:`run` and :code:`pull`. If the image is available on the local computer
then it will run that image. If the image is not available locally then the command will search the `docker hub <https://hub.docker.com/>`_ for the image
and if it is found it will be pulled/downloaded and run as container.

.. code:: bash

    docker run <image name>
    # e.g. 
    docker run -d hello-world
    # or
    docker run -d busybox echo "Hello World"

:code:`-d` option is used to run the container in the background and free terminal to run more commands. 

List Images
^^^^^^^^^^^
To list all the images either downloaded from the internet or created locally:

.. code:: bash

    docker images

List Running Containers
^^^^^^^^^^^^^^^^^^^^^^^
To list all the containers currently under execution

.. code:: bash

    docker ps

List all Containers
^^^^^^^^^^^^^^^^^^^
To list all the containers that are under execution and those which finished execution.

.. code:: bash

    docker ps -a

Stop Container
^^^^^^^^^^^^^^
To stop a running container

.. code:: bash

    # First step is to run the container which you will stop below. 
    # The following command will keep busybox container running for 10 seconds
    docker run -d busybox sleep 10
    # Second step is to find the ID of the container to stop
    docker ps
    # To stop the container
    docker stop <container_ID>

Start Container
^^^^^^^^^^^^^^^
To start a stopped container

.. code:: bash

    # To find the ID of the container to start
    docker ps -a 
    # To start the container
    docker start <container_ID>


Get Container Details
^^^^^^^^^^^^^^^^^^^^^
To get the container details like IP address, image, creation time and much more

.. code:: bash

    # To find the ID of the container to stop
    docker ps -a
    # To get the details of a container
    docker inspect <container_ID>


Get all information
^^^^^^^^^^^^^^^^^^^
To get the complete details about running containers, stopped containers, images, server, network, storage etc.

.. code:: bash

    docker info


Delete Container
^^^^^^^^^^^^^^^^
To remove/delete a container

.. code:: bash

    # To find the ID of the container to delete
    docker ps -a
    # To delete the container
    docker rm -f <container_ID>


Delete all Containers
^^^^^^^^^^^^^^^^^^^^^
To delete all containers (running and stopped both)

.. code:: bash

    docker rm -f $(docker ps -a -q)


Delete Image
^^^^^^^^^^^^
To delete an image

.. code:: bash

    # To find the ID of the image to delete
    docker images
    # To delete the image
    docker rmi -f <image_ID or image_name>
    # e.g.
    docker rmi -f hello-world


Delete all Images
^^^^^^^^^^^^^^^^^
To remove/delete all images

.. code:: bash

    docker rmi -f $(docker images -a -q)

