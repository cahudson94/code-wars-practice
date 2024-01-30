"""
In computing, there are two primary byte order formats: big-endian and little-endian. Big-endian is used primarily for networking (e.g., IP addresses are transmitted in big-endian) whereas little-endian is used mainly by computers with microprocessors.

Here is an example (using 32-bit integers in hex format):

Little-Endian: 00 6D F4 C9 = 7,206,089

Big-Endian: C9 F4 6D 00 = 3,388,239,104

Your job is to write a function that switches the byte order of a given integer. The function should take an integer n for the first argument, and the bit-size of the integer for the second argument. The bit size must be a power of 2 greater than or equal to 8. Your function should return a None value if the integer is negative, if the specified bit size is not a power of 2 that is 8 or larger, or if the integer is larger than the specified bit size can handle. In this kata, assume that all integers are unsigned (non-negative) and that all input arguments are integers (no floats, strings, None/nil values, etc.). Remember that you will need to account for padding of null (00) bytes.

Hint: bitwise operators are very helpful! :)

optimized:
def switch_endian(n, bits):
    out = 0
    while bits > 7:
        bits -= 8
        out <<= 8
        out  |= n & 255
        n   >>= 8
    return None if n or bits else out
"""

def switch_endian(n, bits):
    if n < 0 or bits % 2 or bits < 8:
        return None
    x = 2
    while x < bits:
        x *= 2
    if x != bits:
        return None
    as_hex = "0" + hex(n)[2:] if len(hex(n)) % 2 else hex(n)[2:]
    as_hex = [as_hex[i] + as_hex[i + 1] for i in range(0, len(as_hex), 2)][::-1]
    as_hex.extend(["00" for _ in range(bits // 8 - len(as_hex))])
    if len(as_hex) != bits // 8:
        return None
    return int(''.join(as_hex), 16)
