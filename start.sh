#!/bin/bash

# 获取脚本自身的路径
script_dir=$(dirname "$0")

# 切换到脚本目录
cd "$script_dir" || exit

echo "脚本目录：$script_dir"

# 激活虚拟环境
source venv/bin/activate
#
# 运行 Python 主程序
python  main.py
