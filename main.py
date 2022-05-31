import os
from datetime import datetime
import pandas as pd
import sys
import os.path

def restart_program():
    pass

diretório = input("Digite...:")
df = input("Pergunta...: ")

if df == "":
  var1 = input("Digite...: ")
  var2 = input("Digite...: ")
  var3 = input("Digite...: ")
  if not os.path.exists(diretório+var1.upper()+'/A'+var2+var3):
    os.makedirs(diretório+var1.upper()+'/A'+var2+var3)
elif df == "":
  var1 = input("Digite...: ")
  var2 = input("Digite...: ")
  var3 = input("Digite...: ")
  if not os.path.exists(diretório+var1.upper()+'/A'+var2+var3):
    os.makedirs(diretório+var1.upper()+'/A'+var2+var3)
  print("Pasta criada")
else:
    print("Entrada inválida")
    restart_program()
exit()
