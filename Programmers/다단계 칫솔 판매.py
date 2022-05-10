def solution(enroll, referral, seller, amount):
    n = len(enroll)
    tree = {enroll[i]: {'parent': referral[i], 'money': 0} for i in range(n)}
    for i, a in enumerate(amount):
        money, target = a * 100, seller[i]
        while money > 0 and target != '-':
            tree[target]['money'] += money - (money // 10)
            target, money = tree[target]['parent'], money // 10

    return [tree[enroll[i]]['money'] for i in range(n)]


