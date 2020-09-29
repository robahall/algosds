def maxProfit(prices):
    return calculated(prices, 0)

def calculated(prices, s):
    """
    Max profit recursively
    :param prices: (arr)
    :param s: (int) index
    """
    if s >= len(prices):
        return 0
    current_max = 0
    for b_idx in range(s, len(prices)):
        max_profit = 0
        for s_idx in range(b_idx+1, len(prices)):
            if prices[b_idx] < prices[s_idx]:
                max_profit = max(max_profit, calculated(prices, s_idx+1) + prices[s_idx] - prices[b_idx])
        current_max = max(current_max, max_profit)
    return current_max

def maxProfitPV(prices):
    """
    Max Profit using Peak and Valley Algorithm
    :param prices: (arr)
    """
    idx = 0
    valley = prices[0]
    peak = prices[0]
    max_profit = 0
    arr_size = len(prices) - 1
    while idx < arr_size:
        while idx < arr_size and prices[idx] >= prices[idx+1]:
            idx += 1
        valley = prices[idx]
        while idx < arr_size and prices[idx] <= prices[idx+1]:
            idx += 1
        peak = prices[idx]
        max_profit += peak - valley
    return max_profit

def maxProfitOP(prices):
    """
    Max Profit using one pass algorithm
    :param prices: (arr)
    """
    max_profit = 0
    for idx in range(1, len(prices)):
        if prices[idx] > prices[idx - 1]:
            max_profit += prices[idx] - prices[idx - 1]
    return max_profit



if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
    print(maxProfitPV(prices))
    print(maxProfitOP(prices))
    prices2 = [1, 2, 3, 4, 5]
    print(maxProfit(prices2))
    print(maxProfitPV(prices2))
    print(maxProfitOP(prices2))