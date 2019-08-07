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
        sh 'kubectl get pods --all-namespaces'
      }
    }
    stage("draft up") {
      steps {
        sh 'draft up'
      }
    }
  }
}