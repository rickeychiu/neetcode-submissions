class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
  
        posSpeedArr = []
        for i in range(len(position)):
            posSpeedArr.append( (position[i], speed[i]) )
        posSpeedArr.sort(reverse=True)
        # sorting it by position, using a tuple (position, speed) in reverse 
        #

        times = []
        for i in range(len(posSpeedArr)):
            # time to reach target = (target - position) / speed
            times.append( (target - posSpeedArr[i][0]) / posSpeedArr[i][1] )

        stack = []
        for time in times:
            # if time > top of stack time, 
            if len(stack) < 1 or time > stack[-1]:
                stack.append(time)
            # it will form a fleet if car ahead's time >= time behind it
        return len(stack)