# Age calculator in years,months,days 
from calendar import monthrange
from datetime import datetime

today = datetime.now()

while True:
    
    Birth_date_str = input('Enter your date of birth (dd-mm-yyyy): ')
    Bd_obj = datetime.strptime(Birth_date_str,'%d-%m-%Y')

    if Bd_obj.year <= today.year:
    
        if Bd_obj.month <= today.month and Bd_obj.day <= today.day:
            age = [(today.year - Bd_obj.year),(today.month - Bd_obj.month),(today.day - Bd_obj.day)]
        elif Bd_obj.month <= today.month and Bd_obj.day > today.day:
            age = [(today.year - Bd_obj.year),(today.month - Bd_obj.month)-1,((monthrange(today.year, today.month-1)[1]-Bd_obj.day) + today.day)]
        elif Bd_obj.month > today.month and Bd_obj.day <= today.day:
            age = [(today.year - Bd_obj.year)-1,((12-Bd_obj.month) + today.month),(today.day - Bd_obj.day)]    
        elif Bd_obj.month > today.month and Bd_obj.day > today.day:
            age = [(today.year - Bd_obj.year)-1,((12-Bd_obj.month) + today.month),(Bd_obj.day - today.day)]       

        print(f'Today, you turned {age[0]} years {age[1]} months {age[2]} days old')
        break
    
    else:
        print('Date of birth should be earlier than today')