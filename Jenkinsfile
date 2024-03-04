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
                    // sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }

        stage('Test') {
            steps {
                script {
                    // sh 'pytest'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
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
