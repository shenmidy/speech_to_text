#!/usr/bin/env python3
"""
测试麦克风是否正常工作
"""

import speech_recognition as sr
import sys

def list_microphones():
    """列出所有可用的麦克风"""
    print("正在检测麦克风设备...")

    try:
        microphones = sr.Microphone.list_microphone_names()

        if not microphones:
            print("未找到麦克风设备")
            return False

        print(f"\n找到 {len(microphones)} 个音频输入设备:")
        for i, name in enumerate(microphones):
            print(f"  [{i}] {name}")

        return True

    except Exception as e:
        print(f"检测麦克风时出错: {e}")
        return False

def test_microphone(mic_index=0):
    """测试指定麦克风"""
    print(f"\n正在测试麦克风 #{mic_index}...")

    try:
        microphone = sr.Microphone(device_index=mic_index)
        recognizer = sr.Recognizer()

        print("请说话（测试录音，5秒超时）...")

        with microphone as source:
            # 校准环境噪声
            print("正在校准环境噪声...（请保持安静）")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("校准完成！")

            print("\n>>> 录音中...", end="", flush=True)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            print("完成！")

            print(">>> 测试音频录制成功！")

            # 尝试识别（可选）
            try:
                print(">>> 尝试识别音频...", end="", flush=True)
                text = recognizer.recognize_google(audio, language='zh-CN', show_all=False)
                print("完成！")
                print(f"\n识别结果: {text}")
            except sr.UnknownValueError:
                print("\n音频录制成功，但内容无法识别（可能是空白或噪音）")
            except sr.RequestError:
                print("\n音频录制成功，但无法连接到识别服务（网络问题）")
            except Exception as e:
                print(f"\n音频录制成功，但识别时出错: {e}")

        return True

    except Exception as e:
        print(f"测试麦克风时出错: {e}")
        return False

def test_audio_playback():
    """测试音频播放"""
    print("\n测试音频播放...")

    try:
        import wave
        import pyaudio

        # 创建一个简单的测试音频
        print("正在播放测试音频...")

        p = pyaudio.PyAudio()

        # 打开默认输出设备
        stream = p.open(format=pyaudio.paInt16,
                       channels=1,
                       rate=44100,
                       output=True)

        # 生成一个简单的蜂鸣声
        import math
        duration = 0.5  # 秒
        frequency = 440  # Hz (A4音)

        samples = []
        for i in range(int(44100 * duration)):
            sample = math.sin(2 * math.pi * frequency * i / 44100)
            samples.append(int(sample * 32767))

        # 播放
        import struct
        for sample in samples:
            stream.write(struct.pack('<h', sample))

        stream.stop_stream()
        stream.close()
        p.terminate()

        print("✓ 音频播放测试完成")
        return True

    except ImportError:
        print("未安装pyaudio，跳过音频播放测试")
        return False
    except Exception as e:
        print(f"音频播放测试失败: {e}")
        return False

def main():
    print("="*50)
    print("麦克风测试工具")
    print("="*50)

    # 列出麦克风
    if not list_microphones():
        print("\n请检查:")
        print("1. 麦克风是否已连接")
        print("2. 系统音频设置是否正确")
        print("3. 麦克风权限是否已授予")
        return

    # 测试默认麦克风
    print("\n" + "="*50)
    print("测试默认麦克风...")

    if test_microphone(0):
        print("\n✓ 麦克风测试通过！")
    else:
        print("\n✗ 麦克风测试失败")
        print("\n请检查:")
        print("1. 麦克风是否被其他程序占用")
        print("2. 麦克风音量是否合适")
        print("3. 系统音频设置")

    # 测试音频播放
    print("\n" + "="*50)
    test_audio_playback()

    print("\n" + "="*50)
    print("测试完成！")
    print("\n如果麦克风测试失败，请:")
    print("1. 检查物理连接")
    print("2. 检查系统音频设置")
    print("3. 确保没有其他程序占用麦克风")
    print("4. 尝试使用其他麦克风设备")
    print("="*50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n测试被用户中断")
    except Exception as e:
        print(f"\n测试过程中出现错误: {e}")
        print("\n请确保已正确安装依赖:")
        print("  pip install speechrecognition pyaudio")