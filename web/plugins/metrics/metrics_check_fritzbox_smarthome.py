#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

### HKR
metric_info["hkr_windowopenactiv"] = {
    "title" : _("Window Open"),
    "color": "#7192ad", #
    "unit" : "count",
}

metric_info["hkr_battery"] = {
    "title" : _("Batterystate"),
    "color": "#7192ad", #
    "unit" : "%",
}

metric_info["hkr_tsoll"] = {
    "title" : _("Temperature Should"),
    "color": "#40ff00",
    "unit" : "c",
}

metric_info["hkr_absenk"] = {
    "title" : _("Temperature Saving"),
    "color": "#0080ff",
    "unit" : "c",
}

metric_info["hkr_komfort"] = {
    "title" : _("Temperature Comfort"),
    "color": "#ffbf00",
    "unit" : "c",
}

metric_info["ref_temperature"] = {
    "title" : _("Temperature"),
    "color": "#009999",
    "unit" : "c",
}

graph_info["fritzbox_smarthome_temperature"] = {
    "title"   : _("Temperature Thermostat"),
    "metrics" : [
        ( "ref_temperature", "area" ),
        ( "hkr_komfort", "line" ),
        ( "hkr_absenk", "line" ),
        ( "hkr_tsoll", "line" ),
    ],
}

perfometer_info.append({
    "type"       : "logarithmic",
    "metric"     : "ref_temperature",
    "half_value" : 0.5,
    "exponent"   : 7,
})

### Powermeter

unit_info["kwh"] = {
    "title"  : _("Electrical Energy"),
    "symbol" : _("kWh"),
    "render" : lambda v: physical_precision(v, 3, _("kWh")),
}


metric_info["powermeter_power"] = {
    "title" : _("Power"),
    "color": "#7192ad", #
    "unit" : "w", #watt
}

metric_info["powermeter_energy"] = {
    "title" : _("Consumption"),
    #"help": _("Consumption since Commissioning")
    "color": "#7192ad", #
    "unit" : "kwh", #kWh
}

metric_info["powermeter_voltage"] = {
    "title" : _("Voltage"),
    "color": "#7192ad", #
    "unit" : "v", #volt
}

perfometer_info.append({
    "type"       : "logarithmic",
    "metric"     : "powermeter_power",
    "half_value" : 5,
    "exponent"   : 3,
})


###Swtich
metric_info["switch_state"] = {
    "title" : _("Switch State"),
    "color": "#7192ad",
    "unit" : "count",
}


## Temp

metric_info["temperature_celsius"] = {
    "title" : _("Temperature"),
    "color": "#009999",
    "unit" : "c",
}

metric_info["temperature_offset"] = {
    "title" : _("Temperature Offset"),
    "color": "#cc9900",
    "unit" : "c",
}

metric_info["temperature_real"] = {
    "title" : _("Temperature Offset"),
    "color": "#990000",
    "unit" : "c",
}

graph_info["fritzbox_smarthome_temperature_real"] = {
    "title"   : _("Temperature Sensor"),
    "metrics" : [
        ( "temperature_celsius", "area" ),
        ( "temperature_offset", "stack" ),
        ( "temperature_real", "line" )
    ],
}