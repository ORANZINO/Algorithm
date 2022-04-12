import re
from collections import defaultdict


def solution(word, pages):
    links = [None] * len(pages)
    dic = defaultdict(int)
    for i, page in enumerate(pages):
        link = re.search('<meta property="og:url" content="(https://\S+)"/>', page).group(1)
        links[i] = link
        out_links = re.findall('<a href="(https://[\S]*)">', page)
        basic_score = re.findall('[a-z]+', page.lower()).count(word.lower())
        dic[link] += basic_score
        for out_link in out_links:
            dic[out_link] += basic_score / len(out_links)
    max_val, answer = 0, 0
    for i, link in enumerate(links):
        if dic[link] > max_val:
            max_val = dic[link]
            answer = i
    return answer

