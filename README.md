# Pi O'Clock

An alarm clock for the Raspberry Pi.

[![Build Status](https://travis-ci.org/everett-toews/pi-o-clock.svg)](https://travis-ci.org/everett-toews/pi-o-clock)

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
sudo apt-get -y install build-essential python-dev python-pip mpg123 supervisor
sudo dpkg-reconfigure tzdata

sudo apt-get -y install i2c-tools libffi-dev
sudo sh -c 'echo "i2c-dev\ni2c-bcm2708" >> /etc/modules'
sudo sh -c 'echo "dtparam=i2c1=on\ndtparam=i2c_arm=on" >> /boot/config.txt'

git clone git@github.com:everett-toews/pi-o-clock.git
sudo cp /home/pi/pi-o-clock/pi-o-clock.conf /etc/supervisor/conf.d/

sudo pip install --upgrade setuptools
sudo pip install --upgrade pip
sudo pip install -r /home/pi/pi-o-clock/requirements.txt

git clone git@github.com:adafruit/Adafruit_Python_LED_Backpack.git
sudo python /home/pi/Adafruit_Python_LED_Backpack/setup.py install

sudo reboot
```

## Run

On a Raspberry Pi:

```
ssh -i ~/.ssh/id_rsa.clock pi@raspberry.pi.ip.address
cd pi-o-clock
git pull
sudo supervisorctl restart pi-o-clock
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
