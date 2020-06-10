pipeline {
    agent { dockerfile true }
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('hazel-math')
    }
    stages {
        stage('Unit Tests') {
            steps {
                sh 'tests/testit.sh unit'
            }
        }
        stage('Functional Tests') {
            steps {
                sh 'tests/testit.sh functional'
            }
        }
    }
}