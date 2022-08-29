/* groovylint-disable-next-line CompileStatic */
pipeline {
    agent
    stages {
        stage('Clone stage') {
            steps {
                git credentialsId: 'hook-3', url: 'https://github.com/quang123654/CrawlDataPython.git'
            }
        }

        stage('Build') {
            steps {
                withDockerRegistry(credentialsId: 'docker-hub', url: 'https://index.docker.io/v1/') {
                    sh label: '', script: 'docker build -t quanglathe/crawldatap:v10 .'
                    sh label: '', script:  'docker push quanglathe/crawldatap:v10'
                }
            }
        }
    }
}

