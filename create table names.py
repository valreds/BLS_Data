#creating list for table names at state level
codes = []
prefix = 'LASST01'
suffix = '0000000000003'
for number in range(57):
    if number <=9:
        codes.append(prefix[:6]+str(number)+suffix)
    if number >=10:
        codes.append(prefix[:5]+str(number)+suffix)
print(codes[1])

print(codes)