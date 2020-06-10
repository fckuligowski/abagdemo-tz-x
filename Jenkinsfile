pipeline {
    agent { dockerfile true }
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