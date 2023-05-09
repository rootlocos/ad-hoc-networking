#
# install script for RPiAdHocWifi
#

# install required packages

# make backups of existing files
if [ -e /etc/rc.local ]
then
    cp /etc/rc.local /etc/rc.local.adhoc_bak
fi


if [ -e /etc/dhcpcd.conf ]
then
    cp /etc/dhcpcd.conf /etc/dhcpcd.conf.adhoc_bak
fi

# copy new files
cp rc.local /etc
cp dhcpcd.conf /etc

echo "Installation complete. Please reboot now for changes to take effect."
exit 0
