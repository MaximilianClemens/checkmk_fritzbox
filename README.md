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

## Tested Devices
* AVM FRITZ!DECT210 (FW 04.16)
   * Switching Socket
   * Function Values: powermeter, temperature, switch
* AVM FRITZ!DECT200 (FW 04.16)
   * Switching Socket
   * Function Values: powermeter, temperature, switch
* AVM FRITZ!DECT301 (FW: 04.88)
   * Thermostat
   * Function Values: temperature, hkr
* AVM FRITZ!DECTRepeater100 (FW 04.16)
   * DECTRepeater
   * Function Values: temperature
* AVM FRITZ!DECT400 (FW: 04.90)
   * Button
   * Function Values: button
* Eurotronic CometDECT (FW 03.54)
   * Thermostat
   * Function Values: temperature, hkr

## Function Value implementation:
* base (this means generic device infos)
   * Graphs: None
   * Status: When Device present OK, else WARN
* powermeter
   * Graphs: Consumption (kWh), Voltage (V), Power (W)
   * Status: Always okay (Check Rule Page work in progress)
* temperature
   * Graphs: Temperature Sensor
   * Status: Always okay (Check Rule Page work in progress)
* switch
   * Graphs: Switch State
   * Status: Always okay (Check Rule Page work in progress)
* hkr
   * Graphs: Temperature Thermostat, Battery, Window Open
   * Status: Compare against default params (Check Rule Page work in progress)
* button
   * Nothing yet (no idea what to check here)

## Credits
* Matthias Kettner (for the basic agent) <mk@mathias-kettner.de> / [Matthias Kettner GmbH](https://mathias-kettner.com/)
* Gerold Gruber <info@edv2g.de> / [edv2g](https://edv2g.de/)
* Maximilian Clemens <maximilian.clemens@mailbox.org> / [gamma.red](https://gamma.red/)

## Informations
[AVM - AHA-HTTP-Interface Dokumentation](https://avm.de/fileadmin/user_upload/Global/Service/Schnittstellen/AHA-HTTP-Interface.pdf)
