from rich import print

with open("input.txt", "r") as f:
    input: str = f.read()
lines: list[str] = input.split("\n")
line_sep: list[list[str]] = [line.split("   ") for line in lines]
col_a: list[int] = [int(row[0].strip()) for row in line_sep]
col_a.sort()
col_b: list[int] = [int(row[1].strip()) for row in line_sep]
col_b.sort()
# Part ONE
result = sum(abs(a - b) for a, b in zip(col_a, col_b))
print(result)
# Part TWO

unique_key: set[int] = set(col_a)
total: int = sum(col_b.count(key)*key for key in unique_key)

print(f'Result for part two {total}')
