pipeline {

    agent any

    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                checkout scm
            }
        }

        stage('Prepare Environment') {
                steps {
                    withCredentials([
                        string(credentialsId: 'UNIQUE_ID', variable: 'VAR1')
                    ]) {
                        // Write environment variables to .env file
                        sh 'echo "VAR1=${VAR1}" > .env'
                    }
                }
        }

        stage('Run Pytest') {
            steps {
                // Use withPythonEnv to create and manage the virtual environment
                withPythonEnv("/usr/bin/python3.6") {
                    sh "pip install -r requirements.txt"
                    sh "pytest"
                }
            }
        }
    }
}
