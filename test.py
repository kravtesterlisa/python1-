class Engine(object):
    tank_petrol = 60
    tank_diesel = 75

    def __init__(self):
        self.engine_type2 = 'Petrol'
        self.engine_type1 = 'Diesel'


class Cars(Engine):
    petrol_cost = 2.4
    diesel_cost = 1.8
    cars_created = 0
    car_price = 10000
    max_mileage_petrol = 200000
    max_mileage_diesel = 150000

    def __init__(self, cars_type):
        self.cars_type = cars_type
        super(self.__class__, self).__init__()
        self.__class__.cars_created += 1
        self.engine = Engine()
        # print 'Created car number: '+ str(self.__class__.cars_created)
        if self.__class__.cars_created % 3 == 0:
            self.cars_type = self.engine_type2
        else:
            self.cars_type = self.engine_type1

    def max_mileage(self):
        max_mileage_petrol = 200000
        max_mileage_diesel = 150000

        if max_mileage_petrol > 200000:
            print('Please, return your petrol car for repairs ')
        if  max_mileage_diesel > 150000:
            print('Please, return your diesel car for repairs')

class Tahograph():

    def __init__(self, road):
        self.road = road
        pass

#ostatochnya stoimost mashiny
def __init__(self,meleage,final_price):
    car_price = 10000
    low_cost_petrol = 100
    low_cost_diesel = 120
    self.final_price = final_price
    self.meleage = meleage
    if final_price = car_price -(self.meleage /1000 * self.low_cost_petrol):
         print ('Final price of your car' + str(final_price))

#probeg do utilizacyi
def __init__(self, meleage,meleage_to_util):
    self.meleage = meleage
    max_meleage_petrol = 200000
    max_meleage_diesel = 150000
    self.meleage_to_util = meleage_to_util
    if meleage_to_util = max_meleage_petrol - self.meleage:
         print('Your meleage to util' + str(meleage_to_util))

#potracheno topliva
def __init__(self, meleage,fuel_rate, oil):
    self.fuel_rate = fuel_rate
    self.meleage = meleage
    self.oil = oil
    if oil = meleage/100*fuel_rate_petrol:
        print('You lost oil'+str(oil))







cars_park = [Cars() for _ in range(10)]
for car in cars_park:
    print(car.__dict__)

car=Car()