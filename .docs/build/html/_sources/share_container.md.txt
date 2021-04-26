# How to package your image for sharing

If you would like to submit your docker image containing your Python application to a challenge then you have to upload it to a cloud:

## Upload image to dockerhub
To share the newly created docker image `my-project` we could make use of free service dockerhub. Following are the steps to upload the docker image to to dockerhub.

### Compress image:
The following command will create a compressed `.tar` file of the image in the current directory by the name `my-project.tar`.
```
docker save my-project > my-project.tar
```

### Upload to dockerhub

One of the docker registries where you can upload your created and compressed image `my-project.tar` is [docker hub](https://hub.docker.com/). You need to have an account on the dockerhub. To sign up to docker hub visit [here](https://hub.docker.com/signup).

1. Create a free account on docker hub.
2. Login to docker hub account online.
3. Create a repository
   1. Give a name, better to give same name as image name e.g. `my-project` in our case.
   2. Give a description
   3. Click Create.
4. Now on docker host login to your docker hub account from terminal by the following command and providing the password when requested.

```
# There are multiple ways to provide the password. I am using the environment variable one.
# First you need to create an environment variable and assign your password 
MY_PASSWORD="give_your_password"

# Now run the following command to login to docker hub from terminal
echo "$MY_PASSWORD" | docker login --username <username> --password-stdin
```

5. Now you need to tag your image with your docker hub login name.
   1. To tag the image, you need to know the image name
   2. After finding the ID you can tag the image

```
# To find the image name list all the images
docker images

# To tag the image with your docker hub login name
docker tag my-project yourdockerhubaccount/my-project
```

6. Now you can upload the tagged image to docker hub. It will take time in uploading depending on the size of the image.

```
docker push yourgithubusername/my-project:latest
```

Now you can verify the image online in your dockerhub account.
