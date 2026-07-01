class Twitter:

    def __init__(self):
        self.count=0
        self.follower=defaultdict(set)
        self.posts=defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        heap=[]
        self.follower[userId].add(userId)
        for f in self.follower[userId]:
            if f in self.posts:
                index=len(self.posts[f])-1
                count,tweetId=self.posts[f][index]
                heap.append([count,tweetId,f,index-1])
        heapq.heapify(heap)
        while heap and len(res)<10:
            count,tweetId,f,index=heapq.heappop(heap)
            res.append(tweetId)
            if index>=0:
                count,tweetId=self.posts[f][index]
                heapq.heappush(heap,[count,tweetId,f,index-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
        
