# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts) + 1)]
        rank = [0] * (len(accounts) + 1)

        def find(account_index):
            if parent[account_index] != account_index:
                parent[account_index] = find(parent[account_index])
            return parent[account_index]

        def union(index1, index2):
            root1 = find(index1)
            root2 = find(index2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        email_to_account = {}
        for account_index, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    union(account_index, email_to_account[email])
                else:
                    email_to_account[email] = account_index

        merged_emails = defaultdict(list)
        for email, account_index in email_to_account.items():
            root_account = find(account_index)
            merged_emails[root_account].append(email)

        result = []
        for account_index, emails in merged_emails.items():
            name = accounts[account_index][0]
            result.append([name] + sorted(emails))
        return result
