

**Install**

I had trouble with "pip3 install -r requirements.txt" with the google-cloud-storage library. It would get an error saying *error: invalid command 'bdist_wheel*. To fix this, [this post](https://stackoverflow.com/questions/34819221/why-is-python-setup-py-saying-invalid-command-bdist-wheel-on-travis-ci) said to "pip3 install wheel", which fixes the issue, so I added wheel to the requirements.txt. But I still got that error when it was right before google-cloud-storage. I had to move wheel to the top of the file, then the error stopped coming up. (I'm not sure this isn't going to come back later, though).

**Docker**

Create the image for abagdemo

```
docker build -t fckuligowski/abagdemo:v1.0 -f Dockerfile.prod .
```

If you want to run it from Docker

```
docker run --name abagdemo -d -p 30080:5000 --rm -v instance/creds/justademo-acoustic-apex.json=/abagdemo/justademo-acoustic-apex.json -e GOOGLE_APPLICATION_CREDENTIALS=/abagdemo/instance/creds/justademo-acoustic-apex.json fckuligowski/abagdemo:v1.1
or
docker run --name abagdemo -p 30080:5000 --rm -v instance/creds/justademo-acoustic-apex.json=/abagdemo/justademo-acoustic-apex.json -e GOOGLE_APPLICATION_CREDENTIALS=/abagdemo/instance/creds/justademo-acoustic-apex.json fckuligowski/abagdemo:v1.1
```
If you want to run pytest to test it from Docker
```
docker run --name abagdemo -p 30080:5000 --rm -e MODE='TESTING' -v instance/creds/justademo-acoustic-apex.json=/abagdemo/justademo-acoustic-apex.json -e GOOGLE_APPLICATION_CREDENTIALS=/abagdemo/instance/creds/justademo-acoustic-apex.json -v ~/py/abagdemo/tests/:/abagdemo/tests fckuligowski/abagdemo:v1.1
```
Note that the image name needs to be at the end of the command, after the "-e" env var parms (else Docker will pass them to the shell script as arguments, not env vars).

Docker push to repo

```
docker push fckuligowski/abagdemo:v1.0
```

**Jenkins**
Had to go to this url from my Chrome browser session, the one logged into the GCP account I'm using, to get the Jenkins pipeline to trigger after a commit.
```
https://8080-dot-12675158-dot-devshell.appspot.com/git/notifyCommit?url=https://github.com/fckuligowski/abagdemo.git
```
Gonna need a Jenkins server that's publicly available, so the Git Webhooks can work.



