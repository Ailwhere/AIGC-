from PIL import Image
import os

input_folder = 'C:\\Users\\Ailwhere\\Desktop\\aik\\LibFewShot\\data\\fewshot\\dataset_folder\\images'
output_folder = 'C:\\Users\\Ailwhere\\Desktop\\aik\\LibFewShot\\data\\fewshot\\dataset_folder\\new_img'
target_size = (224, 224)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):  # 假设您的图片格式为jpg，根据实际情况修改
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img = img.resize(target_size, Image.ANTIALIAS)
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

print("图片调整完成！")
