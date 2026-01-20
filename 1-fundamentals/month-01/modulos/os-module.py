import os

print(os.getcwd())

os.chdir(r"C:\Users\iriom\Desktop")
print(os.getcwd())

files = os.listdir()

route = os.path.join(os.getcwd(), "coco.txt")
print(route)

print(os.path.exists(route))
print(os.path.isfile(route))
print(os.path.isdir(route))