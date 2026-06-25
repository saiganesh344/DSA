from itertools import product

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        # Encode a column coloring to an integer
        def encode(column):
            res = 0
            for color in column:
                res = res * 3 + color
            return res

        # Decode integer back to column tuple (optional for debugging)
        def decode(code):
            column = []
            for _ in range(m):
                column.append(code % 3)
                code //= 3
            return tuple(reversed(column))

        # Step 1: Generate valid column colorings (no two adjacent same)
        def generate_valid_columns():
            valid = []
            for column in product([0, 1, 2], repeat=m):
                if all(column[i] != column[i+1] for i in range(m - 1)):
                    valid.append(encode(column))
            return valid

        # Step 2: Build compatibility between encoded columns
        def build_compatibility(valid_columns):
            compatible = {c: [] for c in valid_columns}
            for c1 in valid_columns:
                col1 = decode(c1)
                for c2 in valid_columns:
                    col2 = decode(c2)
                    if all(a != b for a, b in zip(col1, col2)):
                        compatible[c1].append(c2)
            return compatible

        # Step 3: DP with minimal space
        def count_ways(valid_columns, compatible):
            dp = {col: 1 for col in valid_columns}
            for _ in range(1, n):
                new_dp = {col: 0 for col in valid_columns}
                for col in valid_columns:
                    for prev_col in compatible[col]:
                        new_dp[col] = (new_dp[col] + dp[prev_col]) % MOD
                dp = new_dp
            return sum(dp.values()) % MOD

        valid_columns = generate_valid_columns()
        compatible = build_compatibility(valid_columns)
        return count_ways(valid_columns, compatible)