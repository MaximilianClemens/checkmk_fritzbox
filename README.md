# checkmk_fritzbox
This repository contains a modified [check_MK](https://mathias-kettner.com/) Fritz!Box Agent which can gather informations over the AVM AHA HTTP Interface about SmartHome Devices connected to an Fritz!Box.
It also provides a Check for parsing the output, and WATO-Pages for configuring thresholds.

## CLI Usage
```
./agents/special/agent_fritzbox --help
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

## Credits
* Matthias Kettner (for the basic agent) <mk@mathias-kettner.de> / [Matthias Kettner GmbH](https://mathias-kettner.com/)
* Gerold Gruber <info@edv2g.de> / [edv2g](https://edv2g.de/)
* Maximilian Clemens <maximilian.clemens@mailbox.org> / [gamma.red](https://gamma.red/)