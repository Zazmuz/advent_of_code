with open("10.txt", "r") as file:
    lines = file.readlines()

# convert to num
buttons = []
for line in lines:
    a, *rest = line.strip().split(" ")
    toggles, joltage = rest[:-1], rest[-1]

    joltage = [int(_) for _ in joltage[1:][:-1].split(",")]    

    flips = []
    for toggle in toggles:
        toggle = toggle[1:][:-1].split(",")

        flips.append([int(_) for _ in toggle])
    buttons.append((joltage, flips))

import z3

s = 0

for but in buttons:
    target_joltage, flips = but

    opt = z3.Optimize()

    press_vars = [z3.Int(f'b_{i}') for i in range(len(flips))]

    for x in press_vars:
        opt.add(x >= 0)

    for counter_idx, target_val in enumerate(target_joltage):
        counter_sum = 0
        for btn_idx, affected_indices in enumerate(flips):
            if counter_idx in affected_indices:
                counter_sum += press_vars[btn_idx]

        opt.add(counter_sum == target_val)

    opt.minimize(z3.Sum(press_vars))

    model = opt.model()
    machine_presses = sum(model[x].as_long() for x in press_vars)
    s += machine_presses

print(s)