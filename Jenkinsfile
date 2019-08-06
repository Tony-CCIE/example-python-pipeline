pipeline {
  agent any
  stages {
    stage('clone') {
      steps {
        sh 'echo "hello world"'
      }
    }
    stage('helm list') {
      steps {
        echo 'hello k8s'
      }
    }
  }
}