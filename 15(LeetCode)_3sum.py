class Solution(object):
     def threeSum(self, nums):
        y = []
        nums.sort()
        for i in range(len(nums)-1):
            p = i+1
            q = len(nums)-1
            while(p<q):
                if(nums[i]+nums[p]+nums[q]==0):
                    triplet = [nums[i],nums[p],nums[q]]
                    if triplet not in y:
                        y.append(triplet)
                    p += 1
                    q-= 1
                elif(nums[i]+nums[p]+nums[q]<0):
                    p+=1
                else:
                    q-=1
        return y

if __name__ == "__main__" :
    nums = [-1,0,1,2,-1,-4]
    obj = Solution()
    print(obj.threeSum(nums))