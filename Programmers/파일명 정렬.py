def solution(files):
    def convert(word, index):
        num_start = 0
        while num_start < len(word) and not word[num_start].isdigit():
            num_start += 1
        num_end = num_start
        while num_end < len(word) and word[num_end].isdigit():
            num_end += 1
        return (word[:num_start].lower(), int(word[num_start:num_end]), index)
    sort_files = sorted([convert(file, i) for i, file in enumerate(files)])
    return [files[s[2]] for s in sort_files]


