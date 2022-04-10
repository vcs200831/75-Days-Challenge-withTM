class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(A,B):
            return (A[0]-B[0])**2  + (A[1]-B[1])**2
        
        distances = [distance(p1, p2), distance(p1, p3), distance(p1, p4), distance(p2, p3), distance(p2, p4), distance(p3, p4)]
        
        distances.sort()
        
        return 0 < distances[0] == distances[1] == distances[2] == distances[3] and                           2*distances[1] == distances[-1] == distances[-2]
    
    
            