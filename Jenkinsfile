pipeline {
    agent { dockerfile true }
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('hazel-math')
    }
    stages {
        stage('Unit Tests') {
            steps {
                sh 'tests/testit.sh unit --junit-xml test-reports/results.xml'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-reports/results.xml', fingerprint: true
                }
            }
        }
        stage('Functional Tests') {
            steps {
                sh 'tests/testit.sh functional --junit-xml test-reports/results.xml'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-reports/results.xml', fingerprint: true
                }
            }
        }
    }
}