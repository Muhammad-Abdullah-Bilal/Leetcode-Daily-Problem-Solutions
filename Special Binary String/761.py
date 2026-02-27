class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        specials = []
        balance = 0
        start = 0

        for i, ch in enumerate(s):
            balance += 1 if ch == '1' else -1
            if balance == 0:
                # Process inner part recursively
                inner = self.makeLargestSpecial(s[start + 1:i])
                specials.append("1" + inner + "0")
                start = i + 1

        # Sort in descending lexicographical order
        specials.sort(reverse=True)
        return "".join(specials)