import numpy as np
from matplotlib import pyplot as plt

# Complete the following to make the plot
if __name__ == "__main__":
    data = np.load('sdss_galaxy_colors.npy')
    # Get a colour map
    cmap = plt.get_cmap('YlOrRd')
    c = np.random.rand(len(data))
    
    # Define our colour indexes u-g and r-i
    ug = data['u'] - data['g']
    ri = data['r'] - data['i']

    # Make a redshift array
    rs = data['redshift'].tolist()    
    
    # Create the plot with plt.scatter and plt.colorbar
    plt.scatter(ug, ri, s=2, c=rs, lw=0, cmap=cmap)     
    plt.colorbar()
    
    # Define your axis labels and plot title
    plt.xlabel('Colour Index u-g')
    plt.ylabel('Colour Index r-i')
    plt.title('Redshift (colour) u-g versus r-i')
    
    # Set any axis limits
    plt.ylim(-0.5, +1.0)
    plt.xlim(-0.5, +2.5)
    
    plt.show()
