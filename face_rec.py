import face_recognition

# Get our base image
known_face = face_recognition.load_image_file("/home/cian/Pictures/faces/cian-gallagher.jpg")
unknown_face = face_recognition.load_image_file("/home/cian/Pictures/faces/social/cian_twitter.png")

cian_encoding = face_recognition.face_encodings(known_face)[0]
unknown_encoding = face_recognition.face_encodings(unknown_face)[0]

results = face_recognition.compare_faces([cian_encoding], unknown_encoding)
print(results)
