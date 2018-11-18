import random

t1 = 62.137
t0 = 100
e1 = 0.5
e2 = 1
loss1 = t1 - t0 * e1
loss2 = t1 -  t0 * e2
while loss1 * loss2 < 0:
    if loss1 < 0.01:
        break
    e3 = e1 + random.random() * (e2 - e1)
    loss3 = t1 - t0 * e3
    if loss1 * loss3 < 0:
        e2 = e3
        loss1 = t1 - t0 * e1
        loss2 = t1 - t0 * e2
        pass
    if loss2 * loss3 < 0:
        e1 = e3
        loss1 = t1 - t0 * e1
        loss2 = t1 - t0 * e2
        pass
print(e1)