Raplicable Results
=======================

From raplicable reproducible, I mean the process where same analysis script but different data is executed and the results are qualitatively same.

About selected project
----------------------

The same project `Simplified Fet-reg 2021 <https://bit.ly/3iAMZNf>`_ which is used in repeatable reproducible is reused here.

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

    mkdir temp
    cd temp
    git clone https://github.com/mianasbat/FetReg-2021.git
    cd FetReg-2021

**Step 2:** Create a Dockerfile (Remember :code:`D` must be capital and no file extension) and store the following text.

.. code:: bash

    touch Dockerfile
    open Dockerfile

    FROM mianasbat/ubuntu1804-py3.6-pip:latest
    RUN apt-get update
    RUN apt-get install ffmpeg libsm6 libxext6 -y
    RUN python -m pip install --upgrade pip
    RUN mkdir /mnt/input_data
    RUN mkdir /mnt/output_data
    WORKDIR /opt/app
    COPY . .
    RUN python -m pip install -rrequirements.txt
    CMD ["python3", "reg.py"]


**Step 3:** Build the image

.. code:: bash

    docker build -t img_seg:v1 .

**Step 4:** Run the image

.. code:: bash

    docker run -v "$PWD/input_data:/mnt/input_data" -v "$PWD/output_data:/mnt/output_data" img_seg:v4 python3 reg.py /mnt/input_data /mnt/output_data

    # For windows add the / before both $ symbols
    docker run -v "/$PWD/input_data:/mnt/input_data" -v "/$PWD/output_data:/mnt/output_data" img_seg:v4 python3 reg.py /mnt/input_data /mnt/output_data
  
**Step 5:** Now check the output_directory in the current directory to get the results.
 
  ..  code:: bash

    cd output_data
    ls
