import groovy.json.JsonSlurper
node {  
    checkout scm
    echo 'before'
    def branch = getBranchName()
    echo 'aftr'
    
    allbr = sh(
        script: "curl https://api.github.com/repos/fckuligowski/abagdemo/pulls?state=open",
        returnStdout: true
    )
    // echo "allbr: ${allbr}"

    def jsonSlurper = new JsonSlurper()
    pulls = jsonSlurper.parseText(allbr)
    echo 'pulls: ${pulls}'


    def imageName = getImageName()

    stage('Check Version') {
        echo "branch: ${branch}"
        echo "env: ${env}"
        if (branch == 'master') {
            echo 'This is a Merge'
        } else {
            echo 'This is a Pull Request'
        }
        echo "Environment Vars:"
        echo sh(returnStdout: true, script: 'env')
    }

    
    echo 'AT THE END'
}

def getBranchName() {
    fullbr = "${sh(script:'git name-rev --name-only HEAD', returnStdout: true)}"
    echo "branch: ${fullbr}"
    branch = fullbr.substring(fullbr.lastIndexOf('/') + 1, fullbr.length()).trim()
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