
# 🚢 ShipTools

新能源船舶工程计算工具箱。

## 项目介绍

ShipTools 是一个面向新能源船舶专业学习者的工程计算辅助工具，使用 Python 和 Streamlit 开发。

## 当前功能

- 电池总能量计算（V、Ah、kWh）
- 理论电池续航时间估算
- 航速换算（节、km/h、m/s）
- 长度单位换算（m、km、cm、mm）
- 重量单位换算（kg、吨、g）

## 技术栈

- Python
- Streamlit
- Pytest
- Git / GitHub

## 安装与运行

安装依赖：

```bash
python -m pip install -r requirements.txt
```

启动项目：

```bash
python -m streamlit run app.py
```

## 自动化测试

```bash
python -m pytest -v
```

## 项目定位

本项目用于专业学习和基础工程计算，不替代船舶设计规范、专业校核及实际设备技术文件。

## 后续计划

- 增加船舶功率计算
- 增加电池组串并联计算
- 增加推进系统效率估算
- 优化界面与计算结果展示
