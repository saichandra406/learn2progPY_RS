def isEven(dividend):
    if dividend % 2 == 0: return 1
    else: return 0

def wrap_around(num):
    rem = num % 2147483648
    dividend = num // 2147483648
    if isEven(dividend):
        num = rem
    else:
        num = -(2147483648 - rem) 
    return num

def max(num1, num2):
    #python int type(object) has unlimited size
    #num1 and num2 are C int type = 32 bit
    #so need to find wrap around value after overflow if exists    
    num1 = wrap_around(num1)
    num2 = wrap_around(num2)
    
    #convert the value into hex string, needs num1 to be unsigned form
    #i.e if num1 = -1 then unsigned form is num1 = 255
    #   num1_hex = hex(num1)
    #convert hex value into byte string
    #   num1_bytes = bytes.fromhex(num1_hex)
    #convert the int values into 4 bytes Byte string
    #   num1_bytes = num1.to_bytes(4, 'big', signed=True)
    #convert the Byte values into int
    #   num1 = int.from_bytes(num1_bytes, 'big', signed=True)
    #all the above need num1 to wrap around the overflow
    
    #check if num1 is greater than num2
    if num1 > num2:
        #if so, your answer is num1
        return num1
    #otherwise, your answer is num2
    else:
        return num2


print("max(42, -69) is", max(42, -69))
print("max(33, 0) is", max(33, 0))
print("max(0x123456, 123456) is", max(0x123456, 123456))
#compute the max of 0x451215AF and 0x913591AF and print it out as a decimal number
print("max(0x451215AF, 0x913591AF) is", max(0x451215AF, 0x913591AF))
