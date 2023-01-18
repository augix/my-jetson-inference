#!/usr/bin/env python3
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

#net = detectNet("ssd-mobilenet-v2", threshold=0.5)
net = detectNet("facenet-120", threshold=0.1)
# net = detectNet(model="/jetson-inference/shanten-calculator/ssd-mobilenet.onnx", threshold=0.5)
#net = detectNet(model="/jetson-inference/shanten-calculator/ssd-mobilenet.onnx", labels="/jetson-inference/shanten-calculator/labels.txt, threshold=0.5")
# camera = videoSource("v4l2:///dev/video0")      # '/dev/video0' for V4L2
camera = videoSource("rtsp://192.168.110.224:8554/unicast")      # '/dev/video0' for V4L2
#display = videoOutput("display://0") # 'my_video.mp4' for file
display = videoOutput("rtp://192.168.3.198:1234", argv=["--headless"]) # 'my_video.mp4' for file

#while display.IsStreaming():
while True:
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
