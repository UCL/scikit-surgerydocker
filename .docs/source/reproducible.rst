Reproducible Results
=======================

Reproducible results mean the process where same data and same analysis script is executed to always get the same exact results.

About selected project
----------------------

I forked and simplified one of our project on github that is developed for `fet-reg 2021 <https://fetreg2021.grand-challenge.org/>`_ for this exercise.
The repo is at `Simplified Fet-reg 2021 <https://bit.ly/3iAMZNf>`_. 

The :code:`reg.py` file contains an algorithm that reads :code:`.png` images from a directory, process it and store the results in output directory.

.. code:: bash

    python -m virtualenv env_reg
    # On Mac & Linux
    source env_reg/bin/activate
    # On Windows
    env_reg/bin/activate
    pip install -rrequirements.txt
    python reg.py input_data output_data

The above command runs the algorithm on :code:`*.png` images stored in the provided :code:`input_data` directory. The algorithm perform the analysis and 
creates a seperate :code:`.txt` file for each image. The text files are stored in the provided :code:`output_data` directory.


Dockerize the Repo
------------------

**Step 1:** Clone the repo and change directory into it

.. code:: bash

    git clone https://github.com/mianasbat/FetReg-2021.git
    cd FetReg-2021

**Step 2:** Create a Dockerfile (Remember: :code:`D` in Dockerfile must be capital and no file extension) and store the following text.

.. code:: bash

    touch Dockerfile
    open Dockerfile
    
    FROM mianasbat/ubuntu1804-py3.6-pip:latest
    RUN apt-get update
    RUN apt-get install ffmpeg libsm6 libxext6 -y
    RUN python -m pip install --upgrade pip
    WORKDIR /opt/app
    COPY . .
    RUN python -m pip install -rrequirements.txt
    CMD ["python3", "reg.py", "input_data", "output_data"]


**Step 3:** Build the image

.. code:: bash

    docker build -t img_seg:v1 .

**Step 4:** Run the image

.. code:: bash

    docker run img_seg:v1

**Step 5:** Find the container ID and copy the results from the container to current directory

.. code:: bash

    docker ps -a
    docker cp <container_ID or container_name>:/opt/app/output_data .

**Step 6:**

    You can upload the image :code:`img_seg:v1` for others to reproduce the results. Check the share image section of the workshop.
