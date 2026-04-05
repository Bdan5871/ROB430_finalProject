import cv2
import os
import shutil

# Path to your downloaded images
image_dir = "data/CatIndividualImages/cat_individuals_dataset/0002"
# Path to where you want to sort images
output_dir = "data/CatIndividualImages/cat_individuals_dataset/sorted"

# Map keys to emotion folders
key_to_folder = {
    "h": "happy",
    "s": "sad",
    "a": "angry",
    "r": "relaxed"
}

# Make sure output folders exist
for folder in key_to_folder.values():
    os.makedirs(os.path.join(output_dir, folder), exist_ok=True)

# Iterate through all images
for filename in os.listdir(image_dir):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    image_path = os.path.join(image_dir, filename)
    img = cv2.imread(image_path)
    if img is None:
        print(f"Could not read {filename}")
        continue

    cv2.imshow("Image Sorter", img)
    print(f"Displaying: {filename}")
    print("Press h = happy, s = sad, a = angry, r = relaxed, q = quit")
    
    key = cv2.waitKey(0) & 0xFF  # Wait for key press

    if key == ord('q'):  # Quit
        break

    key_char = chr(key)
    if key_char in key_to_folder:
        dest_folder = os.path.join(output_dir, key_to_folder[key_char])
        shutil.copy2(image_path, dest_folder)  # <-- copy instead of move
        print(f"Copied {filename} to {dest_folder}")
    else:
        print("Key not recognized, skipping image.")

cv2.destroyAllWindows()