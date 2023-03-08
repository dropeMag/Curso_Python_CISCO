import os

# APAGA UM DIRETÓRIO SE ESTE ESTIVER VAZIO
os.mkdir("temporario")
print(os.listdir())

os.rmdir("temporario")
print(os.listdir())

print('=-'*90)

# APAGA OS SUBDIRETÓRIOS VAZIOS DE UM DIRETÓRIO
# APAGA O DIRETÓRIO PAI SE ESTE ESTIVER VAZIO
os.mkdir("temporario")
os.makedirs("temporario/temp1")
os.makedirs("temporario/temp2")
os.makedirs("temporario/temp3")
print(os.listdir())
print(os.listdir("temporario"))

os.removedirs("temporario/temp1")
os.removedirs("temporario/temp2")
os.removedirs("temporario/temp3")
print(os.listdir())
