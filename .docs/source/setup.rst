Setting up Docker
=================

Docker is an open platform for developing, shipping, and running applications. 
Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.  
By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, 
you can significantly reduce the delay between writing code and running it in production [`reference 1`_]. 

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



.. _reference 1: https://docs.docker.com/get-docker/ 
.. _Linux installation: https://docs.docker.com/engine/install/ 
.. _Mac download link: https://desktop.docker.com/mac/stable/amd64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-amd64
.. _Mac installation: https://docs.docker.com/docker-for-mac/install/
.. _Windows download link: https://desktop.docker.com/win/stable/amd64/Docker%20Desktop%20Installer.exe
.. _Windows installation: https://docs.docker.com/docker-for-windows/install/
