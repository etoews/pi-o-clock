# Pi Clock

Alarm clock for the Raspberry Pi.

Written on a Raspberry Pi Model B 2011.12 running Raspbian 2015-05-05

## Install

On a Raspberry Pi:

```
sudo apt-get -y update; sudo apt-get -y upgrade
sudo apt-get -y install python-dev python-pip
sudo dpkg-reconfigure tzdata
git clone git@github.com:everett-toews/pi-clock.git
cd pi-clock
sudo pip install --upgrade pip
sudo pip install virtualenv
# system-site-packages for pygame
virtualenv --system-site-packages venv
source venv/bin/activate
pip install -r requirements.txt
sudo reboot
```

## Run

On a Raspberry Pi:

```
cd pi-clock
source venv/bin/activate
sudo venv/bin/python pi-clock/app.py runserver --host 0.0.0.0 --port 80
```

## Develop

On a Mac:

Install [FUSE and SSHFS](https://osxfuse.github.io/)

```
ssh-keygen -t rsa -b 4096 -N '' -f ~/.ssh/id_rsa.clock
mkdir -p ~/dev/sshfs/pi-clock
sshfs -o IdentityFile=~/.ssh/id_rsa.clock pi@pi.clock.ip.addr:pi-clock ~/dev/sshfs/pi-clock/
```
