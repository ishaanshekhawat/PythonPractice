# https://datalemur.com/questions/python-video-ads-insertion

def can_insert_ads(feed_items, n):
    if feed_items[0] == 0:
        n-=1
    
    for i in range(0, len(feed_items) - 1):
        if feed_items[i] == 0:
            if feed_items[i+1] == 0:
                n-=1

    if feed_items[-1] == 0:
        n-=1

    if n <= 0:
        return True
    return False
