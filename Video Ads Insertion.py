# You're on Meta (Facebook's) Newsfeed Ads Team, working on an experiment to increase the number of video ads served 
# up in a person's newsfeed.

# The newsfeed ranking team gives you a list of feed_items which denotes what type of content their algo is 
# planning to serve a user.

# 0 denotes a normal post
# 1 denotes a video
# 2 denotes a non-video ad
# You want to insert n more video ads; however, you can't place a video ad next to an existing video otherwise 
# users will be annoyed about Meta's newsfeed being too video-heavy. Similarly, you can't place a video ad next
#  to a non-video ad, because you don't want to overwhelm the user with consecutive ads.

# Is it possible to insert n more video ads into the feed based on feed_items?

# Example 1:
# Input: feed_items = [1, 2, 0, 0, 0], n = 3
# Output: True
# Explanation:
# The first video ad can be inserted between the third and the fourth elements.
# The second video ad can be inserted between the fourth and the fifth elements.
# The third video ad can be inserted at the end.
# Thus, we can insert 3 out of 3 video ads, so we return True.

# Example 2:
# Input: feed_items = [1, 0, 2, 0, 1, 1, 0], n = 2
# Output: False
# Explanation:
# The only place where we can place a video ad is at the end of feed_items, so we can't insert all 2 video ads 
# as requested, hence we return False.


def can_insert_ads(feed_items, n):
    # Count of how many video ads we can insert
    ct = 0
    
    # Iterate through the feed to find consecutive normal posts (0, 0)
    # Each such pair gives one possible insertion spot between them.
    for i in range(len(feed_items) - 1):
        # If two adjacent items are both normal posts, 
        # we can insert a video ad between them.
        if feed_items[i] == 0 and feed_items[i + 1] == 0:
            ct += 1
    
    # If the first item is a normal post (0),
    # we can also consider placing a video ad before it (at the start of the feed).
    if feed_items[0] == 0:
        ct += 1
    
    # If the last item is a normal post (0),
    # we can consider placing a video ad after it (at the end of the feed).
    if feed_items[-1] == 0:
        ct += 1
    
    # If the number of possible placements is at least `n`,
    # then it's possible to insert all the requested video ads.
    if ct >= n:
        return True
    
    # Otherwise, not enough valid slots are available.
    return False
    
    
