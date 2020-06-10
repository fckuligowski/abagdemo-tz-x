node {
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('hazel-math')
    }
    
    checkout scm

    def customImage = docker.build("my-image:${env.BUILD_ID}")

    customImage.inside {
        sh 'printenv'
    }
}