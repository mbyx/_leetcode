input: str = "4\n01\n01\n10\n10"
input: list[int] = input.strip().split('\n')

last_magnet: str = ''
groups: int = 0
for magnet in input[1:]:
    if last_magnet != magnet:
        groups += 1
    last_magnet = magnet

print(groups)
