try:
    gross= int(input ('what is your gross salary?'))
except ValueError:
    print("sorry, that was not a valid number")
if gross < 1000:
    print ('the income tax is 10%')
    incometax= 10
elif gross <2000 and gross>=1000:
    print('the income tax is 12%')
    incometax=12
elif gross <4000 and gross >=2000:
    print('the income tax is 14%')
    incometax=14
else:
    print('the income tax is 18%')
    incometax=18

numchildren= int(input('how many children do you have?'))
if gross<2000:
    finalincometax=incometax-1*numchildren
    print('Your final income tax is', finalincometax, '%')
else:
    finalincometax=incometax-0.5*numchildren
    print('Your final income tax is', finalincometax, '%')



