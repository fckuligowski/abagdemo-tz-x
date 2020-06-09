node {
    stage('Example') {
        echo "branch: ${env.BRANCH_NAME}"
        if (env.BRANCH_NAME == 'master') {
            echo 'I only execute on the master branch'
        } else {
            echo 'I execute elsewhere'
        }
    }
}