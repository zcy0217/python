genome=input('Enter a genome string:')
if 'ATG' in genome:
    a=genome.count('ATG') 
    b=genome.index('ATG')
    if 'TAG' in genome:
        for i in range(a):
            if 'TAG' in genome:
                c=genome.index('TAG') 
                if len(genome)==6: 
                    print('no gene is found3') #ATGTAG
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]: 
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found1') #ATG+其他英文字母不含ATG、TAG、TAA、TGA且不為三的倍數+TAG
                elif len(genome[b+3:c])%3!=0 and 'ATG' in genome[b+3:c] and 'TAG' in genome[b+3:c] and 'TAA' in genome[b+3:c] and 'TGA' in genome[b+3:c]:
                    print('no gene is found2')
            if 'TAA' in genome:
                c=genome.index('TAA')
                if len(genome)==6:
                    print('no gene is found6')
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found4')
                elif len(genome[b+3:c])%3!=0 and 'ATG' in genome[b+3:c] and 'TAG' in genome[b+3:c] and 'TAA' in genome[b+3:c] and 'TGA' in genome[b+3:c]:
                    print('no gene is found5')
            if 'TGA' in genome:
                c=genome.index('TGA')
                if len(genome)==6:
                    print('no gene is found9')
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found7')
                elif len(genome[b+3:c])%3!=0 and 'ATG' in genome[b+3:c] and 'TAG' in genome[b+3:c] and 'TAA' in genome[b+3:c] and 'TGA' in genome[b+3:c]:
                    print('no gene is found8')
            b+=c+3
    elif 'TAA' in genome:
        for i in range(a):
            if 'TAG' in genome:
                c=genome.index('TAG')
                if len(genome)==6:
                    print('no gene is found12')
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]: 
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found10')
                elif len(genome[b+3:c])%3!=0 and 'ATG' in genome[b+3:c] and 'TAG' in genome[b+3:c] and 'TAA' in genome[b+3:c] and 'TGA' in genome[b+3:c]:
                    print('no gene is found11')
            if 'TAA' in genome:
                c=genome.index('TAA')
                if len(genome)==6: 
                    print('no gene is found15') #ATGTAA
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found13') #ATG+其他英文字母不含ATG、TAG、TAA、TGA且不為三的倍數+TAA
                elif len(genome[b+3:c])%3!=0 and 'ATG' in genome[b+3:c] and 'TAG' in genome[b+3:c] and 'TAA' in genome[b+3:c] and 'TGA' in genome[b+3:c]:
                    print('no gene is found14')
            if 'TGA' in genome:
                c=genome.index('TGA')
                if len(genome)==6:
                    print('no gene is found18')
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found16')
                elif len(genome[b+3:c])%3!=0 and 'ATG' in genome[b+3:c] and 'TAG' in genome[b+3:c] and 'TAA' in genome[b+3:c] and 'TGA' in genome[b+3:c]:
                    print('no gene is found17')
            b+=c+3
    elif 'TGA' in genome:
        for i in range(a):
            if 'TAG' in genome:
                c=genome.index('TAG')
                if len(genome)==6:
                    print('no gene is found21')
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]: 
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found19')
                elif len(genome[b+3:c])%3!=0 and 'ATG' in genome[b+3:c] and 'TAG' in genome[b+3:c] and 'TAA' in genome[b+3:c] and 'TGA' in genome[b+3:c]:
                    print('no gene is found20')
            if 'TAA' in genome:
                c=genome.index('TAA')
                if len(genome)==6:
                    print('no gene is found24')
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found22')
                elif len(genome[b+3:c])%3!=0 and 'ATG' in genome[b+3:c] and 'TAG' in genome[b+3:c] and 'TAA' in genome[b+3:c] and 'TGA' in genome[b+3:c]:
                    print('no gene is found23')
            if 'TGA' in genome:
                c=genome.index('TGA')
                if len(genome)==6: 
                    print('no gene is found27') #ATGTGA
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found25') #ATG+其他英文字母不含ATG、TAG、TAA、TGA且不為三的倍數+TGA
                elif len(genome[b+3:c])%3!=0 and 'ATG' in genome[b+3:c] and 'TAG' in genome[b+3:c] and 'TAA' in genome[b+3:c] and 'TGA' in genome[b+3:c]:
                    print('no gene is found26')
            b+=c+3
    else:
        print('no gene is found~') #ATG+其他英文字母不含ATG、TAG、TAA、TGA
else:
    print('no gene is found~~') #沒有ATG