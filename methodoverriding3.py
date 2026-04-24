class Payment:
    def __init__(self,money):
        self.money=money

    def gateway(self):
        print(f"Processing the Payment of {self.money} rupee. ")

class UPI(Payment):
    def __init__(self,money):
        super().__init__(money)

    def gateway(self):
        print(f"Processing the UPI payment of {self.money} ruppes.")

p1=Payment(20000)
p1.gateway()
u1= UPI(50000)
u1.gateway()