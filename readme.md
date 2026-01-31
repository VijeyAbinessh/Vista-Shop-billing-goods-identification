# Vista – CodeFest’26 Object Detection

This repository contains a YOLO-based computer vision pipeline developed for the **Vista – CodeFest’26 (IIT BHU)** challenge.

## Problem
Automate supermarket checkout by detecting and counting grocery items from table-top images.

## Approach
- Fine-tuned YOLO detector on Vista dataset
- Optimized for low-to-mid resource hardware
- Post-processed detections to generate category-only predictions
- Strictly formatted CSV submission for Kaggle evaluation

## Files
- `make_submission.py` – Converts YOLO predictions to Kaggle submission format
- `convert_to_yolo.py` – Dataset conversion script
- `data.yaml` – YOLO dataset configuration

## Submission Format
```csv
image_id,categories
1,"[2,4,10]"
2,"[]"
