# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict = defaultdict(int)
        for comb_domains in cpdomains:
            count, domain = comb_domains.split()
            count = int(count)
            fragments =  domain.split(".")

            for i in range(len(fragments)):
                dict[".".join(fragments[i:])] += count
        
        return [f"{count} {domain}" for domain, count in dict.items()]