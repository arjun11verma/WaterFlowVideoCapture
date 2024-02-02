import picamera2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--duration')
parser.add_argument('--direction')
parser.add_argument('--speed')
parser.add_argument('--camera_height')

args = parser.parse_args()
duration = args.duration
direction = args.direction
speed = args.speed
camera_height = args.camera_height

recordings_dir = './recordings'

num_recordings = len(os.listdir(recordings_dir))
recording_name = f'test_{num_recordings}'

active_dir = os.path.join(recordings_dir, recording_name)
os.mkdir(active_dir)

metadata = open(os.path.join(active_dir, 'metadata.txt'), "a")
metadata.write(f'Duration: {duration} \n')
metadata.write(f'Direction: {direction} \n')
metadata.write(f'Speed: {speed} m/s \n')
metadata.write(f'Camera Height: {camera_height} m \n')
metadata.close()

cam = picamera2.Picamera2()
cam.start_and_record_video(os.path.join(active_dir, 'recording.mp4'), duration=int(duration))