import cv2

def cartoon(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 5)

    edges = cv2.Canny(gray, 500, 1200, apertureSize=5)
    edges = 255 - edges

    color = cv2.bilateralFilter(img, 9, 150, 2.4)

    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

img = cv2.imread('cartoon_rendering_OpenCV/bird.jpg')

result = cartoon(img)

cv2.imshow('Cartoon Rendering', result)
cv2.waitKey(0)
cv2.destroyAllWindows()