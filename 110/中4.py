cards=int(input('請輸入信用卡號碼:'))
s1=s2=0
for i in range(0,len(str(cards)),2):
    cards=str(cards)
    if int(cards[i])*2<=9:
        s1+=int(cards[i])*2
    elif int(cards[i])*2>=10:
        s1+=int(cards[i])*2//10+int(cards[i])*2%10
        
for i in range(1,len(str(cards)),2):
    s2+=int(cards[i])

if (s1+s2)%10==0 and ((cards[0]==4 or 5 or 6) or (cards[0]==3 and cards[1]==7)):
    print('此信用卡為有效')
else:
    print('此信用卡為無效')