# Set var to int.
cars = 100
# Set var to int.
space_in_a_car = 4.0
# Set var to int.
drivers = 30
# Set var to int.
passengers = 90
# Set var to diff of vars.
cars_not_driven = cars - drivers
# Set var to var val.
cars_driven = drivers
# Set var to val of multiplied vars.
carpool_capacity = cars_driven * space_in_a_car
# Set var to result of var division.
average_passengers_per_car = passengers / cars_driven

# Print a lot of stuff.
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
