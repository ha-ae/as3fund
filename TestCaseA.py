class Artwork:
    '''Creating class for Artwork'''
    def __init__(self, title, artist, date, price, installation_date):
        self.title = title
        self.artist = artist
        self.date = date
        self.price = price
        self.installation_date = installation_date


class Exhibition:
    '''Creating class for Exhibition'''
    def __init__(self, name, location, start_date, end_date):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date


class Visitor:
    '''Creating class for Visitor'''
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality


class Ticket:
    '''Creating class for Ticket'''
    def __init__(self, visitor, event, price):
        self.visitor = visitor
        self.event = event
        self.price = price


class Museum:
    '''Creating class for Museum'''
    #these make up 5 classes, the rest are on the other codes
    def __init__(self):
        self.artworks = []
        self.exhibitions = []
        self.tickets = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def add_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)

    def sell_ticket(self, visitor, event):
        if event.name == "Special Event":
            price = event.price
        elif event.name == "Tour":
            price = 63 * 0.5  # 50% discount for tours
        else:
            price = 63  # Default price for exhibitions
        # Apply VAT
        price_with_vat = price * 1.05
        ticket = Ticket(visitor, event, price_with_vat)
        self.tickets.append(ticket)
        return ticket

    def display_payment_receipt(self, ticket):
        print("Payment Receipt:")
        print(f"Visitor: {ticket.visitor.name}")
        print(f"Event: {ticket.event.name}")
        print(f"Price: {ticket.price} AED")

    def add_new_artwork(self):
        title = input("Enter title of the artwork: ")
        artist = input("Enter artist name: ")
        date = input("Enter date of creation: ")
        price = int(input("Enter price of the artwork: $"))
        installation_date = input("Enter date of installation: ")
        artwork = Artwork(title, artist, date, price, installation_date)
        self.add_artwork(artwork)
        print("New artwork added successfully!")


# Sample usage
if __name__ == "__main__":
    louvre = Museum()

    while True:
        choice = input("Enter 'yes' to add new artwork or 'no' to exit: ")
        if choice == 'yes':
            louvre.add_new_artwork()
        elif choice == 'no':
            break
        else:
            print("Invalid choice. Please try again.")