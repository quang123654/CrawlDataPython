pipeline {

    agent any

    stages {

        stage('pre-install') {

            steps {

                sh "sudo apt update"

                sh "sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev"

            }

        }

        stage('install-python') {

            steps {

                sh "curl -O https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tar.xz"

                sh "tar -xf Python-3.8.12.tar.xz"

                sh "cd Python-3.8.12 && ./configure --enable-optimizations && make -j 4 && sudo make altinstall || sudo make install"

                sh "python3.8 --version"

            }

        }

        stage('Install python required libraries') {

            steps {

                sh "sudo apt install -y python3 python3-dev python3-pip"

                sh "sudo apt install -y libxml2-dev libxslt-dev musl-dev"

            }

        }

        stage('get project') {

            steps {

                sh "rm -rf lrn_jenkin"

                sh "git clone https://github.com/aresgowar/python-crawl-data.git lrn_jenkin"

                sh "cd lrn_jenkin && pip install -r requirements.txt"

            }

        }

    }

}