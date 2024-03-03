class Item:
    def __init__(self, name, net_price, vat_rate):
        self.name = name
        self.net_price = net_price
        self.vat_rate = vat_rate

class Invoice:
    def __init__(self, items):
        self.items = items

    def calculate_total_net(self):
        return sum(item.net_price for item in self.items)

    def calculate_tax_values(self):
        tax_values = {}
        for item in self.items:
            tax_value = item.net_price * item.vat_rate / 100
            if item.vat_rate in tax_values:
                tax_values[item.vat_rate] += tax_value
            else:
                tax_values[item.vat_rate] = tax_value
        return tax_values

    def print_summary(self):
        tax_values = self.calculate_tax_values()
        
        print(f"|{'':<15}", end="")
        print(f"|{'Total':<15}|", end="")
        for item in items:
            print(f" {item.name} |", end="")
        print()

        print(f"|{'-'*15}|{'-'*15}|", end="")
        for item in items:
            print(f"{'-'*(len(item.name)+2)}|", end="")
        print()

        print(f"|{'Net':<15}", end="")
        print(f"|{self.calculate_total_net():<15}|", end="")
        for item in items:
            print(f"{item.net_price:<{len(item.name)+2}}|", end="")
        print()

        print(f"|{'8%':<15}", end="")
        print(f"|{tax_values[8]:<15}|", end="")
        for item in items:
            tax_value = item.net_price*(8/100) if item.vat_rate == 8 else 'none'
            print(f"{tax_value:<{len(item.name)+2}}|", end="")
        print()

        print(f"|{'23%':<15}", end="")
        print(f"|{tax_values[23]:<15}|", end="")
        for item in items:
            tax_value = item.net_price*(23/100) if item.vat_rate == 23 else 'none'
            print(f"{tax_value:<{len(item.name)+2}}|", end="")
        print()

items = [
    Item("Clean Code, Robert C. Martin", 100.00, 8),
    Item("Applying UML and Patterns, C. Larman", 300.00, 8),
    Item("Shipping", 50, 23)
]

invoice = Invoice(items)
invoice.print_summary()