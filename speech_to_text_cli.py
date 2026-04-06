#!/usr/bin/env python3
"""
命令行语音转文字工具
"""

import speech_recognition as sr
import sys
import time

def speech_to_text_cli():
    """命令行语音转文字"""

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("=" * 50)
    print("语音转文字命令行工具")
    print("=" * 50)
    print("\n提示:")
    print("1. 请确保麦克风已连接")
    print("2. 在安静的环境中说话效果更好")
    print("3. 按 Ctrl+C 退出程序")
    print("=" * 50)

    # 校准环境噪声
    print("\n正在校准环境噪声...（请保持安静）")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
    print("校准完成！")

    while True:
        try:
            print("\n" + "-" * 30)
            print("请说话（5秒超时）...")

            with microphone as source:
                print(">>> 录音中...", end="", flush=True)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("完成！")

            print(">>> 识别中...", end="", flush=True)

            try:
                # 使用Google Speech Recognition，支持中文
                text = recognizer.recognize_google(audio, language='zh-CN')
                print("完成！")
                print("\n识别结果:")
                print(f"  {text}")

                # 询问是否继续
                print("\n是否继续？(y/n): ", end="")
                choice = input().strip().lower()
                if choice not in ['y', 'yes', '是']:
                    print("\n感谢使用！")
                    break

            except sr.UnknownValueError:
                print("\n无法识别音频，请重试")
            except sr.RequestError as e:
                print(f"\n无法连接到语音识别服务: {e}")
                print("请检查网络连接后重试")
                break
            except Exception as e:
                print(f"\n发生错误: {e}")

        except KeyboardInterrupt:
            print("\n\n程序已退出")
            break
        except sr.WaitTimeoutError:
            print("\n录音超时，请重试")
        except Exception as e:
            print(f"\n发生错误: {e}")
            print("是否重试？(y/n): ", end="")
            choice = input().strip().lower()
            if choice not in ['y', 'yes', '是']:
                break

def save_to_file():
    """录音并保存到文件"""

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("\n语音转文字并保存到文件")
    print("=" * 50)

    filename = input("请输入保存文件名（默认: output.txt）: ").strip()
    if not filename:
        filename = "output.txt"

    # 校准环境噪声
    print("\n正在校准环境噪声...（请保持安静）")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
    print("校准完成！")

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"录音时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"{'='*50}\n\n")

    while True:
        try:
            print("\n" + "-" * 30)
            print("请说话（5秒超时）...")

            with microphone as source:
                print(">>> 录音中...", end="", flush=True)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("完成！")

            print(">>> 识别中...", end="", flush=True)

            try:
                text = recognizer.recognize_google(audio, language='zh-CN')
                print("完成！")

                # 显示并保存结果
                print(f"\n识别结果: {text}")

                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(f"{text}\n")

                print(f"结果已保存到 {filename}")

                # 询问是否继续
                print("\n是否继续录音？(y/n): ", end="")
                choice = input().strip().lower()
                if choice not in ['y', 'yes', '是']:
                    print("\n感谢使用！")
                    break

            except sr.UnknownValueError:
                print("\n无法识别音频，请重试")
            except sr.RequestError as e:
                print(f"\n无法连接到语音识别服务: {e}")
                break

        except KeyboardInterrupt:
            print("\n\n程序已退出")
            break
        except sr.WaitTimeoutError:
            print("\n录音超时，请重试")

if __name__ == "__main__":
    print("选择模式:")
    print("1. 交互式语音转文字")
    print("2. 录音并保存到文件")

    try:
        choice = input("请输入选择 (1/2): ").strip()

        if choice == "1":
            speech_to_text_cli()
        elif choice == "2":
            save_to_file()
        else:
            print("无效选择，使用默认模式")
            speech_to_text_cli()
    except KeyboardInterrupt:
        print("\n程序已退出")