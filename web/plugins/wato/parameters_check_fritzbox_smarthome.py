#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

register_check_parameters(
    subgroup_applications,
    'fritzbox_smarthome',
    _('Settings for Fritz!Box Smarthome Devices'),
    Dictionary(
        title = _('Parameter'),
        optional_keys = None,
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
        ]
        ),
    TextAscii(title = _('Device-ID')),
    match_type = 'dict',
    )