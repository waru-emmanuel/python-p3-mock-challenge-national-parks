class NationalPark:
    all_parks = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 3:
            raise Exception("Name must be a string longer than 3 characters")
        self._name = name
        self.trips_list = []
        NationalPark.all_parks.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        raise Exception("Cannot change the name of the national park")

    def trips(self):
        return self.trips_list

    def visitors(self):
        return list({trip.visitor for trip in self.trips_list})

    def total_visits(self):
        return len(self.trips_list)

    def best_visitor(self):
        visitors_count = {}
        for trip in self.trips_list:
            if trip.visitor in visitors_count:
                visitors_count[trip.visitor] += 1
            else:
                visitors_count[trip.visitor] = 1
        return max(visitors_count, key=visitors_count.get)

    @classmethod
    def most_visited(cls):
        most_visited_park = max(cls.all_parks, key=lambda park: len(park.trips_list))
        return most_visited_park

class Visitor:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise Exception("Name must be a string between 1 and 15 characters")
        self._name = name
        self.trips_list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (1 <= len(new_name) <= 15):
            raise Exception("Name must be a string between 1 and 15 characters")
        self._name = new_name

    def trips(self):
        return self.trips_list

    def national_parks(self):
        return list({trip.national_park for trip in self.trips_list})

    def total_visits_at_park(self, park):
        return sum(1 for trip in self.trips_list if trip.national_park == park)

class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.validate_date_format(start_date)
        self.validate_date_format(end_date)
        self._visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date
        visitor.trips_list.append(self)
        national_park.trips_list.append(self)
        Trip.all.append(self)

    def validate_date_format(self, date):
        if not isinstance(date, str) or not date.endswith("th") or len(date.split()) != 2:
            raise Exception("Dates must be strings in the format 'MMMDDth'")

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_start_date):
        self.validate_date_format(new_start_date)
        self._start_date = new_start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, new_end_date):
        self.validate_date_format(new_end_date)
        self._end_date = new_end_date

    @property
    def visitor(self):
        return self._visitor

    @property
    def national_park(self):
        return self._national_park
