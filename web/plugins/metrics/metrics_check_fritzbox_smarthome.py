#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-


#metric_info["temperature_celsius"] = {
#    "title" : _("Reference Temperature"),
#    "color": "#7192ad", #
#    "unit" : "c",
#}
#
#metric_info["temperature_offset"] = {
#    "title" : _("Reference Temperature offset"),
#    "color": "#7192ad", #
#    "unit" : "count",
#}

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

#metric_info["hkr_tist"] = {
#    "title" : _("Temperature (internal)"),
#    "color": "#7192ad", #
#    "unit" : "c",
#}

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

#check_metrics["fritzbox_smarthome.temperature"] = {
#    "ref_temperature"      : { "scale" : m },
#    "hkr_komfort"          : { "scale" : m },
#    "hkr_absenk"           : { "scale" : m },
#    "hkr_tsoll"            : { "scale" : m },
#}

graph_info["fritzbox_smarthome_temperature"] = {
    "title"   : _("Temperature"),
    "metrics" : [
        ( "ref_temperature", "area" ),
        ( "hkr_komfort", "line" ),
        ( "hkr_absenk", "line" ),
        ( "hkr_tsoll", "line" ),
    ],
}
