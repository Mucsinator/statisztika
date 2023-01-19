# a<=b<=c
# a2 + b2 =c2 -> derékszögű háromszög
# a2+b2 > c2 -> Hegyesszögű
# a2 +b2 < v2 -> tompaszögű

a = float(input("Kérem az a-t:"))
b = float(input("Kérem a b-t:"))
c = float(input("Kérem a c-t:"))

if a**2 + b**2 > c**2:
    print("Hegyesszögű háromszög")
elif a**2 + b**2 == c**2:
    print("Derékszögű háromszög")
else:
    print("Tompaszögű háromszög")
