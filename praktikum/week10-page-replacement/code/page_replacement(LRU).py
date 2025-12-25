import os

def load_reference_string(filename):
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, filename)
    
    try:
        with open(full_path, "r") as f:
            content = f.read().strip()
            content = content.replace(',', ' ')
            return list(map(int, content.split()))
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        return []

def lru_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0
    page_hits = 0
    total_requests = len(pages)

    print(f"=== SIMULASI LRU PAGE REPLACEMENT ===")
    print(f"Reference String : {pages}")
    print(f"Jumlah Frame     : {frame_count}\n")
    print(f"{'Step':<5} | {'Akses':<6} | {'Status':<7} | {'Frames (Urutan LRU)'}")
    print("-" * 55)

    for i, page in enumerate(pages):
        status = ""
        if page not in frames:
            page_faults += 1
            status = "FAULT"
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
        else:
            page_hits += 1
            status = "HIT"
            frames.remove(page)
            frames.append(page)

        print(f"{i+1:<5} | {page:<6} | {status:<7} | {str(frames)}")

    hit_rate = (page_hits / total_requests) * 100
    fault_rate = (page_faults / total_requests) * 100

    print("-" * 55)
    print(f"HASIL AKHIR (LRU):")
    print(f"Total Page Hits  : {page_hits}")
    print(f"Total Page Faults: {page_faults}")
    print("-" * 55)

if __name__ == "__main__":
    data = load_reference_string("reference_string.txt")
    if data:
        lru_page_replacement(data, frame_count=3)