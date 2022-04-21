import hashlib, bcrypt

jelszo = input("Adj meg egy jelszot: ")
sha = hashlib.sha512(jelszo.encode("utf8")).hexdigest()
#print(sha)
so = bcrypt.gensalt()
bcr = bcrypt.hashpw(jelszo.encode("utf8"),so)
jelszo2 = input("Add meg megegyszer a jelszot: ")
valasz=bcrypt.checkpw(jelszo2.encode("utf8"),bcr)
print(valasz)
