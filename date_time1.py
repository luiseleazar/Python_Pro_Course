from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'LATAM datetime format: {my_str}')

my_str = my_datetime.strftime('%m/%d/%Y')
print(f'US datetime format: {my_str}')
