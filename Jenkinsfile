pipeline {
    agent { dockerfile true }
    triggers {
        pollSCM '* * * * *'
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