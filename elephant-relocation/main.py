import sys

# loading data
# data = sys.stdin.readlines()

with open("data/slo2.in") as file:
    data = file.readlines()

elephant_mass_list = [int(mass) for mass in data[1].split()]
min_mass = min(elephant_mass_list)

current_order = data[2].split()
current_order[-1].strip("\n")
desired_order = data[3].split()
desired_order[-1].strip("\n")

work_needed = 0


# saving "elephant": "desired index" pairs in dictionary
desired_pair_dict = {}
j_1 = 0
for elephant in desired_order:
    desired_pair_dict[elephant] = j_1
    j_1 += 1

# saving "elephant": "starting index" for further permutation
to_perm = {}
j_2 = 0
for elephant in current_order:
    to_perm[elephant] = j_2
    j_2 += 1

# mainloop for calculating work in cycles
while len(to_perm) > 0:

    # setting new cycle
    i = to_perm[next(iter(to_perm))]
    cycle = [current_order[i]]
    del to_perm[current_order[i]]

    eleph = cycle[0]
    i = desired_pair_dict[eleph]
    eleph = current_order[i]
    while eleph != cycle[0]:
        cycle.append(eleph)
        del to_perm[current_order[i]]
        i = desired_pair_dict[eleph]
        eleph = current_order[i]

    # defining basic parameters to calculate work in cycle
    cycle_mass_list = []

    for elephant in cycle:
        mass = elephant_mass_list[int(elephant) - 1]
        cycle_mass_list.append(mass)

    cycle_mass_sum = sum(cycle_mass_list)
    min_mass_cycle = min(cycle_mass_list)
    cycle_lenght = len(cycle_mass_list)

    # method 1
    cycle_work_1 = cycle_mass_sum + (cycle_lenght - 2) * min_mass_cycle

    # method 2
    cycle_work_2 = cycle_mass_sum + min_mass_cycle + (cycle_lenght + 1) * min_mass

    # adding work for cycle from better method
    work_needed += min(cycle_work_1, cycle_work_2)

print(work_needed)
