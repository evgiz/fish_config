
# [path] [query] [pingpong]

import sys, os
import imageio

if __name__ == "__main__":

	path = os.getcwd()
	if len(sys.argv) > 1:
		path = sys.argv[1]
	output = os.path.join(path, "new_gif.gif")
	pingpong = False
	query = None
		
	if len(sys.argv) > 2:
		query = sys.argv[2]
	if len(sys.argv) > 3:
		if sys.argv[3] in ["0", "n", "no", "false"]:
			pingpong = False
		else:
			pingpong = True
		
	if not os.path.isdir(path):
		print("Directory", path, "not found")
		exit(-1)
	
	images = []
	filenames = sorted(os.listdir(path))
	
	os.chdir(path)
	files = filter(os.path.isfile, os.listdir(path))
	files = [os.path.join(path, f) for f in files] # add path to each file
	files.sort(key=lambda x: os.path.getmtime(x))
	
	for filename in files:
		if query is None or query in files:
			if filename.endswith(".png") or filename.endswith(".jpg"):
				images.append(imageio.imread(filename))
	if pingpong:
		r = len(images)
		for i in range(r):
			images.append(images[r-i-1])
	if len(images) > 0:
		print("Creating gif...")
		imageio.mimsave(output, images, duration=0.0001)
		print("Done!")
	else:
		print("No images found at", path)