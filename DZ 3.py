n = int(input("Введите число: "))
n1 = int("%s" % n)
n2 = int("%s%s" % (n, n))
n3 = int('%s%s%s' % (n, n, n))
n4 = n1+n2+n3
print(f'{n1}+{n2}+{n3}={n4}')