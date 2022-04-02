# README #

[![Build and Deploy](https://github.com/ShockSoc/ShockSoc.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/ShockSoc/ShockSoc.github.io/actions/workflows/deploy.yml)

This repo contains the source for [shocksoc.org](http://www.shocksoc.org).

It uses Flask with Jinja2 for templating.

## Contributing ##


## Local Development ##
To edit and run locally, you will require a recent version of Python 3 and pip.

To install the dependancies system-wide, use `pip install -r requirements.txt`; you could also use a venv - I'm not.

### Running ###
To run a local development server, run `python3 shock.py`, and a server will be accessible on: [127.0.0.1:5000](http://127.0.0.1:5000)

### Building ###
To generate a static site with Frozen-Flask, run `python3 shock.py build`, and the files will be placed in the "build" directory.

### Deploying ###
Deployment is through a Github Action on push to `master`, which runs `deploy.sh` to build the site then push the built files to the "gh-deploy" branch. 
