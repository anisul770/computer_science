roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = input('Type Roman numbers: ').strip().upper()
total = 0
i = 0
while i < len(s):
    if i < len(s)-1:
        if roman[s[i]] >= roman[s[i+1]]:
            total = total + roman[s[i]]
        elif roman[s[i]] < roman[s[i+1]]:
            total = total + (roman[s[i+1]]-roman[s[i]])
            i = i+1
    elif s[i] == s[i-1] or roman[s[i]] < roman[s[i-1]]:
        total = total + roman[s[i]]
    i = i + 1
print(total)
