import csv
import os
from pathlib import Path

import numpy as np

from results.results import results_prep_dir


def ensure_dir_creation(filepath):
    directory = os.path.dirname(filepath)
    Path(directory).mkdir(parents=True, exist_ok=True)


def save_csv_plot(results, filename, fieldnames=None):
    if fieldnames is None:
        fieldnames = ['Potential [V]', 'Current [uA]']
    ensure_dir_creation(filename)
    with open(filename, 'w', newline='\n') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(fieldnames)
        for i in range(0, np.size(results, axis=1)):
            writer.writerow([results[0][i], results[1][i]])


def load_csv_plot(filename, header_count=1):
    results = []
    with open(filename, 'r', newline='\n') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count >= header_count:
                results.append([float(row[0]), float(row[1])])
            line_count = line_count + 1
    return np.transpose(np.array(results))


def save_csv_table(results, filename, fieldnames=None):
    ensure_dir_creation(filename)
    with open(filename, 'w', newline='\n') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if fieldnames is None:
            pass
        else:
            writer.writerow(fieldnames)
        for i in range(0, np.size(results, axis=0)):
            writer.writerow(results[i][:])


def load_csv_table(filename, header_count=0):
    results = []
    with open(filename, 'r', newline='\n') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count >= header_count:
                results.append([float(row[0]), float(row[1])])
            line_count = line_count + 1
    return np.array(results)


def save_csv_dict(results, filename, fieldnames=None):
    ensure_dir_creation(filename)
    with open(filename, 'w', newline='\n') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if fieldnames is None:
            pass
        else:
            writer.writerow(fieldnames)
        for k, v in results.items():
            writer.writerow([k, v])


def load_csv_dict(filename, header_count=0):
    results = {}
    with open(filename, 'r', newline='\n') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count >= header_count:
                results[row[0]] = row[1]
                line_count = line_count + 1
    return np.array(results)


def write_to_file(filename, string):
    with open(filename, "w") as f:
        f.write(string)


def load_prepared_samples(suite_name):
    return {
        "unmodified": load_csv_plot(f"{results_prep_dir}/{suite_name}/{suite_name}_raw"),
        "signal": load_csv_plot(f"{results_prep_dir}/{suite_name}/{suite_name}_0"),
        "baseline": load_csv_plot(f"{results_prep_dir}/{suite_name}/{suite_name}_baseline"),
        "noise": load_csv_plot(f"{results_prep_dir}/{suite_name}/{suite_name}_noise"),
    }
