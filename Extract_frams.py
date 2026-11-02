import cv2,os
cap = cv2.VideoCapture('input.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
step = int(fps*2)
os.makedirs('frames',exist_ok=True)
i = 0
saved = 0
while True:
    ok,pic = cap.read()
    if not ok:
        break
    if i%step == 0:
        cv2.imwrite(f'frames/{i:06d}.jpg',pic)
        saved += 1
    i += 1
cap.release()
print('saved',saved)
