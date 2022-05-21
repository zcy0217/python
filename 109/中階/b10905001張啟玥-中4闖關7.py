genome=input('Enter a genome string:')
if 'ATG' in genome:
    a=genome.count('ATG')
    b=genome.find('ATG')
    if 'TAG' in genome[b+3:b+6] or 'TAA' in genome[b+3:b+6] or 'TGA' in genome[b+3:b+6] or 'ATG' in genome[b+3:b+6]:
        print('no gene is found')
    elif 'TAG' in genome:
        for i in range(a):
            if 'TAG' in genome:
                c=genome.find('TAG',b+3)
                if len(genome)==6: 
                    print('no gene is found')
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]: 
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found') 
            if 'TAA' in genome:
                c=genome.find('TAA',b+3)
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c]) 
            if 'TGA' in genome:
                c=genome.find('TGA',b+3)
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
            b+=c+3
    elif 'TAA' in genome:
        for i in range(a):
            if 'TAG' in genome:
                c=genome.find('TAG',b+3)
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]: 
                    print(genome[b+3:c])
            if 'TAA' in genome:
                c=genome.find('TAA',b+3)
                if len(genome)==6: 
                    print('no gene is found')
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found')
            if 'TGA' in genome:
                c=genome.find('TGA',b+3)
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
            b+=c+3
    elif 'TGA' in genome:
        for i in range(a):
            if 'TAG' in genome:
                c=genome.find('TAG',b+3)
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]: 
                    print(genome[b+3:c])
            if 'TAA' in genome:
                c=genome.find('TAA',b+3)
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
            if 'TGA' in genome:
                c=genome.find('TGA',b+3)
                if len(genome)==6: 
                    print('no gene is found')
                elif len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
                elif len(genome[b+3:c])%3!=0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print('no gene is found')
            b+=c+3
    else:
        print('no gene is found')
else:
    print('no gene is found')