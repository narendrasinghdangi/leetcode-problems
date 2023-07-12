class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def dfs(cookies, index,children):
            nonlocal ans
            if index == len(cookies):
                unfairness = max(children)
                ans = min(ans, unfairness)
                return
            for i in range(len(children)):
                children[i] += cookies[index]
                dfs(cookies, index+1, children)
                children[i] -= cookies[index]
                if children[i] == 0: break

        ans = float('inf')
        children = [0]*k
        dfs(cookies, 0, children)
        return ans