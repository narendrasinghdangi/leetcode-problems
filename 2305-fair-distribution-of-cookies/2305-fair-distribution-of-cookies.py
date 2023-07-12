class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        mini=float("inf")
        ch=[0]*k
        def dfs(i,ch):
            nonlocal mini
            if i==len(cookies):
                mini=min(mini,max(ch))
                return
            for idx in range(len(ch)):
                if ch[idx]+cookies[i]>=mini:
                    continue
                ch[idx]+=cookies[i]
                dfs(i+1, ch)
                ch[idx]-=cookies[i]
                
        dfs(0,ch)
        return mini