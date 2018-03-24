import sys
import dlib
from skimage import io

# Take the filename from the CLI
file_name = sys.argv[1]

# Create a HOG face detector using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()

window = dlib.image_window()

# Load image into array
image = io.imread(file_name)

# Run detector on image data
# Should result in a bounding box area if face is detected

detected_faces = face_detector(image, 1)

print("I found {} faces in the file {}".format(len(detected_faces), file_name))

# Open a window showing the detected face image
window.set_image(image)

# Loop through faces found in our image
for i, face_rect in enumerate(detected_faces):
    window.add_overlay(face_rect)

# Wait until the user hits <enter> to continue
dlib.hit_enter_to_continue()
