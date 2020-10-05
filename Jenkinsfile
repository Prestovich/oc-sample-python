pipeline {
  agent { docker { image 'python:3.7.2' }  } //agent type or label "pod"
  stages {
    stage('build') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('unit test') {
      steps {
        sh 'python3 unit_test.py'
      }   
    }
  }
}
