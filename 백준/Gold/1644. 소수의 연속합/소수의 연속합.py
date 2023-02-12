import math

maxrange = 4000000
bool_prime = [True] * (maxrange + 1)
for i in range(2,int(math.sqrt(maxrange)+1)):
    if bool_prime[i]:
        j=2
        while i*j<=maxrange:
            bool_prime[i*j]=False
            j+=1
prime_num_list = [i for i in range(2,maxrange+1) if bool_prime[i]]

n = int(input())
if n==1:
    print(0)
else:
    end,result = 0,0
    total = prime_num_list[0]
    for start in range(len(prime_num_list)):
        while end<len(prime_num_list) and total<n:
            end+=1
            if end!=len(prime_num_list):
                total += (prime_num_list[end])
        if end==len(prime_num_list):break
        if total==n:result +=1
        total -= prime_num_list[start]
    print(result)