@ECHO OFF

SET COMMAND=pwsh -Command "python program/main.py"
IF "%1" == "-wezterm" (wezterm cli spawn --cwd %CD% %COMMAND%)
IF "%1" == "" (START %COMMAND%)
