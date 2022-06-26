# Helloapp

Code language : Python

App Version : v1.0

### Introduction

This is a test webapp with some common functionalities to test various
needs for development, environment setup and devops tools connectivity
and workflows.

### Api's for the app

- Api to update the app version
  `http://localhost:5000/appver?val=<New-version>`

- Api to greet a user for the webapp
  `http://localhost:5000/greet/<name>`
  `http://localhost:5000/api/greet/<name>`

- Api for server info
  `http://localhost:5000/api/info`

### Functionalities

1. Update app version
2. Greet user with POST method
3. Get server info, once deployed on Kubernetes
4. Use with gui or with api based on need and workflow
