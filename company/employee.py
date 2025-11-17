class Employee:
    def __init__(self, name, wage):
        self._name = name
        self._wage = wage

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def wage(self):
        return self._wage

    @wage.setter
    def wage(self, value):
        self._wage = value

    def __str__(self):
        return f"{self._name}, {self._wage}"

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(name={self._name}, wage={self._wage})")

    def increment_wage(self):
        self._wage += 5000

    def __eq__(self, other):
        # Decido il metodo di confronto
        return self.name == other.name

    def __lt__(self, other):
        # Decido il metodo di ordinamento
        return self.name < other.name

# Se voglio mantenere del codice, all'interno del mio modulo posso farlo,
# ma devo evitare che il codice venga eseguito ANCHE quando il modulo
# viene importato. Posso farlo controllando __name__

if __name__ == "__main__":
    e = Employee("Prova",10000)
    print(e)
    e.increment_wage()
    print(e)