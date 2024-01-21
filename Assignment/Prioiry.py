import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
class Priority:

    def processData(self, proc):
        Process = []
        for i in range(proc):
            p = []
            id = i+1
            AT = int(input(f"Enter Arrival Time for Process {id}: "))
            BT = int(input(f"Enter Burst Time for Process {id}: "))
            priority = int(input(f"Enter Priority for Process {id}: "))
            p.extend([id, AT, BT, priority, 0, BT])
            Process.append(p)
        Priority.schedulingProcess(self, Process)

    def schedulingProcess(self, Process):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        Process.sort(key=lambda x: x[1])
        # for i in range(len(Process) - 1):
        #     for j in range(len(Process) - 1):
        #         if Process[j][1] > Process[j + 1][1]:
        #             a = Process[j][1]
        #             Process[j][1] = Process[j + 1][1]
        #             Process[j + 1][1] = a
        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(Process)):
                if Process[i][1] <= s_time and Process[i][4] == 0:
                    temp.extend([Process[i][0], Process[i][1], Process[i][2], Process[i][3], Process[i][5]])
                    ready_queue.append(temp)
                    temp = []
                elif Process[i][4] == 0:
                    temp.extend([Process[i][0], Process[i][1], Process[i][2], Process[i][4], Process[i][5]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3], reverse=True)
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(Process)):
                    if Process[k][0] == ready_queue[0][0]:
                        break
                Process[k][2] = Process[k][2] - 1
                if Process[k][2] == 0:
                    Process[k][4] = 1
                    Process[k].append(e_time)
            if len(ready_queue) == 0:
                normal_queue.sort(key=lambda x: x[1])
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(Process)):
                    if Process[k][0] == normal_queue[0][0]:
                        break
                Process[k][2] = Process[k][2] - 1
                if Process[k][2] == 0:
                    Process[k][4] = 1
                    Process[k].append(e_time)

        t_time = Priority.calculateTurnaroundTime(self, Process)
        w_time = Priority.calculateWaitingTime(self, Process)
        Priority.printData(self, Process, t_time, w_time, sequence_of_process)

    def calculateTurnaroundTime(self, Process):
        total_turnaround_time = 0
        for i in range(len(Process)):
            turnaround_time = Process[i][6] - Process[i][5]
            total_turnaround_time = total_turnaround_time + turnaround_time
            Process[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(Process)
        return average_turnaround_time

    def calculateWaitingTime(self, Process):
        total_waiting_time = 0
        for i in range(len(Process)):
            waiting_time = Process[i][6] - Process[i][2]
            total_waiting_time = total_waiting_time + waiting_time
            Process[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(Process)
        return average_waiting_time

    def printData(self, Process, average_turnaround_time, average_waiting_time, sequence_of_process):

        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print(f'Sequence of Process: {sequence_of_process}')


        result = []
        count = 0
        current = sequence_of_process[0]
        time=0
        start=[Process[0][1]]

        for i in range(len(sequence_of_process)):
            if sequence_of_process[i] == current:
                count += 1
                time+=1
            else:
                result.append([current, count])
                count = 1
                start.append(time)
                time+=1
            current = sequence_of_process[i]

        result.append([current, count])
        print(result)
        print(start)
        print(Process)
        max_completion_time = max(Process, key=lambda x: x[5])[5]
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

if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    priority = Priority()
    priority.processData(n)