genome=input('Enter a genome string:')
if 'ATG' in genome:
    a=genome.count('ATG') 
    b=genome.index('ATG')
    if 'TAG'or'TAA'or'TGA' in genome:
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
                if len(genome[b+3:c])%3==0 and 'ATG' not in genome[b+3:c] and 'TAG' not in genome[b+3:c] and 'TAA' not in genome[b+3:c] and 'TGA' not in genome[b+3:c]:
                    print(genome[b+3:c])
            b+=c+3
    else:
        print('no gene is found')
else:
    print('no gene is found')
#%%
'''正確
1.範例輸出
2.ATG + 三的倍數不含TAG/TAA/TGA + TAG/TAA/TGA
'''
'''錯誤
1.ATG + 三的倍數不含TAG/TAA/TGA (跳出 name 'c' is not defined)
2.ATG + 不是三的倍數也不含TAG/TAA/TGA (跳出 name 'c' is not defined)
'''