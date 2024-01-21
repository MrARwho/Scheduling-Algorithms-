import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
class SJF:
    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            AT = int(input(f"enter Arrival time for {i + 1} : "))
            BT = int(input(f"enter Burst time for {i + 1} : "))
            p = [i + 1, AT, BT, 0, BT]

        # for i in range(no_of_processes):
        #     temporary = []
        #     process_id = int(input("Enter Process ID: "))
        #
        #     arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))
        #
        #     burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
        #
        #     temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
        #     '''
        #     '0' is the state of the process. 0 means not executed and 1 means execution complete
        #     '''
            process_data.append(p)
        SJF.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key=lambda x: x[1])
        # for i in range(len(process_data) - 1):
        #     for j in range(len(process_data) - 1):
        #         if process_data[j][1] > process_data[j + 1][1]:
        #             a = process_data[j][1]
        #             process_data[j][1] = process_data[j + 1][1]
        #             process_data[j + 1][1] = a

        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                # for i in range(len(ready_queue) - 1):
                #     for j in range(len(ready_queue) - 1):
                #         if ready_queue[j][2] > ready_queue[j + 1][2]:
                #             a = ready_queue[j][2]
                #             ready_queue[j][2] = ready_queue[j + 1][2]
                #             ready_queue[j + 1][2] = a

                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
            if len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
        t_time = SJF.calculateTurnaroundTime(self, process_data)
        w_time = SJF.calculateWaitingTime(self, process_data)
        print("seq : " , sequence_of_process)
        SJF.printData(self, process_data, t_time, w_time, sequence_of_process)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            '''
            turnaround_time = completion_time - arrival_time
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        average_turnaround_time = total_turnaround_time / no_of_processes
        '''
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        '''
        average_waiting_time = total_waiting_time / no_of_processes
        '''
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_process):
        process_data.sort(key=lambda x: x[0])

        print("Process_ID  Turnaround_Time  Waiting_Time")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):

                print(process_data[i][j], end="\t\t")
            print()

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')

        print(f'Sequence of Process: {sequence_of_process}')
        #

        result = []
        count = 0
        current = sequence_of_process[0]
        time = process_data[0][1]
        start = [process_data[0][1]]

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
                           # 'end': [process_data[_][5] for _ in range(len(process_data))],
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
    no_of_processes = int(input("Enter number of processes: "))
    sjf = SJF()
    sjf.processData(no_of_processes)