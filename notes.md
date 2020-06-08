

**Install**

I had trouble with "pip3 install -r requirements.txt" with the google-cloud-storage library. It would get an error saying *error: invalid command 'bdist_wheel*. To fix this, [this post](https://stackoverflow.com/questions/34819221/why-is-python-setup-py-saying-invalid-command-bdist-wheel-on-travis-ci) said to "pip3 install wheel", which fixes the issue, so I added wheel to the requirements.txt. But I still got that error when it was right before google-cloud-storage. I had to move wheel to the top of the file, then the error stopped coming up. (I'm not sure this isn't going to come back later, though).

**Docker**

Create the image for abagdemo

```
docker build -t fckuligowski/abagdemo:v1.0 -f Dockerfile.prod .
```

If you want to run it from Docker

```
docker run --name abagdemo -d -p 30080:5000 --rm fckuligowski/abagdemo:v1.0
or
docker run --name abagdemo -p 30080:5000 --rm fckuligowski/abagdemo:v1.0
```

Docker push to repo

```
docker push fckuligowski/abagdemo:v1.0
```



