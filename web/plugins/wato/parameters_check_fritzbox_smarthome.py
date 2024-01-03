#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from typing import Type, Optional, List
from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Alternative,
    Dictionary,
    Integer,
    Tuple,
    FixedValue,
    TextAscii,
    Checkbox,
)
from cmk.gui.plugins.wato.utils import (
    RulespecGroupCheckParametersApplications,
    CheckParameterRulespecWithItem,
    rulespec_registry,
)


def _parameter_valuespec_fritzbox_smarthome():
    return Dictionary(
        title = _('Parameter'),
        optional_keys = [],
        elements = [
            ( 'present', Alternative(
                title = _('Offline Devices'),
                style = 'dropdown',
                elements = [
                    FixedValue(
                            0,
                            totext = '',
                            title = _('show as OK'),
                    ),
                    FixedValue(
                            1,
                            totext = '',
                            title = _('show as WARN'),
                    ),
                    FixedValue(
                            2,
                            totext = '',
                            title = _('show as CRIT'),
                    ),
                ])
            ),

            ( 'hkr', Dictionary(
                title = _('Thermostat (battery settings are also here)'),
                elements = [
                    ('hkr_bat_always', FixedValue(True, totext='Batterystate will be shown in Status Details', title = _('Show Batterystate always'))),
                    ('hkr_warn', Dictionary(
                        title = _('Thresholds for WARN'),
                        optional_keys = [ 'hkr_diff_soll', 'hkr_bat_below' ],
                        elements = [
                            ('hkr_diff_soll', Integer(label = _('by'), title = _('Deviation from the target temperature'), unit = u'°C', default_value = 5)),
                            ('hkr_bat_below', Integer(label = _('less than'), title = _('Battery'), unit = u'%', default_value = 50)),
                            ('hkr_flags', Tuple(
                                title = _('Flags'),
                                elements = [
                                Checkbox(title = _('On Errorstate'), default_value = False),
                                Checkbox(title = _('On Batterywarning'), default_value = False),
                                Checkbox(title = _('On Window open'), default_value = False),
                                ]
                            )),
                        ]
                        )
                    ),
                    ('hkr_crit', Dictionary(
                        title = _('Thresholds for CRIT'),
                        optional_keys = [ 'hkr_diff_soll', 'hkr_bat_below' ],
                        elements = [
                            ('hkr_diff_soll', Integer(label = _('by'), title = _('Deviation from the target temperature'), unit = u'°C', default_value = 10)),
                            ('hkr_bat_below', Integer(label = _('less than'), title = _('Battery'), unit = u'%', default_value = 30)),
                            ('hkr_flags', Tuple(
                                title = _('Flags'),
                                elements = [
                                Checkbox(title = _('On Errorstate'), default_value = True),
                                Checkbox(title = _('On Batterywarning'), default_value = False),
                                Checkbox(title = _('On Window open'), default_value = False),
                                ]
                            )),
                        ]
                        )
                    ),
                ])
            ),

            ( 'humidity', Dictionary(
                title = _('Humidity'),
                
                elements = [
                    ('humidity_warn', Tuple(
                        title = _('Thresholds for WARN'),
                        elements = [
                            Integer(label = _('higher than'), unit = u'%', default_value = 60),
                            Integer(label = _('lesser than'), unit = u'%', default_value = 40),
                        ]
                    )),
                    ('humidity_crit', Tuple(
                        title = _('Thresholds for CRIT'),
                        elements = [
                            Integer(label = _('higher than'), unit = u'%', default_value = 70),
                            Integer(label = _('lesser than'), unit = u'%', default_value = 30),
                        ]
                    )),
                ])
            ),

            # temperature
        ]
    )

def _item_spec_fritzbox_smarthome_devices():
    return TextAscii(title=_("Device-ID"))

rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="fritzbox_smarthome",
        group=RulespecGroupCheckParametersApplications,
        item_spec=_item_spec_fritzbox_smarthome_devices,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_fritzbox_smarthome,
        title=lambda: _('Settings for Fritz!Box Smarthome Devices')
    )
)
