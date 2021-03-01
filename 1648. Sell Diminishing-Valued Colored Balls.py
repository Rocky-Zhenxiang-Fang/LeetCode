from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        """
        Idea:
            We want to sell the most valuable balls (most freq balls) first. Thus first sort it.
            To fast forward the process, we first ask if we can sell it a pile, if cannot, sell a row, if not, sell it
            one by one
        """
        res = 0
        inventory.sort(reverse=True)
        inventory.append(0)  # in case of out of bound
        k = 1
        for i in range(len(inventory)-1):
            if inventory[i] > inventory[i+1]:
                if k*(inventory[i] - inventory[i+1]) < orders:
                    res += k*(inventory[i] + inventory[i+1] + 1)*(inventory[i] - inventory[i+1])//2 # arithmic sum
                    orders -= k*(inventory[i] - inventory[i+1])
                else:
                    q, r = divmod(orders, k)
                    res += k*(2*inventory[i] - q + 1) * q//2 + r*(inventory[i] - q)
                    return res % 1_000_000_007
            k += 1


if __name__ == '__main__':
    inventory = [2, 5]
    orders = 4
    sol = Solution()
    print(sol.maxProfit(inventory, orders))
