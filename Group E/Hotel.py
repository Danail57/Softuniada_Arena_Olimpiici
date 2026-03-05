def hotel():
    floors = []
    apartment_count = 0
    
    for i in range(4):
        key = input().strip()
        floor = int(key[0:2])
        floors.append(floor)
        room_type = key[-1]
        if room_type == 'A':
            apartment_count += 1

    print(*floors, apartment_count)
hotel()
