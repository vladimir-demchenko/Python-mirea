
def f21(a):
    if a[4] == 2002:
        if a[3] == 1998:
            if a[0] == 'nu':
                if a[1] == 'nim':
                    return 0
                elif a[1] == 'qmake':
                    return 1
            elif a[0] == 'lean':
                if a[2] == 'roff':
                    return 2
                elif a[2] == 'kicad':
                    return 3
        elif a[3] == 1978:
            return 4
    elif a[4] == 1965:
        return 5
    elif a[4] == 1992:
        if a[2] == 'roff':
            if a[0] == 'nu':
                if a[3] == 1998:
                    return 6
                elif a[3] == 1978:
                    return 7
            elif a[0] == 'lean':
                if a[3] == 1998:
                    return 8
                elif a[3] == 1978:
                    return 9
        elif a[2] == 'kicad':
            return 10

print(f21(['lean', 'qmake', 'roff', 1998, 2002]))
print(f21(['nu', 'qmake', 'roff', 1978, 1992]))


table = [['+7 592 584-14-11', '0.642;10/10/2002', 'tanudli75@gmail.com'], ['+7 131 152-88-35', '0.257;02/05/2000', 'igor_23@gmail.com'], ['+7 352 200-35-09', '0.088;03/11/2004', 'mutelanz51@rambler.ru'],['+7 592 584-14-11', '0.642;10/10/2002', 'tanudli75@gmail.com']]
import math
import datetime as DT

def f23(table):
  for i in range(0, len(table)):
    table[i][0]= table[i][0].replace(' ', '(', 1)
    table[i][0] = table[i][0].replace(' ', ')')
    table[i][1] = table[i][1].split(';')
    table[i][1][0] = str(math.ceil(float(table[i][1][0])*100))+'%'
    date = DT.datetime.strptime(table[i][1][1], '%d/%m/%Y').date()
    table[i][1][1] = date.strftime('%Y.%m.%d')
    table[i][2] = table[i][2].replace('@', '[at]')
    table[i].append(table[i][1][1])
    table[i][1] = table[i][1][0]
  print(*zip(*table))
    
f23(table)

"""
def f22(n):
  n = bin(n)[2:]
  #print(n)
  d = n[0]
  c = n[1:17]
  b = n[17:19]
  a = n[19:31]
  ans = d+a+b+c
  print(ans)
  print(d,c,b,a)
  return hex(int(ans,base=2))
#print(f22(0x3bbbbf70))
print(f22(0xc3e2238f))
"""