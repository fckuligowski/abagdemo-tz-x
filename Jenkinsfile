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
    /* properties([
        parameters([
            gitParameter(branch: '',
                branchFilter: 'origin/(.*)',
                defaultValue: 'masterXXXX',
                description: '',
                name: 'BRANCH',
                quickFilterEnabled: false,
                selectedValue: 'NONE',
                sortMode: 'NONE',
                tagFilter: '*',
                type: 'PT_BRANCH')
        ])
    ])
    echo "br1: ${params.BRANCH}"
    echo "br2: ${parameters.BRANCH}"
    branch = "${params.BRANCH}" */
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