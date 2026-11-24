import os

LINE = (
    "I bought a standing desk and a fitness tracker to fix my life; "
    "tonight I ate an entire cake standing at the open fridge, lights off, "
    "like a raccoon with a mortgage."
)


def main():
    # One-line limit for this competition is 200 characters (v2: first-person, turn last).
    assert 1 <= len(LINE.strip()) <= 200, len(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
