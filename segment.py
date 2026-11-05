from rembg import remove , new_session
from PIL import Image
input_path="shirt.jpg"
output_path="shirt_no_bg.png"
print("Opening Image...")
input_image=Image.open(input_path)
print("Initializing lightweight model (u2netp)...")
session = new_session("u2net_cloth_seg")
print("Removing background...")
output_image = remove(input_image, session=session)
output_image.save(output_path)
print(f"Success! Saved transparent image to {output_path}")
