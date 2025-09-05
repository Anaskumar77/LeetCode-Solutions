
digits = [9,9,9]

def Solution(digits):
    if len(digits) == 0:
        return []
    number = int(''.join(str(nums) for nums in digits))
    number = number + 1
    digits = [int(d) for d in str(number)]
    return digits

Solution(digits)
    





            
            

            



        
    
   

    
