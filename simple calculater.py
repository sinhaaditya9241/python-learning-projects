operand_1=int(input('enter operand1: '))
operand_2=int(input('enter operand2:'))
oparator=input('enter oparator:')
#if else elif

if oparator=='+':
    print(operand_1 + operand_2)
elif oparator=='-':
    print(operand_1-operand_2)
elif oparator=='*':
    print(operand_1*operand_2)
elif oparator=='/':
    print(operand_1/operand_2)
else:
    print('none')

print('Thankyou')