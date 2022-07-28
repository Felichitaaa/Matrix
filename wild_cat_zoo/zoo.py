from encapsulation.ex.wild_cat_zoo.animal import Animal


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price > self.__budget:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for person in self.workers:
            if worker_name in person.name:
                self.workers.remove(person)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_all_salaries = 0
        for person in self.workers:
            sum_of_all_salaries += person.salary
        if sum_of_all_salaries <= self.__budget:
            self.__budget -= sum_of_all_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        budget_for_all_animals = 0
        for animal in self.animals:
            budget_for_all_animals += animal.money_for_care
        if budget_for_all_animals <= self.__budget:
            self.__budget -= budget_for_all_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        amount_of_animals = {"Lions": [], "Tigers": [], "Cheetahs": []}

        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                amount_of_animals['Lions'].append([animal])

            elif animal.__class__.__name__ == 'Tiger':
                amount_of_animals['Tigers'].append([animal])

            elif animal.__class__.__name__ == 'Cheetah':
                amount_of_animals['Cheetahs'].append([animal])

        for animal, data in amount_of_animals.items():
            count_of_animal = len(data)
            result += f"----- {count_of_animal} {animal}:\n"
            for x in data:
                for y in x:
                    result += repr(y) + "\n"
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        amount_of_workers = {"Keepers": [], "Caretakers": [], "Vets": []}

        for person in self.workers:
            if person.__class__.__name__ == 'Keeper':
                amount_of_workers['Keepers'].append([person])

            elif person.__class__.__name__ == 'Caretaker':
                amount_of_workers['Caretakers'].append([person])

            elif person.__class__.__name__ == 'Vet':
                amount_of_workers['Vets'].append([person])

        for person, data in amount_of_workers.items():
            count_of_workers = len(data)
            result += f"----- {count_of_workers} {person}:\n"
            for x in data:
                for y in x:
                    result += repr(y) + "\n"
        return result
