pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'vikta-framework:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/mniewinskaGD/vikta.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("$DOCKER_IMAGE")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("$DOCKER_IMAGE").inside {
                        sh 'pytest --html=reports/report.html --self-contained-html -m"smoke"'
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }

        success {
            echo 'Tests passed!'
        }

        failure {
            echo 'Tests failed!'
        }
    }
}
