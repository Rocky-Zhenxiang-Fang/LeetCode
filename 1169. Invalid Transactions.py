from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        {name},{time},{amount},{city}
        Idea: for each transactions, first see if the amount is bigger then 1000,
            then see if their is a transaction that have the same name, in different city and with in 60 minutes
            finally, store the [name: transactions] in to a dictionary
        """
        res = []
        name_transaction = {}
        invalid_transactions = [False for _ in range(len(transactions))]
        for i in range(len(transactions)):
            t = transactions[i]
            separate = t.split(",")
            if int(separate[2]) > 1000:
                invalid_transactions[i] = True
            if separate[0] in name_transaction:
                for other in name_transaction[separate[0]]:
                    if other[3] != separate[3] and abs(int(other[1]) - int(separate[1])) <= 60:
                        invalid_transactions[int(other[-1])] = True
                        invalid_transactions[i] = True
            separate.append(str(i))
            name_transaction[separate[0]] = name_transaction.get(separate[0], []) + [separate]
        for j in range(len(transactions)):
            if invalid_transactions[j]:
                res.append(transactions[j])
        return res


if __name__ == '__main__':
    sol = Solution()
    transactions = ["bob,627,1973,amsterdam","alex,387,885,bangkok","alex,355,1029,barcelona","alex,587,402,bangkok","chalicefy,973,830,barcelona","alex,932,86,bangkok","bob,188,989,amsterdam"]
    print(sol.invalidTransactions(transactions))

