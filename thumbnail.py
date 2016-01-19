import cv2
import sys

def detectface(frame):
	cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
	return cascade.detectMultiScale(frame, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

def videoframes(path):
    cap = cv2.VideoCapture(path)
    while not cap.isOpened():
        cap = cv2.VideoCapture(path)
        cv2.waitKey(1000)
        print "Wait for the header"

    pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
    i = 0
    while True:
        flag, frame = cap.read()
        framename = ""
        frames = []
        if flag:
            # The frame is ready and already captured
            cv2.imshow('video', frame)
            pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
            framename = str(pos_frame)
            print framename
            rects = detectface(frame)
            print len(rects)
            if len(rects) == 0:
                continue
            else:
                cv2.imwrite("%s.jpg" %framename, frame);
                break
        else:
            # The next frame is not ready, so we try to read it again
            cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
            print "frame is not ready"
            # It is better to wait for a while for the next frame to be ready
            cv2.waitKey(1000)
            break

        if cv2.waitKey(10) == 27:
            break
        if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
            # If the number of captured frames is equal to the total number of frames,
            # we stop
            break

videoframes(sys.argv[1])
