pipeline {
    agent any

    environment {
        PYTHON = "/usr/bin/python"  // Change if needed
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vigneshrajahart/B12-CI-CD-Pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh "${PYTHON} -m pip install --upgrade pip"
                sh "${PYTHON} -m pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                sh "${PYTHON} -m pytest"
            }
        }

        stage('Deploy') {
            steps {
                sh """
                pkill -f 'flask run' || true
                export FLASK_APP=app.py
                nohup ${PYTHON} -m flask run --host=0.0.0.0 --port=5000 &
                """
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
        success {
            echo "Deployment Successful!"
        }
        failure {
            echo "Pipeline Failed!"
        }
    }
}
