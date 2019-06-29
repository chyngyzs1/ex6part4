class House():
    def __init__(self, household_type):
        self.household_type = household_type
        self.total_area = 40
        self.list_furniture = []

    def add(self,furniture):
        if furniture.lower() == 'bed':
            self.total_area -= 4
        if furniture.lower() == 'wardrobe':
            self.total_area -= 2
        if furniture.lower() == 'table':
            self.total_area -= 1.5
        self.list_furniture.append(furniture)
        print('\nList of furniture: ' + str(self.list_furniture) + '\nRemaining area: ' + str(self.total_area))

    def discribe(self):
        print('Houshold type: ' + self.household_type)
        print('Total area: ' + str(self.total_area))

a = House('Type 1')
a.discribe()
a.add('bed')
a.add('table')
        