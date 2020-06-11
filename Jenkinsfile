node {  
    checkout scm
    
    def imageTag = "fckuligowski/abagdemo:v1.1.${env.BUILD_ID}"

    writeFile file: 'version.txt', text: imageTag

    withCredentials([usernamePassword(credentialsId: 'fckuligowski-git', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
        sh "git checkout master"
        sh "git add ."
        sh "git status"
        sh "git commit -m 'update version ${env.BUILD_ID}'"
        sh('git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/fckuligowski/abagdemo.git --all')
    }

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

    docker.withRegistry('', 'docker-fckuligowski') {
        customImage.push()
    }
    
    echo 'AT THE END'
}