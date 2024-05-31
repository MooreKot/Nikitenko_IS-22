import os

os.chdir("..")
os.chdir("PZ_11")


files = os.listdir()
print("Файлы в каталоге PZ_11:")
for file in files:
    if os.path.isfile(file):
        print(file)


os.chdir("..")
os.makedirs("test/test1", exist_ok=True)


os.rename("PZ_6/PZ_6_1.py", "test/PZ_6_1.py")
os.rename("PZ_6/PZ_6_2.py", "test/PZ_6_2.py")


os.rename("PZ_7/PZ_7_1.py", "test/test1/test.txt")


os.chdir("test")
for file in os.listdir():
    if os.path.isfile(file):
        print(f"{file}: {os.path.getsize(file)} байт")


os.chdir("..")
os.chdir("PZ_11")
shortest_file = min(files, key=len)
print("Файл с самым коротким именем в PZ_11:", os.path.basename(shortest_file))

os.chdir("..")
for file in os.listdir():
    if file.endswith(".pdf"):
        os.startfile(file)

os.remove("test/test1/test.txt")
