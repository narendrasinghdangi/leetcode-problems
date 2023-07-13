class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        exdif = 0
        for i in range(len(energy)):

            if initialExperience <= experience[i]:
                exdif = max(1,exdif,experience[i]+1-initialExperience)

            initialExperience += experience[i]


        return max(sum(energy)-initialEnergy+1,0) + exdif