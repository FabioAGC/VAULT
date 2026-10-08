
### Instalar essa merda
yay -S flutter

sudo pacman -S jdk17-openjdk
sudo groupadd flutterusers
sudo gpasswd -a $USER flutterusers
sudo chown -R :flutterusers /opt/flutter
sudo chmod -R g+w /opt/flutter/

yay -S android-sdk android-sdk-platform-tools android-sdk-build-tools android-sdk-cmdline-tools-latest android-platform

flutter doctor --android-licenses

flutter doctor