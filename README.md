YOLOv8 Vehicle Detection in Video

This Python script utilizes the YOLOv8 model to detect and count vehicles in a video file. It processes each frame of the video, detects cars, and saves the annotated video with vehicle counts.
Features
Vehicle Detection: Detects and counts vehicles (cars) in a video using YOLOv8.
Video Annotation: Annotates the video with detected vehicles and displays the total count.
Output Video: Saves the annotated video to a specified file path.

Requirements
Python 3.x
OpenCV library
Ultralytics YOLOv8
Install the required libraries using pip: pip install opencv-python ultralytics

Usage
Prepare YOLOv8 Model: Download the YOLOv8 model file (yolov8n.pt) and place it in the working directory.
Set Paths: Update the video_path and output_path variables in the script to specify the input video file and the location where the output video will be saved.
Run the Script
Processing: The script will read the input video, process each frame to detect vehicles, annotate the frames with vehicle counts, and save the output video.
Exit: Press 'q' to stop processing and exit the video capture loop if running interactively.

Code Overview
Initialization: Loads the YOLOv8 model and sets up video capture from a file.
Frame Processing: Processes each frame for vehicle detection and tracking.
Annotation: Annotates frames with vehicle counts and writes them to an output video file.
Resource Management: Releases video capture and writer objects and closes all OpenCV windows.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contributing
Feel free to open issues or submit pull requests for improvements or bug fixes.

This README file provides a comprehensive overview of the script's functionality, installation, usage, and contribution guidelines, making it easy for users to understand and use your project.


