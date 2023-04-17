# great self-work №1
roads = list(set(input().split('_')))
strangers = list(set(input().split('+')))
for road in roads:
    all_strangers_to_write = []
    for stranger in strangers:
        c = 0
        used_letters = []
        for letter in road.lower():
            if letter in stranger.lower() and letter not in used_letters:
                used_letters.append(letter)
                c += 1
            if c == 2:
                all_strangers_to_write.append(stranger)
                break
    print(f'{" ".join(list(map(lambda word: word.capitalize(), road.split())))}: {"-".join(all_strangers_to_write)}')
