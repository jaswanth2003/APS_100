
def longest_common_prefix(strs):
    if not strs:
        return ""

    for i, char in enumerate(strs[0]):
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]
    return strs[0]



strs = ["flower", "flow", "flight"]
prefix = longest_common_prefix(strs)
print(prefix) 