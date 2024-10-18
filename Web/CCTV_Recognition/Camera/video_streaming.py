import cv2
import threading
import json
from django.http import StreamingHttpResponse
from django.views.decorators.gzip import gzip_page

# Global variables to store the camera frames
camera_frames = {}

def gen_frames(camera_id):
    """
    Generator function to continuously read frames from the camera and yield them.
    """
    camera = cv2.VideoCapture(camera_id)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Store the frame in the global dictionary
            camera_frames[camera_id] = frame
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@gzip_page
def video_feed(request, camera_id):
    """
    View function to stream the video feed from the specified camera.
    """
    return StreamingHttpResponse(gen_frames(int(camera_id)),
                                content_type='multipart/x-mixed-replace; boundary=frame')

def start_camera_threads():
    """
    Function to start the camera threads in the background.
    """
    for camera_id in range(1, 51):
        threading.Thread(target=gen_frames, args=(camera_id,)).start()

# Start the camera threads when the server starts
start_camera_threads()
