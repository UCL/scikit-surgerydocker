Setting up Docker
=================

Docker is an open platform for developing, shipping, and running applications. 
Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.  
By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, 
you can significantly reduce the delay between writing code and running it in production [`reference 1`_]. 

Install Docker
--------------
Click the tab according to your operating system and follow the steps to install Docker.


.. tabs::

    .. tab:: Linux

        Install Docker using shell script

        .. code:: bash

            curl -fsSL https://get.docker.com -o get-docker.sh
            sudo sh get-docker.sh
        
        For more details check out Docker's official `Linux installation`_ web page.

    .. tab:: Mac OS

        | Download docker using the `Mac download link`_. 
        | Double click the downloaded package and follow the steps to install it.
        | For more details check out Docker's official `Mac installation`_ web page.


    .. tab:: Windows

        | Download docker using the `Windows download link`_. 
        | Double click the downloaded executable and follow the steps to install it.
        | For more details check out Docker's official `Windows installation`_ web page.


Verify installation
-------------------
Click the tab according to your operating system and follow the steps to verify Docker installation.

.. tabs::

    .. tab:: Linux

        Open terminal app

        .. code:: bash

            # First run the following command to confirm that docker is running.
            docker -v

            # Correct output will give the docker's version
            Docker version 18.09.0, build 4d60db4

            # Second run the following command to verify the docker's setup.
            docker run hello-world

            # Correct output should be like the following.
            Unable to find image 'hello-world:latest' locally
            latest: Pulling from library/hello-world
            b8dfde127a29: Pull complete
            Digest: sha256:f2266cbfc127c960fd30e76b7c792dc23b588c0db76233517e1891a4e357d519
            Status: Downloaded newer image for hello-world:latest

            Hello from Docker!
            This message shows that your installation appears to be working correctly.

            To generate this message, Docker took the following steps:
            1. The Docker client contacted the Docker daemon.
            2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
                (amd64)
            3. The Docker daemon created a new container from that image which runs the
                executable that produces the output you are currently reading.
            4. The Docker daemon streamed that output to the Docker client, which sent it
                to your terminal.

            To try something more ambitious, you can run an Ubuntu container with:
            $ docker run -it ubuntu bash

            Share images, automate workflows, and more with a free Docker ID:
            https://hub.docker.com/

            For more examples and ideas, visit:
            https://docs.docker.com/get-started/

    .. tab:: Mac

        Open terminal app

        .. code:: bash

            # First run the following command to confirm that docker is running.
            docker -v

            # Correct output will give the docker's version
            Docker version 18.09.0, build 4d60db4

            # Second run the following command to verify the docker's setup.
            docker run hello-world

            # Correct output should be like the following.
            Unable to find image 'hello-world:latest' locally
            latest: Pulling from library/hello-world
            b8dfde127a29: Pull complete
            Digest: sha256:f2266cbfc127c960fd30e76b7c792dc23b588c0db76233517e1891a4e357d519
            Status: Downloaded newer image for hello-world:latest

            Hello from Docker!
            This message shows that your installation appears to be working correctly.

            To generate this message, Docker took the following steps:
            1. The Docker client contacted the Docker daemon.
            2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
                (amd64)
            3. The Docker daemon created a new container from that image which runs the
                executable that produces the output you are currently reading.
            4. The Docker daemon streamed that output to the Docker client, which sent it
                to your terminal.

            To try something more ambitious, you can run an Ubuntu container with:
            $ docker run -it ubuntu bash

            Share images, automate workflows, and more with a free Docker ID:
            https://hub.docker.com/

            For more examples and ideas, visit:
            https://docs.docker.com/get-started/

    .. tab:: Windows

        Open CMD or powershell app

        .. code:: bash

            # First run the following command to confirm that docker is running.
            docker -v

            # Correct output will give the docker's version
            Docker version 18.09.0, build 4d60db4

            # Second run the following command to verify the docker's setup.
            docker run hello-world

            # Correct output should be like the following.
            Unable to find image 'hello-world:latest' locally
            latest: Pulling from library/hello-world
            b8dfde127a29: Pull complete
            Digest: sha256:f2266cbfc127c960fd30e76b7c792dc23b588c0db76233517e1891a4e357d519
            Status: Downloaded newer image for hello-world:latest

            Hello from Docker!
            This message shows that your installation appears to be working correctly.

            To generate this message, Docker took the following steps:
            1. The Docker client contacted the Docker daemon.
            2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
                (amd64)
            3. The Docker daemon created a new container from that image which runs the
                executable that produces the output you are currently reading.
            4. The Docker daemon streamed that output to the Docker client, which sent it
                to your terminal.

            To try something more ambitious, you can run an Ubuntu container with:
            $ docker run -it ubuntu bash

            Share images, automate workflows, and more with a free Docker ID:
            https://hub.docker.com/

            For more examples and ideas, visit:
            https://docs.docker.com/get-started/



**Note**

If installation of docker is not possible locally then you can use a `free sandbox`_ provided by docker for practicing.
You will need to `register`_ with docker to use the sandbox. You can run the `basic commands`_ after login to sandbox.















.. _reference 1: https://docs.docker.com/get-docker/ 
.. _Linux installation: https://docs.docker.com/engine/install/ 
.. _Mac download link: https://desktop.docker.com/mac/stable/amd64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-amd64
.. _Mac installation: https://docs.docker.com/docker-for-mac/install/
.. _Windows download link: https://desktop.docker.com/win/stable/amd64/Docker%20Desktop%20Installer.exe
.. _Windows installation: https://docs.docker.com/docker-for-windows/install/
.. _free sandbox: https://labs.play-with-docker.com/
.. _register: https://hub.docker.com/signup 
.. _basic commands: https://scikit-surgerydocker.readthedocs.io/en/latest/ 