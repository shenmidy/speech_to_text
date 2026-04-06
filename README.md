# 语音转文字项目

这是一个使用Python实现的简单语音转文字工具，具有图形用户界面(GUI)。

## 功能特性

- 实时语音识别（支持中文）
- 简单的图形用户界面
- 开始/停止录音控制
- 实时显示识别结果
- 清空文本功能

## 系统要求

- Python 3.6+
- 麦克风设备
- 互联网连接（使用Google Speech Recognition API）

## 安装步骤

1. 克隆或下载本项目到本地

2. 安装依赖包：

```bash
pip install -r requirements.txt
```

注意：在某些系统上，可能需要先安装PortAudio才能安装PyAudio：

- **Windows**: 
  ```bash
  pip install pyaudio
  ```

- **macOS**:
  ```bash
  brew install portaudio
  pip install pyaudio
  ```

- **Linux** (Ubuntu/Debian):
  ```bash
  sudo apt-get install portaudio19-dev python3-pyaudio
  pip install pyaudio
  ```

## 使用方法

1. 运行程序：
```bash
python speech_to_text.py
```

2. 程序启动后，会出现一个GUI窗口

3. 点击"开始录音"按钮开始语音识别

4. 对着麦克风说话，识别结果会实时显示在文本框中

5. 点击"停止录音"按钮结束识别

6. 可以使用"清空文本"按钮清除所有识别结果

## 注意事项

- 需要稳定的互联网连接（使用Google Speech Recognition API）
- 首次使用时可能需要几秒钟来校准环境噪声
- 在嘈杂的环境中识别准确率可能会下降
- 支持中文普通话识别

## 依赖库

- `speechrecognition`: 语音识别库
- `pyaudio`: 音频输入库
- `tkinter`: GUI库（通常Python自带）

## 故障排除

### 无法导入PyAudio
- 确保已按照上述步骤安装PyAudio
- Windows用户可能需要安装Microsoft Visual C++ Build Tools

### 无法识别语音
- 检查麦克风是否正常工作
- 确保有互联网连接
- 尝试在安静的环境中录音

### 程序无响应
- 确保没有其他程序占用麦克风
- 尝试重新启动程序

## 许可证

本项目使用MIT许可证。