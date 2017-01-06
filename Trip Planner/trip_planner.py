
"""This is my first program I have coded using python.This program is basically 
a trip planner for users where they can calculate their total fare including travel, stay or rental. 
For now this planner works for certia cities and hotels mentioned
I am hoping to learn more in order to create more complex programs.
I TESTED THE PROGRAM here : https://goo.gl/qFrxnx """
#defining functions
# Rental cost with discount offered based on days stayed in hotel
def rental_cost(days):
    cost = days * 100
    if days >=7:
        cost = cost - 50
    elif days < 7:
        cost = cost - 20
    return cost

#   one of the hotel costs based on city and room type chosen
def single_armada_cost(nights,city):
    if city == "SHARJAH":
        total = 210 * nights
    elif city == "DUBAI":
        total = 300 * nights
    return total

#   one of the hotel costs based on city and room type chosen
def double_armada_cost(nights,city):
    if city == "SHARJAH":
        total = 500 * nights
    elif city == "DUBAI":
        total = 600 * nights
    return total
    
#   one of the hotel costs based on city and room type chosen    
def single_khor_cost(nights,city):
    if city == "SHARJAH":
        total = 200 * nights
    elif city == "DUBAI":
        total = 350 * nights
    return total

#   one of the hotel costs based on city and room type chosen
def double_khor_cost(nights,city):
    if city == "SHARJAH":
        total = 340 * nights
    elif city == "DUBAI":
        total = 600 * nights
    return total

#This function outputs the cost of travel based on their mode of travel and ticket type    
def mod_check(mode,travel):
    while True:
        if mode not in [ "AIR" , "BUS"]:
            print "Type Air or Bus "
            mode = raw_input("Try Again")
        else:
            if mode == "AIR" and travel == "RETURN":
                return  str(plane_oneway_cost(city))
                break
            elif mode == "AIR" and travel == "RETURN":
                return str(plane_return_cost(city))
                break
            elif mode == "BUS" and travel  == "ONEWAY":
                return  str(bus_oneway_cost(city))
                break
            elif mode == "BUS" and travel =="RETURN":
                return  str(bus_return_cost(city))
                break
                
 # plane cost for onway travel based on cities  
def plane_oneway_cost(city):
    if city == "SHARJAH":
        return 900
    if city == "DUBAI":
        return 1100
    
# plane cost for return ticket based on cities  
def plane_return_cost(city):
    if city == "SHARJAH":
        return 2000
    if city == "DUBAI":
        return 3000
    
 # bus cost for oneway travel based on cities 
def bus_oneway_cost(city):
    if city == "SHARJAH":
        return 222
    elif city == "DUBAI":
        return 475
    
   # bus cost for return ticket based on cities
def bus_return_cost(city):
    if city == "SHARJAH":
        return 400
    elif city == "DUBAI":
        return 800
        
     # This entire function has two parts 1) validating user input 2) output the total cost of thier trip based on whether customer 
    # rents a car or not.
