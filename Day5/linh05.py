with open('input.txt') as f:
    polymer = f.readlines()[0].strip()

mapping = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for a in alphabet:
    mapping[a.upper()] = a.lower()
    mapping[a.lower()] = a.upper()

stack = []
for p in polymer:
    if stack and p == mapping[stack[-1]]:
        stack.pop()
    else:
        stack.append(p)
print(len(stack))

shortest_pol = 1e30
for a in alphabet:
    reduced_pol = [c for c in polymer if c != a.lower() and c != a.upper()]
    stack = []
    for c in reduced_pol:
        if stack and c == mapping[stack[-1]]:
            stack.pop()
        else:
            stack.append(c)
    shortest_pol = min(shortest_pol, len(stack))

print(shortest_pol)
