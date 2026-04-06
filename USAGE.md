# 使用说明

## 快速开始

### 方法1：使用安装脚本（推荐）
```bash
python install.py
```

### 方法2：手动安装
```bash
pip install -r requirements.txt
```

注意：如果安装PyAudio失败，请参考下面的"常见问题"部分。

## 运行程序

### 图形界面版本（推荐）
```bash
python speech_to_text.py
```

功能：
- 点击"开始录音"按钮开始识别
- 对着麦克风说话
- 识别结果实时显示
- 点击"停止录音"按钮结束
- 点击"清空文本"按钮清除结果

### 命令行版本
```bash
python speech_to_text_cli.py
```

功能：
- 交互式语音识别
- 支持保存结果到文件
- 按提示操作即可

## 项目文件说明

- `speech_to_text.py` - 图形界面版本
- `speech_to_text_cli.py` - 命令行版本  
- `requirements.txt` - Python依赖包列表
- `install.py` - 自动安装脚本
- `README.md` - 项目说明文档
- `USAGE.md` - 本使用说明文件

## 常见问题

### 1. 安装PyAudio失败

**Windows系统：**
```bash
# 尝试使用预编译的wheel
pip install pipwin
pipwin install pyaudio
```

**macOS系统：**
```bash
# 先安装PortAudio
brew install portaudio
# 再安装PyAudio
pip install pyaudio
```

**Linux系统（Ubuntu/Debian）：**
```bash
# 先安装系统依赖
sudo apt-get install portaudio19-dev python3-pyaudio
# 再安装PyAudio
pip install pyaudio
```

### 2. 无法识别语音

- 检查麦克风是否正常工作
- 确保有互联网连接（使用Google Speech Recognition API需要网络）
- 在安静的环境中尝试
- 首次使用需要几秒钟校准环境噪声

### 3. 程序无响应

- 确保没有其他程序占用麦克风
- 尝试重新启动程序
- 检查Python版本是否为3.6+

### 4. 识别结果不准确

- 尽量在安静的环境中说话
- 说话时靠近麦克风
- 吐字清晰，语速适中
- 避免背景噪音

## 技术支持

如果遇到问题，请：

1. 检查上述"常见问题"部分
2. 确保已正确安装所有依赖
3. 在安静的环境中测试
4. 检查网络连接

## 注意事项

- 需要互联网连接（使用Google Speech Recognition API）
- 支持中文普通话识别
- 识别准确率受环境噪音影响
- 首次使用需要校准环境噪声

## 更新日志

- 2025-04-06: 初始版本发布
  - 图形界面版本
  - 命令行版本
  - 自动安装脚本
  - 完整文档