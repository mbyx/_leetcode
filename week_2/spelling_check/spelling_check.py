import collections

first: str = 'abdrakadabra'
second: str = 'abrakadabra'

diff = collections.Counter(first) - collections.Counter(second)
print(diff)
if len(diff.items()) != 1:
    print(0)
else:
    letter, _ = next(iter(diff.items()))
    indices = [i + 1 for i, c in enumerate(first) if c == letter]
    print(f'{len(indices)}')
    for index in indices:
        print(f"{index} ", end='')
