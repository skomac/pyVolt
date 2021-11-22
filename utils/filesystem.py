import csv
import os
from pathlib import Path

import numpy as np


def ensure_dir_creation(filepath):
    directory = os.path.dirname(filepath)
    Path(directory).mkdir(parents=True, exist_ok=True)


def save_csv(results, filename, fieldnames=None):
    if fieldnames is None:
        fieldnames = ['Potential [V]', 'Current [uA]']
    ensure_dir_creation(filename)
    with open(filename, 'w', newline='\n') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(fieldnames)
        for i in range(0, np.size(results, axis=1)):
            writer.writerow([results[0][i], results[1][i]])


def load_csv(filename, header_count=1):
    results = []
    with open(filename, 'r', newline='\n') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count >= header_count:
                results.append([float(row[0]), float(row[1])])
            line_count = line_count + 1
    return np.transpose(np.array(results))