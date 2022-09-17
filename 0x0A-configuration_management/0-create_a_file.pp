# Script to create a file and assign properties in Puppet
file { 'school':
    path    => '/tmp/school',
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744'
}
