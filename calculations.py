
"""ShipTools 核心计算模块
用于新能源船舶基础工程计算与单位换算。
"""


def battery_energy_kwh(voltage_v, capacity_ah):
    """根据电压和容量计算电池总能量，单位：kWh。"""
    if voltage_v < 0 or capacity_ah < 0:
        raise ValueError("电压和电池容量不能小于 0")

    return voltage_v * capacity_ah / 1000


def estimated_runtime_hours(voltage_v, capacity_ah, usable_fraction, load_kw):
    """估算电池续航时间，单位：小时。"""
    if not 0 <= usable_fraction <= 1:
        raise ValueError("可用电量比例必须在 0 到 1 之间")

    if load_kw <= 0:
        raise ValueError("负载功率必须大于 0")

    energy = battery_energy_kwh(voltage_v, capacity_ah)
    usable_energy = energy * usable_fraction

    return usable_energy / load_kw


# ---------- 航速换算 ----------

def knots_to_kmh(knots):
    """节转换为 km/h。"""
    return knots * 1.852


def kmh_to_knots(kmh):
    """km/h 转换为节。"""
    return kmh / 1.852


def knots_to_ms(knots):
    """节转换为 m/s。"""
    return knots * 0.514444


def ms_to_knots(ms):
    """m/s 转换为节。"""
    return ms / 0.514444


# ---------- 长度换算 ----------

def meters_to_kilometers(meters):
    return meters / 1000


def kilometers_to_meters(kilometers):
    return kilometers * 1000


def meters_to_centimeters(meters):
    return meters * 100


def centimeters_to_meters(centimeters):
    return centimeters / 100


def meters_to_millimeters(meters):
    return meters * 1000


def millimeters_to_meters(millimeters):
    return millimeters / 1000


# ---------- 重量换算 ----------

def kg_to_tons(kg):
    """千克转换为公吨（1吨 = 1000千克）。"""
    return kg / 1000


def tons_to_kg(tons):
    """公吨转换为千克。"""
    return tons * 1000


def kg_to_grams(kg):
    return kg * 1000


def grams_to_kg(grams):
    return grams / 1000
