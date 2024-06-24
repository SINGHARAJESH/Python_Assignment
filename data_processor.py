
def Average(lst): 
    return sum(lst) / len(lst) 

def Sorting(lst):
    return sorted(lst)

def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
    

