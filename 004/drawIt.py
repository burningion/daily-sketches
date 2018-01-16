import json
from PIL import Image, ImageDraw

for i in range(1,284):
    inputImage = Image.open("imageseqin/%05d.jpg" % i)
    # print("openpose_data/colvin_%012d_pose.json" % (i - 1))
    inputJSON = json.load(open("openpose_data/colvin_%012d_pose.json" % (i - 1)))

    inputDraw = ImageDraw.Draw(inputImage)
    
    for person in inputJSON["people"]:
        print(person["body_parts"])
        for c, place in enumerate(person["body_parts"]):
            if c % 6 == 0 and c != 0:
                inputDraw.line([person["body_parts"][c-6], person["body_parts"][c-5], person["body_parts"][c-3], person["body_parts"][c-2]], (255, 0, 0), width=5)
    inputImage.save("output/%05d.jpg" % i)
