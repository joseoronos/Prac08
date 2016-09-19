# from taxi import Taxi
# from taxi import UnreliableCar
from taxi import SilverServiceTaxi


# prius = Taxi("Prius 1", 100)
# prius.drive(40)
# prius.get_fare()
# print(prius)

# prius.start_fare()
# prius.drive(100)
# prius.get_fare()
# print(prius)

# test_car = UnreliableCar("Test Car", 100, 10)
# test_car.drive(50)
# print(test_car)

test_taxi = SilverServiceTaxi("Test Taxi", 100, 2)
test_taxi.drive(10)
test_taxi.get_fare()
print(test_taxi)
print("${:.2f}". format(test_taxi.get_fare()))