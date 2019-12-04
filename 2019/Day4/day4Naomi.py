from collections import Counter

lb = 171309
ub = 643603

def possible_password(pw):
    as_word=str(pw)
    if all([as_word[i]!=as_word[i+1] for i in range(5)]):
        return False
    if any([int(as_word[i])>int(as_word[i+1]) for i in range(5)]):
        return False
    return True

password_range=[possible_password(pw) for pw in range(lb,ub)]
possible_passwords=[range(lb,ub)[row] for row in range(ub-lb) if password_range[row]==True]
num_possibles=sum(password_range)
print("Part 1: "+str(num_possibles))

smaller_range=[]

for pw in possible_passwords:
    as_word=str(pw)
    letter_counts=list(Counter(str(as_word)).values())
    if any([ct==2 for ct in letter_counts]):
        smaller_range.append(pw)

print("Part 2: "+str(len(smaller_range)))
