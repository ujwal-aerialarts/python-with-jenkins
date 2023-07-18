pipeline {
    agent any
    triggers {
        cron('H/3 * * * *') // Run the pipeline every day at midnight (00:00)
    }
    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                checkout scm
            }
        }
        // Add more stages for your build and test process
    }
}
