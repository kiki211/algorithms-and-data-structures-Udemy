# 1 Anagram. Second method preferred

sentence1 = "dog and cat"
sentence2 = "cat and god"


def anagram(sentence1, sentence2):
    s1 = sentence1.replace(" ", "").lower()
    s2 = sentence2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

print(anagram(sentence1, sentence2))

def anagram2(sentence1, sentence2):
    s1 = sentence1.replace(" ", "").lower()
    s2 = sentence2.replace(" ", "").lower()

    # Edge case check
    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


print(anagram2(sentence1, sentence2))


# 2 Return number of pairs making a target sum


def pairs_sum(in_list, k):
    if len(in_list) < 2:
        return

    seen = set()
    output = set()

    for i in in_list:
        target = k - i
        if target in seen:
            output.add( ((min(target, i)), max(target, i)) )
        else:
            seen.add(i)

    return f"{len(output)} and the values are {output}."
    #return '\n'.join(map(str, output))


print(pairs_sum(in_list=[1, 2, 3, 2], k=4))



list1 = [0,1,2,3,4,5,6,7,8,9,10]
list2 = [i+4 for i in list1]
print(list2)

print(list1[-4::]) # slicing return last 4 digs










