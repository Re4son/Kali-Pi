# Bluetooth PAN AP

## PAN Access Point installation:  

`cp bt-pan /usr/local/sbin/`  
`cp pan /usr/local/sbin/`  
`cp BT-AP /usr/local/sbin/`  
`cp pan.netdev /etc/systemd/network/`  
`cp pan.network /etc/systemd/network/`  
`cp pan.service /etc/systemd/system/`  
`chmod +x /usr/local/sbin/bt-pan`  
`chmod +x /usr/local/sbin/pan`  
`chmod +x /usr/local/sbin/BT-AP`  

`systemctl daemon-reload`  
`systemctl restart systemd-networkd`  
`systemctl start pan`  

### Pair client and connect:  
`bluetoothctl`  
`agent on`  
`default-agent`  
`scan on`  
`scan off`  
`pair XX:XX:XX:XX:XX:XX`  
`trust XX:XX:XX:XX:XX:XX`  

## Bluetooth PAN Client installation  

`cp pan-client.network /etc/systemd/network/`  
`cp pan@.service /etc/systemd/system/`  
`systemctl start pan@00:11:22:33:44:55 ## <- Address of your AP`  



### Thanks to:  
[Mike Kazantsev](http://blog.fraggod.net/2015/03/28/bluetooth-pan-network-setup-with-bluez-5x.html)  
[The Blind Guru - Bluetooth PAN](https://blind.guru/tag/bluetooth-pan.html)  
