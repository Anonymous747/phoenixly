pipeline {
    agent none
    triggers {
        pollSCM '* * * * *'
    }
    stages {
//         stage('Initial'){
//             def dockerHome = tool 'myDocker'
//             env.PATH = "${dockerHome}/bin:${env.PATH}"
//         }
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                    sh 'python WebChecker.py'
                }
            }
            post {
                always {
                    junit 'output.xml'
                }
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
               sh 'python -v'
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}