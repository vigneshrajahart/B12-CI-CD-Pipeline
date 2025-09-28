pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Setting up virtual environment and installing dependencies...'
                // Create virtual environment
                sh 'python -m venv venv'
                // Upgrade pip
                sh '${VENV_DIR}/bin/pip install --upgrade pip'
                // Install dependencies
                sh '${VENV_DIR}/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests using pytest...'
                // Run tests
                sh '${VENV_DIR}/bin/pytest tests/'
            }
        }

        stage('Deploy') {
            when {
                branch 'main' // Only deploy from main branch
            }
            steps {
                echo 'Deploying to staging environment...'
                // Example deployment command
                sh 'echo "Deploying application to staging server..."'
                // Here you can add commands like scp, docker-compose, kubectl, etc.
            }
        }
    }

    post {
        success {
            echo 'Build, test, and deployment succeeded!'
            // Optional: add email notification here
        }
        failure {
            echo 'Pipeline failed!'
            // Optional: add email notification here
        }
    }
}
