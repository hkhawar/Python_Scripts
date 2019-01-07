from PIL import Image
from pathlib import Path
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('input_dir', help="input dir path")
parser.add_argument('output_dir', help="output dir path")
args = parser.parse_args()

input_dir = Path(args.input_dir)
output_dir = Path(args.output_dir)

if not output_dir.exists():
    output_dir.mkdir()

image_list = input_dir.glob('*.tif')

for image in tqdm(image_list):
    img = Image.open(image)

    image_base_name = image.name[:-4]

    for i in range(3):
        try:
            img.seek(i)
            img.save(Path(output_dir) / (image_base_name + "_ch_" + str(i) + ".tif"))
        except EOFError:
            break
