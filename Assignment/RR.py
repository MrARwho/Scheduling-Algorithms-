import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
class RoundRobin:
    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            p = []
            process_id = i+1
            arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))
            burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
            p.extend([process_id, arrival_time, burst_time, 0, burst_time])
            process_data.append(p)

        quantam_time = int(input("Enter Time Slice: "))

        RoundRobin.schedulingProcess(self, process_data, quantam_time)

    def schedulingProcess(self, process_data, quantam_time):
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])

        while 1:
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if process_data[i][0] == ready_queue[k][0]:
                                present = 1
                    if present == 0:
                        temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                        ready_queue.append(temp)
                        temp = []

                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))

                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []

            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break

            if len(ready_queue) != 0:
                if ready_queue[0][2] > quantam_time:
                    start_time.append(s_time)
                    s_time = s_time + quantam_time
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - quantam_time
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= quantam_time:
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
                    ready_queue.pop(0)

            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                if normal_queue[0][2] > quantam_time:
                    start_time.append(s_time)
                    s_time = s_time + quantam_time
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - quantam_time

                elif normal_queue[0][2] <= quantam_time:
                    start_time.append(s_time)
                    s_time = s_time + normal_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)

        t_time = RoundRobin.calculateTurnaroundTime(self, process_data)
        w_time = RoundRobin.calculateWaitingTime(self, process_data)
        RoundRobin.printData(self, process_data, t_time, w_time, executed_process)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, executed_process):


        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print(f'Sequence of Processes: {executed_process}')

        result = []
        count = 0
        current = executed_process[0]
        time=0
        start=[0]

        for i in range(len(executed_process)):
            if executed_process[i] == current:
                count += 1
                time+=1
            else:
                result.append([current, count])
                count = 1
                start.append(time)
                time+=1
            current = executed_process[i]

        result.append([current, count])
        print(result)
        print(start)
        print(process_data)
        max_completion_time = max(process_data, key=lambda x: x[5])[5]
        print(f"Maximum Completion Time: {max_completion_time}")
        df = pd.DataFrame({'Process': [result[_][0] for _ in range(len(result))],
                           # 'team': ['R&D', 'Accounting', 'Sales', 'Sales', 'IT', 'R&D', 'IT', 'Sales',
                           # 'Accounting', 'Accounting', 'Sales', 'IT'], 'start': pd.to_datetime(['20 Oct 2022',
                           # '24 Oct 2022', '26 Oct 2022', '31 Oct 2022', '3 Nov 2022', '7 Nov 2022', '10 Nov 2022',
                           # '14 Nov 2022', '18 Nov 2022', '23 Nov 2022', '28 Nov 2022', '30 Nov 2022']),
                           # 'end': pd.to_datetime(['31 Oct 2022', '28 Oct 2022', '31 Oct 2022', '8 Nov 2022',
                           # '9 Nov 2022', '18 Nov 2022', '17 Nov 2022', '22 Nov 2022', '23 Nov 2022', '1 Dec 2022',
                           # '5 Dec 2022', '5 Dec 2022']),
                           'Duration': [result[_][1] for _ in range(len(result))],
                           # 'end': [Process[_][5] for _ in range(len(Process))],
                           'time': [start[_] for _ in range(len(result))]
                           })
        # 'completion_frac': [1, 1, 1, 1, 1, 0.95, 0.7, 0.35, 0.1, 0, 0, 0]})
        print(df)
        # df['Duration'] = df['end'] - df['start']
        fig, ax = plt.subplots()
        plt.barh(y=df['Process'], width=df['Duration'], left=df['time'])
        plt.gca().invert_yaxis()
        xticks = np.arange(0, max_completion_time + 2, 1)
        ax.set_xticks(xticks)
        ax.xaxis.grid(True, alpha=0.5)
        plt.ylabel("Process ")
        plt.xlabel("Time")
        plt.show()

RR = RoundRobin()
RR.processData(3)