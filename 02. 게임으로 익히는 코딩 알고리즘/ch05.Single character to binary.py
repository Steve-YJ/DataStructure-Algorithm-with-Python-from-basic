# from Chuck Noris

while decimal // 2 > 0:
    print('start decimal: ', decimal)
    remain = str(decimal % 2)
    print('remain:', remain)
    binary = remain + binary
    print('binary:', binary)
    decimal //= 2
    print('decimal: ', decimal)
    print('='*20)

    if decimal == 2:
        print('decimal==2?:', decimal)
        # binary = "10"+binary
        fin = str(decimal // 2)
        remain = str(decimal % 2)
        binary = fin + remain + binary
        print('final_binary: ', binary)
        decimal = 2//2
    
print(binary)

