

konv_klm = 1.609344
konv_miles = 0.621371
while True :
    user = input('Please Type "k" konvert to kilometers or "m" konvert to Miles: ').lower()
    if user == 'k':
        try:
            kilometer = float(input('please Type kilometers: '))
            result = format(kilometer * konv_miles, '.3f') 
            print('Mile: ', result)
        except ValueError :
            print('Please Enter The Number! ')

    elif user == 'm':
        try:
            miles = float(input('please type Miles: '))
            result = format(miles * konv_klm, '.3f')
            print('Kilometers =',result)
        except ValueError :
            print('Please Enter The Number! ')
    


# konv_klm = 1.609344
# g = format(konv_klm,'.2f')
# print(g)

# format( ცვლადი ,'.1f' ) რიცხვი წერტილის შემდეგ ნიშნავს რამდენი ციფრი იყვეს . შემდეგ