# Verifying the creation of new container
You can verify the newly created container by running the following command on docker host.
```
docker ps -a
```
Check the status column and you will see that the status say `Exited`. It is because that the docker container exit after performing its job. In our case, its job was to read text from input file and append text with it and write to output file.
