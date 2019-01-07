import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import skimage
import os
import argparse

os.chdir('/Users/habbasi/Desktop') 

def resize_image(input_dir, infile, output_dir, size = (800, 800)):
    outfile = os.path.splitext(infile)[0] + 'resized'
    extension = os.path.splitext(infile)[1]
    
    try:
        img = Image.open(input_dir + '/' + infile)
        img = img.resize((size[0], size[1]), Image.LANCZOS)
        
        new_file = output_dir + '/' + outfile + extension
        img.save(new_file)
        
    except IOError:
        
        print('unable to resize image {}'.format(infile))

if __name__ =='__main__':
    curr_dir = os.getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', help= 'Full input path')
    parser.add_argument('-o', '--output_dir', help= 'Full Output path')
    args = parser.parse_args()
    print(args)
    
    if args.input_dir:
        input_dir = args.input_dir
    else:
        input_dir = curr_dir + '/images'
        
    if args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = curr_dir + '/resized'
    
    
    if not os.path.exists(os.path.join(curr_dir, output_dir)):
        os.mkdir(output_dir)
        
    try:
        for file in os.listdir(input_dir):
            print('file: {}'.format(file))
            resize_image(input_dir, file, output_dir)
            
    except OSError:
        print('file not found')

