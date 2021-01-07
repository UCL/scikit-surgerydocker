# Verifying the creation of new container

You can verify the newly created container by running the following command on docker host.

```
docker ps -a
```

Check the status column, which should show `Exited`, as the container exits after the script has been run. In our case, its job was to read text from input file and append text with it and write to output file.
