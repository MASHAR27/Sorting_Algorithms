def bubble_sort(nums):
    """Implements bubble sort """
    lenght = len(nums)
    for i in range(lenght-1):
        switched = False # to bring the loop to an early end once the list has been sorted
        for j in range(lenght-1):
            if nums[j] > nums[j+1]:
                larger,smaller = nums[j],nums[j+1]
                nums[j] = smaller
                nums[j+1] = larger
                switched = True
        if not switched:
            print("Your array has been sorted!")
            return nums
    return nums






      
                

                
                



            
        
    

