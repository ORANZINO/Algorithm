from collections import defaultdict

def solution(id_list, report, k):
    report_dic = defaultdict(set)
    idx_dic = {id_list[i]: i for i in range(len(id_list))}
    answer = [0] * len(id_list)
    for r in report:
        reporter, reported = r.split()
        report_dic[reported].add(reporter)
    for key in report_dic.keys():
        if len(report_dic[key]) >= k:
            for id in report_dic[key]:
                answer[idx_dic[id]] += 1
    return answer


