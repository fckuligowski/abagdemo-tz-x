node {  
    // checkout scm
    git status
    
    def imageName = getImageName()

    stage('Check Version') {
        echo "branch: ${env.BRANCH_NAME}"
        if (env.'CHANGE_ID' == '') {
            echo 'This is a Pull Request'
        } else {
            echo 'This is a Merge'
        }
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