fajlnev = input("Add meg a fajl nevet: ") 

try:
    f=open(fajlnev, 'r')
    f2=open((fajlnev + "-kimenet"), 'wt')
except:
    print("valami nemjo")
    exit()

sor = f.readline()
i = 0
print("")
while sor:
    if(i % 2 ==0):
    	line = sor.upper()
    else:
        line = sor.lower()
    i += 1
    print(line, end="")
    f2.write(line)
    sor = f.readline()
print("")
f.close()
f2.close()
