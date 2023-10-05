
def calculate_direction_offset(direction: str) -> tuple[int, int]:
    direction = direction.upper()
    # todo: handle names instead of symbols

    # future: this could be match/case statements
    # but that's only in Python 3.10 so depends on compatibility
    if direction == 'N':
        return 0, -1
    elif direction == 'S':
        return 0, 1
    elif direction == 'E':
        return 1, 0
    elif direction == 'W':
        return -1, 0
    elif direction == 'NE':
        return -1, 1
    elif direction == 'NW':
        return -1, -1
    elif direction == 'SE':
        return 1, 1
    elif direction == 'SW':
        return 1, -1
    else:
        return 0, 0  # todo: actually handle this

def check_borders(current_location: tuple[int, int], x_offset: int, y_offset: int) -> bool:
    if x_offset != 0:  # note: if we are moving along the x
        if current_location[0] == 0 and x_offset == -1:
            return False
        elif current_location[0] == len(map[0]) and x_offset == 1:
            return False
    # note: if x movement is okay

    if y_offset != 0:  # note: if we are moving along the y
        if current_location[1] == 0 and y_offset == -1:
            return False
        elif current_location[1] == len(map) and y_offset == 1:
            return False
    # note: if y movement is okay
    
    return True

def change_location(current_location: tuple[int, int], x_offset: int, y_offset: int) -> tuple[tuple[int, int], str]:
    if check_borders(current_location, x_offset, y_offset):
        new_location = (
            current_location[0] + x_offset,
            current_location[1] + y_offset
        )
        return new_location
    else: 
        return current_location  # todo: actually handle this


map: list[list[str]] = [
    # 0    1    2    3    4
    ['a', 'b', 'c', 'd', 'e'],  # 0
    ['f', 'g', 'h', 'i', 'j'],  # 1
    ['k', 'l', 'm', 'n', 'o'],  # 2
    ['p', 'q', 'r', 's', 't'],  # 3
    ['u', 'v', 'w', 'x', 'y']   # 4
]

desc_of_locations: dict[str, str] = {
    'a': 'some text about a',
    'b': 'some text about b',
    'c': 'some text about c',
    'd': 'some text about d',
    'e': 'some text about e',
    'f': 'some text about f',
    'g': 'some text about g',
    'h': 'some text about h',
    'i': 'some text about i',
    'j': 'some text about j',
    'k': 'some text about k',
    'l': 'some text about l',
    'm': 'some text about m',
    'n': 'some text about n',
    'o': 'some text about o',
    'p': 'some text about p',
    'q': 'some text about q',
    'r': 'some text about r',
    's': 'some text about s',
    't': 'some text about t',
    'u': 'some text about u',
    'v': 'some text about v',
    'w': 'some text about w',
    'x': 'some text about x',
    'y': 'some text about y'
}

for row in map:
    print(row)

current_location = (2, 2)

while True:
    name_of_current_location = map[current_location[1]][current_location[0]]
    print(f'\nYou are currently in: {name_of_current_location}')
    print(desc_of_locations[name_of_current_location])

    user_req_direction = input('Please enter a direction: ').upper()
    current_location = change_location(current_location, *calculate_direction_offset(user_req_direction))
