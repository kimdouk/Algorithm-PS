def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
a = input()
b = input()
len_a,len_b = len(a),len(b)
result_a = ((len_a*len_b//gcd(len_a,len_b))//len_a)*a
result_b = ((len_a*len_b//gcd(len_a,len_b))//len_b)*b
print(1 if result_a==result_b else 0)