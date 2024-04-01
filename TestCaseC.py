class Ticket:
    '''Creating class for Ticket'''
    def __init__(self, event_name, ticket_type, price):
        self.event_name = event_name
        self.ticket_type = ticket_type
        self.price = price

class Visitor:
    '''Creating class for Visitor'''
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

class TicketingSystem:
    '''Creating class for Ticket System'''
    def __init__(self):
        self.ticket_types = {
            "Adult": 63,
            "Child": 0,
            "Teacher/Student/Senior": 0,
            "Group": 0  # Discount applied separately
        }

    def purchase_ticket(self, visitor, event_name, ticket_type):
        if ticket_type == "Group":
            print("Group discounts are applied separately. Please contact the ticketing office.")
            return None

        elif ticket_type in self.ticket_types:
            price = self.calculate_price(ticket_type, visitor)
            if price == 0:
                show_id = input("Do you have valid ID proof? [yes/no]: ").lower()
                if show_id == "yes":
                    print("Valid ID: The ticket is free.")
                else:
                    price = self.ticket_types[ticket_type]  # Original price
            price_with_vat = self.apply_vat(price)
            ticket = Ticket(event_name, ticket_type, price_with_vat)
            print(f"Ticket purchased for {visitor.name} for {price_with_vat} AED.")
            return ticket

        else:
            print("Invalid ticket type")
            return None

    def purchase_group_ticket(self, group_size, event_name):
        group_discount = 0.5
        price_per_person = self.calculate_price("Adult", Visitor("", 30, ""))
        total_price_before_discount = group_size * price_per_person
        total_price_after_discount = total_price_before_discount * (1 - group_discount)
        price_with_vat = self.apply_vat(total_price_after_discount)
        ticket = Ticket(event_name, "Group", price_with_vat)
        print(f"Group ticket purchased for {group_size} people for {event_name} for {price_with_vat} AED. A 50% discount was given.")
        return ticket

    def calculate_price(self, ticket_type, visitor):
        if ticket_type == "Child" or (ticket_type == "Adult" and (visitor.age < 18 or visitor.age >= 60)):
            return 0
        elif ticket_type == "Teacher/Student/Senior":
            if visitor.occupation == "Student":
                return 0
            else:
                return 63  # Default adult price
        else:
            return self.ticket_types.get(ticket_type, 0)

    def apply_vat(self, price):
        vat_rate = 0.05
        return price * (1 + vat_rate)

# Example usage
ticketing_system = TicketingSystem()

# Individual ticket purchase
name = input("Enter your name: ")
age = int(input("Enter your age: "))
occupation = input("Enter your occupation (Teacher/Student/Senior): ")

visitor1 = Visitor(name, age, occupation)
individual_ticket = ticketing_system.purchase_ticket(visitor1, "Special Exhibition", "Teacher/Student/Senior")

# Group ticket purchase
group_size = int(input("Enter group size: "))
group_ticket = ticketing_system.purchase_group_ticket(group_size, "Guided Tour")