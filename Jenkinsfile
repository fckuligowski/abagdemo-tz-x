pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                echo 'before'
                sh 'tests/testit.sh'
                echo 'after'
            }
        }
    }
}