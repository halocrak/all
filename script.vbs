Dim objShell
Set objShell = WScript.CreateObject("WScript.Shell")

' Define the JavaScript code for the alert
Dim jsCode
jsCode = "alert('This is a VBScript-triggered JavaScript alert!');"

' Create a temporary HTML file with the JavaScript code
Dim tempFile
tempFile = "C:\Temp\AlertExample.html"
Dim fileContent
fileContent = "<html><head><script>" & jsCode & "</script></head><body></body></html>"
CreateHTMLFile tempFile, fileContent

' Open the HTML file using the default browser
objShell.Run tempFile

' Clean up: delete the temporary HTML file after a delay
WScript.Sleep 5000  ' 5000 milliseconds (5 seconds)
objShell.Run "cmd /c del " & tempFile

Sub CreateHTMLFile(filePath, content)
    Dim objFSO, objFile
    Set objFSO = CreateObject("Scripting.FileSystemObject")
    Set objFile = objFSO.CreateTextFile(filePath, True)
    objFile.Write content
    objFile.Close
End Sub
