class Exhibition:
    '''Creating class for Exhibition'''
    def __init__(self, title, location, start_date, end_date):
        self.title = title
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

class Event:
    '''Creating class for Event''' #makes up a sixth new class if not counting repeats
    def __init__(self, title, location, date, duration):
        self.title = title
        self.location = location
        self.date = date
        self.duration = duration

class Museum:
    '''Creating class for Museum'''
    def __init__(self, name):
        self.name = name
        self.exhibitions = []
        self.events = []

    def add_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)

    def add_event(self, event):
        self.events.append(event)

    def announce_opening(self):
        print(f"Welcome to {self.name} Museum's GRAND OPENING!")
        print("We are thrilled to announce the opening of our Historical Art Show!")
        print("--DETAILS--")
        for exhibition in self.exhibitions:
            print("**EXHIBITION")
            print(f" Exhibition: {exhibition.title}")
            print(f" Location: {exhibition.location}")
            print(f" Dates: {exhibition.start_date} to {exhibition.end_date}")
        for event in self.events:
            print("**EVENT")
            print(f" Event: {event.title}")
            print(f" Location: {event.location}")
            print(f" Date: {event.date}")
            print(f" Duration: {event.duration} hours")
        print("--END OF DETAILS--")
        print("Enjoy your visit!")

# Creating a museum instance
my_museum = Museum("Torathy")

# Adding exhibitions
exhibition1 = Exhibition("Arab Artifacts", "Ahli Galleries", "7/3/2024", "17/3/2024")
my_museum.add_exhibition(exhibition1)

# Adding events
event1 = Event("Surprise Celebrity Concert", "Ahli Stadium", "12/3/2024", 3.5)
my_museum.add_event(event1)

# Announcing the opening
my_museum.announce_opening()