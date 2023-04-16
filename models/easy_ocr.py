# https://medium.com/artificialis/how-to-extract-text-from-any-image-with-deep-learning-e834d5a9863e
from easyocr import Reader
import argparse
import cv2

parser = argparse.ArgumentParser( )
parser.add_argument("--image", required=True, help="path to input image")
parser.add_argument("--langs", type=str, default="en", help="comma separated list of languages to recognize")
parser.add_argument("-g", "--gpu", type=int, default=-1, help="whether or not GPU should be used")
args = vars(parser.parse_args())

langs = args["langs"].split(",")
print("[INFO] Using the following languages: {}".format(langs))
# load the input image from disk
image = cv2.imread(args["image"])
# OCR the input image using EasyOCR
print("[INFO] Performing OCR on the input image...")
reader = Reader(langs, gpu=args["gpu"] > 0)
results = reader.readtext(image)

for (bbox, text, prob) in results:
    print("[INFO] {:.4f}: {}".format(prob, text))
    # unpack the bounding box
    (tl, tr, br, bl) = bbox

    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))

    cv2.rectangle(image, tl, br, (0, 255, 0), 2)
    cv2.putText(image, text, (tl[0], tl[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)