class Employee:
    def input(self):
        self.Employee_num = int(input("Enter emp number: "))
        self.Employee_name = input("Enter emp name: ")
        self.pay = float(input("Enter cost: "))
        self.ta = float(input("Enter TA: "))
        self.da = float(input("Enter DA: "))

    def calculate(self):
        self.gross_pay = self.cost * self.quantity

    def display(self):
        print("Product No:", self.product_num)
        print("Product Name:", self.product_name)
        print("Cost:", self.cost)
        print("Quantity:", self.quantity)
        print("Total Amount:", self.total_amount)


products = []

for i in range(5):
    print(f"\nEnter details for Product {i+1}")
    p = Product()
    p.input()
    p.calculate()
    products.append(p)

highest = products[0]

for p in products:
    if p.total_amount > highest.total_amount:
        highest = p

print("\nProduct with Highest Total Amount:")
highest.display()
