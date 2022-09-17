# Manifest that kills the killmenow process
exec { 'killmenow':
    command => '/bin/pkill killmenow'
}
