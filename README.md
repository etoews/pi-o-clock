# Pi Clock

Alarm clock for the Raspberry Pi.

Written on a Raspberry Pi Model B 2011.12 running Raspbian 2015-05-05

## Installation

On a Raspberry Pi:
1. sudo apt-get update
1. sudo apt-get -y upgrade
1. sudo dpkg-reconfigure tzdata
1. git clone git@github.com:everett-toews/pi-clock.git
1. sudo reboot

On a Mac:
1. Install [FUSE and SSHFS](https://osxfuse.github.io/)
1. mkdir -p ~/dev/sshfs/clock
1. sshfs -o IdentityFile=id_rsa.clock pi@clock.wkx.io:pi-clock ~/dev/sshfs/pi-clock/
