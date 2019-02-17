from os import listdir
from os.path import isfile, join
from pathlib import Path
from PIL import Image
import numpy as np
from wordcloud import WordCloud, STOPWORDS

# user settings
output_directory = Path('output')
code_directory = Path(r'resources\Apollo-11-master')
image = Path(r'resources\saturn-v-stencil.png')
font_path = Path(r'resources\fonts\RobotoMono-Regular.ttf')
# matplotlib color maps
colors = ['magma', 'plasma', 'viridis', 'inferno', 'autumn', 'ocean', 'gist_earth']
width = 8
height = 24
dpi = 400

# get code files
code_files = [f for f in listdir(code_directory) if isfile(join(code_directory, f))]
text = ''

# make into one string, removing comments
for file in code_files:
    for line in open(code_directory / file):
        li = line.strip()
        if not li.startswith('#'):
            text = text + line.rstrip()

# open mask file
rocket_mask = np.array(Image.open(image))

# set stop words
stopwords = set(STOPWORDS)
stopwords.add('t')
stopwords.add('https')

# generate wordcloud
wordcloud = WordCloud(width=width*dpi, height=height*dpi, stopwords=stopwords, mask=rocket_mask,
                      background_color='black', contour_width=0, contour_color='white', font_path=str(font_path))
wordcloud.generate(text)

# save in different colors
for color in colors:
    wordcloud.recolor(random_state=3, colormap=color)
    file_name = 'saturn-v-' + color + '.png'
    wordcloud.to_file(output_directory / file_name)
