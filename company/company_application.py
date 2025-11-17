import operator
from employee import Employee
from manager import Manager
from operator import attrgetter

e1 = Employee("M. Rossi", 20000)

m = Manager("B. Boss", 50000,
             "Marketing")

print(m)

e2 = Employee("A. Arancioni", 3000)

employees = [e1, e2, m]

for emp in employees:
    emp.increment_wage() # Incrementa la paga in base al tipo di lavoratore (employee/manager)
    #print(emp.__class__.__name__)
    print(emp)

eA = Employee("G. Verdi", 20000)
eB = Employee("G. Verdi", 35000)

# Così come quando stampo viene verificata la presenza del metodo __str()__,
# quando confronto viene verificata quella del metodo __eq()__

if eA == eB:
    print("Sono uguali")
else:
    print("Sono diversi")

print("\nLista odinata")

# Come ordinare una lista di Employee definendo metodi __eq__() e __lt__()
sortedList = sorted(employees)

# Come ordinare una lista di Employee con operator
sortedList = sorted(employees, key=operator.attrgetter("wage")) # In base alla paga

# Come ordinare una lista di Employee con lambda expression
sortedList = sorted(employees, key=lambda emp: emp.wage) # In base alla paga

for emp in sortedList:
    print(emp)