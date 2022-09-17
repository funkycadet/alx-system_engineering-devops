# Script to install flask from pip3 using puppet
exec { 'pip3-install-flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
}
