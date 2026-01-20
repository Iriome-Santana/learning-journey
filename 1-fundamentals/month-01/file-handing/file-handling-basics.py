
"""Open files to read"""
f = open("C:\\Users\\iriom\\Desktop\\Texto.txt")
txt = f.read()
print(txt)

"""Read for characters"""
"""txt2 = f.read(7)
print(txt2)"""

"""Read only the first line"""
"""txt = f.readline()
print(txt)"""

"""Read in lines and make a lines list"""

#txt = f.readlines()
#print(txt)

"""Read and close the files with"""

"""with open("C:\\Users\\iriom\\Desktop\\Texto.txt") as f:
    txt = f.read().splitlines()
    print(txt)"""
    
"""Open files to write"""

"""with open("C:\\Users\\iriom\\Desktop\\Texto.txt", "a") as f:
    txt = f.write("Texto añadido al final")
    print(txt)"""
    
"""with open("C:\\Users\\iriom\\Desktop\\Texto12434.txt", "w") as f:
    txt = f.write("Creará un nuev archivo")
    print(txt)"""