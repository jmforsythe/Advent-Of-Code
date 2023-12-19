out = 0

worfkflows = {}
do_ratings = False
for line in open("input.txt"):
    if not do_ratings:
        if line.strip() == "":
            do_ratings = True
            continue
        name, b = line.strip()[:-1].split("{")
        rules = [x.split(":") if ":" in x else ["True",x] for x in b.split(",")]
        worfkflows[name] = rules
    else:
        for var in line.strip()[1:-1].split(","):
            exec(var)
        cur_state = "in"
        while cur_state not in ("A", "R"):
            for cond, dest in worfkflows[cur_state]:
                if eval(cond):
                    cur_state = dest
                    break

        if cur_state == "A":
            for var in line.strip()[1:-1].split(","):
                out += int(var.split("=")[1])

print(out)

def get_ranges(key, x_range, m_range, a_range, s_range):
    if key == "A":
        return [("A", x_range, m_range, a_range, s_range)]
    if key == "R":
        return []
    out = []
    m = {"x": x_range, "m": m_range, "a": a_range, "s": s_range}
    for cond, dest in worfkflows[key]:
        if cond == "True":
            out += get_ranges(dest, m["x"], m["m"], m["a"], m["s"])
            continue
        sym = "<" if "<" in cond else ">"
        var, val = cond.split(sym)
        val = int(val)
        less = (m[var][0], min(m[var][1], val))
        less_eq = (m[var][0], min(m[var][1], val+1))
        greater = (max(m[var][0], val+1), m[var][1])
        greater_eq = (max(m[var][0], val), m[var][1])
        if sym == "<":
            m[var] = less
            out += get_ranges(dest, m["x"], m["m"], m["a"], m["s"])
            m[var] = greater_eq
        else:
            m[var] = greater
            out += get_ranges(dest, m["x"], m["m"], m["a"], m["s"])
            m[var] = less_eq
    return [(key + "-" + r[0], *r[1:]) for r in out]

out = 0
for r in get_ranges("in", (1,4001), (1,4001), (1,4001), (1,4001)):
    t = 1
    for a, b in r[1:]:
        t *= b-a
    out += t
print(out)

516228205000000
