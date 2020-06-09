pipeline {
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('hazel-math-cred-file')
    }
    agent {
        node {
            checkout scm
            def dockerImage = docker.build("abagdemo:${env.BUILD_ID}")
            dockerImage.inside {
                echo 'Inside the new container' 
                sh("head -4 ${GOOGLE_APPLICATION_CREDENTIALS}")
                sh("pwd")
                sh("ls -al")

            }
        }
    } 
    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello World!' 
                sh("head -4 ${GOOGLE_APPLICATION_CREDENTIALS}")
                sh("pwd")
                sh("ls -al")
            }
        }
    }
}