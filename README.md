* Download [Small http server](https://github.com/sgreben/http-file-server/)
* Add Mikrotik DNS rule:
```
[MikroTik] > /ip/dns/static/print 
Flags: X - DISABLED
Columns: NAME, ADDRESS, TTL
#   NAME            ADDRESS        TTL
;;; defconf
1 X api.coolkit.cn  52.57.118.192  1d 
2   api.coolkit.cn  192.168.7.27   1d 
```
* Download the [firmware](http://ota.tasmota.com/tasmota/release/) & run web-server and sonoff_unlock_server.py

```  base
SONOFF_IP="xxx.xxx.xxx.xxx"
WEBSERVER_IP="192.168.7.27"
FIRMWARE="tasmota-latest-lite.bin"
FIRMWARE_PATH="/home/user/SmartHome/webserver/"
FIRMWARE_SHA256=$(sha256sum ${FIRMWARE_PATH}${FIRMWARE} | cut -f1 -d " ")

echo "${FIRMWARE_PATH}${FIRMWARE}: ${FIRMWARE_SHA256}"

curl -s -XPOST --header "Content-Type: application/json" --data-raw '{"deviceid": "", "data": {}}' http://$SONOFF_IP:8081/zeroconf/info | jq .data.otaUnlock
curl -XPOST --header "Content-Type: application/json" --data-raw '{"deviceid": "", "data": {}}' http://$SONOFF_IP:8081/zeroconf/ota_unlock
curl -s -XPOST --header "Content-Type: application/json" --data-raw '{"deviceid": "", "data": {}}' http://$SONOFF_IP:8081/zeroconf/info | jq .data.otaUnlock
curl -XPOST --header "Content-Type: application/json" --data-raw '{"deviceid":"","data":{"downloadUrl": "http://'${WEBSERVER_IP}':8080/webserver/'${FIRMWARE}'", "sha256sum": "'${FIRMWARE_SHA256}'"} }' http://$SONOFF_IP:8081/zeroconf/ota_flash
````

Details [one](https://github.com/itead/Sonoff_Devices_DIY_Tools/issues/45), [two](https://tasmota.github.io/docs/Sonoff-DIY/)
