node {  
    checkout scm
    echo 'before'
    def branch = getBranchName()
    echo 'after'
    
    stage('Check Version') {
        echo "branch: ${branch}"
    }

    if (isaPullRequest(branch) || isaMerge(branch)) {
        echo "Run the Tests here"
    }
    if (isaMerge(branch)) {
        echo "Do the Docker Push here"
    }
    def imageName = getImageName() 
    if (!imageExists(imageName)) {
        echo "Image has not been built"
    }
    echo "imageName: ${imageName}"
    echo 'AT THE END'
}

// Get the current Git branch name by running the Git
// command to tell us what our current branch is.
// Returns the name of the branch.
def getBranchName() {
    fullbr = "${sh(script:'git name-rev --name-only HEAD', returnStdout: true)}"
    echo "branch: ${fullbr}"
    branch = fullbr.substring(fullbr.lastIndexOf('/') + 1, fullbr.length()).trim()
    echo "branch: ${branch}"
    return branch
}

def isaMerge(branch) {
    rtn = false
    if (branch == 'master') {
        rtn = true
    }
    return rtn
}

def isaPullRequest(branch) {
    openPulls = sh(
        script: "curl 'https://api.github.com/repos/fckuligowski/abagdemo/pulls?state=open' -o pulls.json",
        returnStdout: true
    )
    // echo "openPulls: ${openPulls}"
    branchPulls = sh(
        script: "jq '.[] .head.ref' pulls.json",
        returnStdout: true
    )
    echo "branchPulls: ${branchPulls}"
    rtn = false
    if (branchPulls.indexOf(branch) >= 0) {
        echo 'This is a Pull Request'
        rtn = true
    }  
    cleanup = sh(
        script: "rm pulls.json",
        returnStdout: true
    )
    return rtn
}

def getImageName() {
    rtn = ''
    images = sh(
        script: "grep 'image:' k8s/abagdemo-deploy.yaml",
        returnStdout: true
    ).split('\n')
    echo "images: ${images}"
    if (images.size() > 0) {
        imageStr = images[images.size()-1]
        imageStrs = imageStr.split(' ')
        rtn = imageStrs[imageStrs.size()-1]
    }
    return rtn
}

def imageExists(imageName) {
    iparts = imageName.split(':')
    repo = iparts[0]
    tag = iparts[1]
    withCredentials([usernamePassword(credentialsId: 'docker-fckuligowski', usernameVariable: 'UNAME', passwordVariable: 'UPASS')]) {
        echo "repo: ${repo}, tag: ${tag}, UNAME=${UNAME}, UPASS=${UPASS}"
        dataMap = "{'username': \"'${UNAME}'\", 'password': ''${UPASS}''}"
        echo "dataMap: ${dataMap}"
        //token = sh(
        //    script: "curl -s -H 'Content-Type: application/json' -X POST -d ${dataMap} https://hub.docker.com/v2/users/login/ | jq -r .token",
        //    returnStdout: true
        //)
        token = sh(
            script: "curl -s -H \\\"Content-Type: application/json\\\" -X POST -d '{\\\"username\\\": \\\"'${UNAME}'\\\", \\\"password\\\": \\\"'${UPASS}'\\\"}' https://hub.docker.com/v2/users/login/ | jq -r .token",
            returnStdout: true
        )
        echo "token: ${token}"
        // create payload
        httpCreds = """
            {"username": "$UNAME",
             "password": "$UPASS"}
        """
        echo "httpCreds: ${httpCreds}"
        response = httpRequest httpMode: 'POST', requestBody: httpCreds, url: "https://hub.docker.com/v2/users/login", acceptType: 'APPLICATION_JSON', contentType: 'APPLICATION_JSON'
        echo "response: ${response.getContent()}"
        responseBody = response.getContent()
        token = responseBody.token
        echo "token: ${token}"
    }
}