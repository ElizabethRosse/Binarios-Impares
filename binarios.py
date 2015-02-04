r=1
n = int(raw_input("Dame el numero: "))
conjunto= set()
while(len(conjunto) < n ):
    f = bin(r)
    unos = str(f).count("1")
    if(unos%2!=0):
        conjunto.add(r)
    r = r+1

print r-1
