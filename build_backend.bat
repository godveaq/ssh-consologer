@echo off
echo Building Glitch Console Backend...
g++ -o backend.exe backend.cpp -std=c++11
if %ERRORLEVEL% == 0 (
    echo Build successful! backend.exe created.
) else (
    echo Build failed.
)
pause