class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # time = (target - position) / speed
        # use stack 

        # positions = [_, _, _, _, _, _]
        # speeds =    [_, _, _, _, _, _]

        # sorting it by position, using a tuple (position, speed) in reverse 

        # it will form a fleet if car ahead's time >= time behind it

        posSpeedArr = []
        for i in range(len(position)):
            posSpeedArr.append( (position[i], speed[i]) )
        posSpeedArr.sort(reverse=True)

        times = []
        for i in range(len(posSpeedArr)):
            times.append( (target - posSpeedArr[i][0]) / posSpeedArr[i][1] )
            #print(times[i])

        stack = []
        for time in times:
            if len(stack) < 1 or time > stack[-1]:
                stack.append(time)
        
        return len(stack)