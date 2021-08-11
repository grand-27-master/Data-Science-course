#The first line contains an integer,denoting the size of the array.
#The second line contains  space-separated integers representing the
#array's elements.
#constraints:
 #   0<n,ar[i]<=1000
#Print the sum of the array's elements as a single integer.


import os
import sys
def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
 
