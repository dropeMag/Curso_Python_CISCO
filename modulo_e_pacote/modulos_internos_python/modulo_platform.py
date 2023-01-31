from platform import *

print(platform())               # permite aceder os dados da platarforma subjacente: hardware, OS e versão do intérprete
print(platform(aliased=True))   # aliased, quando True, pode apresentar nomes alternativos das camadas subjacentes
print(platform(terse=True))     # terse, quando True, pode convencer a função a apresentar uma forma mais breve
print('-='*15)
print(machine())                # retorna o nome genérico do processador
print(processor())              # retorna uma string preenchida com o nome do processador real (se possível)
print(system())                 # devolve o nome genérico do OS como uma cadeia
print(version())                # fornece a versão do OS
print('-='*15)
print(python_implementation())  # devolve uma string denotando a implementação do python
print(python_version_tuple())   # devolve uma tupla com:
                                #     - parte principal da versão;
                                #     - parte secundária da vesão;
                                #     - número da patch level.
