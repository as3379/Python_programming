"""Find the largest sum of consecutive integers in an array
 - Kadane's Algorithm
"""


def maxSubArraySum(a,size):

    max_so_far = 0
    max_ending_here = 0
    start = 0
    end = 0


    for i in range(0,size):

        max_ending_here += a[i]

        if max_ending_here < 0:
            max_ending_here = 0
            start = i+1

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end = i



    print ("Maximum contiguous sum is %d"%(max_so_far))
    print ("Starting Index %d"%(start))
    print ("Ending Index %d"%(end))

# Driver program to test maxSubArraySum
a = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSubArraySum(a,len(a))
