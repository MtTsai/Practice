t = int(raw_input())

for i in xrange(1, t + 1):
    D, P = raw_input().split(' ')
    D = int(D)

    atk, beamstr = 0, 1

    for cmd in P:
        if cmd == 'C':
            beamstr <<= 1
        elif cmd == 'S':
            atk += beamstr

    shot, hack = 0, 0
    for cmd in reversed(P):
        if cmd == 'C':
            beamstr >>= 1
            for _ in range(shot):
                atk  -= beamstr
                hack += 1
                if atk <= D:
                    break
        elif cmd == 'S':
            shot += 1

        if atk <= D:
            break

    print "Case #{}: {}".format(i, hack if atk <= D else 'IMPOSSIBLE')
