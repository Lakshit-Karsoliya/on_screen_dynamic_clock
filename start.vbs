Set oShell = CreateObject("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c D:\current_work\on_screen_dynamic_clock\start.bat"
oShell.Run strArgs,0,false