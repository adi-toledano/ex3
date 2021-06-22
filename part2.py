def check_strings(s1: str, s2: str):
    s2_dict = {}
    s1 = s1.lower()
    s2 = s2.lower()
    for char in s2:
        if char in s2_dict:
            s2_dict[char] += 1
        else:
            s2_dict[char] = 1
    for char in s1:
        if not s2_dict.get(char):
            return False
        s2_dict[char] -= 1
    return True

