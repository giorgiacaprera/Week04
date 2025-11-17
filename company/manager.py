from company.employee import Employee

class Manager(Employee):
    def __init__(self, name, wage, managedUnit ):
        # La prima cosa che devo fare per costruire/ inizializzare un Manager
        # è costruire/inizializzare la "sua parte" da Employee, lo faccio
        # usando la funzione super()
        super().__init__(name, wage)

        # Poi posso definire/inizializzare eventuali attributi specifici del manager
        self._managedUnit = managedUnit

    # Anche se non definisco di nuovo __str__() E __repr()__ sono ereditate da Employee
    # Se volessi un comportamento diverso da Employee potrei ridefinirle diversamente

    def __str__(self):
        # Per stampare posso creare un nuovo metodo:
        #return f"{self._name}, {self._wage}, {self._managedUnit}"

        # Opuure delegare all'Employee du stamparsi ed aggiungere solo managedUNit:
        return f"{super().__str__()}, {self._managedUnit}"

    # Creo una versione del metodo increment_wage() definito in Employee
    # ma specifica per il Manager
    def increment_wage(self):
        self._wage += 20000