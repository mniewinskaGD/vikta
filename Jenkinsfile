pipeline {
    agent any

    stages {
        stage('Start') {
            steps {
                echo "*****************Starting running tests****************"
            }
        }

        stage('Environment Info') {
            steps {
                script {
                    sh 'whoami'
                    sh 'pwd'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'which python3'
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo "********************Running tests*********"
                sh 'python3 -m pytest --html=reports/report.html --self-contained-html -m "smoke"'
            }
        }

        stage('Finish') {
            steps {
                script {
                    sh 'date'
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
