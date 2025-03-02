
# Chase Burks
# Date: 3/02/2025
# P1HW2
# Basic Math Equation Solver

print('This program will calculate your travel expenses')

budget = int(input(f'Enter Budget: '))
destination = input('Enter your travel destination: ')
gas_money = int(input(f'How much do you think you will spend on gas: '))
accommodation = int(input(f'Approximately, how much will you need for accomodation/hotel?: '))
food= int(input(f'Last, how much do you need for food?: '))
total = budget - (gas_money + accommodation + food)

print('------------ Travel Expenses ------------')
print('Location:', destination)
print('Initial Budget:', budget,'\n')
print('Fuel:', gas_money)
print('Accommodation:', accommodation)
print('Food:', food,'\n')
print('remaining Balance:', total)