import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from Assignment.Prioiry import Priority
from Assignment.SJF import SJF
from Assignment.RR import RoundRobin

process = []
time = 0
while True:
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
    elif a == 3:
        n = int(input("how many process are there ?"))
        priority = Priority()
        priority.processData(n)
    elif a == 4:
        n = int(input("how many process are there ?"))
        RR = RoundRobin()
        RR.processdata(n)
    else:
        print("you entered an invalid input")

    choice = input("do you want to run any other algorithms : ? Y/N")
    if choice == 'N' or choice == 'n':
        break
