# from pyzbar import pyzbar
# import argparse
# import cv2
# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#     help="path to input image")
# args = vars(ap.parse_args())

# # load the input image
# image = cv2.imread(args["C:\\Users\\jfern\\OneDrive\\Desktop\\12345.png"])

# # find the barcodes in the image and decode each of the barcodes
# barcodes = pyzbar.decode(image)

# for barcode in barcodes:
# 	# extract the bounding box location of the barcode and draw the
# 	# bounding box surrounding the barcode on the image
# 	(x, y, w, h) = barcode.rect
# 	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# 	# the barcode data is a bytes object so if we want to draw it on
# 	# our output image we need to convert it to a string first
# 	barcodeData = barcode.data.decode("utf-8")
# 	barcodeType = barcode.type

# 	# draw the barcode data and barcode type on the image
# 	text = "{} ({})".format(barcodeData, barcodeType)
# 	cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
# 		0.5, (0, 0, 255), 2)

# 	# print the barcode type and data to the terminal
# 	print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

# # show the output image
# cv2.imshow("Image", image)
# cv2.waitKey(0)


import hashlib
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

a = 0

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-o", "--output", type=str, default="",
#                 help="path to output CSV file containing barcodes")
# args = vars(ap.parse_args())

print("[INFO] starting video stream...")
# vs = VideoStream(src=0).start()
vs = VideoStream(0).start()
time.sleep(1.0)

# open the output CSV file for writing and initialize the set of
# barcodes found thus far
# csv = open(args["output"], "w")
found = set()
while True:
    # grab the frame from the threaded video stream and resize it to
    # have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # find the barcodes in the frame and decode each of the barcodes
    barcodes = pyzbar.decode(frame)
    # loop over the detected barcodes
    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw
        # the bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it
        # on our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # draw the barcode data and barcode type on the image
        text = "{}".format(barcodeData)
        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        a = 1

        # if the barcode text is currently not in our CSV file, write
        # the timestamp + barcode to disk and update the set
        # if barcodeData not in found:
        #     csv.write("{},{}\n".format(datetime.datetime.now(),
        #                                barcodeData))
        #     csv.flush()
        #     found.add(barcodeData)

        # show the output frame
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q") or a == 1:
        break

# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
print(text)

# initializing string
str = text


# encoding GeeksforGeeks using encode()
# then sending to SHA256()
result = hashlib.sha256(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())

print("\r")
# csv.close()
cv2.destroyAllWindows()
vs.stop()


