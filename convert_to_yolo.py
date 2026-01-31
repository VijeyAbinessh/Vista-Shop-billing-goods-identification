import json
import os

# ---------- PATHS ----------
JSON_FILE = "instances_train_supercategory.json"
IMAGE_DIR = "train"
OUT_IMG_DIR = "yolo_data/images/train"
OUT_LBL_DIR = "yolo_data/labels/train"

os.makedirs(OUT_IMG_DIR, exist_ok=True)
os.makedirs(OUT_LBL_DIR, exist_ok=True)

# ---------- LOAD JSON ----------
with open(JSON_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# ---------- IMAGE INFO ----------
image_info = {}
for img in data["images"]:
    image_info[img["id"]] = img

# ---------- GROUP ANNOTATIONS ----------
from collections import defaultdict
image_annotations = defaultdict(list)

for ann in data["annotations"]:
    image_annotations[ann["image_id"]].append(ann)

# ---------- CONVERT ----------
for image_id, anns in image_annotations.items():
    img = image_info[image_id]
    img_w = img["width"]
    img_h = img["height"]
    img_name = img["file_name"]

    src_img = os.path.join(IMAGE_DIR, img_name)
    dst_img = os.path.join(OUT_IMG_DIR, img_name)

    if os.path.exists(src_img):
        if not os.path.exists(dst_img):
            os.system(f'copy "{src_img}" "{dst_img}"')

    label_path = os.path.join(
        OUT_LBL_DIR,
        os.path.splitext(img_name)[0] + ".txt"
    )

    with open(label_path, "w") as f:
        for ann in anns:
            x, y, w, h = ann["bbox"]

            x_center = (x + w / 2) / img_w
            y_center = (y + h / 2) / img_h
            w_norm = w / img_w
            h_norm = h / img_h

            cls = ann["category_id"]

            f.write(f"{cls} {x_center} {y_center} {w_norm} {h_norm}\n")

print("YOLO TRAIN DATA READY ✅")
