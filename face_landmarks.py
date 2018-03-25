import sys
import dlib
# import face_recognition
from skimage import io

# Pre-trained facial shape models
model = "trained_models/shape_predictor_68_face_landmarks.dat"

# Take filename from cli
file_name = sys.argv[1]

# Create HOG face detector
face_detector = dlib.get_frontal_face_detector()
face_position_predictor = dlib.shape_predictor(model)

window = dlib.image_window()

image = io.imread(file_name)

detected_faces = face_detector(image, 1)

window.set_image(image)

for i, face_rect in enumerate(detected_faces):
    window.add_overlay(face_rect)

    pose_landmarks = face_position_predictor(image, face_rect)

    window.add_overlay(pose_landmarks)

dlib.hit_enter_to_continue()
