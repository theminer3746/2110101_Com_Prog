s1 = input().strip()
s2 = input().strip()

ps1 = s1.replace(' ', '').lower()
ps2 = s2.replace(' ', '').lower()

if sorted(ps1) == sorted(ps2):
    print(s1)
else:
    print(s1, s2)
