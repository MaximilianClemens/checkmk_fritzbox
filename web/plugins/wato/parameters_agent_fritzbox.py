#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

register_rulegroup("datasource_programs",
    _("Datasource Programs"),
    _("Specialized agents, e.g. check via SSH, ESX vSphere, SAP R/3"))
group = "datasource_programs"

register_rule(group,
    "special_agents:fritzbox",
     Dictionary(
        title = _("Check state of Fritz!Box Devices"),
        help = _("This rule selects the Fritz!Box agent, which uses HTTP/UPNP to gather information "
                 "about configuration and connection status information."),
        elements = [
            ('check_smarthome', Tuple(
                title = _('Query SmartHome Devices'),
                help = _("Enter Credentials for the Fritz!Box."),
                elements = [
                    TextAscii(
                        title = _('Username'),
                        allow_empty = False
                    ),
                    Password(
                        title = _('Password'),
                        allow_empty = False
                    ),
                    Integer(
                        title = _('Port'),
                        default_value = 80,
                        allow_empty = False
                    ),
                    Alternative(
                    title = _('Protocol'),
                    style = 'dropdown',
                    elements = [
                        FixedValue(
                                0,
                                totext = '',
                                title = _('HTTP'),
                        ),
                        FixedValue(
                                1,
                                totext = '',
                                title = _('HTTPS'),
                        )
                    ]),
                ],
            )),
            ('check_upnp', FixedValue(0,totext='The Agent will use UPNP',title = _("Use UPNP"))
            ),
            #("check_upnp", Label(0, totext = '', title = _('UPNP prüfen')))
            ( "timeout",
              Integer(
                  title = _("Connect Timeout"),
                  help = _("The network timeout in seconds when communicating via UPNP. "
                           "The default is 10 seconds. Please note that this "
                           "is not a total timeout, instead it is applied to each API call."),
                  default_value = 10,
                  minvalue = 1,
                  unit = _("seconds"),
              )
            ),
        ],
        optional_keys = [ "timeout", "check_smarthome", "check_upnp" ],
    ),
    factory_default = Rulespec.FACTORY_DEFAULT_UNUSED, # No default, do not use setting if no rule matches
    match = 'first')