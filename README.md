## Apollo 11 Source Code Visuals

A simple python script to generate word clouds in the shape of the Saturn V rocket using the original source code, 
obtained from [here](https://github.com/chrislgarry/Apollo-11). Currently it is set to generate a 8"x24" print at 400 ppi.
There is some sort of bug which locks the output image size to the size of the stencil used, so for different sizes open
`saturn-v-stencil.svg` in your favorite image editor and export a different size.

### Dependencies
* PIL
* numpy
* wordcloud

### Output

#### Autumn
![autumn rocket](output\saturn-v-autumn.png)

#### Gist Earth
![autumn rocket](output\saturn-v-gist_earth.png)
