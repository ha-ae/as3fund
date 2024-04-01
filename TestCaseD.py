class MuseumTicket:
    def __init__(self, exhibition, location, date, quantity, visitor_type):
        self.exhibition = exhibition
        self.location = location
        self.date = date
        self.quantity = quantity
        self.visitor_type = visitor_type

    def calculate_total(self):
        ticket_price = self.calculate_ticket_price()
        subtotal = ticket_price * self.quantity
        total = self.apply_discount(subtotal)
        return total

    def calculate_ticket_price(self):
        if self.visitor_type == "Adult":
            return 63
        elif self.visitor_type in ["Child", "Teacher", "Student", "Senior"]:
            return 0  # Free ticket for children, teachers, students, and seniors
        else:
            return 0  # Handle other visitor types here

    def apply_discount(self, subtotal):
        if self.visitor_type == "group":
            return subtotal * 0.5  # 50% discount for groups
        else:
            return subtotal

    def generate_receipt(self, total):
        print("----------------------------------")
        print("Museum Ticket Purchase Receipt    ")
        print("----------------------------------")
        print("Exhibition:", self.exhibition)
        print("Location:", self.location)
        print("Dates Valid:", self.date)
        print("Quantity:", self.quantity)
        print("Visitor Type:", self.visitor_type)
        print("----------------------------------")
        print("TOTAL PRICE: {}.00 AED".format(total))
        print("Paid by: Visa")
        print("Change: 0.00AED")
        print("----------------------------------")
        print("Thank you for visiting our museum!")
        print("                                  ")
        print("Please show the receipt if you plan")
        print("to visit during valid days for admission")
        print("----------------------------------")

# Example usage:
ticket1 = MuseumTicket("Torathy Civilizations Exhibition", "Ahli Galleries", "7/3/24 - 17/3/24", 2, "Adult")
total_amount = ticket1.calculate_total()
ticket1.generate_receipt(total_amount)
