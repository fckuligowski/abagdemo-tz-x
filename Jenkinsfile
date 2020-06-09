pipeline {

    agent {
        dockerfile true
    } 
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('hazel-math-cred-file')
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