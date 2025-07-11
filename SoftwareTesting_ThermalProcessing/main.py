import os
import numpy as np
import cv2
from thermal_utils import process_thermal_image

# Generate fake thermal image as we dont own a thermal camera yet
if not os.path.exists("test_image.png"):
    print("test_image.png not found, generating mock thermal image...")

    # Create a 120x160 "thermal" image with values between 0 and 6000
    fake_thermal = (np.random.rand(120, 160) * 6000).astype(np.uint16)

    # simulate a "hot zone" in the center
    fake_thermal[50:70, 70:90] = 10000

    # Save as 16-bit PNG
    cv2.imwrite("test_image.png", fake_thermal)
    print("Generated test_image.png")

# Load the image
img = cv2.imread("test_image.png", cv2.IMREAD_UNCHANGED)

if img is None:
    print("Failed to load test_image.png")
    exit(1)

if img.dtype != np.uint16:
    print(f"Image dtype incorrect: {img.dtype}, expected uint16")
    exit(1)

# Send to C function
detected = process_thermal_image(img)

# Output result
if detected:
    print("Detection triggered!")
else:
    print("No detection.")
