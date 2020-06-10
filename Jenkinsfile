node {  
    checkout scm

    def customImage = docker.build("fckuligowski/abagdemo:${env.BUILD_ID}")

    customImage.inside {
        withCredentials([file(credentialsId: 'hazel-math', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
            sh 'printenv'
            sh 'head -4 $GOOGLE_APPLICATION_CREDENTIALS'
                stage('Unit Tests') {
                    steps {
                        sh 'tests/testit.sh unit --junit-xml test-reports/results.xml'
                    }
                    post {
                        always {
                            junit allowEmptyResults: true, testResults: 'test-reports/results.xml'
                        }
                    }
                }
                stage('Functional Tests') {
                    steps {
                        sh 'tests/testit.sh functional --junit-xml test-reports/results.xml'
                    }
                    post {
                        always {
                            junit allowEmptyResults: true, testResults: 'test-reports/results.xml'
                        }
                    }
                }
        }
    }
}