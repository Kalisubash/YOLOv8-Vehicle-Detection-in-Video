import cv2  # importing open cv library
from ultralytics import YOLO
import os
model = YOLO("yolov8n.pt")
video_path = r"C://Users//ransu//Documents//Python//video.mp4"
cap = cv2.VideoCapture(video_path)

# Getting  the video's width, height, and frames per second (fps)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Defining the video format and creating  VideoWriter object
output_path = r"C://Users//ransu//Documents//Python//output_video1.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # format of mp4
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Initializing  a set to keep track of unique car track IDs so that the same vehicle is not  detected multiple times
car_track_ids = set()
car_count = 0
while cap.isOpened():
    success, frame = cap.read()
    if success:
        # Running YOLOv8 tracking on the frame

        results = model.track(frame, persist=True)

        # Iterate over results for each frame and plot
        for result in results:
            for box in result.boxes:
                # Check if the detected object is a car

                if model.names[int(box.cls)] == 'car':
                    # Only count if a valid track ID is available
                    if box.id is not None:
                        track_id = int(box.id)
                        # If a new track ID is detected, increase the car counter
                        if track_id not in car_track_ids:
                            car_track_ids.add(track_id)
                            car_count += 1
            annotated_frame = result.plot()
            # Display the car count on the video
            cv2.putText(annotated_frame, f'Car Count: {car_count}', (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            # Write the frame to the output video file
            out.write(annotated_frame)

        # Uncomment to display the video frame by frame
        # cv2.imshow("YOLOv8 Tracking", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release the video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()

# Print the total number of cars detected
print(f'Total number of cars detected: {car_count}')