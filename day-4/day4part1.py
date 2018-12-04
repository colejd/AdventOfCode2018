from datetime import datetime
from collections import defaultdict


class Event:
    def __init__(self, line):
        self.line = line
        split = line.split("]")
        time_str = split[0][1:]
        self.timestamp = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        self.event_text = split[1][1:]

    def __repr__(self):
        return self.line + "\n"

    def get_guard_id(self):
        return int(self.event_text.split()[1][1:])

    def is_shift_change(self):
        return self.event_text[0] == "G"

    def is_sleep_event(self):
        return self.event_text[0] == "f"

    def is_wake_event(self):
        return self.event_text[0] == "w"


def get_lines():
    with open("input.txt") as fp:
        return [line[:-1] for line in fp]


def get_solution():
    events = [Event(line) for line in get_lines()]
    events.sort(key=lambda item: item.timestamp)

    # Keyed by guard ID. Inner dict represents total minutes slept indexed by minute
    guard_events = defaultdict(lambda: defaultdict(int))

    # Populate the guard events
    current_guard = -1
    sleep_minute = -1
    for event in events:
        if event.is_shift_change():
            current_guard = event.get_guard_id()
        elif event.is_sleep_event():
            sleep_minute = event.timestamp.minute
        elif event.is_wake_event():
            # Mark all minutes from sleep_minute to the current_minute - 1 as asleep
            for i in range(sleep_minute, event.timestamp.minute):
                guard_events[current_guard][i] += 1

    # From the guard events, find the guard that slept the most
    sleepiest_guard_id = max(guard_events, key=lambda k: sum(guard_events[k].values()))
    # And from that guard, find the minute that he slept most commonly on
    sleepiest_minute = max(guard_events[sleepiest_guard_id], key=guard_events[sleepiest_guard_id].get)

    return sleepiest_guard_id * sleepiest_minute


print(get_solution())

# Correct answer is 87681
