#input convert inte there respective value
destination = input('what is your destination ?')
distance = float(input('what is the distance of your traject, in miles ?'))
mpg = float(input('what is the fuel efficiency of the car in miles/gallon?'))
gas_price = float(input('current gas price?'))
nights = int(input('number of nights you will stay?'))
hotel_cost = float(input('average hotel cost per night?'))
food_budget = float(input('daily food budget?'))
#different calculations
Gallons = distance / mpg
Total_gas_cost = Gallons * gas_price
Total_hotel_cost = nights * hotel_cost
Total_food_cost = (nights + 1) * food_budget
Grand_total = Total_gas_cost + Total_hotel_cost + Total_food_cost


print('='*4 + 'Road Trip Budget Planner' + '='*4 + '\n')
print(f'Destination:  {destination}')
print(f'Distance:   {distance} miles\n')
print('-'*4 + 'Cost Breakdown' + '-'*4)
print(f'Gas ({Gallons:.2f} gal @ ${gas_price:.2f}/gal):   ${Total_gas_cost:.2f}')
print(f'Hotel ({nights} nights @ ${hotel_cost:.2f}):     ${Total_hotel_cost:.2f}')
print(f'Food ({nights + 1} days @ ${food_budget:.2f}):    ${Total_food_cost:.2f}') # +1 it is for the day after the last night
print('-' * 40)
print(f'Estimated Total:                 ${Grand_total:.2f}')

