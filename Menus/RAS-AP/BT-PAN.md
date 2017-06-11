# Bluetooth PAN AP

## PAN Access Point installation:  

`./bt-pan-ap-install`  

## PAN Access Point operation:

`systemctl start pan` to start the service  
`systemctl stop pan` to stop the service  
`systemctl enable pan` to start the service automatically on boot  


###

### Pair client and connect:  
`bluetoothctl`  
`agent on`  
`default-agent`  
`scan on`  
`scan off`  
`pair XX:XX:XX:XX:XX:XX`  
`trust XX:XX:XX:XX:XX:XX`  

## Bluetooth PAN Client installation  

`bt-pan-client-install`  
`systemctl start pan@00:11:22:33:44:55 ## <- Address of your AP`  



### Thanks to:  
[Mike Kazantsev](http://blog.fraggod.net/2015/03/28/bluetooth-pan-network-setup-with-bluez-5x.html)  
[The Blind Guru - Bluetooth PAN](https://blind.guru/tag/bluetooth-pan.html)  
