class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        onenum , i = 1,0
        
        while onenum:
            if i<len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] +=1
                    onenum = 0
            else:
                digits.append(1)
                onenum = 0
            i+=1
        return digits[::-1]
                
                
                    
        
        