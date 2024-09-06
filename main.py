import cv2
import numpy as np
import google.generativeai as genai
from PIL import Image, ImageDraw, ImageFont

#Creating Image canvas
canvas = np.zeros((640,900,3),np.uint8)
dvdr = np.zeros((640,5,3)) + 255
canvas[0:,595:600] = dvdr

#Model Configuaration
apk= 'AIzaSyBftyAMQwKRgyt7aBfTbUJfxAoWHUyDYiY'
genai.configure(api_key=apk)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

#Model solving problem
def senttoAi(frm):
    
    PIL_image = Image.fromarray(frm)
    response = model.generate_content(["solve this math problem only give final answer",PIL_image])
    
     # Convert response text to an image
    text_image = Image.new("RGB", (300, 640), (0, 0, 0))  # White background
    draw = ImageDraw.Draw(text_image)
    font = ImageFont.truetype("arial.ttf", 25)  # Adjust font and size as needed
    draw.text((10, 10), response.text, font=font, fill=(0, 255, 255))  # Black text

    # Convert text image to NumPy array and overlay on canvas
    text_array = np.array(text_image)
    canvas[0:,600:] = text_array

ix,iy = 0,0
drawing = False

#Drawing function
def draw(event,x,y,param,flag):
    global canvas,ix,iy,drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if ix==0 and iy==0:
                ix,iy=x,y
            cv2.line(canvas,pt1=(ix,iy),pt2=(x,y),thickness=5,color=(0,255,255))
            ix,iy=x,y
        
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        ix,iy= 0,0
        
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        canvas = np.zeros((400,720,3),np.uint8)
        canvas[0:,595:600] = dvdr
        
    elif event == cv2.EVENT_RBUTTONDOWN:
        senttoAi(canvas)
    
    
cv2.namedWindow(winname='MouseWindow')
cv2.setMouseCallback('MouseWindow',draw)

while True:
    cv2.imshow('MouseWindow', canvas)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
    