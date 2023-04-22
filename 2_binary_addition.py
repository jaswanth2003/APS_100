#Given two binary strings a and b, return their sum as a binary string.
# Input: a = "11", b = "1"
# Output: "100"


# The bin() function is a built-in Python function that converts an integer to a binary string.
# The binary string starts with the prefix 0b, which indicates that the string represents a binary number.
#Time Complexity-o(n+m) and space complexity -o(n)
# using bitwise operator
def bit_add(a,b):
    i_a=int(a,2)
    i_b=int(b,2)
    i_sum=i_a+i_b
    return bin(i_sum)[2:]


#Time Complexity-O(n)
#Space Complexity-O(n)
def bin_add(a,b):
    a,b=a[::-1],b[::-1]
    res=""
    carry=0
    for i in range(max(len(a),len(b))):
        t_a=int(a[i]) if i < len(a) else 0
        t_b=int(b[i]) if i < len(b) else 0
        total=t_a+t_b+carry
        char=str(total%2)
        res=char+res
        carry=total//2
    if carry:
        res="1"+res
    return res
print(bin_add("11","1"))
#100
print(bit_add("11","1"))
#100

