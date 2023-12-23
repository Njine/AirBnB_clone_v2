# Install Nginx package
package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
}

# Create directory structure for web_static
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
}

# Create HTML files
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Holberton School Puppet\n",
}

file { ['/var/www', '/var/www/html']:
  ensure => 'directory',
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School Nginx\n",
}

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n",
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

# Set ownership
exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}

# Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => template('path/to/nginx_config.erb'),
}

# Restart Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
