unit=int(input('enter unit use '))

bill=unit*5 if unit<=100 else unit*7 if unit>100 and unit<=200 else unit*10
print('Total bill ',bill)