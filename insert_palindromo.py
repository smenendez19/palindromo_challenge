import os

# Verificar palindromo
def is_palindromo(string):
    length = len(string)
    pal = True
    for i in range(0, length // 2):
        if string[i] == string[length - 1 - i]:
            pal = True
        else:
            pal = False
            break
    return pal

# Substring palindromo de mayor longitud en string
def sub_max_palindromos(string):
    pal = ""
    length = len(string)
    for i in range(0, length):
        for j in range(length - 1, 0, -1):
            if string[i] == string[j] and i < j and len(string[i:j + 1]) > 1:
                if len(string[i:j + 1]) > len(pal) and is_palindromo(string[i:j + 1]):
                    pal = string[i:j + 1]
                    if len(string[i:j + 1]) > length // 2:
                        break
    return pal

# Insertar caracteres para que sea palindromo
def insert_palindromo(string, length):
    count = 0
    pal = sub_max_palindromos(string)
    max_len = len(pal)
    if max_len == 0:
        count = length - 1
    elif max_len < length:
        count = length - max_len
    return count


for path, _, files in os.walk("input/"):
    for file in files:
        print(path + file)
        with open(path + file, "rt") as f:
            lines = f.readlines()
            length = int(lines[0].replace("\n",""))
            string = lines[1].replace("\n","")
        count = insert_palindromo(string, length)
        with open("output/" + file,"wt") as fw:
            fw.write(str(count))