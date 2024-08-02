from PIL import Image
import threading
from queue import Queue

def getRGB(i, pix, size, queue):
    out = ""
    for j in range(size[1]):
        r, g, b = pix[i, j]
        hex_color = '%02x%02x%02x' % (r, g, b)
        out += f"{hex_color}"
    queue.put(out)

def generator(img):
    try:
        im = Image.open(img)
        pix = im.load()
        size = im.size

        queue = Queue()
        threads = []
        num_threads = size[0]

        for i in range(num_threads):
            t = threading.Thread(target=getRGB, args=(i, pix, size, queue))
            threads.append(t)
            t.start()

        for th in threads:
            th.join()

        with open(str(img.split(".")[0]) + ".key", "w") as file:
            while not queue.empty():
                out = queue.get()
                file.write(out)
    except:
        raise
