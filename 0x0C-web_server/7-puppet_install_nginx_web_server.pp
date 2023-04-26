# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "
server {
    listen 80;
    server_name localhost;

    location / {
        echo 'Hello World!';
    }

    location /redirect_me {
        return 301 https://example.com/new_page;
    }
}
",
}

# Enable the default Nginx site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Restart Nginx after configuration changes
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/sites-enabled/default'],
}

