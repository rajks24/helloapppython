# Helloapppython

![App Version : v2.0](https://img.shields.io/badge/version-2.0-green?style=flat-square) ![GitHub last commit](https://img.shields.io/github/last-commit/rajks24/helloapppython?style=flat-square) ![Python](https://img.shields.io/badge/python-3670A0?style=flat-square&logo=python&logoColor=ffdd54) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white) ![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=flat-square&logo=kubernetes&logoColor=white)

<hr>

### Introduction

This is a test api and webapp with some common functionalities to test various
needs for development, environment setup and devops tools connectivity
and workflows.

![helloapp snapshot](website/static/img/helloapppython.jpg "Helloapp Snapshot")

### Api's for the app

- Api to update the app version

  `http://localhost:5000/appver?val=<New-version>`

- Api to greet a user for the webapp

  `http://localhost:5000/greet/<name>`

  `http://localhost:5000/api/greet/<name>`

- Api for server info

  `http://localhost:5000/api/info`

### Functionalities

1. Update app version for the webapp ( by api)
2. Greet user with POST method ( via api and web)
3. Get server info, once deployed on Kubernetes (on homepage and via api in json format)
4. For running on Kubernetes, by using `kubectl kustomise` we can modify image (name & tag) and other configurable parans via updating kustomization.yaml in kubernetes folder.
5. This app can be built in 3 ways

   5.1 With gunicorn WSGI server - Dockerfile added.

   5.2 With python and Flask module only - Dockerfile added.

   5.3 With buildpack,

   - The build command can be overriden by Procfile in root folder.
   - Other params can be passed as command line options in build command.
   - The buildpack command to build OCI image for app using **pack** CLI locally using container runtime.

   ```
    $ pack build helloapp-img \
       --path ~/files/helloapppython \
       --env BP_CPYTHON_VERSION=3.9.13  \
       --buildpack paketo-buildpacks/python  \
       --builder paketobuildpacks/builder:full
   ```

   - The buildpack command to build OCI image for app using **kpack** [kp] CLI in kubernetes cluster configured with remote image registry.

     ```
     $ kp image create helloapppython \
        --tag registry.mylab.com/rsingh-lib/helloapppython \
        --cluster-builder default \
        --namespace helloapppython \
        --wait \
        --git https://github.com/rajks24/helloapppython.git \
        --git-revision main \
        --env BP_CPYTHON_VERSION=3.9.13
     ```

### TODOS

1. Add open api swagger

## Contact

You can reach me on [Twitter @rajinh24](https://twitter.com/rajinh24)

## License

[![Licence](https://img.shields.io/github/license/rajks24/markdown-badges?style=flat-square&logo=github)](./LICENSE)

<hr>
