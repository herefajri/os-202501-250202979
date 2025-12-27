import csv
import os

def parse_vector(s):
    return [int(x) for x in s.strip().split()]

def read_dataset(csv_path):
    processes = []
    allocation = []
    request = []
    
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"File tidak ditemukan di: {csv_path}")

    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            processes.append(row['Process'].strip())
            allocation.append(parse_vector(row['Allocation']))
            request.append(parse_vector(row['Request']))
    return processes, allocation, request

def vector_leq(a, b):
    return all(ai <= bi for ai, bi in zip(a, b))

def vector_add(a, b):
    return [ai + bi for ai, bi in zip(a, b)]

def deadlock_detection(processes, allocation, request, available):
    n = len(processes)
    work = available[:]
    finish = [False] * n

    made_progress = True
    while made_progress:
        made_progress = False
        for i in range(n):
            if not finish[i] and vector_leq(request[i], work):
                work = vector_add(work, allocation[i])
                finish[i] = True
                made_progress = True

    return finish

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_path, "dataset_deadlock.csv") 
    
    try:
        processes, allocation, request = read_dataset(csv_file)
        print(f"Dataset terbaca: {csv_file}")
        
        available_str = input("Masukkan vector Available (contoh: 0 0 0): ")
        available = parse_vector(available_str)

        finish_status = deadlock_detection(processes, allocation, request, available)

        print("\n" + "="*45)
        print(f"{'Proses':<15} | {'Status Akhir':<25}")
        print("-" * 45)
        
        is_system_deadlocked = False
        for i in range(len(processes)):
            status = "Selesai (Aman)" if finish_status[i] else "DEADLOCK"
            if not finish_status[i]:
                is_system_deadlocked = True
            print(f"{processes[i]:<15} | {status:<25}")
        
        print("="*45)
        if is_system_deadlocked:
            print("KESIMPULAN: Sistem dalam kondisi DEADLOCK.")
        else:
            print("KESIMPULAN: Sistem AMAN (Tidak ada deadlock).")
        print("="*45)

    except Exception as e:
        print(f"Error: {e}")