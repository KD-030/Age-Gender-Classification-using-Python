import os

# Your absolute file path
faceModel = "/home/mypi/Age_Gender_Classfication/opencv_face_detector_uint8.pb"

# Check if the file exists
if os.path.exists(faceModel):
    faceNet = cv2.dnn.readNet(faceModel, faceProto)
else:
    print(f"Error: The file {faceModel} does not exist.")