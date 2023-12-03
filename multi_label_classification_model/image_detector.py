#------------------------------------------------------------------------------#
#                                                                              #
#  Purpose : Test multi-label model for images placed in 'images' folder       #
#  AUTHOR :  Rafael Dolores                                                    #
#  ACKNOWLEDGMENT: This work was done without looking at any external sources  #
#------------------------------------------------------------------------------#

import cv2
from ultralytics import YOLO
import os

# Load the YOLOv8 model
model = YOLO('garbage.pt')

# Path to the directory containing images2
image_directory = "images"

# Get a list of all image files in the directory
image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Process each image in the directory
for image_file in image_files:
    # Path to the current image
    image_path = os.path.join(image_directory, image_file)

    # Read the image
    frame = cv2.imread(image_path)

    # Run YOLOv8 inference on the image
    resized_frame = cv2.resize(frame, (600, 500))
    results = model(resized_frame, conf = 0.3)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLOv8 Inference", annotated_frame)

    # Wait for the user to press the Esc key
    key = cv2.waitKey(0)
    if key == 27:  # Esc key
        break

# Close all open windows
cv2.destroyAllWindows()
