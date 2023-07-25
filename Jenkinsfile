pipeline {

    agent any

    triggers {
        cron('H/2 * * * *') // Run the pipeline every day at midnight (00:00)
    }

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
                        file(credentialsId: 'test_pytest_env', variable: 'DOT_ENV_FILE')
                    ]) {
                        // Write environment variables to .env file
                        sh "cat \${DOT_ENV_FILE} > .env"
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
                // def recipients = 'uzwalparajuli07+jenkins@gmail.com' // List of email recipients separated by comma
                def htmlReportPath = 'test-reports/report.html'
                def receivers = [
                    // The DevelopersRecipientProvider will include email addresses of developers who contributed to the changes in the build
                    [$class: 'DevelopersRecipientProvider'],

                    // The RequesterRecipientProvider will include the email address of the user who triggered the build
                    [$class: 'RequesterRecipientProvider'],

                    // The CulpritsRecipientProvider will include email addresses of users (culprits) who caused the build to fail
                    [$class: 'CulpritsRecipientProvider']
                ]
                emailext attachmentsPattern: htmlReportPath, attachLog: true, compressLog: true, subject: '$DEFAULT_SUBJECT', recipientProviders: receivers, body: '$DEFAULT_CONTENT'
            }
        }
    }
}
