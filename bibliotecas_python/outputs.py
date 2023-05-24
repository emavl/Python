import os

def limpiar_consola(): 
  print("\n")
  os.system("pause")
  os.system("cls")


def limpiar_consola() -> None: 
     """ 
     This function clears the console screen and waits for user input to continue. 
     """ 
     _ = input('Presione una tecla para continuar...') 
     if os.name in ['ce', 'nt', 'dos']: os.system("cls") 
     else: os.system("clear")













