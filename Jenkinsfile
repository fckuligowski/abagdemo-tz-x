node {  
    checkout scm

    def customImage = docker.build("fckuligowski/abagdemo:${env.BUILD_ID}")

    customImage.inside {
        environment {
            GOOGLE_APPLICATION_CREDENTIALS = credentials('hazel-math')
        }

        sh 'printenv'
    }
}