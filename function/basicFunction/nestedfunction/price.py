def total(price,tax):
    def calculate():
        return price*tax
    return price+calculate()
#print(total(1000,0.18))

def bill(amount):
    def discount():
        if amount>10000:
            return amount*0.10
        return 0
    d=discount()
    final=amount-d
    return final
print(bill(15000))
print(bill(5000))