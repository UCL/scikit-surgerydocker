Docker Intermediate Commands
============================

The following are the intermediate level commands that are needed to work with Docker. Open the terminal and run the commands.

Port Mapping
------------
To open port on the container and map it to the port on dockerhost. Run the command

.. code:: bash
    docker run -p 5000:80 nginx

where

- :code:`-p` is used for port mapping.
- :code:`5000:80` means map port 80 of nginx container to port 5000 on dockerhost.

Volume Mapping
--------------

To keep the data of container persistant (keeping the data even when the container is deleted), 
Run the command

.. code:: bash
    docker run -v  /opt/data:/var/lib/mysql mysql

- :code:`-v` is used for volumen mapping.
- :code:`/opt/data:/var/lib/mysql` means map /var/lib/mysql directory in the container to /opt/data directory in dockerhost. \
Since MySQL server writes all data to /var/lib/mysql therefore the benefit of mounting the volume \
is that all data will be persistant even if the container is deleted.



