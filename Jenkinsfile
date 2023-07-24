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
            // agent {
            //     docker {
            //         image 'python:3-alpine'
            //     }
            // }
            steps {
                withPythonEnv("/usr/bin/python3.9") {
                    sh "pip install -r requirements.txt"
                    sh 'pytest -o log_cli=true --log-cli-level=INFO --junitxml=test-reports/results.xml --html=test-reports/report.html'
                }

                // sh "export PYTHONPATH=$WORKSPACE:$PYTHONPATH"
                // sh "python -m venv venv"
                // sh "source venv/bin/activate"
                // sh "pip install -r requirements.txt"
                // sh "pytest --junitxml=test-reports/results.xml --html=test-reports/report.html"
                // sh "deactivate"
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

            // Archive the HTML report for each build
            archiveArtifacts artifacts: 'test-reports/report.html', allowEmptyArchive: true
        }

        // Send email notification on failure
        failure {
            script {
                def recipients = 'woozaal7@gmail.com,ujwal.aerialarts@gmail.com' // List of email recipients separated by comma
                def htmlReportPath = "${JENKINS_HOME}/workspace/${JOB_NAME}/test-reports/report.html"
                emailext attachmentsPattern: htmlReportPath, attachLog: true, compressLog: true, subject: '$DEFAULT_SUBJECT', to: recipients, body: '$DEFAULT_CONTENT'
            }
        }
    }
}
