import os

if os.path.exists("C:\\Users\\iriom\\Desktop\\Texto.txt"):
    os.remove("C:\\Users\\iriom\\Desktop\\Texto.txt")
else:
    print("Inexistent file")
    
    