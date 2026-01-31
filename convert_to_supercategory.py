import json

# ---------- FILE PATHS ----------
CATEGORIES_FILE = "categories.json"
INSTANCES_FILE = "instances_train.json"
OUTPUT_FILE = "instances_train_supercategory.json"

# ---------- LOAD FILES ----------
with open(CATEGORIES_FILE, "r", encoding="utf-8") as f:
    categories_data = json.load(f)

with open(INSTANCES_FILE, "r", encoding="utf-8") as f:
    instances_data = json.load(f)

# ---------- BUILD PRODUCT_ID -> SUPERCATEGORY ----------
product_to_super = {}
super_categories = {}
super_id_counter = 0

for cat in categories_data["categories"]:
    super_name = cat["supercategory"]

    if super_name not in super_categories:
        super_categories[super_name] = super_id_counter
        super_id_counter += 1

    product_to_super[cat["id"]] = super_categories[super_name]

# ---------- UPDATE ANNOTATIONS ----------
for ann in instances_data["annotations"]:
    original_id = ann["category_id"]
    ann["category_id"] = product_to_super[original_id]

# ---------- UPDATE CATEGORY LIST ----------
new_categories = []
for name, sid in super_categories.items():
    new_categories.append({
        "id": sid,
        "name": name
    })

instances_data["categories"] = new_categories

# ---------- SAVE NEW FILE ----------
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(instances_data, f, indent=2)

print("DONE ✅")
print(f"Supercategories: {len(super_categories)}")
print("Saved as:", OUTPUT_FILE)
