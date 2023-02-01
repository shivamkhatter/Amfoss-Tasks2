import pyinputplus as pyip

response = pyip.inputMenu(['Wheat : 10' ,'White : 20','Sourdough : 15'],'Which type of bread \n', numbered=True)
response2 = pyip.inputMenu(['Chicken : 25','Turkey : 20','Ham : 30','Tofu : 20'],'Which meat \n', numbered=True)
print('Do you want cheese')
response3 = pyip.inputYesNo()
if response3 == 'yes':
    Cheesetype = pyip.inputMenu(['Cheddar : 15','Swiss : 20','Mozzarella : 25'],'Which type of cheese \n', numbered=True)
    
else :
    Cheesetype='none'
print('Do you want sauce')
response4 = pyip.inputYesNo()
if response4 == 'yes':
    sauce = pyip.inputMenu(['Mayo : 25','Mustard : 30','Lettuce : 15','Tomato : 10'],'Which sauce \n', numbered=True)
else:
    sauce='none'
last = pyip.inputNum('Enter no. of Sandwiches: ',min =1)


menu={'Wheat : 10':10,'White : 20':20,'Sourdough : 15':15,'Chicken : 25':25,'Turkey : 20':20,'Ham : 30':30,
      'Tofu : 20':20,'none':0,'Cheddar : 15':15,'Swiss : 20':20,
      'Mozzarella : 25':25,'Mayo : 25':25,'Mustard : 30':30,'Lettuce : 15':15,'Tomato : 10':10}
price = ((menu[response]+menu[response2]+menu[Cheesetype]+menu[sauce])*last)
print('price is ',price)
    
