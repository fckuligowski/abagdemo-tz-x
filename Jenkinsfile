node {  
    checkout scm
    
    def imageTag = "fckuligowski/abagdemo:${env.BUILD_ID}"

    def imageName = getImageName()

    def customImage = docker.build(imageTag)

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

    // docker.withRegistry('', 'docker-fckuligowski') {
    //    customImage.push()
    // }
    
    echo 'AT THE END'
}

def getImageName() {
    images = sh(
        script: "git diff origin/master -- k8s/abagdemo-deploy.yaml",
        returnStdout: true
    ).split('\n')
    echo "images: " images
}