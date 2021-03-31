#!/usr/bin/python3
"""
0-prime_game.py
Module that defines the winner of the prime game between 2 players
"""


def isPrime(n):
    """
    Function that determines if an integer is prime

    Args:
        n (int): Integer
    """
    if n <= 1:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True


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
    p1, p2 = 0, 0
    for i in range(x):
        for j in range(len(nums)):
            if isPrime(nums[j]):
                temp = nums[j]
                nums.pop(j)
                for k in nums:
                    if k % temp == 0:
                        nums.remove(k)
                if i % 2 == 0:
                    p1 += 1
                else:
                    p2 += 1
                break
            if j + 1 == len(nums) and p1 == 0 and p2 == 0:
                return None
    if p1 == p2:
        return None
    if p1 > p2:
        return "Maria"
    return "Ben"
