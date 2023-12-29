import cv2

# Open the video file
input_file = 'vid1.mp4'
cap = cv2.VideoCapture(input_file)

# Get the original video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Calculate the new width and height (70% smaller)
new_width = int(width * 0.7)
new_height = int(height * 0.7)

# Create VideoWriter object to save the resized video
output_file = 'new_vid1.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also use 'XVID'
out = cv2.VideoWriter(output_file, fourcc, cap.get(cv2.CAP_PROP_FPS), (new_width, new_height))

# Read frames from the original video, resize, and write to the new video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame
    resized_frame = cv2.resize(frame, (new_width, new_height))

    # Write the resized frame to the output video
    out.write(resized_frame)

# Release video capture and writer objects
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
