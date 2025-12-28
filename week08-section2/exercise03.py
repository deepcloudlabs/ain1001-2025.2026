class Employee:
    def __init__(self, identity, fullname, salary):
        self.identity = identity
        self.fullname = fullname
        self.salary = salary

    def __str__(self):
        #return f'identity:{self.identity},fullname: {self.fullname},salary: {self.salary}'
        return 'identity: %-18s, full name: %24s, salary: %6.0f' % (self.identity, self.fullname, self.salary)

jack = Employee(identity='11111111110', fullname='jack shephard', salary=200_000.52845678)
x = str(jack)
print(x)
print(str(jack))
