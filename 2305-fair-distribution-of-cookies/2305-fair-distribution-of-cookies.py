class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def dfs(index,children):
            nonlocal ans
            if index == len(cookies):
                unfairness = max(children)
                ans = min(ans, unfairness)
                return
            for i in range(len(children)):
                children[i] += cookies[index]
                dfs(index+1, children)
                children[i] -= cookies[index]
                if children[i] == 0: break

        ans = float('inf')
        children = [0]*k
        dfs(0, children)
        return ans