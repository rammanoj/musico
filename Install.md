## Collect Pre-requisites
Install `python-pip`, `python-dev` and `virtualenvwrapper`
```bash
sudo apt-get install python-pip python-dev
sudo -H pip install virtualenvwrapper
```
## Get the files
```bash
git clone https://github.com/rammanoj/musico
```
## Setup development environment
First, some initialization steps. Most of this only needs to be done
one time. You will want to add the command to source
`/usr/local/bin/virtualenvwrapper.sh` to your shell startup file
(`.bashrc` or `.zshrc`) changing the path to `virtualenvwrapper.sh`
depending on where it was installed by `pip`.
```bash
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
```
Lets create a virtual environment for our project
```bash
mkvirtualenv --python=`which python3` musics
workon musics
```
## Install requirements
All the requirements are mentioned in the file `requirements.txt`.
```bash
pip install -r requirements.txt
```

Now create the migrations
```bash
python manage.py makemigrations
```

Now run the migrations
```bash
python manage.py migrate
```

You can create a superuser with the command
```bash
python manage.py createsuperuser
```

and you can login to the app, after creating the superuser.

