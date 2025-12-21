def fifo_page_replacement(reference_string, frame_count):
    frames = []
    page_faults = 0
    hits = 0
    pointer = 0  

    print("Reference String:", reference_string)
    print("Jumlah Frame:", frame_count)
    print("\nStep | Page | Frame State | Hit/Fault")

    for step, page in enumerate(reference_string, start=1):
        if page in frames:
            hits += 1
            status = "Hit"
        else:
            page_faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % frame_count
            status = "Fault"

        print(f"{step:>4} | {page:>4} | {frames} | {status}")

    print("\nTotal Hits:", hits)
    print("Total Page Faults:", page_faults)


reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_count = 3

fifo_page_replacement(reference_string, frame_count)
