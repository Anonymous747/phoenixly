pipeline {
    agent { docker { image 'python:3.10' } }
    triggers {
        pollSCM '* * * * *'
    }
    stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''

                pip install -r requirements.txt
                docker-compose up -d
                '''
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