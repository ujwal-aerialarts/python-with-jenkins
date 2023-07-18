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
                        sh 'cat "VAR1=${VAR1}" > .env'
                    }
                }
        }

        stage('Run Pytest') {
            steps {
                // Use withPythonEnv to create and manage the virtual environment
                withPythonEnv("/usr/bin/python3.6") {
                    sh "pip install -r requirements.txt"
                    sh 'pytest --capture=tee-sys --junitxml=test-reports/results.xml --html=test-reports/report_$(date +"%Y%m%d_%H%M%S").html'
                }
            }
        }

    }

    post {
        always {
            junit 'test-reports/results.xml'

            publishHTML target: [
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: 'test-reports/',
                reportFiles: '*.html',
                reportName: 'HTML Report'
            ]
        }
    }
}
