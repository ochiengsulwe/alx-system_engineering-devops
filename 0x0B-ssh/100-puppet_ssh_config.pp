# A puppet manifest that makes changes to a config file
file { '~/ubuntu.ssh/config':
  ensure  => file,
  content => "\
Host 13422-web-01
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
  owner   => ubuntu,
  group   => ubuntu,
  mode    => '0600',
}
