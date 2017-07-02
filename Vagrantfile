# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "debian/jessie64"

  ENV['LC_ALL']="en_US.UTF-8"

  config.vm.provider :virtualbox do |vb|
    vb.memory = 1024 * 2
  end

  $script = <<-SCRIPT
  echo "deb http://ftp.us.debian.org/debian testing main contrib non-free" > /etc/apt/sources.list.d/testing.list
  echo > /etc/apt/apt.conf.d/90forceyes
  echo "APT::Get::Assume-Yes \"true\";" >> /etc/apt/apt.conf.d/90forceyes
  echo "APT::Get::force-yes \"true\";" >> /etc/apt/apt.conf.d/90forceyes
  export DEBIAN_FRONTEND=noninteractive
  apt-get update
  apt-get autoremove
  apt-get -f install
  apt-get upgrade
  apt-get install atool git build-essential autoconf ncurses-dev

  # Scala/Akka

  apt-get install -y openjdk-8-jdk
  test -e scala-2.11.6.tgz || wget https://downloads.lightbend.com/scala/2.11.6/scala-2.11.6.tgz
  aunpack scala-2.11.6.tgz
  echo 'PATH="/home/vagrant/scala-2.11.6/bin:$PATH"' >> /home/vagrant/.bashrc

  # Erlang

  cd /vagrant
  cp -r otp* /home/vagrant
  cd /home/vagrant

  cd otp-default
  ./otp_build autoconf
  ./configure
  make clean
  make
  cd ..

  cd otp-msg
  ./otp_build autoconf
  ./configure
  make clean
  make
  cd ..

  cd otp-systemtap
  ./otp_build autoconf
  ./configure
  make clean
  make
  cd ..

  # dont include Erlang bin in PATH; must call them using explicit path
  # /home/vagrant/otp-default/bin
  # /home/vagrant/otp-msg/bin
  # /home/vagrant/otp-systemtap/bin

  # Pony

  apt-get install zlib1g-dev libssl-dev llvm-3.8-dev libpcre2-dev
  test -e ponyc || git clone --depth 1 https://github.com/jupvfranco/ponyc.git
  cd ponyc
  make clean; make
  make use=telemetry clean; make use=telemetry
  make use=telemetry clean; make use=telemetry
  make use=no_gc clean; make use=no_gc

  # dont include pony release in PATH; must call them using explicit path
  # /home/vagrant/ponyc/build/release
  # /home/vagrant/ponyc/build/release-telemetry

  SCRIPT

  config.vm.provision "shell", inline: $script

end
