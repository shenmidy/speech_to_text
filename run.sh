#!/bin/bash

# 语音转文字工具 - Linux/macOS启动器

show_menu() {
    clear
    echo "========================================"
    echo "     语音转文字工具 - Linux/macOS启动器"
    echo "========================================"
    echo ""
    echo "请选择要运行的程序："
    echo "1. 图形界面版本 (speech_to_text.py)"
    echo "2. 命令行版本 (speech_to_text_cli.py)"
    echo "3. 测试麦克风 (test_microphone.py)"
    echo "4. 安装依赖 (install.py)"
    echo "5. 退出"
    echo ""
}

check_python() {
    if ! command -v python3 &> /dev/null; then
        echo "错误: 未找到python3，请先安装Python"
        exit 1
    fi
}

check_dependencies() {
    echo "检查Python依赖..."
    if ! python3 -c "import speech_recognition" 2>/dev/null; then
        echo "警告: speech_recognition模块未安装"
        read -p "是否立即安装？(y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            python3 install.py
        fi
    fi
}

main() {
    check_python

    while true; do
        show_menu
        read -p "请输入数字选择 (1-5): " choice

        case $choice in
            1)
                echo ""
                echo "正在启动图形界面版本..."
                python3 speech_to_text.py
                ;;
            2)
                echo ""
                echo "正在启动命令行版本..."
                python3 speech_to_text_cli.py
                ;;
            3)
                echo ""
                echo "正在启动麦克风测试..."
                python3 test_microphone.py
                ;;
            4)
                echo ""
                echo "正在安装依赖..."
                python3 install.py
                ;;
            5)
                echo ""
                echo "感谢使用！"
                exit 0
                ;;
            *)
                echo "无效选择，请重试"
                sleep 1
                continue
                ;;
        esac

        echo ""
        read -p "按回车键返回菜单..." -n 1 -r
    done
}

# 检查是否为第一次运行
if [ ! -f "requirements.txt" ]; then
    echo "错误: 未找到项目文件"
    exit 1
fi

# 给脚本添加执行权限
chmod +x "$0" 2>/dev/null

# 运行主程序
main