import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
import torch
from torchvision import transforms
from huggingface_hub import hf_hub_download
from datasets import load_dataset
from PIL import Image
from torchvision.models import inception_v3
from torchmetrics.image.fid import FrechetInceptionDistance
from vis_utils import turboedit_img

dataset = load_dataset("dhruvrnaik/flintstones_story", split="train[:10%]")
image_folder = "true_img"
generated_folder = "turbo_img"
os.makedirs(image_folder, exist_ok=True)
os.makedirs(generated_folder, exist_ok=True)

def save_ground_truth_images():
    for i, example in enumerate(dataset):
        image = example['image']  # Automatically decoded to a PIL Image by the dataset
        image.save(os.path.join(image_folder, f"image_{i}.png"))


save_ground_truth_images()

def generate_images():
    for i in range(len(dataset) - 1):
        source_example = dataset[i]
        target_example = dataset[i + 1]

        source_prompt = source_example['text']
        target_prompt = target_example['text']
        source_image = source_example['image']

        # Generate target image using turboedit_img
        generated_image = turboedit_img(
            image=source_image,
            src_prompt=source_prompt,
            target_prompt=target_prompt, 
            seed=7,
            w1=1
        )

        generated_image.save(os.path.join(generated_folder, f"image_{i}.png"))

generate_images()

fid = FrechetInceptionDistance(feature=1024)

transform = transforms.Compose([
    transforms.Resize((299, 299)),
    transforms.ToTensor(),
    transforms.ConvertImageDtype(torch.uint8) 
])

def prepare_images(folder):
    images = []
    for image_file in sorted(os.listdir(folder)):
        image = Image.open(os.path.join(folder, image_file))
        image = transform(image)
        images.append(image)
    return torch.stack(images)

print("Preparing ground truth images...")
ground_truth_images = prepare_images(image_folder)
print("Preparing generated images...")
generated_images = prepare_images(generated_folder)

fid.update(ground_truth_images, real=True)
fid.update(generated_images, real=False)

fid_score = fid.compute()
print(f"FID Score: {fid_score}")
