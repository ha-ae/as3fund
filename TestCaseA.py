class Artwork:
    '''Creating class for Artwork'''
    def __init__(self, title, artist, date, price, installation_date):
        self._title = title
        self._artist = artist
        self._date = date
        self._price = price
        self._installation_date = installation_date

    # Getter methods
    def get_title(self):
        return self._title

    def get_artist(self):
        return self._artist

    def get_date(self):
        return self._date

    def get_price(self):
        return self._price

    def get_installation_date(self):
        return self._installation_date

    # Setter methods
    def set_title(self, title):
        self._title = title

    def set_artist(self, artist):
        self._artist = artist

    def set_date(self, date):
        self._date = date

    def set_price(self, price):
        self._price = price

    def set_installation_date(self, installation_date):
        self._installation_date = installation_date


class Exhibition:
    '''Creating class for Exhibition'''
    def __init__(self, name, location, start_date, end_date):
        self._name = name
        self._location = location
        self._start_date = start_date
        self._end_date = end_date

    # Getter methods
    def get_name(self):
        return self._name

    def get_location(self):
        return self._location

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_location(self, location):
        self._location = location

    def set_start_date(self, start_date):
        self._start_date = start_date

    def set_end_date(self, end_date):
        self._end_date = end_date


class Visitor:
    '''Creating class for Visitor'''
    def __init__(self, name, age, nationality):
        self._name = name
        self._age = age
        self._nationality = nationality

    # Getter methods
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_nationality(self):
        return self._nationality

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_nationality(self, nationality):
        self._nationality = nationality


class Ticket:
    '''Creating class for Ticket'''
    def __init__(self, visitor, event, price):
        self._visitor = visitor
        self._event = event
        self._price = price

    # Getter methods
    def get_visitor(self):
        return self._visitor

    def get_event(self):
        return self._event

    def get_price(self):
        return self._price

    # Setter methods
    def set_visitor(self, visitor):
        self._visitor = visitor

    def set_event(self, event):
        self._event = event

    def set_price(self, price):
        self._price = price


class Museum:
    '''Creating class for Museum'''
    def __init__(self):
        self._artworks = []
        self._exhibitions = []
        self._tickets = []

    # Getter methods
    def get_artworks(self):
        return self._artworks

    def get_exhibitions(self):
        return self._exhibitions

    def get_tickets(self):
        return self._tickets

    # Setter methods
    def set_artworks(self, artworks):
        self._artworks = artworks

    def set_exhibitions(self, exhibitions):
        self._exhibitions = exhibitions

    def set_tickets(self, tickets):
        self._tickets = tickets

    def add_artwork(self, artwork):
        self._artworks.append(artwork)

    def add_exhibition(self, exhibition):
        self._exhibitions.append(exhibition)

    def sell_ticket(self, visitor, event):
        if event.get_name() == "Special Event":
            price = event.get_price()
        elif event.get_name() == "Tour":
            price = 63 * 0.5  # 50% discount for tours
        else:
            price = 63  # Default price for exhibitions
        # Apply VAT
        price_with_vat = price * 1.05
        ticket = Ticket(visitor, event, price_with_vat)
        self._tickets.append(ticket)
        return ticket

    def display_payment_receipt(self, ticket):
        print("Payment Receipt:")
        print(f"Visitor: {ticket.get_visitor().get_name()}")
        print(f"Event: {ticket.get_event().get_name()}")
        print(f"Price: {ticket.get_price()} AED")

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