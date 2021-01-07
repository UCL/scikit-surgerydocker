# How to package your image for sharing

If you would like to submit your docker image containing your Python application to a challange then this can be achieved in two common ways:

## Compress the image and upload it to cloud drive

This following command will create the compressed `tar` file of the image in the current directory by the name `my-project-team1.tar`.

```
# You dont need to be in scikit-surgerydocker directory to do this.
# The following command will work from any where in docker host

docker save my-project:team1 > my-project-team1.tar
```

Now you can upload this tar file to the cloud drive (Google drive, Drop box, One drive etc) and you can share it with any one you want.

## Upload it docker hub

One of the docker registries where you can upload your created image `my-project` is [docker hub](https://hub.docker.com/).

1. Create a free account in docker hub.
2. Login to docker hub account online.
3. Create a repository
   1. Give a name (e.g. new-user-1)
   2. Give a description
   3. Click Create.
4. Now on docker host login to your docker hub account from terminal by the following command and providing the password when requested.

```
docker login --username=yourgithubusername --email=youremail@company.com
```

5. Now you need to tag your image with your docker hub ID.
   1. To tag the image, first you need to find the image ID.
   2. After finding the ID you can tag the image

```
# To find the ID of your image run command
docker images

# To tag the image with your docker hub username
docker tag <image id found in step 1> yourgithubusername/my-project:team1
```

6. Now you can upload the tagged image to docker hub. It will take time in uploading depending on the size of the image.

```
docker push yourgithubusername/my-project:team1
```
