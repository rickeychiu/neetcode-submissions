import heapq

class Twitter:

    def __init__(self):

        self.feed = [] # store as [userID, tweetID]]
        self.following = {} # store as {userID : set(userID1, userID2)}

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.feed.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:

        if userId not in self.following: # initialize if you haven't followed anyone yet
            self.following[userId] = {userId}
        
        answer = []
        followingIds = []
        if userId in self.following:
            followingIds = self.following[userId]

        i = len(self.feed) - 1
        count = 0
        while count < 10 and i >= 0:
            if self.feed[i][0] in followingIds:
                answer.append(self.feed[i][1])
                count += 1
            i -= 1
        
        return answer


    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.following:
            self.following[followerId] = {followerId}
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:

       self.following[followerId].discard(followeeId)
        
