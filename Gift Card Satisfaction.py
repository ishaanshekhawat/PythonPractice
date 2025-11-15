# Imagine you're a VP at FAANG, and you want to reward your team with gifts at the end of the year during Christmas time. 
# You check in with stingy HR, and the best they could do is scrounge up a limited set of gift cards 
# – each with different values and to various stores.

# Each teammate has different expectations for their end-of-year gift – your Director expects a $1000+ gift card 
# for something luxurious, while the new grad on your team would be thrilled with something as simple as a $10 gift card 
# to Starbucks.

# You can only give each person at most one gift card, and if a gift card doesn’t meet someone’s minimum expectation, 
# it’s better not to give them one at all, as we definitely don't want to disappoint.

# Find a way to satisfy as many teammates as possible by assigning each one a gift card that meets or exceeds their 
# expectation.

# Return the maximum number of teammates you can make satisfy.

# Example #1
# Input:
# Expectations = [5, 20, 1000], Cards = [10, 15, 100]
# Output: 2
# Explanation:
# The team member expecting $5 can be satisfied with the $10 gift card.
# The team member expecting $20 is satisfied with the $100 card.
# Unfortunately, your Director, expecting a $1000 gift card, will have to wait – 
# nothing in stock would satisfy their high standards!

# Example #2
# Input:
# Expectations = [10, 30, 100, 200], Cards = [5, 2, 5, 3, 9]
# Output: 0
# Explanation:
# None of the available gift cards can satisfy any expectations, as even the lowest is $10, 
# while the highest card is just $9. Looks like everyone will be going home empty-handed!

def max_satisfaction(expectations, cards):
    # Sort both expectations and cards in ascending order
    expectations.sort()
    cards.sort()
    
    # Initialize an empty dictionary to store matched pairs
    dict1 = {}
    
    # Iterate through the expectations, matching each with the smallest card that is >= expectation
    for i in range(min(len(expectations), len(cards))):
        # If the current card can satisfy the expectation, store it in the dictionary
        if expectations[i] <= cards[i]:
            dict1[expectations[i]] = cards[i]
        else:
            # If the current card cannot satisfy the expectation, find the next card that can
            for j in range(i + 1, len(cards)):
                if expectations[i] <= cards[j]:
                    dict1[expectations[i]] = cards[j]
                    break  # Break once a valid card is found for the current expectation
    
    # Return the number of matched pairs (i.e., the length of the dictionary)
    return len(dict1)
