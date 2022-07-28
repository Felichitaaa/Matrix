from classes_and_objects.movie_world.customer import Customer
from classes_and_objects.movie_world.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []#list Customer object
        self.dvds = []#list DVD's objects

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    @staticmethod
    def age(list_dvds, movie_id):
        for d in list_dvds:
            if d.id == movie_id:
                age_ = d.age_restriction
                return age_

    @staticmethod
    def is_the_movie_rented(movie_id, list_dvds):
        name = ''
        for dvd in list_dvds:
            if dvd.id == movie_id:
                name = dvd.name
                if dvd.is_rented:
                    return True, name
        return False, name

    @staticmethod
    def find_the_customer(list_cust, person_id):
        for person in list_cust:
            if person_id == person.id:
                return person

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd_state, dvd_name = MovieWorld.is_the_movie_rented(dvd_id, self.dvds)
        age_restriction = MovieWorld.age(self.dvds, dvd_id)
        customer = MovieWorld.find_the_customer(self.customers, customer_id)
        if customer.id == customer_id:
            if dvd_state:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        return f"{customer.name} has already rented {dvd}"
                return f"DVD is already rented"

            if customer.age < age_restriction:
                return f"{customer.name} should be at least" \
                       f" {age_restriction} to rent this movie"
            else:
                the_movie = None
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = True
                        the_movie = dvd
                for person in self.customers:
                    if person.id == customer_id:
                        person.rented_dvds.append(the_movie)
                return f"{customer.name} has successfully rented {dvd_name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = MovieWorld.find_the_customer(self.customers, customer_id)
        for dvd in customer.rented_dvds:
            if dvd.id == dvd_id:
                dvd.is_rented = False
                customer.rented_dvds.remove(dvd)
                return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for cust in self.customers:
            result += f"{cust}\n"
        for dvd in self.dvds:
            result += f"{dvd}\n"
        return result