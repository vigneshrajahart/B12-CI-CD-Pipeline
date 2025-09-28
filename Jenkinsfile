pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "${WORKSPACE}/venv"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Creating virtual environment and installing dependencies...'
                sh 'python3 -m venv venv'
                sh '${VIRTUAL_ENV}/bin/pip install --upgrade pip'
                sh '${VIRTUAL_ENV}/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '${VIRTUAL_ENV}/bin/pytest tests/'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying to staging environment...'
                # Add your deployment commands here
                sh 'echo "Deploying application..."'
            }
        }
    }

    post {
        success {
            mail to:'vignesh.vv11@gmail.com',
                 subject: "Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Good news! The build succeeded."
        }
        failure {
            mail to: 'vignesh.vv11@gmail.com',
                 subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Oops! The build failed. Check Jenkins for details."
        }
    }
}
