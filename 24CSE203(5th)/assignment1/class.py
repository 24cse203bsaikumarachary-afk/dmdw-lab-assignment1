class Product:
    def input(self):
        self.product_no=int(input("enter product number:"))
        self.product_name=input("enter product name:")
        self.cost=float(input("enter cost:"))
        self.quantity=int(input("enter quantity:"))
    def calculate(self):
        self.total_amount=self.cost*self.quantity
    def display(self):
        print("product no:",self.product_no)
        print("product name:",self.product_name)
        print("cost:",self.cost)
        print("quantity:",self.quantity)
        print("total amount:",self.total_amount)
products=[]
for i in range(5):
    print("\n enter Product",i+1)
    p=Product()
    p.input()
    p.calculate()
    products.append(p)
highest=products[0]
for p in products:
    if p.total_amount>highest.total_amount:
        highest=p
print("\nProduct with highest total amount")
highest.display()
    
