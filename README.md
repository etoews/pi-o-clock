# Pi O'Clock

An alarm clock for the Raspberry Pi.

![Pi O'Clock](clock/static/pi-o-clock.png)

Deployed on a Raspberry Pi Model B 2011.12 running Raspbian 2015-05-05

## Features

Development is ongoing.

* [x] Alarms
* [x] Play songs
* [ ] Tell the weather
* [ ] Tell a joke
* [ ] Words of wisdom
* [ ] Say something random
* [ ] Pester your children
* [ ] LED clock display

## Install

On a Raspberry Pi:

```
sudo apt-get -y update; sudo apt-get -y upgrade
sudo apt-get -y install python-dev python-pip mpg123 supervisor
sudo dpkg-reconfigure tzdata
git clone git@github.com:everett-toews/pi-o-clock.git
cd pi-o-clock
sudo cp pi-o-clock.conf /etc/supervisor/conf.d/
sudo pip install --upgrade pip
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install ipython
sudo reboot
```

## Run

On a Raspberry Pi:

```
cd pi-o-clock
source venv/bin/activate
sudo /home/pi/pi-o-clock/venv/bin/python /home/pi/pi-o-clock/manage.py runserver --no-reload --host 0.0.0.0 --port 80
```

### Supervisor

```
service supervisor status
sudo supervisorctl status pi-o-clock
sudo supervisorctl update pi-o-clock
sudo supervisorctl start pi-o-clock
sudo supervisorctl restart pi-o-clock

# on pi-o-clock.conf file changes
sudo supervisorctl reread
sudo supervisorctl update
```

## Develop

On a Mac:

Install [FUSE and SSHFS](https://osxfuse.github.io/)

```
ssh-keygen -t rsa -b 4096 -N '' -f ~/.ssh/id_rsa.clock
mkdir -p ~/dev/sshfs/pi-o-clock
sshfs -o IdentityFile=~/.ssh/id_rsa.clock pi@raspberry.pi.ip.address:pi-o-clock ~/dev/sshfs/pi-o-clock/

cd pi-o-clock
source venv/bin/activate
python -m unittest discover tests
python manage.py runserver --debug

cd ..
sudo umount pi-o-clock
```
