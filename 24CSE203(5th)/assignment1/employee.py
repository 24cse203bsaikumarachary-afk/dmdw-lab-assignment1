class Employee:
    def __init__(self):
        self.empid=int(input("enter employee id"))
        self.name=input("enter name")
        self.basic_pay=float(input("enter basic pay"))
        self.ta=float(input("enter ta"))
        self.da=float(input("enter da"))
        
    def calculate(self):
        self.gross_pay=self.basic_pay+(0.10*self.ta)+(0.40*self.da)
    def display(self):
        print("\nEmployee Details")
        print("Employee ID:",self.empid)
        print("name:",self.name)
        print("basic pay:",self.basic_pay)
        print("TA:",self.ta)
        print("DA:",self.da)
        print("Gross Pay:",self.gross_pay)
e=Employee()
e.calculate()
e.display()
