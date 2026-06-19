from ultralytics import YOLO
def main():
  model="yolo26l"
  model.train(data.yaml , 
            worker=6,
            batch=6,
            epochs=300,
            device = 0)
if "__name__"=="__main__":
  main()
