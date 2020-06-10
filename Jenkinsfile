node {  
    checkout scm

    def customImage = docker.build("fckuligowski/abagdemo:v1.1.${env.BUILD_ID}")

    customImage.inside {
        withCredentials([file(credentialsId: 'hazel-math', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
            try {
                stage('Unit Tests') {
                    sh 'tests/testit.sh unit --junit-xml test-reports/results.xml'
                }
            } finally {
                junit allowEmptyResults: true, testResults: 'test-reports/results.xml'
            }
            try {
                stage('Functional Tests') {
                    sh 'tests/testit.sh functional --junit-xml test-reports/results.xml'
                }
            } finally {
                junit allowEmptyResults: true, testResults: 'test-reports/results.xml'
            }
        }
    }

    customImage.push('latest')
    echo 'AT THE END'
}