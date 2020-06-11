node {  
    checkout scm
    
    def imageName = getImageName()

    stage('Check Version') {
        if (env.'CHANGE_ID' == '') {
            echo 'This is a Pull Request'
        } else {
            echo 'This is a Merge'
        }
        sh 'printenv'
        echo "change_id: ${CHANGE_ID}"
    }

    
    echo 'AT THE END'
}

def getImageName() {
    images = sh(
        script: "git diff origin/master -- k8s/abagdemo-deploy.yaml",
        returnStdout: true
    ).split('\n')
    echo "images: ${images}"
}