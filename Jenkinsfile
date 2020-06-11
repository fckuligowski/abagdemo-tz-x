node {  
    checkout scm
    echo 'before'
    def branch = getBranchName()
    echo 'aftr'
    
    def imageName = getImageName()

    stage('Check Version') {
        echo "branch: XX${branch}XX"
        if (branch == 'master') {
            echo 'This is a Merge'
        } else {
            echo 'This is a Pull Request'
        }
    }

    
    echo 'AT THE END'
}

def getBranchName() {
    fullbr = "${sh(script:'git name-rev --name-only HEAD', returnStdout: true)}"
    echo "branch: ${fullbr}"
    branch = fullbr.substring(fullbr.lastIndexOf('/') + 1, fullbr.length())
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