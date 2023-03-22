import cv2
import os
from mtcnn import MTCNN

detector = MTCNN(min_face_size=40)

def detect_faces(img, threshold=0.5, min_face_size=(80, 80)):
    detections = detector.detect_faces(img)
    faces = []
    for detection in detections:
        confidence = detection['confidence']
        if confidence >= threshold:
            x, y, width, height = detection['box']
            if width >= min_face_size[1] and height >= min_face_size[0]:
                faces.append((x, y, width, height))
    return faces

def save_cropped_faces(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        # Check if the file is an image (you can add more extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            filename_without_extenstion = os.path.splitext(filename)[0]
            img = cv2.imread(os.path.join(input_dir, filename))
            if img is not None:
                print ("[INFO] Processing: ", filename_without_extenstion)
                faces = detect_faces(img, threshold=0.8, min_face_size=(80, 80))
                for i, (x, y, w, h) in enumerate(faces):
                    cropped_face = img[y:y+h, x:x+w]
                    output_path = f"{output_dir}/{filename_without_extenstion}_face_{i}.jpg"
                    success = cv2.imwrite(output_path, cropped_face)
                    if not success:
                        print ("[WARN] Saving failed!")

def main():
    input_dir = "./data/input"
    output_dir = "./data/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    save_cropped_faces(input_dir, output_dir)

if __name__ == "__main__":
    main()
