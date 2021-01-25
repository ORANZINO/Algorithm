e, s, m = map(int, input().split())
count = 1
e_, s_, m_ = [1, 1, 1]

while (e != e_) or (s != s_) or (m != m_):
    e_ += 1
    s_ += 1
    m_ += 1
    if e_ > 15:
        e_ = 1
    if s_ > 28:
        s_ = 1
    if m_ > 19:
        m_ = 1
    count += 1

print(count)

