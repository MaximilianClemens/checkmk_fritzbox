# checkmk_fritzbox
Extended CheckMK FritzBox Agent for SmartHome Devices.

## CLI Usage
```./agents/special/agent_fritzbox --help
usage: agent_fritzbox [-h] [--debug] [--timeout TIMEOUT] [--check-upnp]
                      [--check-smarthome]
                      host [username] [password] [port] [{http,https}]

Check_MK Fritz!Box Agent

positional arguments:
  host                  Host name or IP address of your Fritz!Box
  username              Only needed for smarthome check
  password              Only needed for smarthome check
  port                  Only needed for smarthome check
  {http,https}          Only needed for smarthome check

optional arguments:
  -h, --help            show this help message and exit
  --debug               Debug mode: let Python exceptions come through
  --timeout TIMEOUT, -t TIMEOUT
                        Set the network timeout to <SEC> seconds. Default is
                        10 seconds. Note: the timeout is not applied to the
                        whole check, instead it is used for each API query.
  --check-upnp          Use the UPNP API
  --check-smarthome     Use the AHA HTTP Interface
```