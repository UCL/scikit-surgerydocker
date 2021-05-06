Docker Basic Commands
=====================

The following are the most common commands that are needed to work with Docker. Open the terminal and run the commands.

.. note::

   If you have installed docker on local computer then make sure docker service is running before executing any command.

Docker Version
^^^^^^^^^^^^^^
To find the version of installed docker client and docker server:

.. code:: bash

    docker version

Runing Container
^^^^^^^^^^^^^^^^
The run command is the combination of two commands `run` and `pull`. If the image is available on the local computer
then it will run that image. If the image is not available locally then the command will search the docker hub (internet) for the image
and if it is found it will be pulled/downloaded and run.

.. code:: bash

    docker run hello-world

If you run the same command then you will notice that this time the container runs very fast because the image is stored locally
in the first step.

.. code:: bash

    docker run hello-world

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

    # To find the ID of the container to stop
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
To get the container Details like IP address, image, creation time and much more

.. code:: bash

    # To find the ID of the container to stop
    docker ps -a
    # To get the details of a container
    docker inspect <container_ID>


Delete Container
^^^^^^^^^^^^^^^^
To delete a container

.. code:: bash

    # To find the ID of the container to delete
    docker ps -a
    # To delete the container
    docker rmi -f <container_ID>


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
    docker rmi -f <image_ID>


Delete all Images
^^^^^^^^^^^^^^^^^
To delete all images

.. code:: bash

    docker rmi -f $(docker images -a -q)



