ff = {}
cj = {}
broadcaster = []

def read_input():
    for line in open("input.txt"):
        source, dests = line.strip().split(" -> ")
        if source[0] == "%":
            ff[source[1:]] = [False, dests.split(", ")]
        elif source[0] == "&":
            cj[source[1:]] = [{}, dests.split(", ")]
        else:
            broadcaster.extend(dests.split(", "))

    for dest in broadcaster:
        if dest in cj:
            cj[dest][0]["broadcaster"] = "low"

    for label, (_, dests) in ff.items():
        for dest in dests:
            if dest in cj:
                cj[dest][0][label] = "low"

    for label, (_, dests) in cj.items():
        for dest in dests:
            if dest in cj:
                cj[dest][0][label] = "low"
read_input()

low_pulse_count = 0
high_pulse_count = 0

rx_input = [label for label, (inp, dests) in cj.items() if dests == ["rx"]][0]
rx_input_inputs = {label: 0 for label, (inp, dests) in cj.items() if rx_input in dests}

def push_button():
    global low_pulse_count
    global high_pulse_count
    global rx_low_pulse
    q = []
    q2 = [("button", "low", "broadcaster")]

    while q2:
        q = q2
        q2 = []
        while q:
            src, pulse, label = q.pop(0)
            if label == rx_input and pulse == "high":
                rx_input_inputs[src] = i - rx_input_inputs[src]
            if pulse == "low":
                low_pulse_count += 1
            elif pulse == "high":
                high_pulse_count += 1
            if label == "broadcaster":
                for dest in broadcaster:
                    q2.append(("broadcaster", pulse, dest))
            elif label in ff:
                if pulse == "low":
                    for dest in ff[label][1]:
                        q2.append((label, "low" if ff[label][0] else "high", dest))
                    ff[label][0] = not ff[label][0]
            elif label in cj:
                cj[label][0][src] = pulse
                if all(v == "high" for l, v in cj[label][0].items()):
                    for dest in cj[label][1]:
                        q2.append((label, "low", dest))
                else:
                    for dest in cj[label][1]:
                        q2.append((label, "high", dest))

i = 0
while i <= 1000 or not all(rx_input_inputs.values()):
    if i == 1000:
        print(low_pulse_count * high_pulse_count)
    i += 1
    push_button()

from math import lcm
print(lcm(*map(int, rx_input_inputs.values())))
