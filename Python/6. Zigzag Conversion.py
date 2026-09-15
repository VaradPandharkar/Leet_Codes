class Solution:

    def convert(self, s, numRows):
        if numRows == 1:
            return s

        row = 0
        i = 0
        direction = True  # True means top to down

        zigzag = [""] * numRows

        while True:

            if direction:
                # Move from top to bottom
                while i < len(s) and row < numRows:
                    zigzag[row] += s[i]
                    row += 1
                    i += 1

                row = numRows - 2

            else:
                # Move from bottom to top
                while row >= 0 and i < len(s):
                    zigzag[row] += s[i]
                    row -= 1
                    i += 1

                row = 1

            if i >= len(s):
                break

            direction = not direction

        return "".join(zigzag)