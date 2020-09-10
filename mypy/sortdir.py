

# Sorts directory by category

# Used to sort downloads folder automatically

import os, sys
import shutil

CATEGORIES = {
    "images": ["png", "jpg", "jpeg", "heic", "ico"],
    "gifs": ["gif"],
    "zips": ["zip", "tar", "gz", "bz2", "tbz2"],
    "pdfs": ["pdf"],
    "audio": ["wav", "mp3", "aiff"],
    "dmgs": ["dmg"],
    "office": ["docx", "pptx", "xlsx", "xlsm", "doc", "ppt", "xls", "dotx"],
    "java": ["jar", "java"],
    "text": ["txt", "csv", "log", "tex", "html", "md", "xml"],
    "fonts": ["ttf", "otf"],
    "apps": ["app"],
    "script": ["py", "lua", "sql", "js", "fish"]
}

MAX_RECENT_FILES = 15
recent_files = []

# Paths
path = os.getcwd()
recent_path = os.path.join(path, "recent")
recent_file_path = os.path.join(path, ".recent")
all_path = os.path.join(path, "all")

def load_recent_files():
    global recent_files
    # Create .recent file
    if not os.path.exists(recent_file_path):
        with open(recent_file_path, "w") as f:
            pass
    # Load recent files
    if os.path.exists(".recent"):
        with open(recent_file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                # Assert file still exists
                if os.path.exists(os.path.join(path, line.strip())):
                    recent_files.append(line.strip())

def get_category(filename):
    _, ext = os.path.splitext(filename)
    ext = ext[1:].lower()
    for cat in CATEGORIES:
        if ext in CATEGORIES[cat]:
            return cat
    if os.path.isdir(os.path.join(path, filename)):
        return "directories"
    return "other"

def move_file(filename):
    cat = get_category(filename)

    # Make category dir if not exists
    cat_path = os.path.join(all_path, cat)
    if not os.path.exists(cat_path):
        os.mkdir(cat_path)
   
    # Filename split
    fn, ext = os.path.splitext(filename)
    
    # Dodge duplicates
    move_name = filename
    move_path = os.path.join(cat_path, filename)
    number = 2
    while os.path.exists(move_path):
        move_name = fn+"_"+str(number)+ext
        move_path = os.path.join(cat_path, move_name)
        number += 1
    if move_name != filename:
        os.rename(filename, move_name)
        
    # Move file
    shutil.move(move_name, move_path)

def scan_root():
    global recent_files

    files = os.listdir(path)
    new_files = [f for f in files if f not in recent_files]

    for filename in new_files:
        fn, ext = os.path.splitext(filename)
        ext = ext[1:].lower()

        # Ignore meta or downloads
        if fn in ["all", ".recent", ".DS_Store"] or ext in ["download", "part"]:
            continue
        
        # Check if new file
        print(f"Detected new file '{filename}', current recent = {len(recent_files)}")
        # Remove oldest file in max limit
        if len(recent_files) == MAX_RECENT_FILES:
            oldest = recent_files.pop(0)
            move_file(oldest)
            print(f" ... moved oldest file {oldest}, now {len(recent_files)} remain")
        # Add new file
        recent_files.append(filename)
    
    # Write recents file
    print("\n .recent")
    with open(recent_file_path, "w") as f:
        for r in recent_files:
            f.write(r+"\n")
            print(f" {r}")

if __name__ == "__main__":

    if len(sys.argv) < 2 or sys.argv[1] != "skip":
        if input("Are you sure? [y/n]") not in ["Y","y"]:
            print("Aborted")
            exit(-1)   

    # Create directories
    if not os.path.exists(all_path):
        os.mkdir(all_path)

    load_recent_files()
    scan_root()

    print("Done")