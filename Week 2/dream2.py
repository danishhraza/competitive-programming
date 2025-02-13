def process_events():
    n = int(input().strip())
    event_stack = []
    results = []

    for _ in range(n):
        event = input().strip()
        if event.startswith('E '):
            event_name = event[2:]
            event_stack.append(event_name)
        elif event.startswith('D '):
            k = int(event[2:])
            event_stack = event_stack[:-k]
        elif event.startswith('S '):
            parts = event.split()
            m = int(parts[1])
            scenario_events = parts[2:]
            results.append(check_scenario(event_stack, m, scenario_events))

    for result in results:
        print(result)

def check_scenario(event_stack, m, scenario_events):
    for i in range(len(event_stack) + 1):
        current_events = event_stack[:len(event_stack) - i]
        if is_scenario_possible(current_events, scenario_events):
            if i == 0:
                return "Yes"
            else:
                return f"{i} Just A Dream"
    return "Plot Error"

def is_scenario_possible(current_events, scenario_events):
    for scenario_event in scenario_events:
        if scenario_event.startswith('!'):
            event_name = scenario_event[1:]
            if event_name in current_events:
                return False
        else:
            if scenario_event not in current_events:
                return False
    return True

# Run the process_events function to handle input and output
process_events()