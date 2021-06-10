Building your own docker image
==============================

.. There are two common ways to build your own docker image. Both ways are described below


.. Note::

   If you have installed docker on local computer then make sure docker service is running before executing any command.
   

.. Method 1
.. --------
.. This is an interactive way of making your image. First you will setup the container according to your desire and then you will commit the changes to make the image.

.. Step 1: Start the container and get inside the container.

.. .. code:: bash

..     docker run -it ubuntu:18.04:latest bash

.. Step 2: Update the package lists

.. .. code:: bash

..     apt-get update

.. Step 3: Install required version of Python in the container

.. .. code:: bash

..     apt-get install -y python3.6


.. Step 4: Install pip in the container

.. .. code:: bash

..     apt-get install -y python3-pip

.. Step 5: Install a package in the container e.g. wget

.. .. code:: bash

..     apt-get install -y wget

.. Step 6: Exit the container

.. .. code:: bash

..     exit

.. Step 7: Note the container ID of the container

.. .. code:: bash

..     exit

.. Step 8: Commit the container and give image name and version

.. .. code:: bash

..     docker commit <image ID> myimage:v1

.. Step 9: Check your created image by

.. .. code:: bash

..     docker images

The following two examples explains the process of creating your own docker image.


Example 1
---------


**Step 1:** Create a new directory and change to that directory

.. code:: bash

    mkdir image_1
    cd image_1

**Step 2:** Clone the repo and change into animated_text directory

.. code:: bash

    git clone https://github.com/mianasbat/animated_text.git
    cd animated_text

**Step 3:** create a Dockerfile (case sensitive)

.. code:: bash

    touch Dockerfile

**Step 4:** Open Dockerfile, write the following text in it and save the changes.

.. code:: bash

    FROM ubuntu
    RUN apt-get update
    RUN apt-get install -y python3.6
    RUN apt-get install -y python3-pip
    RUN apt-get install -y wget
    WORKDIR /usr/app
    COPY . .
    RUN pip3 install -r requirements.txt
    WORKDIR /usr/app/src
    CMD ["python3", "app.py"]


**Step 5:** Now run the command to create the image. The -t is used to tag it. Dont forget the . at the end of the command.

.. code:: bash

    docker build -t mian_image_1:v1 .

**Step 6:** Now verify that the image is created by

.. code:: bash

    docker images

**Step 7:** To test the image, run your image using

.. code:: bash

    docker run -it mian_image_1:v1

**Step 8:** Press `q` to quit the animation.



Example 2
---------

In this example, we will create the same image but starting from different base image

**Step 1:** Create a new directory and change to that directory

.. code:: bash

    mkdir image_2
    cd image_2

**Step 2:** Clone the repo and change into animated_text directory

.. code:: bash

    git clone https://github.com/mianasbat/animated_text.git
    cd animated_text

**Step 3:** create a Dockerfile (case sensitive)

.. code:: bash

    touch Dockerfile

**Step 4:** Open Dockerfile, write the following text in it and save the changes.

.. code:: bash

    FROM python:3.6.9-slim
    WORKDIR /usr/app
    COPY . .
    RUN pip install -r requirements.txt
    WORKDIR /usr/app/src
    CMD ["python", "app.py"]



**Step 5:** Now run the command to create the image. The -t is used to tag it. Dont forget the . at the end of the command.

.. code:: bash

    docker build -t mian_image_2:v1 .

**Step 6:** Now verify that the image is created by

.. code:: bash

    docker images

**Step 7:** To test the image, run your image using

.. code:: bash

    docker run -it mian_image_2:v1

**Step 8:** Press `q` to quit the animation.