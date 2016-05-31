Wellthy
=======

[![Circle CI](https://circleci.com/gh/Wellthy/wellthy.com/tree/integration.svg?style=svg&circle-token=f1c95a443fb487665798ade66df37e934c471ff4)](https://circleci.com/gh/Wellthy/wellthy.com/tree/integration)
[![codecov](https://codecov.io/gh/Wellthy/wellthy.com/branch/integration/graph/badge.svg?token=33cql26hiz)](https://codecov.io/gh/Wellthy/wellthy.com)

## Set Up Docker

Follow directions to [install docker on Mac OS X](https://docs.docker.com/installation/mac/)  

## Clone This repo

> You will end up with a REPO_DIR of ./wellthy.com, unless you name it
something else.  It's recommended to put your working area inside a Dropbox folder so it is backed up even between commits.

```sh
$ cd ~/Dropbox/Code
// if cloning with https
$ git clone https://github.com/Wellthy/wellthy.com.git
// if cloning with ssh [set this up for use with 2FA](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
$ git clone git@github.com:Wellthy/wellthy.com.git
$ cd [REPO_DIR]
$ git checkout integration
```

## Create Docker containers

```sh
$ pwd
  -> ~/Dropbox/Code/[REPO_DIR]
$ docker-compose up -d
```

## Make Things Easy on Yourself

Docker is now running on its default ip. This is fine and works but its much
nicer to have a more readable domain to be developing on:

```sh
$ docker-machine ip default
  -> [DEV_IP]
```

Once you know [DEV_IP], you should update to point dev.wellthy.com to it:

```sh
$ sudo vim /etc/hosts
// enter your password
```

Then you'll need to modify the file by adding the line:

```sh
127.0.0.1       localhost
.
.
.
[DEV_IP]        dev.wellthy.com

```

## Set Up Node and Get To Work

Install homebrew if not already installed:
```sh
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

You will need `node` and OSX build tools (gcc, clang).

```sh
$ xcode-select -p
// if not installed, then do
$ xcode-select --install
// otherwise
$ brew install node
$ cd [REPO_DIR]/wellthy/static
$ npm install
$ ./node_modules/.bin/gulp watch
// this listens for code changes, so you'll probably want to use screen
```

You can optionally install gulp globally which shortens your command:

```sh
$ npm install gulp -g
$ cd [REPO_DIR]/wellthy/static
$ gulp watch
// this listens for code changes, so you'll probably want to use screen   
```
Now you're ready to get to work!

## Testing

Use the following command to run the tests locally:
```sh
docker exec -it wellthycom_web_1 /bin/bash -c 'source /venv/bin/activate && python manage.py test'
```


## Blog

To work on changes to the blog theme, you can update the files directly in `.docker/ghost/themes/wellthy-dev`.  If you need to change default.hbs, you should modify it in `wellthy/templates/blog` and then have it rendered and copied to your Ghost container using:
```sh
$ docker exec -it wellthycom_web_1 /bin/bash -c 'source /venv/bin/activate && python manage.py build_ghost'
```
To deploy changes to the blog theme, copy from `.docker/ghost/themes/wellthy-dev` to `.docker/ghost/themes/wellthy` and ensure default.hbs points to the production domain throughout.  Commit the changes for version management purposes and once the pull request is approved, the wellthy theme folder should be zipped and uploaded to our Ghost(Pro) account.

## Notes

* Start the docker environment by launching the Docker Quickstart Terminal app or by running:
```sh
. '/Applications/Docker/Docker Quickstart Terminal.app/Contents/Resources/Scripts/start.sh'
```
* Bring up your docker container by running:
```
docker-compose up -d
```
* Stop the docker environment by closing the Terminal window
* `gulp build` builds minified files to the `[REPO_DIR]/wellthy/static/public` directory suitable for a production build
* `gulp watch` builds files to and runs collectstatic using `[REPO_DIR]/wellthy/static/build`. `gulp build` will still need to be run before committing for a production release. If you leave `gulp watch` running while working, it will automatically detect and compile changes to any files inside the static dir.
* If you change any python files and need them to get picked up, you can simply touch the wsgi file to get Apache to reload the changes:
```sh
$ touch [REPO_DIR]/wellthy/config/wsgi.py
```
* If you merge some changes that have a database migration, you should run:
```
docker exec -it wellthycom_web_1 /bin/bash -c 'source /venv/bin/activate && python manage.py migrate'
```
* If you need to install some new dependencies, you should run:
```
docker exec -it wellthycom_web_1 /bin/bash -c 'source /venv/bin/activate && pip install -r ../requirements/_base.txt'
```
* If you restart your laptop you'll need to:
   1. Launch the Docker Quickstart Terminal
   2. Run `docker-compose up -d` to bring up your docker containers
   3. Run `gulp watch` to build the static files


## When things go wrong

### Start from Scratch

Note that removing wellthycom_db_1 with the -v flag will delete your database and you'll have to repopulate it.
```
docker-compose stop
docker rm -v wellthycom_blog_1
docker rm -v wellthycom_web_1
docker rm -v wellthycom_db_1
docker rmi wellthycom_web

- Close terminal running docker environment
- Relaunch docker enviroment

docker-compose up -d
```

