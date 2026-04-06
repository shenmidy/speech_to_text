import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import queue

class SpeechToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("语音转文字工具")
        self.root.geometry("600x400")

        # 初始化识别器
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.audio_queue = queue.Queue()
        self.is_listening = False

        # 创建GUI组件
        self.create_widgets()

        # 校准环境噪声
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

    def create_widgets(self):
        # 标题标签
        title_label = tk.Label(self.root, text="语音转文字工具", font=("Arial", 16))
        title_label.pack(pady=10)

        # 说明标签
        desc_label = tk.Label(self.root, text="点击'开始录音'开始语音识别，点击'停止录音'结束")
        desc_label.pack(pady=5)

        # 按钮框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.start_button = tk.Button(button_frame, text="开始录音", command=self.start_listening,
                                      bg="green", fg="white", font=("Arial", 12))
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(button_frame, text="停止录音", command=self.stop_listening,
                                     bg="red", fg="white", font=("Arial", 12), state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # 文本显示区域
        text_frame = tk.Frame(self.root)
        text_frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=10)

        self.text_area = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # 清空按钮
        clear_button = tk.Button(self.root, text="清空文本", command=self.clear_text)
        clear_button.pack(pady=5)

        # 状态标签
        self.status_label = tk.Label(self.root, text="准备就绪", relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def start_listening(self):
        self.is_listening = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="正在录音... 请说话")

        # 在新线程中开始录音
        self.listen_thread = threading.Thread(target=self.record_audio)
        self.listen_thread.daemon = True
        self.listen_thread.start()

        # 开始处理音频
        self.process_audio()

    def record_audio(self):
        with self.microphone as source:
            while self.is_listening:
                try:
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=5)
                    self.audio_queue.put(audio)
                except sr.WaitTimeoutError:
                    continue
                except Exception as e:
                    if self.is_listening:  # 仅在仍然在监听时报告错误
                        self.root.after(0, lambda: messagebox.showerror("错误", f"录音错误: {str(e)}"))

    def process_audio(self):
        if not self.is_listening and self.audio_queue.empty():
            return

        try:
            while not self.audio_queue.empty():
                audio = self.audio_queue.get_nowait()
                # 在新线程中处理识别，避免阻塞GUI
                threading.Thread(target=self.recognize_audio, args=(audio,), daemon=True).start()
        except queue.Empty:
            pass

        # 继续处理
        if self.is_listening or not self.audio_queue.empty():
            self.root.after(100, self.process_audio)

    def recognize_audio(self, audio):
        try:
            text = self.recognizer.recognize_google(audio, language='zh-CN')
            self.root.after(0, self.append_text, text)
        except sr.UnknownValueError:
            self.root.after(0, self.append_text, "[无法识别音频]")
        except sr.RequestError as e:
            self.root.after(0, lambda: messagebox.showerror("错误", f"无法请求结果: {str(e)}"))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("错误", f"识别错误: {str(e)}"))

    def append_text(self, text):
        self.text_area.insert(tk.END, text + "\n")
        self.text_area.see(tk.END)
        self.status_label.config(text="识别完成")

    def stop_listening(self):
        self.is_listening = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="已停止录音")

    def clear_text(self):
        self.text_area.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = SpeechToTextApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()