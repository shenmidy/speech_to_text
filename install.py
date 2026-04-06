#!/usr/bin/env python3
"""
安装脚本 - 自动安装语音转文字项目依赖
"""

import sys
import subprocess
import platform

def run_command(command, description):
    """运行命令并处理错误"""
    print(f"正在{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True,
                              capture_output=True, text=True)
        print(f"✓ {description}成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description}失败")
        print(f"错误信息: {e.stderr}")
        return False

def check_python_version():
    """检查Python版本"""
    print("检查Python版本...")
    if sys.version_info < (3, 6):
        print(f"✗ Python版本过低: {sys.version_info.major}.{sys.version_info.minor}")
        print("请安装Python 3.6或更高版本")
        return False
    print(f"✓ Python版本: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    return True

def install_pip_packages():
    """使用pip安装依赖包"""
    packages = ["speechrecognition"]

    # 根据操作系统选择PyAudio安装方式
    system = platform.system()

    if system == "Windows":
        print("\n检测到Windows系统")
        packages.append("pyaudio")

    elif system == "Darwin":  # macOS
        print("\n检测到macOS系统")
        print("提示: macOS可能需要先安装PortAudio")
        print("可以使用以下命令安装: brew install portaudio")
        packages.append("pyaudio")

    elif system == "Linux":
        print("\n检测到Linux系统")
        print("提示: Linux可能需要先安装系统依赖")
        print("Ubuntu/Debian: sudo apt-get install portaudio19-dev python3-pyaudio")
        print("CentOS/RHEL: sudo yum install portaudio-devel")
        packages.append("pyaudio")

    else:
        print(f"\n未知系统: {system}")
        packages.append("pyaudio")

    # 安装所有包
    print("\n开始安装Python依赖包...")
    for package in packages:
        if not run_command(f"pip install {package}", f"安装{package}"):
            print(f"警告: {package}安装失败，可能会影响功能")

    return True

def check_installation():
    """检查安装是否成功"""
    print("\n" + "="*50)
    print("检查安装结果...")

    test_imports = [
        ("speechrecognition", "speech_recognition"),
        ("pyaudio", "pyaudio"),
    ]

    all_ok = True
    for pip_name, import_name in test_imports:
        try:
            __import__(import_name)
            print(f"✓ {pip_name} 导入成功")
        except ImportError as e:
            print(f"✗ {pip_name} 导入失败: {e}")
            all_ok = False

    return all_ok

def main():
    print("="*50)
    print("语音转文字项目 - 安装脚本")
    print("="*50)

    # 检查Python版本
    if not check_python_version():
        sys.exit(1)

    # 安装依赖包
    install_pip_packages()

    # 检查安装结果
    if check_installation():
        print("\n" + "="*50)
        print("安装完成！")
        print("\n使用方法:")
        print("1. 图形界面版本: python speech_to_text.py")
        print("2. 命令行版本: python speech_to_text_cli.py")
        print("\n注意事项:")
        print("- 确保麦克风已连接")
        print("- 首次使用需要网络连接（使用Google Speech Recognition API）")
        print("- 在安静环境中使用效果更佳")
        print("="*50)
    else:
        print("\n" + "="*50)
        print("安装存在一些问题，部分功能可能无法正常工作")
        print("请根据上面的错误信息进行手动安装")
        print("="*50)
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n安装被用户中断")
        sys.exit(1)