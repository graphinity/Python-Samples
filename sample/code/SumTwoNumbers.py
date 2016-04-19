'''
Created on Apr 18, 2016

@author: karya
'''
def sumProblemString(x, y):
    sum = x + y
    return 'The sum of {} and {} is {}.'.format(x, y, sum)

def main():
    
    print("This is my %d program in %s language..!!" % (1, 'Python'))
    
    # print(sumProblemString(2, 3))
    # print(sumProblemString(1234567890123, 535790269358))
    
    try:
      a = int(input("Enter an integer: "))
      b = int(input("Enter another integer: "))
    except ValueError:
       print("Error: Please enter only integer values.")
       main()
    else:
       print("Identified input values as valid integer values.. Result of their addition is:"+ sumProblemString(a, b))
    
    print("Program Completed Successfully, keep running for fun..")

main()