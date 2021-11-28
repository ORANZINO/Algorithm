def convert(c):
    if c in ['A', 'B', 'C']:
        return 3
    elif c in ['D', 'E', 'F']:
        return 4
    elif c in ['G', 'H', 'I']:
        return 5
    elif c in ['J', 'K', 'L']:
        return 6
    elif c in ['M', 'N', 'O']:
        return 7
    elif c in ['P', 'Q', 'R', 'S']:
        return 8
    elif c in ['T', 'U', 'V']:
        return 9
    else:
        return 10


print(sum(map(convert, input())))



"""
알파벳별로 숫자를 지정한 후 합을 출력한다
"""