sample_strings = ['abc', 'xyz', 'aba', '1221']
count = 0
for s in sample_strings:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print(f"Expected Result : {count}")
