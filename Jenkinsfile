node {  
    checkout scm

    def customImage = docker.build("fckuligowski/abagdemo:${env.BUILD_ID}")

    customImage.inside {
        withCredentials([file(credentialsId: 'hazel-math', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
            sh 'printenv'
        }
    }
}