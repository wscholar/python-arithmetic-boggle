import argparse

# A function that takes as input, a target integer and a sequence of integers (space delimited list)
# returns true if the target integer can be obtained by placing
# addition or subtraction operations in the list. Otherwise, returns false.
#
# For example:
#
# f(5, [5, 2]) = false. There's no way to add or subtract 5 and 2 to get 5.
# f(13, [3, 9, 3, 2]) = true. 3 + 9 + 3 - 2 = 13.

def arithmetic_boggle(magic_number, numbers):
    return recursivecheck(magic_number, numbers, 0, 0)

def recursivecheck(magic_number, numbers, index,total):
    #check to see if we are at the last number
    if index == len(numbers):
        #if we have the last number, does the total match the magic number
        if magic_number == total:
            return True
        else:
            return False
    else:
        #add current number and check again recursvely
        curr = total + numbers[index]
        if(recursivecheck(magic_number, numbers, index + 1, curr)):
            return True
        # subtract current number and check again recursvely
        curr = total - numbers[index]
        if(recursivecheck(magic_number, numbers, index + 1, curr)):
            return True
        #no match to magic number
        return False


ap = argparse.ArgumentParser()
ap.add_argument("-m", "--magic_number", required=True, type=int, help="Magic Number to match")
ap.add_argument("-n", "--numbers", metavar='N', type=int, nargs='+',required=True, help="List of numbers to use")
args = ap.parse_args()

numbers = args.numbers
magic_number = args.magic_number
print (arithmetic_boggle(magic_number,numbers))
