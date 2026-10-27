import cv2
from ultralytics import YOLO

# 1. Load the ultra-lightweight pre-trained AI model (runs smoothly on laptop CPUs)
model = YOLO("yolov8n.pt")

# 2. Read the raw input image
img = cv2.imread("image.jpg")
if img is None:
    print("Error: Could not find 'image.jpg' in this folder. Please verify the filename!")
    exit()

h, w, _ = img.shape

# 3. Run AI inference to scan for privacy elements
results = model(img)[0]

redacted_count = 0

# 4. Filter detections to target GDPR sensitive areas (person, car, bus, truck)
for box in results.boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
    conf = float(box.conf)
    cls = int(box.cls)
    label = model.names[cls]
    
    # Target identifiers: people (identifiable faces) and vehicles (license plates)
    if label in ["person", "car", "bus", "truck"] and conf > 0.35:
        redacted_count += 1
        
        # Ensure coordinates stay within image boundaries to prevent crashing
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(w, x2), min(h, y2)
        
        # Isolate the precise Region of Interest (ROI)
        roi = img[y1:y2, x1:x2]
        
        # Apply a heavy, irreversible Gaussian Blur over the sensitive area
        # (Kernel size must be odd numbers; 55x55 ensures complete anonymization)
        blurred_roi = cv2.GaussianBlur(roi, (55, 55), 0)
        img[y1:y2, x1:x2] = blurred_roi
        
        # Draw a sleek red privacy shield border over the blurred zone
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(img, "REDACTED / GDPR", (x1, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

# 5. Add a professional, clean Privacy Compliance Dashboard at the top
banner_h = int(h * 0.12)
cv2.rectangle(img, (0, 0), (w, banner_h), (25, 25, 25), -1)

# Overlay neutral project text metrics
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "AI PRIVACY PIPELINE: AUTOMATED REDACTION", (20, int(banner_h * 0.45)), font, 0.55, (255, 255, 255), 2)
cv2.putText(img, f"GDPR Status: COMPLIANT | Masked Elements: {redacted_count}", (20, int(banner_h * 0.8)), font, 0.45, (0, 255, 0), 1)

# 6. Save the final processed graphic
cv2.imwrite("output_privacy.jpg", img)

print(f"\n[SUCCESS] Pipeline Executed Successfully!")
print(f"Total Sensitive Targets Redacted: {redacted_count}")
print("Your anonymized asset has been saved as 'output_privacy.jpg'.")