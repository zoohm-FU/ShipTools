
import streamlit as st

from calculations import (
    battery_energy_kwh,
    estimated_runtime_hours,
    knots_to_kmh,
    kmh_to_knots,
    knots_to_ms,
    ms_to_knots,
    meters_to_kilometers,
    kilometers_to_meters,
    meters_to_centimeters,
    centimeters_to_meters,
    meters_to_millimeters,
    millimeters_to_meters,
    kg_to_tons,
    tons_to_kg,
    kg_to_grams,
    grams_to_kg,
)

# ---------- 页面设置 ----------

st.set_page_config(
    page_title="ShipTools",
    page_icon="🚢",
    layout="wide"
)

st.title("🚢 ShipTools")
st.subheader("新能源船舶工程计算工具箱")

st.caption("面向新能源船舶专业学习与基础工程计算")

st.divider()

# ---------- 侧边栏导航 ----------

menu = st.sidebar.selectbox(
    "选择工具",
    [
        "电池能量与续航计算",
        "航速单位换算",
        "长度单位换算",
        "重量单位换算",
    ]
)

# ---------- 电池计算 ----------

if menu == "电池能量与续航计算":

    st.header("🔋 电池能量与续航计算")
    st.write("输入电池参数，估算电池总能量和理论续航时间。")

    col1, col2 = st.columns(2)

    with col1:
        voltage = st.number_input(
            "电池电压（V）",
            min_value=0.0,
            value=400.0,
            step=10.0
        )

    with col2:
        capacity = st.number_input(
            "电池容量（Ah）",
            min_value=0.0,
            value=200.0,
            step=10.0
        )

    usable = st.slider(
        "可用电量比例（%）",
        min_value=10,
        max_value=100,
        value=90
    )

    power = st.number_input(
        "平均负载功率（kW）",
        min_value=0.0,
        value=20.0,
        step=1.0
    )

    if st.button("开始计算", type="primary"):

        energy = battery_energy_kwh(voltage, capacity)

        st.success("计算完成！")

        col1, col2 = st.columns(2)

        col1.metric("电池总能量", f"{energy:.2f} kWh")

        if power > 0:
            runtime = estimated_runtime_hours(
                voltage,
                capacity,
                usable / 100,
                power
            )

            col2.metric("理论续航时间", f"{runtime:.2f} 小时")

        else:
            st.warning("负载功率必须大于 0，才能计算续航时间。")

        st.info(
            f"可用电量：{energy * usable / 100:.2f} kWh"
        )

# ---------- 航速换算 ----------

elif menu == "航速单位换算":

    st.header("🚢 航速单位换算")

    direction = st.selectbox(
        "选择换算方向",
        [
            "节 → km/h",
            "km/h → 节",
            "节 → m/s",
            "m/s → 节",
        ]
    )

    value = st.number_input(
        "输入数值",
        value=10.0,
        step=1.0
    )

    if st.button("开始换算", type="primary"):

        if direction == "节 → km/h":
            result = knots_to_kmh(value)
            unit = "km/h"

        elif direction == "km/h → 节":
            result = kmh_to_knots(value)
            unit = "节"

        elif direction == "节 → m/s":
            result = knots_to_ms(value)
            unit = "m/s"

        else:
            result = ms_to_knots(value)
            unit = "节"

        st.success(f"换算结果：{result:.4f} {unit}")

# ---------- 长度换算 ----------

elif menu == "长度单位换算":

    st.header("📏 长度单位换算")

    direction = st.selectbox(
        "选择换算方向",
        [
            "米 → 千米",
            "千米 → 米",
            "米 → 厘米",
            "厘米 → 米",
            "米 → 毫米",
            "毫米 → 米",
        ]
    )

    value = st.number_input(
        "输入长度数值",
        value=10.0,
        step=1.0
    )

    if st.button("开始换算", type="primary"):

        if direction == "米 → 千米":
            result = meters_to_kilometers(value)
            unit = "km"

        elif direction == "千米 → 米":
            result = kilometers_to_meters(value)
            unit = "m"

        elif direction == "米 → 厘米":
            result = meters_to_centimeters(value)
            unit = "cm"

        elif direction == "厘米 → 米":
            result = centimeters_to_meters(value)
            unit = "m"

        elif direction == "米 → 毫米":
            result = meters_to_millimeters(value)
            unit = "mm"

        else:
            result = millimeters_to_meters(value)
            unit = "m"

        st.success(f"换算结果：{result:.4f} {unit}")

# ---------- 重量换算 ----------

elif menu == "重量单位换算":

    st.header("⚖️ 重量单位换算")

    direction = st.selectbox(
        "选择换算方向",
        [
            "千克 → 吨",
            "吨 → 千克",
            "千克 → 克",
            "克 → 千克",
        ]
    )

    value = st.number_input(
        "输入重量数值",
        value=1000.0,
        step=100.0
    )

    if st.button("开始换算", type="primary"):

        if direction == "千克 → 吨":
            result = kg_to_tons(value)
            unit = "吨"

        elif direction == "吨 → 千克":
            result = tons_to_kg(value)
            unit = "kg"

        elif direction == "千克 → 克":
            result = kg_to_grams(value)
            unit = "g"

        else:
            result = grams_to_kg(value)
            unit = "kg"

        st.success(f"换算结果：{result:.4f} {unit}")

# ---------- 页面底部 ----------

st.divider()

st.caption("ShipTools | 新能源船舶工程计算工具箱")

st.caption(
    "免责声明：本工具仅用于学习和初步估算，"
    "计算结果不能替代专业设计计算、设备说明书或规范校核。"
)
