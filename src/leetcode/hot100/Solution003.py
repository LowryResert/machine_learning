def length_of_longest_substring(s: str) -> int:
    # hash set, record if a letter occurred
    occ = set()
    n = len(s)
    # left pointer-left, right pointer - right
    ans, right = 0, -1
    for i in range(n):
        if i != 0:
            # left pointer right move, remove the letter which left pointer pointing from occ
            occ.remove(s[i - 1])
        while right + 1 < n and s[right + 1] not in occ:
            occ.add(s[right + 1])
            right += 1

        ans = max(ans, right - i + 1)

    return ans


print(length_of_longest_substring(''))
