class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        print(mat)
        c = -len(mat[0])+1
        r = len(mat)
        lol = [[0]*len(mat[0]) for i in range(r)]
        print(lol)

        for k in range(c, r):
            li = []
            for i in range(len(mat)):
                for j in range((len(mat[0])-1), -1, -1):
                    if i-j == k:
                        li.append(mat[i][j])
            li.sort()
            l = 0
            print(li)
            for i in range(len(mat)):
                for j in range((len(mat[0])-1), -1, -1):
                    if i-j == k:
                        lol[i][j] = li[l]
                        l += 1
            print(lol)


s = Solution()
s.diagonalSort([[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [
               75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]])
