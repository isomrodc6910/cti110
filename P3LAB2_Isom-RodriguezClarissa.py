desired_service = input('Enter desired auto service:\n') 
print('You entered:',desired_service) 
if desired_service.lower() == 'oil change': 
    print('Cost of oil change: $35')
elif desired_service.lower() == 'tire rotation': 
    print('Cost of tire rotation: $19')
elif desired_service.lower() == 'car wash': 
    print('Cost of car wash: $7')
else: #else case 
    print('Error: Requested service is not recognized') 
