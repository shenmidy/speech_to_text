@echo off
chcp 65001 >nul
echo ========================================
echo     语音转文字工具 - Windows启动器
echo ========================================
echo.

:menu
echo 请选择要运行的程序：
echo 1. 图形界面版本 (speech_to_text.py)
echo 2. 命令行版本 (speech_to_text_cli.py)
echo 3. 测试麦克风 (test_microphone.py)
echo 4. 安装依赖 (install.py)
echo 5. 退出
echo.

set /p choice="请输入数字选择 (1-5): "

if "%choice%"=="1" goto gui
if "%choice%"=="2" goto cli
if "%choice%"=="3" goto test
if "%choice%"=="4" goto install
if "%choice%"=="5" goto exit

echo 无效选择，请重试
echo.
goto menu

:gui
echo.
echo 正在启动图形界面版本...
python speech_to_text.py
goto end

:cli
echo.
echo 正在启动命令行版本...
python speech_to_text_cli.py
goto end

:test
echo.
echo 正在启动麦克风测试...
python test_microphone.py
goto end

:install
echo.
echo 正在安装依赖...
python install.py
goto end

:exit
echo.
echo 感谢使用！
timeout /t 2 >nul
exit

:end
echo.
echo 程序执行完毕。
echo 按任意键返回菜单...
pause >nul
goto menu