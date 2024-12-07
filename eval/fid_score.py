import torch
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torchvision.utils import save_image
from torch.utils.data import DataLoader
from torch_fidelity import calculate_metrics

# Define paths
real_images_path = "path_to_real_images"  # Folder containing real images
generated_images_path = "path_to_generated_images"  # Folder containing generated images

# Prepare images (optional preprocessing if needed)
transform = transforms.Compose([
    transforms.Resize((299, 299)),  # Resize to match InceptionV3 input size
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # Normalization
])

# Load Real Images
real_dataset = ImageFolder(root=real_images_path, transform=transform)
real_dataloader = DataLoader(real_dataset, batch_size=32, shuffle=False)

# Load Generated Images
gen_dataset = ImageFolder(root=generated_images_path, transform=transform)
gen_dataloader = DataLoader(gen_dataset, batch_size=32, shuffle=False)

# Optionally save the images to verify preprocessing
# Uncomment below to save transformed images locally
# for idx, (image, _) in enumerate(real_dataloader):
#     save_image(image, f"preprocessed_real_{idx}.png")

# Calculate FID score using torch-fidelity
metrics = calculate_metrics(
    input1=real_images_path,
    input2=generated_images_path,
    fid=True,  # Specify to calculate FID
)

# Print the FID Score
print(f"FID Score: {metrics['frechet_inception_distance']}")
