#!/usr/bin/python3
"""
0-prime_game.py
Module that defines the winner of the prime game between 2 players
"""


def isWinner(x, nums):
    """
    Function that determines the winner of the game

    Args:
        x (int): Number of rounds
        nums (list): List of integers

    Notes:
        If the winner cannot be determined, return None
        Otherwise, return the name of the player that won the most rounds
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    prime = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not prime[i]:
            continue
        for j in range(i*i, n + 1, i):
            prime[j] = False

    prime[0] = prime[1] = False
    c = 0
    for i in range(len(prime)):
        if prime[i]:
            c += 1
        prime[i] = c

    player1 = 0
    for n in nums:
        player1 += prime[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
