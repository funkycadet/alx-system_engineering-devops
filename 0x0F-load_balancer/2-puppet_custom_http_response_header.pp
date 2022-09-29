# Installs an Nginx server with custom HTTP header

exec {'update':
  command  => '/usr/bin/apt update',
}

exec {'install Nginx':
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

exec { 'add_header':
  command     => 'sed -i "25i\\\tadd_header X-Served-By \$hostname;" /etc/nginx/sites-available/default,
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  command  => 'sudo service nginx restart',
}
