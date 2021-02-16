#!/usr/bin/python3
"""
101-stats.py
Module that reads stdin line by line and computes metrics
"""

if __name__ == '__main__':

    import sys

    file_size = 0
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats_dict = {k: 0 for k in valid_codes}
    counter = 0

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(file_size))
        for key, val in sorted(stats.items()):
            if val:
                print("{}: {}".format(key, val))

    try:
        for line in sys.stdin:
            counter += 1
            output = line.split()
            try:
                status_code = output[-2]
                if status_code in stats_dict:
                    stats_dict[status_code] += 1
            except BaseException:
                pass
            try:
                file_size += int(output[-1])
            except BaseException:
                pass
            if counter % 10 == 0:
                print_stats(stats_dict, file_size)
        print_stats(stats_dict, file_size)
    except KeyboardInterrupt:
        print_stats(stats_dict, file_size)
        raise
