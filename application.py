from company.employee import Employee
from company.super_manager import SuperManager
import flet
from miaclasse import MiaClasse

e = Employee("John", 120000)
print(e)

# Python stampa il riferimento di memoria se non viene inizializzato il medoto __str()__
# altrimenti come nel caso delle classi che abbiamo creato, viene stampato l'oggetto

s = SuperManager("Super Manager", 12000000, "All")
print(s)

# Uso della classe MiaClasse creata con il decoratore @dataclass
mia1 = MiaClasse(100, "Ciao") # Assegno i valori ai due attributi (int, str)
mia2 = MiaClasse(50, "Hello")

lista = []

lista.append(mia1)
lista.append(mia2)

print("\nLista di oggetti MiaClasse prima dell'ordinamento")
for o in lista:
    print(o) # stampabile grazie al metodo __repr__() definito in @dataclass

lista_ordinata = sorted(lista) # Ordinabile grazie ai metodi di ordinamento definiti in @dataclass
print(lista_ordinata)