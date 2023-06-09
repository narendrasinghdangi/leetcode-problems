class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        f=ord(letters[0])
        t=ord(target)
        for i in letters:
            i=ord(i)
            if i>t:
                f=i
                break
        return chr(f)
                