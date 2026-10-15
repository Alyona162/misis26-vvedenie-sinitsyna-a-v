import random

SIZE = 5
START = (0, 0)
EXIT = (SIZE - 1, SIZE - 1)

ROOM_TYPES = ["пусто", "сундук", "монстр", "ловушка", "портал"]
ICONS = {
    "пусто":   "🟫",
    "сундук":  "🎁",
    "монстр":  "🧟",
    "ловушка": "🕳️",
    "портал":  "💫",
    "старт":   "🟩",
    "выход":   "🏆",
    "ключ":    "🗝️",
}
PLAYER_ICON = "🧝"
UNKNOWN_ICON = "⬛"


LOOT_POOL = ["зелье", "меч", "щит", "золото"]

UPGRADES = {
    "меч":   "клинок",
    "щит":   "бастион",
    "зелье": "эликсир",
}


#генерация поля
def generate_maze():
    maze = []
    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            row.append({"type": random.choice(ROOM_TYPES), "visited": False, "items": []})
        maze.append(row)

    maze[START[0]][START[1]]["type"] = "старт"
    maze[START[0]][START[1]]["visited"] = True
    maze[EXIT[0]][EXIT[1]]["type"] = "выход"

    chests = [(i, j) for i in range(SIZE) for j in range(SIZE)
              if maze[i][j]["type"] == "сундук"]
    if not chests:
        i, j = random.choice([(i, j) for i in range(SIZE) for j in range(SIZE)
                              if (i, j) not in (START, EXIT)])
        maze[i][j]["type"] = "сундук"
        chests = [(i, j)]

    kx, ky = random.choice(chests)
    maze[kx][ky]["items"].append("ключ")

    for (i, j) in chests:
        if (i, j) != (kx, ky) and random.random() < 0.8:
            maze[i][j]["items"].append(random.choice(LOOT_POOL))

    return maze


#отрисовка
def show_map(maze, pos):
    print("\n" + "─" * (SIZE * 3))
    for i in range(SIZE):
        line = ""
        for j in range(SIZE):
            if (i, j) == pos:
                line += PLAYER_ICON + " "
            elif maze[i][j]["visited"]:
                line += ICONS.get(maze[i][j]["type"], "?") + " "
            else:
                line += UNKNOWN_ICON + " "
        print(line)
    print("─" * (SIZE * 3))


#бой
def fight(state):
    monster_hp = random.randint(15, 25)
    print(f"\n🧟 Монстр! У него {monster_hp} HP.")

    while monster_hp > 0 and state["hp"] > 0:
        print(f"Монстр: {monster_hp} HP | Вы: {state['hp']} HP")
        action = input("1 — атака, 2 — зелье, 3 — бежать: ").strip()

        if action == "1":
            dmg = random.randint(5, 15)
            if "меч" in state["inv"]:
                dmg += 5
            if "клинок" in state["inv"]:
                dmg += 10
            monster_hp -= dmg
            print(f"Вы нанесли {dmg} урона.")

        elif action == "2":
            heal = None
            if "эликсир" in state["inv"]:
                heal, item = 50, "эликсир"
            elif "зелье" in state["inv"]:
                heal, item = 30, "зелье"
            if heal:
                state["inv"].remove(item)
                state["hp"] = min(100, state["hp"] + heal)
                print(f"Вы выпили {item}: +{heal} HP.")
            else:
                print("Нет зелья.")

        elif action == "3":
            if random.random() < 0.5:
                print("Вы сбежали!")
                return
            print("Сбежать не удалось.")

        else:
            continue

        if monster_hp > 0:
            hit = random.randint(5, 12)
            if "бастион" in state["inv"]:
                hit //= 2
            elif "щит" in state["inv"]:
                hit = int(hit * 0.75)
            state["hp"] -= hit
            print(f"Монстр бьёт на {hit}.")

    if state["hp"] > 0:
        print("Монстр побеждён! Выпало золото.")
        state["inv"].append("золото")


#комнаты
def enter_room(maze, state):
    x, y = state["pos"]
    room = maze[x][y]

    if room["visited"] and room["type"] != "портал":
        return

    room["visited"] = True
    kind = room["type"]
    print(f"\n>>> Комната: {kind}")

    if kind == "сундук":
        if room["items"]:
            print(f"Внутри: {room['items']}")
            for item in room["items"]:
                state["inv"].append(item)
                print(f"  + {item}")
            room["items"] = []
        else:
            print("Сундук пуст.")

    elif kind == "монстр":
        fight(state)

    elif kind == "ловушка":
        dmg = random.randint(10, 20)
        if "бастион" in state["inv"]:
            dmg //= 3
            print("Бастион сильно смягчил удар!")
        elif "щит" in state["inv"]:
            dmg //= 2
            print("Щит смягчил удар!")
        state["hp"] -= dmg
        print(f"Ловушка! -{dmg} HP")

    elif kind == "портал":
        state["pos"] = [random.randrange(SIZE), random.randrange(SIZE)]
        print("Портал перенёс вас в другое место!")
        enter_room(maze, state)
        
    elif kind == "пусто":
        if random.random() < 0.15:
            print("Вы нашли зелье!")
            state["inv"].append("зелье")

    elif kind == "выход":
        if "ключ" in state["inv"]:
            print("🏆 Выход открыт! Вы победили!")
            return "win"
        else:
            print("Выход заперт. Нужен ключ.")
    return None


#инвентарь
def show_inventory(state):
    inv = state["inv"]
    print(f"\nИнвентарь: {inv if inv else 'пусто'}")
    print("1 — выкинуть, 2 — улучшить, 3 — использовать, 0 — назад")
    c = input("Выбор: ").strip()

    if c == "1":
        name = input("Что выкинуть? ").strip()
        if name in inv:
            inv.remove(name)
            print(f"Выкинуто: {name}")
        else:
            print("Такого предмета нет.")

    elif c == "2":
        for base, better in UPGRADES.items():
            if inv.count(base) >= 2:
                inv.remove(base)
                inv.remove(base)
                inv.append(better)
                print(f"{base} + {base} -> {better}")
                return
        print("Нечего улучшать (нужно 2 одинаковых предмета).")

    elif c == "3":
        if "эликсир" in inv:
            inv.remove("эликсир")
            state["hp"] = min(100, state["hp"] + 50)
            print("+50 HP")
        elif "зелье" in inv:
            inv.remove("зелье")
            state["hp"] = min(100, state["hp"] + 30)
            print("+30 HP")
        else:
            print("Нечего использовать.")

    elif c == "0":
        return


#основной цикл
def main():
    maze = generate_maze()
    state = {"hp": 100, "inv": [], "pos": [START[0], START[1]]}

    moves = {
        "w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1),
        "ц": (-1, 0), "ы": (1, 0), "ф": (0, -1), "в": (0, 1),
    }

    while state["hp"] > 0:
        show_map(maze, state["pos"])
        print(f"HP: {state['hp']} | Инвентарь: {state['inv']}")

        result = enter_room(maze, state)
        if result == "win":
            return
        if state["hp"] <= 0:
            break

        cmd = input("w/a/s/d — идти, i — инвентарь, q — выход: ").strip().lower()

        if cmd == "q":
            print("Вы вышли из игры.")
            return
        elif cmd == "i":
            show_inventory(state)
        elif cmd in moves:
            nx = state["pos"][0] + moves[cmd][0]
            ny = state["pos"][1] + moves[cmd][1]
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                state["pos"] = [nx, ny]
            else:
                print("Там стена.")
        else:
            print("Неизвестная команда.")

    print("\n💀 Вы проиграли.")


if __name__ == "__main__":
    main()
