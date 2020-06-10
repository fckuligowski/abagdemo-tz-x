pipeline {
    agent { dockerfile true }
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('hazel-math')
    }
    stages {
        stage('Test') {
            steps {
                sh 'ls -al'
                sh 'tests/testit.sh'
                echo 'after'
            }
        }
    }
}