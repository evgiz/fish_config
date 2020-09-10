
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
        (167, 2),
        (152, 2),
        # Spotlight
        (80, 2),
        # Settings
        (58, 2),
        # Notifications
        (40, 2)
    ],

    "ios-marketing": [
        (1024, 1)
    ]
}

if __name__ == "__main__":

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
    os.mkdir("./AppIcon.appiconset")

    print("Generating images...")

    for idiom in CONFIG:
        for pixels, scale in CONFIG[idiom]:

            name = pixels + ".png"
            if name in created:
                continue
            created.append(name)

            img = source.resize((size, size), Image.BICUBIC)
            img.save("./AppIcon.appiconset/" + name)

            images.append(
                {
                    "size":  pixels/scale,
                    "idiom": idiom,
                    "filename": name,
                    "scale": scale + "x"
                }
            )
        print(idiom, "OK")

    with open("./AppIcon.appiconset/Contents.json") as f:
        json.dumps(
            {
                "images": images,
                "info": {
                    "version": 1,
                    "author": "python-generator"
                }
            }
        )

    print("Complete!")