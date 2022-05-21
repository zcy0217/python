genome=input('Enter a genome string:')
if 'ATG' in genome:
    a=genome.count('ATG') #出現幾次
    b=genome.index('ATG') #出現位子
    if 'TAG' in genome[b+3:b+6] or 'TAA' in genome[b+3:b+6] or 'TGA' in genome[b+3:b+6] or 'ATG' in genome[b+3:b+6]:
        print('no gene is found')
    elif 'TAG' in genome:
        for i in range(a):
            if 'TAG' in genome:
                c=genome.index('TAG') 
                if len(genome)==6: 
                    print('no gene is found1') #ATGTAG
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]: 
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found2') #ATG+其他英文字母不含ATG、TAG、TAA、TGA且不為三的倍數+TAG
            if 'TAA' in genome:
                c=genome.index('TAA')
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c]) 
            if 'TGA' in genome:
                c=genome.index('TGA')
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
            b+=c+3
    elif 'TAA' in genome:
        for i in range(a):
            if 'TAG' in genome:
                c=genome.index('TAG')
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]: 
                    print(genome[b+3:c])
            if 'TAA' in genome:
                c=genome.index('TAA')
                if len(genome)==6: 
                    print('no gene is found3') #ATGTAA
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found4') #ATG+其他英文字母不含ATG、TAG、TAA、TGA且不為三的倍數+TAA
            if 'TGA' in genome:
                c=genome.index('TGA')
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
            b+=c+3
    elif 'TGA' in genome:
        for i in range(a):
            if 'TAG' in genome:
                c=genome.index('TAG')
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]: 
                    print(genome[b+3:c])
            if 'TAA' in genome:
                c=genome.index('TAA')
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
            if 'TGA' in genome:
                c=genome.index('TGA')
                if len(genome)==6: 
                    print('no gene is found5') #ATGTGA/ATGATG
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found6') #ATG+其他英文字母不含ATG、TAG、TAA、TGA且不為三的倍數+TGA
            b+=c+3
    else:
        print('no gene is found~') #ATG+其他英文字母不含ATG、TAG、TAA、TGA
else:
    print('no gene is found~~') #沒有ATG