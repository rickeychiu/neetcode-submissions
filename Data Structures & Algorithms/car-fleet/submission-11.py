class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
  
        # pair each car's position and speed
        posSpeedArr = []
        for i in range(len(position)):
            posSpeedArr.append( (position[i], speed[i]) )
        # sort it from closest to furthest from target, 
        # since you want to examine car in front first, 
        # cars behind it my catch up to it but never pass it
        posSpeedArr.sort(reverse=True)
        

        times = []
        for i in range(len(posSpeedArr)):
            # time to reach target = (target - position) / speed
            times.append( (target - posSpeedArr[i][0]) / posSpeedArr[i][1] )

        fleetTime = -1 # keep track of the arrival time of most recent fleet ahead 
        fleets = 0
     
        for time in times:
            # if time takes longer than the fleet ahead, becomes a new fleet
            if time > fleetTime:
                fleets += 1
                fleetTime = time

        return fleets