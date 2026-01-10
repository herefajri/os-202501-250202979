import os
import csv

filename = os.path.join(os.path.dirname(__file__), "dataset.csv")

if not os.path.exists(filename):
    print(f"File '{filename}' tidak ditemukan.")
    exit()

def read_csv(filename):
    processes = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            processes.append({
                'pid': row['PID'],
                'arrival': int(row['Arrival']),
                'burst': int(row['Burst'])
            })
    return processes

def fcfs(processes):
    processes.sort(key=lambda x: x['arrival'])
    time = 0
    for p in processes:
        p['start'] = max(time, p['arrival'])
        p['finish'] = p['start'] + p['burst']
        p['waiting'] = p['start'] - p['arrival']
        p['turnaround'] = p['finish'] - p['arrival']
        time = p['finish']
    return processes

def print_result(processes):
    print("PID\tArrival\tBurst\tStart\tFinish\tWaiting\tTurnaround")
    for p in processes:
        print(f"{p['pid']}\t{p['arrival']}\t{p['burst']}\t{p['start']}\t{p['finish']}\t{p['waiting']}\t{p['turnaround']}") 
              
        
if __name__ == "__main__": 
    processes = read_csv(filename) 
    result = fcfs(processes) 
    print_result(result)