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
