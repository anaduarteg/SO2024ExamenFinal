import sys

def sjf_preemptive(processes):
    time = 0
    gantt_chart = []
    while processes:
        # Seleccionar proceso con el menor tiempo de ráfaga restante
        ready_queue = [p for p in processes if p['arrival'] <= time]
        if not ready_queue:
            time += 1
            continue

        current = min(ready_queue, key=lambda x: x['burst'])
        gantt_chart.append((current['name'], time, time + 1))
        current['burst'] -= 1
        time += 1

        if current['burst'] == 0:
            processes.remove(current)

    return gantt_chart


if __name__ == "__main__":
    processes = [
        {'name': 'A', 'arrival': 0, 'burst': 7},
        {'name': 'B', 'arrival': 2, 'burst': 13},
        {'name': 'C', 'arrival': 4, 'burst': 3},
        {'name': 'D', 'arrival': 4, 'burst': 5},
        {'name': 'E', 'arrival': 6, 'burst': 7},
        {'name': 'F', 'arrival': 6, 'burst': 3},
    ]

    # Ejecución
    gantt_chart = sjf_preemptive(processes)
    for entry in gantt_chart:
        print(f"Proceso {entry[0]}: {entry[1]} - {entry[2]}")
