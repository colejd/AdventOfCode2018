from datetime import datetime
from collections import defaultdict
import collections


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

    # # Method 1
    # sleepiest_guard_id = -1
    # most_frequent_minute = -1
    #
    # largest_minute_val = -1
    # for guard_id, sleep_times in guard_events.items():
    #     # print(collections.OrderedDict(sorted(times.items())).values())
    #     m = max(sleep_times, key=sleep_times.get)
    #     if sleep_times[m] >= largest_minute_val:
    #         largest_minute_val = sleep_times[m]
    #         most_frequent_minute = m
    #         sleepiest_guard_id = guard_id

    # Method 2
    # Of all guards, which one is most frequently asleep on the same minute?
    sleepiest_guard_id = max(guard_events, key=lambda k: max(guard_events[k].values()))
    most_frequent_minute = max(guard_events[sleepiest_guard_id], key=guard_events[sleepiest_guard_id].get)

    return sleepiest_guard_id * most_frequent_minute


print(get_solution())

# Correct answer is 136461
