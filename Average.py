

##საშვალო არითმეტიკულის გამოთვლა. ეს მეთოდი ლისტით იყენებს უფრო მეტ მეხსიერებას ვიდრე ქვედა მეთოდი 2

number = [5,3,6,9 ]
print(sum(number)/len(number)) # 5.75

numLine = [] # ან list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done': 
        break
    value = float(inp)
    numLine.append(value)

average = sum(numLine) / len(numLine)
print('Average:', average)

#საშვალო არითმეტიკულის გამოთვლა სხვა მეთოდით 2

total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == "done" : 
        break
    value = float(inp)
    total = total + value
    count += 1
average = total / count
print('Average:', average)
