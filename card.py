class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

#def __repr__(self): make program translate it into readable that human can understand.
# if not using def __repr__(self):  it will print likethis
# <__main__.Card object at 0x7f9c2e3d1c40> tells where this card object being store.
    def __repr__(self):
        return f"Card(ra0nk={self.rank}, suit={self.suit})"
    
    def __lt__(self, other):
        rank_order  = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
        suit_order = ['clubs', 'diamonds', 'hearts', 'spades']

        return rank_order.index(self.rank) < rank_order.index(other.rank)
       # if suit_order.index(self.suit) != suit_order.index(other.suit):
        #    return suit_order.index(self.suit)< suit_order.index(other.suit)
        #else:
         #   return rank_order.index(self.rank)< rank_order.index(other.rank)
        


'''Returning True tells Python “self comes before other” in the ordering.

Returning False tells Python “self does not come before other” (i.e. it comes after, or they’re equal for this check).

In a class’s __lt__ (less‑than) method, 
Python uses that Boolean result to sort or compare objects. There’s no printing or side‑effect—
just a yes/no answer about which object is “smaller.”
'''
cs = input("enter card:" ).split()
cs.sort()
print([c.rank for c in cs]) 
        

                       
    

