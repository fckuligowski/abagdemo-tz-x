# abagdemo
This is a demo app for me (Frank Kuligowski) to try and do a DevOps pipeline.

The app is called **abagdemo**. It is meant to be an app that can record and show scan records for luggage bags, as they go through the airport conveyors. That's the premise for the app, so I had something to build for.

It is a Python Flask app that serves up a REST endpoint that one can use to interact with the app, at these endpoints (routes).

- /index is the home page
- /history/001 to show all the scans for bag id 001
- /status/001 to show just the latest scan for bag id 001
- /scan to add a new scan for a bag

The data is  stored in a Google Cloud Platform Storage object. It will automatically create the object on the fly, from a base data file in this repo. This requires GCP credentials. These can't be stored in the repo. They're stored in Jenkins for testing, and in a Kubernetes Secret for 'production'. Everything expects the creds file to be in the instance/creds directory of this repo's dir structure.  If the file name changes it needs to be changed in two places - k8s/create_secret.sh, and in Jenkins itself.

This app uses pytest to do some tests, to ensure the app isn't broken.

It uses Jenkins to build a container, run the tests, and push the container to Docker Hub. The name of the image that's pushed needs to be defined in k8s/abagdemo-deploy.yaml. When that "image:" name changes, Jenkins will push the image to Docker Hub (provided the tests  pass, and provided it is on a Merge).

The container image is deployed to 'production' with [Flux](https://docs.fluxcd.io/en/latest/tutorials/get-started/). That's all done outside of this repo. See the notes.md  for my notes on that.

I never could get Webhooks working with GitHub and Ahead's Jenkins lab, and publishing code is kind of clunky - you have issue a PR, then add in another change, before the Jenkins pipeline will run the tests. If a connection from GitHub to Ahead's Jenkins, then it would be great to update this repo with those details and re-run this pipeline to test everything out and see if its all running smoothly (i.e. can run the pipeline when a PR is created).

I had a boatload of trouble getting my own Jenkins server running, with Docker. I built one in GCP, but it kept telling me that the "docker" command wasn't available. I built another one on my Linux Academy servers, but it kept telling me that the "dockerfile" agent wasn't found.

This Jenkins pipeline is a scripted pipeline, not a declarative pipeline like most Jenkins pipelines. That's because I couldn't figure out how to push the container to Docker unless I used a scripted pipeline. Perhaps I didn't pick the best tool for pushing the container, but hey.

The container image doesn't do anything but install the app and it's Python requirements. Use the "runit.sh" script to start  the app in the container. Use the "tests/testit.sh" script to run the pytests from the container. Use the "rundev.sh" script to run the app from a container on your dev machine (I used a Linux Ubuntu host from Linux Academy).
