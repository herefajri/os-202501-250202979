import time

print("--- Memulai Tes Resource Docker ---")
memory_hog = []

try:
    while True:
        for i in range(1000000):
            _ = i * i
        if len(memory_hog) < 100:
            memory_hog.append(' ' * 10**6)
        print(f"Berjalan... Memori: ~{len(memory_hog)}MB")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nSelesai.")