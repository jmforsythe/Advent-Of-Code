stones = []
for line in open("input.txt"):
    pos, v = line.strip().split(" @ ")
    stones.append((tuple(map(int, pos.split(", "))), tuple(map(int, v.split(", ")))))

X_MIN = 200000000000000
X_MAX = 400000000000000
Y_MIN = X_MIN
Y_MAX = X_MAX

out = 0

for i, (p1, v1) in enumerate(stones):
    for j, (p2, v2) in enumerate(stones[i+1:]):
        x1,y1,_ = p1
        x2,y2,_ = p2
        a1,b1,_ = v1
        a2,b2,_ = v2
        # We have [a1, -a2] [t1] = [x2-x1]
        #         [b1, -b2] [t2]   [y2-y1]
        # [t1] = 1/(a2*b1-a1*b2) [-b2, a2][x2-x1]
        # [t2]                   [-b1, a1][y2-y1]
        determinant = a2*b1-a1*b2
        if determinant == 0:
            continue
        t1 = ((x2-x1)*(-b2) + (y2-y1)*a2) / determinant
        t2 = ((x2-x1)*(-b1) + (y2-y1)*a1) / determinant
        if t1 < 0 or t2 < 0:
            continue
        pos1 = (x1+t1*a1, y1+t1*b1)
        pos2 = (x2+t2*a2, y2+t2*b2)
        if X_MIN <= pos1[0] <= X_MAX and X_MIN <= pos2[0] <= X_MAX and Y_MIN <= pos1[1] <= Y_MAX and Y_MIN <= pos2[1] <= Y_MAX:
            out += 1

print(out)

"""
We want to calculate p and v, the position and velocity of the fired particle
If p = (x,y,z), v = (u,v,w), and p_i = (x_i,y_i,z_i), v_i = (u_i,v_i,w_i)
for each given particle
We have (p-p_i) x (v-v_i) = 0 for all i
This gives us
[0    w_i  -v_i 0    -z_i y_i ][x y z u v w]^T + [-y_i*w_i+z_i*v_i]
[-w_i 0    u_i  z_i  0    -x_i]                  [-z_i*u_i+x_i*w_i] = pxv
[v_i  -u_i 0    -y_i x_i  0   ]                  [-x_i*v_i+y_i*u_i]

or

M_i S + O_i = pxv
Taking i and j as different indices
M_i S + O_i = M_j S + O_j
(M_i-M_j) S = O_j-O_i
similarly
(M_i-M_k) S = O_k-O_i
Giving 6 equations 6 unknowns
"""

def M(p, vel):
    x,y,z = p
    u,v,w = vel
    return (
        (0, w, -v, 0, -z, y),
        (-w, 0, u, z, 0, -x),
        (v, -u, 0, -y, x, 0)
    )

def O(p, vel):
    x,y,z = p
    u,v,w = vel
    return (
        -y*w + z*v,
        -z*u + x*w,
        -x*v + y*u
    )

(p0, v0), (p1, v1), (p2, v2) = stones[:3]

M_0 = M(p0,v0)
O_0 = O(p0,v0)
M_1 = M(p1,v1)
O_1 = O(p1,v1)
M_2 = M(p2,v2)
O_2 = O(p2,v2)

M_01 = [[M_0[i][j]-M_1[i][j] for j in range(len(M_0[0]))] for i in range(len(M_0))]
M_02 = [[M_0[i][j]-M_2[i][j] for j in range(len(M_0[0]))] for i in range(len(M_0))]

O_01 = [j-i for i,j in zip(O_0, O_1)]
O_02 = [j-i for i,j in zip(O_0, O_2)]

big_M = M_02 + M_01
big_O = O_02 + O_01
# big_M * [x,y,z,u,v,w] = big_O

# numpy was not precise enough
import sympy
print(sum(list(sympy.matrices.Matrix(big_M).solve(sympy.matrices.Matrix(big_O)))[:3]))
