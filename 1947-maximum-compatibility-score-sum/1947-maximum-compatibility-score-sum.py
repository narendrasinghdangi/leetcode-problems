class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        def get_score(m, s):
            c = 0
            for i in range(len(m)):
                if m[i] == s[i]:
                    c += 1
            return c
        
        @cache
        def dp(curr_index_student, tuple_ment):
            if curr_index_student == n:
                return 0
            list_ment = list(tuple_ment)
            m = -inf
            for mentor_index in range(n):
                if list_ment[mentor_index-1] == True:
                    continue
                list_ment[mentor_index-1] = True
                score = get_score(mentors[mentor_index], students[curr_index_student])
                m = max(m, score + dp(curr_index_student+1, tuple(list_ment)))
                list_ment[mentor_index-1] = False
            
            return m
        return dp(0, tuple([False] * n))