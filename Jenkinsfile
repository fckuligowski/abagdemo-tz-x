// Define the method to parse JSON results
// This library must be approved in Jenkins
// Manage Jenkins -> In-process Script Approval
import groovy.json.JsonSlurperClassic 

@NonCPS
def jsonParse(def json) {
    new groovy.json.JsonSlurperClassic().parseText(json)
}

// Begin main Pipeline process
node {  
    checkout scm

    // Determine the current GitHub branch that we are on
    def branch = getBranchName()
    
    // Determine if we are doing a PR and/or Merge
    def doingPR = isaPullRequest(branch)
    def doingMerge = isaMerge(branch)

    // Build the Docker Image so we can test with it
    def imageName = getImageFullName()
    def imageRepo = getImageRepo(imageName)
    def imageTag = "${imageRepo}:${env.BUILD_ID}"
    echo "Build Tag: ${imageTag}"
    def customImage = docker.build(imageTag)
    
    // Testing section
    customImage.inside {
        withCredentials([file(credentialsId: 'hazel-math', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
            // Unit Tests
            stage('Unit Tests') {
                if (doingPR || doingMerge) {
                    echo "Running the Unit Tests"
                    try {
                        sh 'tests/testit.sh unit --junit-xml test-reports/results.xml'
                    } finally {
                        junit allowEmptyResults: true, testResults: 'test-reports/results.xml'
                    }
                    echo "Ran the Unit Tests"
                }
            }
            // Functional Tests
            stage('Functional Tests') {
                if (doingPR || doingMerge) {
                    echo "Running the Functional Tests"
                    try {
                        sh 'tests/testit.sh functional --junit-xml test-reports/results.xml'
                    } finally {
                        junit allowEmptyResults: true, testResults: 'test-reports/results.xml'
                    }
                    echo "Ran the Functional Tests"
                }
            }
        }
    }

    // Push Container to Repo if this is a GitHub Merge
    // and if the Image Tag doesn't already exist in Docker.
    def newImage = false
    stage('Push Container Image to Repo') {
        if (doingMerge) {
            if (!imageExists(imageName)) {
                echo "Push Container to Docker Repo"
                imageTag = getImageTag(imageName)
                echo "Push Tag: ${imageTag}"
                docker.withRegistry('', 'docker-fckuligowski') {
                    customImage.push(imageTag)
                }
                newImage = true
            } else {
                echo "Image ${imageName} already exists in repo"
            }
        }
    }
    
    // Add a version tag to the GitHub repo
    stage('Tag GitHub repo') {
        if (newImage) {
            imageTag = getImageTag(imageName)
            addGitHubTag(imageTag)
        }
    }
    echo 'AT THE END'
}

// Get the current Git branch name by running the Git
// command to tell us what our current branch is.
// Returns the name of the branch.
def getBranchName() {
    fullbr = "${sh(script:'git name-rev --name-only HEAD', returnStdout: true)}"
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
    // Get a list of open PRs for the GitHub repo
    openPulls = sh(
        script: "curl 'https://api.github.com/repos/fckuligowski/abagdemo/pulls?state=open' -o pulls.json",
        returnStdout: true
    )
    // Find if any of those PRs are for the Branch we're on
    branchPulls = sh(
        script: "jq '.[] .head.ref' pulls.json",
        returnStdout: true
    )
    echo "branchPulls: ${branchPulls}"
    // If there is an open PR for this Branch then we
    // consider that yes, there is an open PR
    rtn = false
    if (branchPulls.indexOf(branch) >= 0) {
        echo 'This is a Pull Request'
        rtn = true
    }  
    // Remove the temp file
    cleanup = sh(
        script: "rm pulls.json",
        returnStdout: true
    )
    return rtn
}

// Extract the full container image name from the releases file.
// It comes from two fields - image.repository and image.tag.
def getImageFullName() {
    repo = ''
    releaseFile = 'releases/abagdemo.yaml'
    repos = sh(
        script: "grep 'repository:' ${releaseFile}",
        returnStdout: true
    ).split('\n')
    echo "repository: ${repos}"
    if (repos.size() > 0) {
        repoStr = repos[repos.size()-1]
        repoStrs = repoStr.split(' ')
        repo = repoStrs[repoStrs.size()-1]
    }
    tag = ''
    tags = sh(
        script: "grep 'tag:' ${releaseFile}",
        returnStdout: true
    ).split('\n')
    echo "tag: ${tags}"
    if (tags.size() > 0) {
        tagStr = tags[tags.size()-1]
        tagStrs = tagStr.split(' ')
        tag = tagStrs[tagStrs.size()-1]
    }
    rtn = "${repo}:${tag}"
    echo "getImageFullName: ${rtn}"
    return rtn
}

def getImageRepo(imageFullName) {
    iparts = imageFullName.split(':')
    repo = iparts[0]
    tag = iparts[1]
    return repo
}

def getImageTag(imageFullName) {
    iparts = imageFullName.split(':')
    tag = iparts[1]
    return tag
}

// Call the Docker API to see if the specified container Image 
// already exists.
def imageExists(imageName) {
    rtn = false
    iparts = imageName.split(':')
    repo = getImageRepo(imageName)
    tag = getImageTag(imageName)
    withCredentials([usernamePassword(credentialsId: 'docker-fckuligowski', usernameVariable: 'UNAME', passwordVariable: 'UPASS')]) {
        echo "repo: ${repo}, tag: ${tag}, UNAME=${UNAME}, UPASS=${UPASS}"
        // Get Docker login token
        // create payload
        httpCreds = """
            {"username": "$UNAME",
             "password": "$UPASS"}
        """
        echo "httpCreds: ${httpCreds}"
        // Call API to get login Token for next API call
        response = httpRequest httpMode: 'POST', requestBody: httpCreds, 
            url: "https://hub.docker.com/v2/users/login", 
            acceptType: 'APPLICATION_JSON', contentType: 'APPLICATION_JSON'
        // Parse Token from result
        responseBody = response.getContent()
        responseMap = jsonParse(responseBody)
        token = responseMap.token
        echo "token: ${token}"
        // Call API to get list of Images in Repo
        response = httpRequest customHeaders: [[name:'Authorization', value:"JWT ${token}"]],
            url: "https://hub.docker.com/v2/repositories/${repo}/tags/?page_size=10000", 
            acceptType: 'APPLICATION_JSON'
        // Parse results and determine if our Tag is already in Repo results
        responseBody = response.getContent()
        responseMap = jsonParse(responseBody)  
        for (img in responseMap.results) {
            if (img.name == tag) {
                rtn = true
            }
        }
    }
    echo "imageExists - repo: ${repo}, tag: ${tag}, return: ${rtn}"
    return rtn
}

def addGitHubTag(imageTag) {
    withCredentials([usernamePassword(credentialsId: 'fckuligowski-git', 
        passwordVariable: 'GIT_PASSWORD', 
        usernameVariable: 'GIT_USERNAME')]) {
            // Add a Tag to the Git repo to mark our new version
            sh "git tag -a ${imageTag} -m 'abagdemo version ${imageTag}'"
            sh "git push 'https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/fckuligowski/abagdemo' --tags"
    }
}