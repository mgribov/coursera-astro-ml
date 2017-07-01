import numpy as np
from astropy.io import fits

def mean_fits(lst):  
    data = []
    for file in lst:
        f = fits.open(file)
        data.append(f[0].data)    

        # brightest pixel
        # img = f[0].data
        # np.unravel_index(img.argmax(), img.shape)
  
    # "vertically" stack the data
    st = np.stack(data, axis=2)

    # get mean for each rowXcol, down the stack, round
    # return np.around(mean, decimals=1)
    return st.mean(axis=2)
  
if __name__ == '__main__':
  
    # Test your function with examples from the question
    data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
    print(data[100, 100])

    # You can also plot the result:
    import matplotlib.pyplot as plt
    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()
