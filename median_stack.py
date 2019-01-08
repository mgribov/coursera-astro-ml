import numpy as np
from astropy.io import fits
import time
import sys

def median_fits(lst):
    data = [] 
    start = time.perf_counter()
        
    for file in lst:
        f = fits.open(file)
        data.append(f[0].data)        
    
    st = np.stack(data, axis=2)
    med = np.median(st, axis=2)
    
    runtime = time.perf_counter() - start    
    runmem = (sys.getsizeof(data) + st.nbytes + med.nbytes) / 1024
    
    return (med, runtime, runmem)
    

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your function with first example in the question.
    result = median_fits(['image0.fits', 'image1.fits'])
    print(result[0][100, 100], result[1], result[2])
    
    # Run your function with second example in the question.
    result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
    print(result[0][100, 100], result[1], result[2])
