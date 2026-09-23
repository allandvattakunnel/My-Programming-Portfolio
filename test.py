class Event():
    def __init__(self, name, event_id, location, duration=0, is_booked=False):
        self.__name = name
        self.__event_id = event_id
        self.__location = location
        self.__duration = duration
        self.is_booked = is_booked

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        if isinstance(duration, int):
            self.__duration = duration
        else:
            return

    def get_event_id(self):
        return self.__event_id

    def __str__(self):
        return f"{self.__name} {self.__event_id} {self.__location} {self.__duration}"


class Itinerary():
    def __init__(self, visitor_name):
        self.__events = []
        self.visitor_name = visitor_name

    def add_event(self, event):
        if isinstance(event, Event):
            self.__events.append(event)
        else:
            return

    def __str__(self):
        txt = f"{self.visitor_name}'s Adelaide University Open Day Itinerary:"
        for event in self.__events:
            if event.is_booked:
                book = "is booked"
            else:
                book = ""

            txt += f"\n - {event} {book} "
        return txt


event_1 = Event("Campus Tour", "E001", "Main Quad", 45)
event_2 = Event("Engineering Info Session", "E002",
                "Engineering Building", 30, True)
print(event_1)
my_itinerary = Itinerary("Riley")
my_itinerary.add_event(event_1)
my_itinerary.add_event(event_2)

print(my_itinerary)
