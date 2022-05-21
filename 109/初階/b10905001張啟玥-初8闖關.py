ID=input('輸入ID:')

a=0
total=0

if ID[0]=='A': 
    a=10
if ID[0]=='B': 
    a=11
if ID[0]=='C': 
    a=12
if ID[0]=='D': 
    a=13
if ID[0]=='E': 
    a=14
if ID[0]=='F': 
    a=15
if ID[0]=='G': 
    a=16
if ID[0]=='H': 
    a=17
if ID[0]=='I': 
    a=34
if ID[0]=='J': 
    a=18
if ID[0]=='K': 
    a=19
if ID[0]=='L': 
    a=20
if ID[0]=='M': 
    a=21
if ID[0]=='N': 
    a=22
if ID[0]=='O': 
    a=35
if ID[0]=='P': 
    a=23
if ID[0]=='Q': 
    a=24
if ID[0]=='R': 
    a=25
if ID[0]=='S': 
    a=26
if ID[0]=='T': 
    a=27
if ID[0]=='U': 
    a=28
if ID[0]=='V': 
    a=29
if ID[0]=='W': 
    a=32
if ID[0]=='X': 
    a=30
if ID[0]=='Y': 
    a=31
if ID[0]=='Z': 
    a=33

a=((a//10)+(a%10)*9)
total=8*int(ID[1])+7*int(ID[2])+6*int(ID[3])+5*int(ID[4])+4*int(ID[5])+3*int(ID[6])+2*int(ID[7])+1*int(ID[8])+int(ID[9])+a

if total%10==0:
    print('real')
else:
    print('fake')