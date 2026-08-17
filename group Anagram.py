def groupAnagram(strs):
    groups = {}

    for word in strs:
        count = [0] * 26
        for char in word:
            index = ord(char) - ord('a')
            count[index] += 1
        key = tuple(count)

        if key not in groups:
            groups[key] = []

        groups[key].append(word)
    result = []
    for key in groups:
        result.append(groups[key])
    return result