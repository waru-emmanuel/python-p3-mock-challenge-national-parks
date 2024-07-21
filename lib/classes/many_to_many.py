class NationalPark:
    
    def __init__(self, name):
        self.name = name
        self._trips = []  # List to store trips related to this park
    
    def add_trip(self, trip):
        self._trips.append(trip)  # Method to add a trip to the park
    
    def trips(self):
        return self._trips  # Return the list of trips
    
    def visitors(self):
        # Return a set of unique visitors to the park
        return set(trip.visitor for trip in self._trips)
    
    def total_visits(self):
        # Return the total number of trips to the park
        return len(self._trips)
    
    def best_visitor(self):
        # Find the visitor with the most visits to the park
        from collections import Counter
        visitor_counter = Counter(trip.visitor for trip in self._trips)
        if visitor_counter:
            return visitor_counter.most_common(1)[0][0]
        return None


class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        
        # Add the trip to the visitor and national park
        visitor.add_trip(self)
        national_park.add_trip(self)


class Visitor:
    
    def __init__(self, name):
        self.name = name
        self._trips = []  # List to store trips related to this visitor
    
    def add_trip(self, trip):
        self._trips.append(trip)  # Method to add a trip to the visitor
    
    def trips(self):
        return self._trips  # Return the list of trips
    
    def national_parks(self):
        # Return a set of unique national parks visited by the visitor
        return set(trip.national_park for trip in self._trips)
    
    def total_visits_at_park(self, park):
        # Return the total number of trips the visitor has made to a specific park
        return sum(1 for trip in self._trips if trip.national_park == park)
