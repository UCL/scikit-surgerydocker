Building your own docker image
==============================

There are two common ways to build your own docker image. Both ways are described below

Method 1
--------
This is an interactive way of making your image. First you will setup the container according to your desire and then you will commit the changes to make the image.

Step 1: Start the container and get inside the container.

.. code:: bash

    docker run -it ubuntu:18.04:latest bash

Step 2: Update the package lists

.. code:: bash

    apt-get update

Step 3: Install required version of Python in the container

.. code:: bash

    apt-get install -y python3.6


Step 4: Install pip in the container

.. code:: bash

    apt-get install -y python3-pip

Step 5: Install a package in the container e.g. wget

.. code:: bash

    apt-get install -y wget

Step 6: Exit the container

.. code:: bash

    exit

Step 7: Note the container ID of the container

.. code:: bash

    exit

Step 8: Commit the container and give image name and version

.. code:: bash

    docker commit <image ID> myimage:v1

Step 9: Check your created image by

.. code:: bash

    docker images




Method 2 Example 1
------------------


Method 2 Example 2
------------------