x,y=int(input('enter first number:')),int(input('enter second number:'))
op=input('enter operation:')
if op=='sum':
    print(x+y)
elif op=='dif':
    print(x-y)
elif op=='mul':
    print(x*y)
elif op=='div':
    print(x/y)
else:
    print('no operations')