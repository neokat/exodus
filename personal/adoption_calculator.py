wantayn = {
    'name': 'Wantayn',
    'level': 278,
    'strength': 505,
    'defence': 365,
    'movement': 176,
    'health': 550
}

betrayn = {
    'name': 'Betrayn',
    'level': 20,
    'strength': 38,
    'defence': 40,
    'movement': 15,
    'health': 39
}

bonesmasher = {
    'name': 'Bonesmasher',
    'level': 50,
    'strength': 100,
    'defence': 100,
    'movement': 17,
    'health': 100
}


def calculate(pet):
    cost = 0
    transfers = 0
    hsd_gained = 0

    print("Starting stats: {}".format(pet))

    while transfers <= 4:

        transfer_cost = 1100 + (pet['level'] * (pet['strength'] + pet['defence'] + pet['movement'] + 60))
        cost += transfer_cost

        if transfers < 4:
            pet['strength'] += 3
            pet['health'] += 4
            pet['movement'] += 4
            hsd_gained += 11

        transfers += 1

    cost_per_hsd = cost / hsd_gained

    print("Ending stats: {}".format(pet))
    print("The total cost of 4 transfers will be {}. {} will gain {} HSD points at a cost of {} per HSD point.".format(
        cost, pet['name'], hsd_gained, cost_per_hsd)
    )
    print()


if __name__ == '__main__':
    calculate(wantayn)
    calculate(betrayn)
    calculate(bonesmasher)
