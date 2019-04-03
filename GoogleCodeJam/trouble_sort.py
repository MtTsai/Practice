t = int(raw_input())

for i in xrange(1, t + 1):
    N = int(raw_input())
    V = [int(s) for s in raw_input().split(' ')]

    # Trouble Sort
    done = False
    while not done:
        done = True
        for j in range(N - 2):
            if V[j] > V[j + 2]:
                done = False
                V[j], V[j + 2] = V[j + 2], V[j]

    err_id = -1
    for j in range(N - 1):
        if V[j] > V[j + 1]:
            err_id = j
            break

    print "Case #{}: {}".format(i, err_id if err_id != -1 else 'OK')
