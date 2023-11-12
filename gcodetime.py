import math
from scipy.linalg import solve


def codeG0(refp, curp):

    if hasattr(curp, 'X'):
        refp['X'] = curp['X']
    if hasattr(curp, 'Y'):
        refp['Y'] = curp['Y']
    if hasattr(curp, 'Z'):
        refp['Z'] = curp['Z']
   # time = machine dependent time
    refp['T'] = refp['T']  # + time

    return refp


def codeG1(refp, curp):

    (x1, y1, z1) = (refp['X'], refp['Y'], refp['Z'])
    if hasattr(curp, 'X'):
        x2 = curp['X']
    else:
        x2 = refp['X']
    if hasattr(curp, 'Y'):
        y2 = curp['Y']
    else:
        y2 = refp['Y']
    if hasattr(curp, 'Z'):
        z2 = curp['Z']
    else:
        z2 = refp['Z']

    refp['X'] = x2
    refp['Y'] = y2
    refp['Z'] = z2
    if hasattr(curp,'F'):
        refp['F'] = curp['F']
    if hasattr(curp,'S'):
        refp['S'] = curp['S']

    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    time = dist / refp['F']
    refp['T'] = refp['T'] + time

    return refp


def codeG2(refp, curp):

    (x2, y2, z2) = (refp['X'], refp['Y'], refp['Z'])
    x3 = curp['X'] if 'X' in curp else refp['X']
    y3 = curp['Y'] if 'Y' in curp else refp['Y']
    z3 = curp['Z'] if 'Z' in curp else refp['Z']

    if 'R' in curp:
        a = (x2 - x3)/2
        b = (y2 - y3)/2
        c = (z2 - z3)/2
        d = (x2**2 + y2**2 + z2**2) - (x3**2 + y3**2 + z3**2)
        [x1, y1, z1] = solve([a, b, c], d)
        N = (x3 - x1)*(x2 - x1) + (y3 - y1)*(y2 - y1) + (z3 - z1)*(z2 - z1)
        dist = curp['R']*math.acos(N/(curp['R']**2))
    else:
        i = curp['I'] if 'I' in curp else 0
        j = curp['J'] if 'J' in curp else 0
        k = curp['K'] if 'K' in curp else 0

        (x1, y1, z1) = ((x2 - i), (y2 - j), (z2 - k))
        r2 = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
        N = (x3 - x1)*(x2 - x1) + (y3 - y1)*(y2 - y1) + (z3 - z1)*(z2 - z1)
        print(N)
        print(r2)
        dist = math.sqrt(r2)*math.acos(N/r2)
    print(dist)

    refp['X'] = x3
    refp['Y'] = y3
    refp['Z'] = z3
    if hasattr(curp,'F'):
        refp['F'] = curp['F']
    if hasattr(curp,'S'):
        refp['S'] = curp['S']

    time = dist / refp['F']
    refp['T'] = refp['T'] + time
    print(time)
    print(refp)

    return refp


def codeG3(refp, curp):

    (x2, y2, z2) = (refp['X'], refp['Y'], refp['Z'])
    if hasattr(curp, 'X'):
        x3 = curp['X']
    else:
        x3 = refp['X']
    if hasattr(curp, 'Y'):
        y3 = curp['Y']
    else:
        y3 = refp['Y']
    if hasattr(curp, 'Z'):
        z3 = curp['Z']
    else:
        z3 = refp['Z']

    if hasattr(curp,'R'):
        a = (x2 - x3)/2
        b = (y2 - y3)/2
        c = (z2 - z3)/2
        d = (x2**2 + y2**2 + z2**2) - (x3**2 + y3**2 + z3**2)
        [x1, y1, z1] = solve([a, b, c], d)
        N = (x3 - x1)*(x2 - x1) + (y3 - y1)*(y2 - y1) + (z3 - z1)*(z2 - z1)
        dist = curp['R']*math.acos(N/(curp['R']**2))
    else:
        (i, j, k) = (0, 0, 0)
        if hasattr(curp,'I'):
            i = curp['I']
        if hasattr(curp,'J'):
            i = curp['J']
        if hasattr(curp,'K'):
            i = curp['K']
        (x1, y1, z1) = ((x2 - i), (y2 - j), (z2 - k))
        r2 = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
        N = (x3 - x1)*(x2 - x1) + (y3 - y1)*(y2 - y1) + (z3 - z1)*(z2 - z1)
        dist = math.sqrt(r2)*math.acos(N/(r2+1))

    refp['X'] = x3
    refp['Y'] = y3
    refp['Z'] = z3
    if hasattr(curp,'F'):
        refp['F'] = curp['F']
    if hasattr(curp,'S'):
        refp['S'] = curp['S']

    time = dist / refp['F']
    refp['T'] = refp['T'] + time

    return refp


def codeG4(refp, curp):

    refp['X'] = curp['X']
    refp['Y'] = curp['Y']
    refp['Z'] = curp['Z']
    time = curp['P']/1000
    refp['T'] = refp['T'] + time

    return refp
