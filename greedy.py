def pcmax_greedy(processes, processors):
    # posortuj zadania malejaco
    # processes.sort(reverse=True)

    # utowrz tablice z zaplanowanymi procesami
    schedules = [[] for _ in range(processors)]

    for process in processes:
        # znalezienie procesora z najkrotszym czasem wykonywania i przydzielenie mu procesu
        shortest_processor = min(schedules, key=sum)
        shortest_processor.append(process)

    # oblicz laczny czas wykonywania dla procesorow i znajdz czas ostatniego procesora
    end_times = [sum(processor) for processor in schedules]
    max_end_time = max(end_times)

    return max_end_time
