Sub ConnectToNetcat()
    Dim objShell
    Set objShell = WScript.CreateObject("WScript.Shell")

    ' Replace "nc -zv your_netcat_server_ip your_netcat_server_port" with the actual Netcat command
    Dim netcatCommand
    netcatCommand = "nc -zv 127.0.0.1 8787"

    ' Execute Netcat command using the shell
    objShell.Run netcatCommand, 1, True

    Set objShell = Nothing
End Sub
