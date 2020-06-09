pipeline {
    agent any 
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('hazel-math-cred-file')
    }
    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello world!' 
                sh("echo ${GOOGLE_APPLICATION_CREDENTIALS}")
                sh("cat ${GOOGLE_APPLICATION_CREDENTIALS}")
                echo 'here we go again' 
            }
        }
    }
}