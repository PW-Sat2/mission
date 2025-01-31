pipeline {
    agent none
    options {
		skipDefaultCheckout() 
	}

    stages {
        stage('Build') {
            agent { label 'pwsat-build' }
            steps {
                deleteDir()

                checkout scm

                withEnv(['PATH+NODE=C:/Tools/node8', 'PATH+GITBOOK=C:/tools/gitbook/node_modules/.bin']) {
                    bat('gitbook install')
                    bat('node "plugins/gitbook-plugin-pwsat/summary.js"')
                    bat('gitbook build')
                }

                dir('_book') {
                    withEnv(['PATH+ZIP=C:/Program Files/7-Zip']) {
                        bat('7z a archive.zip .\\*')
                    }

                    retry(3) {
                        sshPublisher(publishers: [
                            sshPublisherDesc(
                                configName: 'gajoch.pl', 
                                transfers: [
                                    sshTransfer(
                                        cleanRemote: false, 
                                        excludes: '', 
                                        latten: false, 
                                        makeEmptyDirs: true, 
                                        noDefaultExcludes: false, 
                                        patternSeparator: '[, ]+', 
                                        remoteDirectory: "WWW/mission/${env.BRANCH_NAME}", 
                                        remoteDirectorySDF: false, 
                                        removePrefix: '', 
                                        sourceFiles: 'archive.zip',
                                        execCommand: "pwd && ls && cd WWW/mission/${env.BRANCH_NAME} && unzip -o archive.zip"
                                    )
                                ], 
                                usePromotionTimestamp: false, 
                                useWorkspaceInPromotion: false, 
                                verbose: false
                            )
                        ])
                    }
                }

                step([
                    $class: 'GitHubCommitStatusSetter', 
                    contextSource: [
                        $class: 'ManuallyEnteredCommitContextSource', 
                        context: 'jenkins/deploy'
                    ], 
                    statusBackrefSource: [
                        $class: 'ManuallyEnteredBackrefSource', 
                        backref: "http://mission.pw-sat.pl/${env.BRANCH_NAME}"
                    ], 
                    statusResultSource: [
                        $class: 'ConditionalStatusResultSource', 
                        results: [
                            [
                                $class: 'BetterThanOrEqualBuildResult', 
                                message: 'Deployed', 
                                result: 'SUCCESS', 
                                state: 'SUCCESS'
                            ]
                        ]
                    ]
                ])
            }
        }
    }
}