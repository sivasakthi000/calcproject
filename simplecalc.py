x,y=int(input('enter first number:')),int(input('enter second number:'))
summ=x+y
dif=x-y
mul=x*y
div=x/y
op=input('enter operation:')
if op=='sum':
    print(summ)
elif op=='dif':
    print(dif)
elif op=='mul':
    print(mul)
elif op=='div':
    print(div)
else:
    print('no operation')