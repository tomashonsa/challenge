volba=input("(ddb) dec do bin nebo (bdd) bin do dec")


if volba==("ddb"):
    b1=input("zadej 1 byte ip adresy")
    b2=input("zadej 2 byte ip adresy")
    b3=input("zadej 3 byte ip adresy")
    b4=input("zadej 4 byte ip adresy")
    b1 = int(b1)
    b2 = int(b2)
    b3 = int(b3)
    b4 = int(b4)
    print(bin(b1),".",bin(b2),".",bin(b3),".",bin(b4))
elif volba=="bdd":
    ip1=input("zadej binarni cislo")
    ip1=str(ip1)
    ip2=input("zadej binarni cislo")
    ip2=str(ip2)
    ip3=input("zadej binarni cislo")
    ip3=str(ip3)
    ip4=input("zadej binarni cislo")
    ip4=str(ip4)
    binary_num1 = ip1
    binary_num2 = ip2
    binary_num3 = ip3
    binary_num4 = ip4
    decimal_num1 = int(binary_num1, 2)
    decimal_num2 = int(binary_num2, 2)
    decimal_num3 = int(binary_num3, 2)
    decimal_num4 = int(binary_num4, 2)
    print(decimal_num1,".", decimal_num2,".", decimal_num3,".", decimal_num4)