def rental_room(room,rental):
    if hotel_rev == "ARMADA" and room == "SINGLE" and rental == "N":
        print "DEAR %s,your total trip cost for %s %s rooms at %s for %s days is: $"%(name,room_num,room_type,hotel_rev,hotel_days) + str((int(room_num  )*single_armada_cost(int(hotel_days),city)) + int(mod_check(mode,ticket)) + int(spending))
    elif hotel_rev == "ARMADA"and room == "DOUBLE" and rental == "N":
        print "DEAR %s,your e total trip cost for %s %s rooms at %s for %s days is: $" %(name,room_num,room_type,hotel_rev,hotel_days) + str((int(room_num)*double_armada_cost(int(hotel_days),city)) + int(mod_check(mode,ticket)) + int(spending))
        
    elif hotel_rev == "ARMADA"and room == "SINGLE" and rental == "Y":
        rental_days = raw_input("For how many days you want to rent?: ") 
        print " "
        if int(rental_days) > int(hotel_days):
            print " You cannot rent a car more then days you are planning to stay!"
            print " "
            rental_days = raw_input("For how many days you want to rent?: ")
            print "DEAR %s, your total trip cost for %s %s rooms at %s HOTEL for %s days is: $" %(name ,room_num,room_type,hotel_rev,hotel_days) + str((int(room_num)*single_armada_cost(int(hotel_days),city)) + int(mod_check(mode,ticket)) + int(spending) + rental_cost(int(rental_days)))
        else:
            print " "
            print "DEAR %s, your total trip cost for %s %s rooms at %s HOTEL for %s days is: $" %(name ,room_num,room_type,hotel_rev,hotel_days) + str((int(room_num)*single_armada_cost(int(hotel_days),city)) + int(mod_check(mode,ticket)) + int(spending) + rental_cost(int(rental_days)))
        
    elif hotel_rev == "ARMADA" and room == "DOUBLE" and rental == "Y":
        rental_days = raw_input("For how many days you want to rent?: ")
        print " "
        if int(rental_days) > int(hotel_days):
            print " You cannot rent a car more then days you are planning to stay!"
            print " "
            rental_days = raw_input("For how many days you want to rent?: ")
            print " "
            print "DEAR %s, your total trip cost for %s %s rooms at %s HOTEL for %s days is: $" %(name ,room_num,room_type,hotel_rev,hotel_days) + str((int(room_num)*double_armada_cost(int(hotel_days),city)) + int(mod_check(mode,ticket)) + int(spending) + rental_cost(int(rental_days)))
        else:
            print " "
            print "DEAR %s, your total trip cost for %s %s rooms at %s HOTEL for %s days is: $" %(name ,room_num,room_type,hotel_rev,hotel_days) + str((int(room_num)*double_armada_cost(int(hotel_days),city)) + int(mod_check(mode,ticket)) + int(spending) + rental_cost(int(rental_days)))
             
    elif hotel_rev == "KHOR" and  room == "SINGLE" and rental == "N":
        print "DEAR %s, your total trip cost for %s %s rooms at %s HOTEL for %s days is: $" %(name,room_num,room_type,hotel_rev,hotel_days) + str((int(room_num)*single_khor_cost(int(hotel_days),city)) + int(mod_check(mode,ticket)) + int(spending))
        
    elif hotel_rev == "KHOR"and  room == "DOUBLE" and rental == "N":
        print "DEAR %s, your total trip cost for %s %s rooms at %s HOTEL for %s days is: $" %(name,room_num,room_type,hotel_rev,hotel_days) + str((int(room_num)*double_khor_cost(int(hotel_days),city)) + int(mod_check(mode,ticket)) + int(spending))
        
    elif hotel_rev == "KHOR"and  room == "SINGLE" and rental == "Y":
        rental_days = raw_input("For how many days you want to rent?: ")
        print " "
        if int(rental_days) > int(hotel_days):
            print " You cannot rent a car more then days you are planning to stay!"
            print " "
            rental_days = raw_input("For how many days you want to rent?: ")
            print "  "
            print "DEAR %s, your total trip cost for %s %s rooms at %s HOTEL for %s days is: $" %(name ,room_num,room_type,hotel_rev,hotel_days) + str((int(room_num)*single_khor_cost(int(hotel_days),city)) + int(mod_check(mode,ticket)) + int(spending) + rental_cost(int(rental_days)))
        else:
            print " "
            print "DEAR %s, your total trip cost for %s %s rooms at %s HOTEL for %s days is: $" %(name ,room_num,room_type,hotel_rev,hotel_days) + str((int(room_num)*single_khor_cost(int(hotel_days),city)) + int(mod_check(mode,ticket)) + int(spending) + rental_cost(int(rental_days)))
        
    elif hotel_rev == "KHOR"and  room == "DOUBLE" and rental == "Y":
        rental_days = raw_input("For how many days you want to rent?: ")
        print " " 
        if int(rental_days) > int(hotel_days):
            print " You cannot rent a car more then days you are planning to stay!"
            print " "
            rental_days = raw_input("For how many days you want to rent?: ")
            print " "
            print "DEAR %s, your total trip cost for %s %s rooms at %s HOTEL for %s days is: $" %(name ,room_num,room_type,hotel_rev,hotel_days) + str((int(room_num)*double_khor_cost(int(hotel_days),city)) + int(mod_check(mode,ticket)) + int(spending) + rental_cost(int(rental_days)))
        else:
            print " "
            print "DEAR %s, your total trip cost for %s %s rooms at %s HOTEL for %s days is: $" %(name ,room_num,room_type,hotel_rev,hotel_days) + str((int(room_num)*double_khor_cost(int(hotel_days),city)) + int(mod_check(mode,ticket)) + int(spending) + rental_cost(int(rental_days)))
        
