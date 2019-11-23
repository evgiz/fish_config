
# Quickly open subject folder from terminal

import sys, os

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

if __name__ == "__main__":

    home_path = os.path.expanduser('~')
    stud_path = os.path.join(home_path, "Studies")

    if len(sys.argv) < 2:
        query = None
    else:
        query = sys.argv[1].lower()

    subjects = os.listdir(stud_path)
    keys = {}
    subject_meta = {}

    for subject in subjects:
       
        subject_path = os.path.join(stud_path, subject)
        if not os.path.isdir(subject_path):
            continue
        
        subject = subject.lower()
        keys[subject] = subject_path
        subject_meta[subject] = []

        if "-" in subject:
            keys[subject.split("-")[1]] = subject_path

        meta_path = os.path.join(subject_path, ".meta")
        if not os.path.exists(meta_path):
            continue

        with open(meta_path, "r") as meta:
            lines = meta.readlines()
            for k in lines:
                meta_key = k.strip().lower()
                keys[meta_key] = subject_path
                subject_meta[subject].append(meta_key)

    if query is None:
            for sub in sorted(subject_meta):
                print(OKGREEN, sub.upper(), "\t", WARNING, *subject_meta[sub])
    else:
        if query in keys:
            print(keys[query], end="")
        else:
            print(stud_path, end="")
        sys.stdout.flush()
        exit(0)
