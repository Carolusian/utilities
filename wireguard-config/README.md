== Wireguard Mac Client ==

* `brew install wireguard-tools`
* Generate wireguard client config from TunSafe  
* Put the config file to `/usr/local/etc/wireguard/wg0.conf`
* `wg-quick up ~/usr/local/etc/wireguard/wg0.conf` to start wireguard
* `wg-quick down ~/usr/local/etc/wireguard/wg0.conf` to stop wireguard
* `sudo wg show` to show the status, returns nothing if not running
