#!/usr/bin/env python3
import shutil


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(lst)
    cols = shutil.get_terminal_size().columns

    text_buffer = len(str(total)) * 2 + 10
    bar_total_len = cols - text_buffer

    if bar_total_len < 10:
        bar_total_len = 10

    for i, item in enumerate(lst):
        progress = i + 1
        percent = int((progress / total) * 100)

        filled_len = int(bar_total_len * progress // total)

        if filled_len < bar_total_len:
            bar = '=' * filled_len + '>'
        else:
            bar = '=' * filled_len

        # Construct the line
        info = f"{percent}%|[{bar:<{bar_total_len + 1}}]| {progress}/{total}"
        print(f"{info}", end="\r", flush=True)

        yield item

    print()
