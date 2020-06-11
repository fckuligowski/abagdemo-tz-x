node {  
    checkout scm
    echo 'before'
    def branch = getBranchName()
    echo 'aftr'
    
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

def getBranchName() {
    branch = scm.branches[0].name
    echo "branch: ${branch}"
    return branch
}

def getImageName() {
    images = sh(
        script: "git diff origin/master -- k8s/abagdemo-deploy.yaml",
        returnStdout: true
    ).split('\n')
    echo "images: ${images}"
}