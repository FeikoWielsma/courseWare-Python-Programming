import os
import subprocess

os.startfile(r"C:\Windows\System32\notepad.exe")  # Windows specific

os.system(r"C:\Windows\System32\calc.exe")  # portable

subprocess.Popen([r"C:\Windows\System32\SnippingTool.exe"])
