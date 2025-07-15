"""
Utilizamos o gerenciador de pacote Pip

pip install coloroma
pip install --upgrade pip

colorama-> Colorir textos no terminal

"""
from colorama import Fore, Back, Style
print(Fore.RED + "Geek University")
print("Geek University")
print(Style.RESET_ALL)
print("Geek University")