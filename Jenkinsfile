pipeline {
  agent any
  stages {
    stage('helm list') {
      steps {
        sh 'kubectl get pods --all-namespaces'
      }
    }
    stage('draft up') {
      steps {
        sh 'draft up'
      }
    }
  }
}