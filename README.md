# B12-CI-CD-Pipeline
TASK 1 : 1. Jenkins CI CD pipeline for flask application
# Python Web Application CI/CD Pipeline with Jenkins

This repository demonstrates a **CI/CD pipeline** for a Python web application using **Jenkins**. The pipeline automates the build, testing, and deployment processes, ensuring a reliable workflow for application updates.

---

## Table of Contents

1. [Prerequisites](#prerequisites)  
2. [Setup](#setup)  
3. [Jenkins Pipeline](#jenkins-pipeline)  
4. [Pipeline Stages](#pipeline-stages)  
5. [Triggers](#triggers)  
6. [Notifications](#notifications)  
7. [Repository Structure](#repository-structure)  
8. [Screenshots](#screenshots)  
9. [Usage](#usage)

---

## Prerequisites

Before setting up the pipeline, ensure you have the following:

- **Jenkins** installed on a virtual machine or cloud service ([Jenkins official](https://www.jenkins.io/))  
- **Python 3.x** installed on the Jenkins server  
- Required Python libraries (listed in `requirements.txt`)  
- A GitHub account to fork and clone the repository  
- SMTP access for email notifications (e.g., Gmail, Outlook, or company mail server)  

---

## Setup

1. **Fork the Repository**

   Fork the sample Python web application repository:  
   [Sample Python Web App](https://github.com/pallets/flask/tree/main/examples/tutorial)

2. **Clone the Forked Repository on Jenkins Server**

   ```bash
   git clone https://github.com/<your-username>/<forked-repo>.git
   cd <forked-repo>
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Jenkins Pipeline
A Jenkinsfile has been added to the root of the repository defining a declarative pipeline:

groovy
Copy code
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
            mail to: 'your-email@example.com',
                 subject: "Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Good news! The build succeeded."
        }
        failure {
            mail to: 'your-email@example.com',
                 subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Oops! The build failed. Check Jenkins for details."
        }
    }
}
Pipeline Stages
Build:

Creates a virtual environment

Installs Python dependencies

Test:

Runs unit tests using pytest

Deploy:

Deploys the application to the staging environment only if tests pass

Can be extended to deploy to production

Triggers
The pipeline is configured to trigger automatically whenever changes are pushed to the main branch.

Notifications
Email notifications are sent on build success or build failure.

Ensure the SMTP settings in Jenkins are configured correctly.

Repository Structure
css
Copy code
<forked-repo>/
│
├── Jenkinsfile
├── requirements.txt
├── README.md
├── app/
│   └── main.py
└── tests/
    └── test_app.py
Screenshots
Include screenshots showing the Jenkins pipeline UI:

Pipeline Overview

Build Stage Output

Test Stage Output

Deployment Stage Output

(Screenshots can be added here after running the pipeline.)

Usage
Push changes to the main branch.

Jenkins will automatically trigger the pipeline.

Monitor pipeline progress in the Jenkins dashboard.

Check email notifications for build results.