#from this point it is my main program    
mod = [ "Air" , "Bus"]

#user interface   
print "Welcome to Trip Planner!"
print " "
print "**Please note your answers should be CASE-SENSITIVE**"
print " "
name = raw_input("May I know you name: ")
print " "
print "***Please select DUBAI or SHARJAH as city"
print " " 
city = raw_input("Which city are you planning to visit: ")

while True: # condition to make sure user doesnot enter cities other then specified
    if city != "DUBAI" and city != "SHARJAH":
        print "This trip planner only for DUBAI and SHARJAH"
        city = raw_input("Which city are you planning to visit: ")
    else:
        break
        
mode = raw_input("Please choose the mode of transaport (AIR/BUS): ")
while True:# condition to make sure user doesnot enter mode other then specified
    if mode != 'AIR' and mode != 'BUS':
        print "Type Air or Bus"
        mode = raw_input("Try Again")
    else:
        break
        
ticket = raw_input("Do you want ONEWAY or RETURN ticket? ")
while True: # condition to make sure user doesnot enter ticket type other then specified
    if ticket != "ONEWAY" and ticket != "RETURN":
        print " Not valid option"
        ticket  = raw_input("Do you want ONEWAY or RETURN ticket? ")
    else: 
        print " "
        print "**YOUR %s fare to %s by %s is: $" %(ticket,city,mode) +str(mod_check(mode,ticket))
        break
#below is my calculation total trip cost based on thier choice to live in hotel or not!        
print " "       
hotel_ans = raw_input("Are you planning to stay in Hotel? (Y/N): ") # total cost calculation based on user choice
if hotel_ans == "N": # if user does not wants to live in hotel
    spending = raw_input("Please enter you aprox spending money otherthen ticket or hotell fares: $")
    print " "
    print "**Your Total travel cost is: $" + str(int(spending) + int(mod_check(mode,ticket)))
           
elif hotel_ans == "Y": # if user wants to live in hotel
    print " "
    print "**Here are the two hotels available!!: ARMADA and KHOR."
    print " "
    hotel_rev = raw_input("Please select the Hotel: " )
    
    if hotel_rev == "ARMADA": # if user agrees to live, However user need to tell which hotel
        room_type = raw_input("Do you prefer a SINGLE room or a DOUBLE room?: ")
        if room_type != "SINGLE" and room_type != "DOUBLE":
            print " "
            print " Select valid option (SINGLE/DOUBLE)"
            room_type = raw_input("Do you prefer a SINGLE room or a DOUBLE room?: ")
            print " " 
        room_num = raw_input("How many rooms do you need?: ")
        hotel_days = raw_input("How many days are you planning to stay at ARMADA Hotel: ")
        spending = raw_input("Please enter your aprox spending money other then hotel or flight: $")
        rental = raw_input("Do you want to rent a car during your stay?(Y/N): ")
        print " "
        rental_room(room_type,rental) # calling function declared above to cacluate cost based on user response to whether rent a car or not
    elif hotel_rev== "KHOR": # if user agrees to live, However user need to tell which hotel
        room_type = raw_input("Do you prefer SINGLE room or DOUBLE room?: ")
        if room_type != "SINGLE" and room_type != "DOUBLE":
            print " "
            print " Select valid option (SINGLE/DOUBLE)"
            room_type = raw_input("Do you prefer a SINGLE room or a DOUBLE room?: ")
            print " " 
        room_num = raw_input("How many rooms do you need?: ")
        hotel_days = raw_input("How many days are you planning to stay at KHOR Hotel: ")
        spending = raw_input("Please enter your aprox spending money other then hotel/flight fares: $")
        rental = raw_input("Do you want to rent a car?(Y/N): ")
        print " "
        rental_room(room_type,rental)# calling function declared above to cacluate cost based on user response to whether rent a car or not
else : # if nethier Y or N entered
    print "Not a valid selection"
    hotel_ans = raw_input("Are you planning to stay in Hotel? (Y/N): ")

    
        
