import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from Assignment.Prioiry import Priority
from Assignment.RR import RoundRobin
from Assignment.SJF import SJF

# class SJF:
#
#     def processData(self, no_of_processes):
#         process_data = []
#         for i in range(no_of_processes):
#             temporary = []
#             process_id = int(input("Enter Process ID: "))
#
#             arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))
#
#             burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
#
#             temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
#             '''
#             '0' is the state of the process. 0 means not executed and 1 means execution complete
#             '''
#             process_data.append(temporary)
#         SJF.schedulingProcess(self, process_data)
#
#     def schedulingProcess(self, process_data):
#         start_time = []
#         exit_time = []
#         s_time = 0
#         sequence_of_process = []
#         process_data.sort(key=lambda x: x[1])
#         '''
#         Sort processes according to the Arrival Time
#         '''
#         while 1:
#             ready_queue = []
#             normal_queue = []
#             temp = []
#             for i in range(len(process_data)):
#                 if process_data[i][1] <= s_time and process_data[i][3] == 0:
#                     temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
#                     ready_queue.append(temp)
#                     temp = []
#                 elif process_data[i][3] == 0:
#                     temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
#                     normal_queue.append(temp)
#                     temp = []
#             if len(ready_queue) == 0 and len(normal_queue) == 0:
#                 break
#             if len(ready_queue) != 0:
#                 ready_queue.sort(key=lambda x: x[2])
#                 '''
#                 Sort processes according to Burst Time
#                 '''
#                 start_time.append(s_time)
#                 s_time = s_time + 1
#                 e_time = s_time
#                 exit_time.append(e_time)
#                 sequence_of_process.append(ready_queue[0][0])
#                 for k in range(len(process_data)):
#                     if process_data[k][0] == ready_queue[0][0]:
#                         break
#                 process_data[k][2] = process_data[k][2] - 1
#                 if process_data[k][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
#                     process_data[k][3] = 1
#                     process_data[k].append(e_time)
#             if len(ready_queue) == 0:
#                 if s_time < normal_queue[0][1]:
#                     s_time = normal_queue[0][1]
#                 start_time.append(s_time)
#                 s_time = s_time + 1
#                 e_time = s_time
#                 exit_time.append(e_time)
#                 sequence_of_process.append(normal_queue[0][0])
#                 for k in range(len(process_data)):
#                     if process_data[k][0] == normal_queue[0][0]:
#                         break
#                 process_data[k][2] = process_data[k][2] - 1
#                 if process_data[k][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
#                     process_data[k][3] = 1
#                     process_data[k].append(e_time)

process = []
time = 0
while (True):
    process = []
    a = int(input("Press 1 for FCFS Algorithm \nPress 2 for SJF Algorithm \nPress 3 for Priority Algorithm \nPress 4 "
                  "for Round Robin Algorithm"))

    if a == 1:

        n = int(input("how many process are there ?"))
        for i in range(n):
            AT = int(input(f"enter Arrival time for {i + 1} : "))
            BT = int(input(f"enter Burst time for {i + 1} : "))
            p = [i + 1, AT, BT]
            process.append(p)

        for i in range(len(process) - 1):
            for j in range(len(process) - 1):
                if process[j][1] > process[j + 1][1]:
                    a = process[j][1]
                    process[j][1] = process[j + 1][1]
                    process[j + 1][1] = a

        print(process)
        START = []
        time = 0
        END = []
        for i in range(len(process)):
            START.append(time)
            time += process[i][2]
            END.append(time)

        # for i in range(len(process) - 1):
        #     for j in range(len(process) - 1):
        #         if process[j][1] > process[j + 1][1]:
        #             a = process[j][1]
        #             process[j][1] = process[j + 1][1]
        #             process[j + 1][1] = a
        #
        # print(process)

        df = pd.DataFrame({'Process': [process[_][0] for _ in range(len(process))],
                           # 'team': ['R&D', 'Accounting', 'Sales', 'Sales', 'IT', 'R&D', 'IT', 'Sales',
                           # 'Accounting', 'Accounting', 'Sales', 'IT'], 'start': pd.to_datetime(['20 Oct 2022',
                           # '24 Oct 2022', '26 Oct 2022', '31 Oct 2022', '3 Nov 2022', '7 Nov 2022', '10 Nov 2022',
                           # '14 Nov 2022', '18 Nov 2022', '23 Nov 2022', '28 Nov 2022', '30 Nov 2022']),
                           # 'end': pd.to_datetime(['31 Oct 2022', '28 Oct 2022', '31 Oct 2022', '8 Nov 2022',
                           # '9 Nov 2022', '18 Nov 2022', '17 Nov 2022', '22 Nov 2022', '23 Nov 2022', '1 Dec 2022',
                           # '5 Dec 2022', '5 Dec 2022']),
                           'start': START,
                           'end': END})
        # 'completion_frac': [1, 1, 1, 1, 1, 0.95, 0.7, 0.35, 0.1, 0, 0, 0]})
        print(df)
        df['Duration'] = df['end'] - df['start']
        fig, ax = plt.subplots()
        plt.barh(y=df['Process'], width=df['Duration'], left=df['start'])
        plt.gca().invert_yaxis()
        xticks = np.arange(0, df['end'].max() + 2, 1)
        ax.set_xticks(xticks)
        ax.xaxis.grid(True, alpha=0.5)
        plt.ylabel("Process ")
        plt.xlabel("Time")
        plt.show()



    elif a == 2:
        n = int(input("how many process are there ?"))
        sjf = SJF()
        sjf.processData(n)
    elif (a == 3):
        n = int(input("how many process are there ?"))
        priority = Priority()
        priority.processData(n)

    elif (a == 4):
        n = int(input("how many process are there ?"))
        RR = RoundRobin()
        RR.processData(n)
    else:
        print("you entered an invalid input")

    choice = input("do you want to run any other algorithms : ? Y/N")
    if choice == 'N' or choice == 'n':
        break


