"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.


input: none
output: an array representing a shuffled deck


CAN NOT:
    iterate while iterating through the deck (more than O(N))
    sort the array (O (n log n))
    call any O(N) methods while we iterate

CAN:
    iterate 
    select index

UNCERTAIN:
    make sure each permutation is equally likely
        

i. generate the array
ii.  iterate through the array
    iii. swap the card at index i with the card at index random number
iv. return the array

"""

def shuffle_deck():
    
    deck = [
        "Ah", "Ad", "Ac", "As",
        "2h", "2d", "2c", "2s",
        "3h", "3d", "3c", "3s",
        "4h", "4d", "4c", "4s",
        "5h", "5d", "5c", "5s",
        "6h", "6d", "6c", "6s",
        "7h", "7d", "7c", "7s",
        "8h", "8d", "8c", "8s",
        "9h", "9d", "9c", "9s",
        "10h", "10d", "10c", "10s",
        "Jh", "Jd", "Jc", "Js",
        "Qh", "Qd", "Qc", "Qs",
        "Kh", "Kd", "Kc", "Ks"
    ]

    for i in range(len(deck)):
        random = perfectly_random_number(52) - 1
        deck[i], deck[random] = deck[random], deck[i]

    return deck
