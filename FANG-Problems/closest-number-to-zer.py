

class ClosesetNumberToZero:


    def solution(self,arr):

        # arr=[-2,-3,2,3,4,-1,1]

        closest_number = arr[0] #c_n=-2

        for num in arr:#num=1

            if abs(num) < abs(closest_number):#1<1

                closest_number = num #c_n=-1

        if closest_number<0 and abs(closest_number) in arr:#-1<0 and 1 in arr

            return abs(closest_number)
        else:
            return closest_number
             
    
clst_instance=ClosesetNumberToZero()

print(clst_instance.solution([-2,-3,2,3,4,-1,1]))

