#!/bin/sh
lan_ip=$(ubus call network.interface.lan status | jsonfilter -e '@["ipv4-address"][0].address')

echo "Status: 302 Found"
echo "Location: http://${lan_ip}/cgi-bin/luci/admin/wifiwizard"
echo ""
