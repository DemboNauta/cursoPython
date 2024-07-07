v = "otro texto"
n = 10
c = "Un texto '{texto}' y un número '{numero}'".format(texto=v, numero=n)

print("{:^30}".format("palabra"))

for x in range(8):
    print("{:.{prec}}".format("palabra", prec=x))


print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

print("{:.2f}".format(3.1415926))


print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))