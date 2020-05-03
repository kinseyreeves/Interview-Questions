"""
N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
"""
from typing import *

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions_ranked = sorted([[position[x],x] for x in range(0, len(position))])[::-1]

        print(positions_ranked)
        total = 0
        prev = 0

        while any(x[0] < target for x in positions_ranked):
            
            # we want to move from the first car backwards
            for i in range(len(positions_ranked)-1,-1,-1):
                
                idx = positions_ranked[i][1]
                #add the speed the position
                positions_ranked[i][0]+=speed[idx]
            
            #Don't let cars overtake
            for i in range(1,len(positions_ranked)):
                if(positions_ranked[i][0] > positions_ranked[i-1][0]):
                    positions_ranked[i-1][0] = positions_ranked[i][0]
            
            print(positions_ranked)
        
            #current cars at target 
            curr=len([x[0] for x in positions_ranked if x[0] >= target])
            print(curr)
            #If we got new cars at the target, a bunch has arrived, add to total
            if(curr > prev):
                total += 1
            
            prev = curr

        return total

a = Solution()

print(a.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))

