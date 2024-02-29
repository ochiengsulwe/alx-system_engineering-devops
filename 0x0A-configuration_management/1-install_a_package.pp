# Puppet manifest to install Flask version 2.1.0 using pip3
# Install flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install Werkzeug 2.0.
package { 'werkzeug':
    ensure   => '2.0.3',
    provider => 'pip3',
}
