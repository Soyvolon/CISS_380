# One example of the application of 2d-arrays is in image processing. A digital,
# grayscale image can be thought of as a 2d array of integers between 0 and 255. 
# Each element of the 2d array represents light intensity of a single pixel in the 
# image. Let's write a function that uses so called mean filter to smooth an image.  
# The idea of mean filtering is simply to replace each pixel value in an image with the 
# mean (`average') value of its neighbors, including itself. This has the effect of eliminating 
# pixel values which are unrepresentative of their surroundings. Most pixels have eight neighbors. 
# The pixels in the boundary rows and columns have 5 neighbors and the corner pixels have only three neighbors. 

# Your function called meanFitler should take one parameter which is an object of type Grid 
# (defined in the attached file) and apply mean filter to that object. The function should 
# not return anything it should modify the object passed as a parameter.

from grid import Grid

def median_filter(data: Grid):
    xmax = data.getWidth()
    ymax = data.getHeight()

    for x in range(0, xmax):
        for y in range(0, ymax):
            _run_filter(x, y, xmax, ymax, data)

def _run_filter(x: int, y: int, xmax: int, ymax: int, data: Grid):
    mean = data[y][x]
    vals = 1
    for xrel in range(-1, 2):
        for yrel in range(-1, 2):
            absx = x + xrel
            absy = y + yrel
            if absx < 0 or absy < 0 or absx >= xmax or absy >= ymax:
                continue
            mean += data[absy][absx]
            vals += 1

    mean /= vals
    data[y][x] = mean

def main():
    g = Grid(3, 3, 1)
    g[1][1] = 2
    print(g)
    median_filter(g)
    print("------------------")
    print("SMOOTHED")
    print("------------------")
    print()
    print(g)

if __name__ == "__main__":
    main()