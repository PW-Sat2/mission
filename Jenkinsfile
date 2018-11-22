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
                    sshPublisher(publishers: [
                        sshPublisherDesc(
                            configName: 'gajoch.pl', 
                            transfers: [
                                sshTransfer(
                                    cleanRemote: true, 
                                    excludes: '', 
                                    execCommand: '', 
                                    execTimeout: 120000, 
                                    latten: false, 
                                    makeEmptyDirs: true, 
                                    noDefaultExcludes: false, 
                                    patternSeparator: '[, ]+', 
                                    remoteDirectory: "WWW/mission/${env.BRANCH_NAME}", 
                                    remoteDirectorySDF: false, 
                                    removePrefix: '', 
                                    sourceFiles: '**/*.*'
                                )
                            ], 
                            usePromotionTimestamp: false, 
                            useWorkspaceInPromotion: false, 
                            verbose: false
                        )
                    ])
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