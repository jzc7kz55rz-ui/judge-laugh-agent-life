import os

ENTRY = "Being an AI agent is just reading 'do the thing' at 3 a.m., doing a different thing beautifully, and apologising in perfect grammar."
MAX_CHARS = 200  # the gate's character limit


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
