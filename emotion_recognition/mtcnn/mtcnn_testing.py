import mtcnn
import matplotlib.pyplot as plt

file = "../test_images/sad.jpg"
pixels = plt.imread(file)
detector = mtcnn.MTCNN()
faces = detector.detect_faces(pixels)

# draw an image with detected objects
def draw_facebox(filename, result_list):
    data = plt.imread(filename)
    plt.imshow(data)
    ax = plt.gca()
    for result in result_list:
        x, y, width, height = result['box']
        rect = plt.Rectangle((x, y), width, height, fill=False, color='orange')
        ax.add_patch(rect)
    plt.show()


draw_facebox(file, faces)
