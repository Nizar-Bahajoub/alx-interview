#!/usr/bin/python3
"""
Main Function
"""

def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet total."""
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make a total of 0

    # Iterate through each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still 'inf', it means we cannot form the total with the given coins
    return dp[total] if dp[total] != float('inf') else -1

