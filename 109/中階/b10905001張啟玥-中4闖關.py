genome=input('Enter a genome string:')
if 'ATG' and ('TAG'or'TAA'or'TGA') in genome:
    a=genome.count('ATG') #出現幾次ATG
    b=genome.index('ATG') #ATG在第幾個位子
    for i in range(a):
        if 'TAG' in genome:
            c=genome.index('TAG') #TAG在第幾個位子
            if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]: #基因長度為三的倍數且不包含ATG、TAG、TAA、TGA
                print(genome[b+3:c]) #ATG和TAG之間的字
        if 'TAA' in genome:
            c=genome.index('TAA')
            if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                print(genome[b+3:c])
        if 'TGA' in genome:
            c=genome.index('TGA')
            if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                print(genome[b+3:c])
        b+=c+3 #ATG下一次的位子
else:
    print('no gene is found')