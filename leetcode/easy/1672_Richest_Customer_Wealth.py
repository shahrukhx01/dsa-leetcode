class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        net_wealth = []
        for custom_wealth in accounts:
            net_wealth.append(sum(custom_wealth))

        return max(net_wealth)
