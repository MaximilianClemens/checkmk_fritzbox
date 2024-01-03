#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from cmk.gui.watolib.rulespecs import Rulespec
from cmk.gui.plugins.wato.utils import rulespec_registry, HostRulespec
from cmk.gui.plugins.wato.special_agents.common import RulespecGroupDatasourceProgramsHardware

def _factory_default_special_agents_fritzbox_smarthome():
    # No default, do not use setting if no rule matches
    return Rulespec.FACTORY_DEFAULT_UNUSED

def _valuespec_special_agents_fritzbox_smarthome():
    return Dictionary(
        title=_("Check state of Fritz!Box Smarthome Devices"),
        help=_("This rule selects the Fritz!Box agent, which uses HTTP to gather information "
               "about configuration and connection status information."),
        elements=[
            ('username',
                TextAscii(
                    title = _('Username'),
                ),
            ),
            ('password',
                Password(
                    title = _('Password'),
                ),
            ),
            ('port',
                Integer(
                    title = _('Port'),
                    default_value = 80,
                ),
            ),
            ('protocol',
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
            ),
            ( 'ssl', FixedValue(
                    0,
                    totext = 'Agent will ignore SSL errors',
                    title = _('Ignore SSL errors'),
                )
            ),
        ],
        optional_keys=['port', 'protocol', 'ssl'],
    )

rulespec_registry.register(
    HostRulespec(
        factory_default=_factory_default_special_agents_fritzbox_smarthome(),
        group=RulespecGroupDatasourceProgramsHardware,
        name="special_agents:fritzbox_smarthome",
        valuespec=_valuespec_special_agents_fritzbox_smarthome,
    ))
