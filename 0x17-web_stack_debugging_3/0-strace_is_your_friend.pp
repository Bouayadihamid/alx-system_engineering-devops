# Automation for the error 500 using Puppet.
$file_path = '/var/www/html/wp-settings.php'
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => ['/bin','/usr/bin']
}
