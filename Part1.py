import matplotlib.pyplot as plt
import pandas as pd


def line_chart_for_total_steps(path):
    df  = pd.read_csv(path)

    print(df.dtypes)

    list1 = df['TotalSteps'].values.tolist()
    list2 = df['ActivityDate'].values.tolist()
    
    date = []
    addition = []
    
    for i in range(len(list2)):
        s = 0
        select = list2[i]
        if date.__contains__(select) == False:
            date.append(select)
        else:
            continue
        for j in range(len(list2)):
            if select == list2[j]:
                s = s + list1[j]
        addition.append(s)
    
    plt.title('Part 1')
    plt.plot(date, addition)
    plt.xlabel('Dates')  # Add an x-label to the axes.
    plt.ylabel('Total Steps')  # Add a y-label to the axes.
    plt.xticks(rotation = 90)

    plt.show()
    
    
def bar_chart_for_daily_distance(path):
    df  = pd.read_csv(path)

    print(df.dtypes)

    list1 = df['TotalDistance'].values.tolist()
    list2 = df['ActivityDate'].values.tolist()
    
    date = []
    addition = []
    
    for i in range(len(list2)):
        s = 0
        select = list2[i]
        if date.__contains__(select) == False:
            date.append(select)
        else:
            continue
        for j in range(len(list2)):
            if select == list2[j]:
                s = s + list1[j]
        addition.append(s)
    
    plt.title('Part 1')
    plt.bar(date, addition)
    plt.xlabel('Dates')  # Add an x-label to the axes.
    plt.ylabel('Total Distance')  # Add a y-label to the axes.
    plt.xticks(rotation = 90)

    plt.show()
    
def scatter_chart_for_time_in_bed(path):
    df  = pd.read_csv(path)

    print(df.dtypes)

    list1 = df['TotalTimeInBed'].values.tolist()
    list2 = df['SleepDay'].values.tolist()
    
    date = []
    addition = []
    
    for i in range(len(list2)):
        s = 0
        select = list2[i]
        if date.__contains__(select) == False:
            date.append(select)
        else:
            continue
        for j in range(len(list2)):
            if select == list2[j]:
                s = s + list1[j]
        addition.append(s)
    
    print(date)
    
    plt.title('Part 1')
    plt.scatter(date, addition)
    plt.xlabel('Dates')  # Add an x-label to the axes.
    plt.ylabel('Total Sleep Time')  # Add a y-label to the axes.
    plt.xticks(rotation = 90)

    plt.show()
    
def pie_chart_for_hourly_steps(path):
    df  = pd.read_csv(path)

    print(df.dtypes)

    list1 = df['ActivityHour'].values.tolist()
    list2 = df['StepTotal'].values.tolist()
    
    #print(list1)
    
    date = []
    addition = []
    
    k = 0
    
    for i in range(24):
        s = 0
        if i < 12:
            select = "4/12/2016 " + str(i+1) + ":00:00 " + "AM"
        else:
            select = "4/12/2016 " + str(i-11) + ":00:00 " + "PM"
            k += 1
        for j in range(len(list1)):
            if select == list1[j]:
                s = s + list2[j]
        addition.append(s)
        date.append(select)
    
    print(date)
    print(addition)
    
    plt.title('Part 1')
    plt.pie(addition, labels = date)
    #plt.xticks(rotation = 90)

    plt.show()
    
path1 = "dailyActivity_merged.csv"
path2 = "sleepDay_merged.csv"
path3 = "hourlySteps_merged.csv"

line_chart_for_total_steps(path1)
#bar_chart_for_daily_distance(path1)
#scatter_chart_for_time_in_bed(path2)
#pie_chart_for_hourly_steps(path3)
