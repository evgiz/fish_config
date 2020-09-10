
import sys, os
from PIL import Image
import json

# Idiom: (pixels, scale)
CONFIG = {
   
    "iphone": [
         # Icons
        (180, 3),
        (120, 2),
        # Spotlight
        (120, 3),
        (80, 2),
        # Settings
        (87, 3),
        (58, 2),
        # Notifications
        (60, 3),
        (40, 2)
    ],

    "ipad": [
        # Icons
        (76, 1),
        (152, 2),
        (167, 2),
        # Spotlight
        (40, 1),
        (80, 2),
        # Settings
        (29, 1),
        (58, 2),
        # Notifications
        (20, 1),
        (40, 2)
    ],

    "ios-marketing": [
        (1024, 1)
    ]
}

def generate():
    if len(sys.argv) != 2 or sys.argv[1].lower() == "-h":
        print("Usage: ios_icon_gen.py <path>")
        return

    created = []

    try:
        source = Image.open(sys.argv[1])
    except IOError:
        print("Failed to find image")
        return


    images = []

    try:
        os.mkdir("./AppIcon.appiconset")
    except FileExistsError:
        print("Directory already exists, replacing images.")

    print("Generating images...")

    for idiom in CONFIG:
        for pixels, scale in CONFIG[idiom]:

            name = str(pixels) + ".png"

            if name not in created:
                img = source.resize((pixels, pixels), Image.BICUBIC)
                img.save("./AppIcon.appiconset/" + name)

            size = pixels/scale
            size = int(size) if int(size) == size else size

            images.append(
                {
                    "size":  "{}x{}".format(size, size),
                    "expected-size": str(pixels),
                    "idiom": idiom,
                    "filename": name,
                    "scale": str(scale) + "x"
                }
            )
        print(idiom, "OK")

    with open("./AppIcon.appiconset/Contents.json", "w") as f:
        f.write(
            json.dumps(
                {
                    "images": images,
                    "info": {
                        "version": 1,
                        "author": "python-generator"
                    }
                },
                indent = 4
            )
        )

    print("Complete!")



if __name__ == "__main__":
    generate()
