ATT, COMP, YDS, TD, INT = map(int, input().split())
rating = (((COMP / ATT - 0.3) * 5 + (YDS/ATT - 3) * 0.25 + (TD/ATT) * 20 + 2.375 - (INT/ATT*25))/6)*100
print(rating)
