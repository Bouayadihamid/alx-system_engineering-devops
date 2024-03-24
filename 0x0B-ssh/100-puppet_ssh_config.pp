# Puppet configuration script
file_line {'PasswordAuthentication':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'PasswordAuthentication no',
  match    => '^PasswordAuthentication',
  provider => puppet,
}

file_line {'IdentityFile':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'IdentityFile ~/.ssh/school',
  match    => '^IdentityFile',
  provider => puppet,
}
