def hotel_cost(num_nights): #  this function calculates the cost of staying num_nights at a hotel in new york, london or tokyo. The cost depends on the location as well was the number of nights
    if city_flight.lower() == "london": # we use lower() so that it does not matter what cases the subject uses 
        cost = 482*num_nights
    elif city_flight.lower() == "new york":
        cost = 562*num_nights
    elif city_flight.lower() == "tokyo":
        cost = 585*num_nights
    return cost

def plane_cost(city_flight): # this function calculates the cost of the flight depending on the destination city
    if city_flight.lower() == "london":
        cost = 100
    elif city_flight.lower() == "new york":
        cost = 200
    elif city_flight.lower() == "tokyo":
        cost = 300
    return cost

def car_rental(rental_days): # this function calculates the total cost of leasing a car for rental_days 
    cost = rental_days*27
    return cost

def holiday_cost(hotel_cost, plane_cost, car_rental): # this function will sum up the above three values
    cost = hotel_cost + plane_cost + car_rental
    return cost

city_flight = input("To what city are you flying? London, New York or Tokyo? ")

if city_flight.lower() == "london" or city_flight.lower() == "new york" or city_flight.lower() == "tokyo": # this if statement is for error handling purposes in case the subject enters a city that is not covered  
    num_nights = int(input("How many nights will you be staying? "))
    rental_days = int(input("How many days will you be leasing a car? "))
    if rental_days > num_nights + 1:
        print("You have asked to lease a car for " + str(rental_days) + " days but you are only staying for " + str(num_nights) + " nights. Please try again.") # I have included this if statement to prevent the user from leasing the car for longer than the length of his or her stay
    else:
        print("The total cost of the holiday is £" + str(holiday_cost(hotel_cost(num_nights),plane_cost(city_flight),car_rental(rental_days))) + ", comprising £" + str(hotel_cost(num_nights)) + " for the cost of staying " + str(num_nights) + " nights at the hotel, £" + str(plane_cost(city_flight)) + " for the cost of the flight to " + city_flight[0].upper() + city_flight[1:].lower() + ", and £" + str(car_rental(rental_days)) + " for the cost of leasing a car for " + str(rental_days) + " days.") # here we print in sentence form the full cost with a breakdown
else:
    print("Sorry. We only book holidays to London, New York and Tokyo.")