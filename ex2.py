#total number of cars
cars = 100

#number of seats in car
space_in_car = 4

#total number of drivers
drivers = 30

#total number of passengers
passengers = 90

#total number of cars not driven today
cars_not_driven = cars - drivers

#total number of cars that can be driven
cars_driven = drivers

#the total capcity for carpooling today
carpool_capacity = cars_driven * space_in_car

#average passengers per car that can be driven
avg_passenger_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "passengers today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", avg_passenger_per_car, "in each car.")


