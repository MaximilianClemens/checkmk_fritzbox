#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import cmk.gui.watolib as watolib


from cmk.gui.plugins.wato import (
    IndividualOrStoredPassword,
    RulespecGroup,
    monitoring_macro_help,
    rulespec_group_registry,
    rulespec_registry,
    HostRulespec,
)

@rulespec_group_registry.register
class RulespecGroupDatasourcePrograms(RulespecGroup):
    @property
    def name(self):
        return "datasource_programs"

    @property
    def title(self):
        return _("Datasource Programs")

    @property
    def help(self):
        return _("Specialized agents, e.g. check via SSH, ESX vSphere, SAP R/3")


def _valuespec_datasource_programs():
    return TextAscii(
        title=_("Individual program call instead of agent access"),
        help=_("For agent based checks Check_MK allows you to specify an alternative "
               "program that should be called by Check_MK instead of connecting the agent "
               "via TCP. That program must output the agent's data on standard output in "
               "the same format the agent would do. This is for example useful for monitoring "
               "via SSH.") + monitoring_macro_help() +
        _("This option can only be used with the permission \"Can add or modify executables\"."),
        label=_("Command line to execute"),
        empty_text=_("Access Check_MK Agent via TCP"),
        size=80,
        attrencode=True,
    )


rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourcePrograms,
        name="datasource_programs",
        valuespec=_valuespec_datasource_programs,
    ))




def _factory_default_special_agents_fritzbox_smarthome():
    # No default, do not use setting if no rule matches
    return watolib.Rulespec.FACTORY_DEFAULT_UNUSED

def _valuespec_special_agents_fritzbox_smarthome():
    return Dictionary(
        title=_("Check state of Fritz!Box Smarthome Devices"),
        help=_("This rule selects the Fritz!Box agent, which uses HTTP to gather information "
               "about configuration and connection status information."),
        elements=[
            ('username',
                TextAscii(
                    title = _('Username'),
                    allow_empty = False
                ),
            ),
            ('password',
                Password(
                    title = _('Password'),
                    allow_empty = False
                ),
            ),
            ('port',
                Integer(
                    title = _('Port'),
                    default_value = 80,
                    allow_empty = False
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
        group=RulespecGroupDatasourcePrograms,
        name="special_agents:fritzbox_smarthome",
        valuespec=_valuespec_special_agents_fritzbox_smarthome,
    ))
