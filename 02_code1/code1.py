def wrap_around(num):
    '''
    In C, signed integers use two's complement, meaning the most significant bit (MSB) determines if the number is negative.
    i.e MSB = 0, num is +ve; MSB = 1, num is -ve
    When an integer surpasses its maximum value, it flips to the minimum value and continues from there
    (or wrap around to negative)
    e.g: for int8_t, num = 127, num + 1 gives -128 while unsigned form is num = 128
    e.g. for int8_t, num = -1 = 0xFF, then unsigned or raw byte = 255 or x0FF
    If num // 2 ^ {size of int type in bits} >=2 overflow occured & bytes after MSB are ignored.
    It looks as if num was reset.
    e.g. for int8_t, num = 0xFF, MSB = 1. 0XFF + 0x01 = 0x100, overflow occured, bytes after MSB ignored. Hence num = 0x00
    
    Method 1(used here):
    Extract 31 bits from LSB by remainder = num % 2^32
    Take quotient = num // 2^32 
    If quotient is odd, the 32nd bit is 1(which is MSB for C int type) & extracted 31 bits is negative.
    If quotient is even, extracted 31 bits is positive.
    When its negative, to get its absolute value, subtract remainder from 2^32.
    
    Method 2:
    1.convert the value into hex string,
    2.convert hex value into byte string,
    3.convert the 4 bytes Byte string into int value.
    4.convert the Byte values into int

    (a) Step 1 & 2 combined, when num is in C int range (-2_147_473_648 to +2_147_483_647)
    num_bytes = num.to_bytes(4, 'big', signed=True)

    (b) when num is out of C int range
    python_num_hex = hex(num)
    num_bytes = bytes.fromhex(python_num_hex[len(python_num_hex) - 4 :])

    num = int.from_bytes(num_bytes, 'big', signed=True)
    '''
    rem = num % 2147483648
    quotient = num // 2147483648
    if (quotient % 2 == 0):
        num = rem
    else:
        num = -(2147483648 - rem) 
    return num

def max(num1, num2):
    #python int type(object) has theoretically unlimited size
    #num1 and num2 are C int type (implicitly signed), size = 32 bit (32/64 bit systems)
    #so need to find wrap around value if 32th bit is 1.    
    num1 = wrap_around(num1)
    num2 = wrap_around(num2)
    
    #check if num1 is greater than num2
    if num1 > num2:
        #if so, your answer is num1
        return num1
    #otherwise, your answer is num2
    else:
        return num2

if __name__ == "__main__":
    #In C, integer literlas are implicitly int type (implicitly signed), size = 32 bit (32/64 bit systems)
    #So need to specify u for unsigned int or llu for 8 Byte unsigned. e.g 0xFFFFFFFFllu
    print("max(42, -69) is", max(42, -69))
    print("max(33, 0) is", max(33, 0))
    print("max(0x123456, 123456) is", max(0x123456, 123456))
    #compute the max of 0x451215AF and 0x913591AF and print it out as a decimal number
    #decimal number is %d, unsigned decimal number is %u
    print("max(0x451215AF, 0x913591AF) is", max(0x451215AF, 0x913591AF))
