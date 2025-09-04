# RC Step Response Demo

## 简介
这是一个用 Python 模拟一阶 RC 电路阶跃响应的小项目。输入电阻 R、电容 C 和输入电压 V_in，脚本会计算电容两端电压随时间的变化，并绘制曲线。

## 文件结构
- rc_step_response.py: 主脚本，包含仿真函数。
- rc_step_response.png: 运行脚本后生成的示例图。
- requirements.txt: 依赖库列表。

## 使用方法
1. 安装依赖:
   ```bash
   pip install -r requirements.txt
   ```

2. 运行脚本:
   ```bash
   python rc_step_response.py
   ```

运行后会显示曲线图，并在目录下生成 rc_step_response.png。