# Pi Clock

Alarm clock for the Raspberry Pi.

Deployed on a Raspberry Pi Model B 2011.12 running Raspbian 2015-05-05

## Install

On a Raspberry Pi:

```
sudo apt-get -y update; sudo apt-get -y upgrade
sudo apt-get -y install python-dev python-pip mpg123 supervisor
sudo dpkg-reconfigure tzdata
git clone git@github.com:everett-toews/pi-clock.git
cd pi-clock
sudo cp pi-clock.conf /etc/supervisor/conf.d/
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
cd pi-clock
source venv/bin/activate
sudo /home/pi/pi-clock/venv/bin/python /home/pi/pi-clock/manage.py runserver --no-reload --host 0.0.0.0 --port 80
```

### Supervisor

```
service supervisor status
sudo supervisorctl status pi-clock
sudo supervisorctl update pi-clock
sudo supervisorctl start pi-clock
sudo supervisorctl restart pi-clock

# on pi-clock.conf file changes
sudo supervisorctl reread
sudo supervisorctl update
```

## Develop

On a Mac:

Install [FUSE and SSHFS](https://osxfuse.github.io/)

```
ssh-keygen -t rsa -b 4096 -N '' -f ~/.ssh/id_rsa.clock
mkdir -p ~/dev/sshfs/pi-clock
sshfs -o IdentityFile=~/.ssh/id_rsa.clock pi@pi.clock.ip.addr:pi-clock ~/dev/sshfs/pi-clock/

cd pi-clock
source venv/bin/activate
python -m unittest discover tests
python manage.py runserver --debug

cd ..
sudo umount pi-clock
```

