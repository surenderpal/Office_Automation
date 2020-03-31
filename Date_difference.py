from datetime import datetime,timedelta,date
current_date=datetime.date(datetime.now())
Daily_trend = current_date-timedelta(180)
Product=current_date-timedelta(90)
Location=current_date-timedelta(90)
Daily_trend1 = current_date+timedelta(180)
Product1=current_date+timedelta(90)
Location1=current_date+timedelta(90)
custom_date=date(2019,10,3)
custom_product_date=custom_date+ timedelta(90)
print('\t\t\t\tPast')

print('Select Daily tred (180 Days) Past date from Today is: ',Daily_trend)
print('Seledt Product (90 Days) Past date from Today is: ',Product)
print('Select Location (90 Days) Past date from Today is: ',Location)

print('\t\t\t\tfuture')

print('Select Daily tred (180 Days) Future date from Today is: ',Daily_trend1)
print('Seledt Product (90 Days) Future date from Today is: ',Product1)
print('Select Location (90 Days) Future date from Today is: ',Location1)

print('\t\t\t\tCustom Date:')
print('custom product date from the "2019,10,3"for product is:',custom_product_date)
print('custom product date from the "2019,10,3"for location is:',custom_product_date)
print('custom product date from the "2019,10,3"for Daily trend is:',custom_date+ timedelta(180))
