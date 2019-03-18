import pywt
print(dir(pywt.__file__))

x = [3, 7, 1, 1, -2, 5, 4, 6]
cA, cD = pywt.dwt(x, 'db2')
print(cA)
print(cD)
