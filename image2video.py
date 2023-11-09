import cv2
import os

# Define the folder containing your images
image_folder = r'001'

# Define the output video file
# output_video = 'output_video.mp4'
output_video = 'output_video.avi'

# Get the list of image files in the folder
images = [img for img in os.listdir(image_folder) if img.endswith(".bmp")]

# Sort the images in numerical order (if file names are numbered sequentially)
images.sort(key=lambda x: int(x.split('.')[0]))

# Define the frame size based on the first image (assuming all images have the same size)
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# Define the frames per second (FPS) for the video
fps = 10

# Define the codec and create a VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fourcc = cv2.VideoWriter_fourcc("X", "V", "I", "D")
video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Iterate through the images and add them to the video
for image in images:
    image_path = os.path.join(image_folder, image)
    frame = cv2.imread(image_path)
    video.write(frame)

# Release the VideoWriter object and close the video file
video.release()

# Optionally, you can destroy any remaining OpenCV windows
cv2.destroyAllWindows()
