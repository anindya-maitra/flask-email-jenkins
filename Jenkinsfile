pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = "1"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install pytest'
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                sh 'sudo docker build -t anindyamaitra/flask-app:latest .'
                sh 'sudo docker run -it -p 1234:5000 anindyamaitra/flask-app:latest'
            }
        }

        stage('Test') {
            steps {
                script {
                    sh '. venv/bin/activate'
                    sh 'pytest'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf venv'
        }

        success {
            echo 'Build and tests succeeded!'
            mail to: 'anindyamaitra007@gmail.com',
                 subject: "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Job URL: ${env.BUILD_URL}\n\nBuild was successful."
        }

        failure {
            echo 'Build or tests failed.'
            mail to: 'anindyamaitra007@gmail.com',
                 subject: "FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Job URL: ${env.BUILD_URL}\n\nBuild failed. Please check the logs."
        }

        // Optionally, you can add more conditions like 'unstable' for unstable builds
    }
}
