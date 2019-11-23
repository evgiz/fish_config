

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

if __name__ == "__main__":

    path = os.getcwd()
    files = os.listdir(path)
    
    if len(sys.argv) < 2 or sys.argv[1] != "skip":
        if input("Are you sure? [y/n]") not in ["Y","y"]:
            print("Aborted")
            exit(-1)   

    results = {"directories": []}
    for c in CATEGORIES:
        results[c] = []

    other = []

    for filename in files:
        fn, ext = os.path.splitext(filename)
        ext = ext[1:].lower()

        if ext == "download":
            continue
        if ext != "app" and os.path.isdir(os.path.join(path, filename)):
            if fn not in CATEGORIES and fn != "other":
                results["directories"].append(filename)
        else:
            ok = False
            for cat in CATEGORIES:
                if ext in CATEGORIES[cat]:
                    results[cat].append(filename)
                    ok = True
                    break
            if not ok:
                other.append(filename)
    
    for cat in results:
        if len(results[cat]) > 0:
            cat_path = os.path.join(path, cat)
            if not os.path.exists(cat_path):
                os.mkdir(cat_path)

            for fname in results[cat]:
                fn, ext = os.path.splitext(fname)
                number = 2
                move_name = fname
                move_path = os.path.join(cat_path, fname)
                while os.path.exists(move_path):
                    move_name = fn+"_"+str(number)+ext
                    move_path = os.path.join(cat_path, move_name)
                    number += 1
                if move_name is not fname:
                    os.rename(fname, move_name)
                shutil.move(move_name, cat_path)

    if len(other) > 0:
        other_path = os.path.join(path, "other")
        if not os.path.exists(other_path):
            os.mkdir(other_path)

        for fname in other:
            fn, ext = os.path.splitext(fname)
            number = 2
            move_name = fname
            move_path = os.path.join(other_path, fname)
            while os.path.exists(move_path):
                move_name = fn+"_"+str(number)+ext
                move_path = os.path.join(other_path, move_name)
                number += 1
            if move_name is not fname:
                os.rename(fname, move_name)
            shutil.move(move_name, other_path)

    print("Done")