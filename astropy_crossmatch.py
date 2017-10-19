# Write your crossmatch function here.
import numpy as np
import time
from astropy.coordinates import SkyCoord
from astropy import units as u

def crossmatch(cat1, cat2, max_dist):
  start = time.perf_counter()
  cat1 = SkyCoord(cat1*u.degree, frame='icrs')
  cat2 = SkyCoord(cat2*u.degree, frame='icrs')
  
  idx = 0
  match = []
  nomatch = []
  
  closest_ids, closest_dists, closest_dists3d = cat1.match_to_catalog_sky(cat2)
  closest_dists_array = closest_dists.value  
  
  for i in closest_dists_array:
    if i < max_dist:
      match.append( (idx, closest_ids[idx], i) )
      
    else:      
      nomatch.append(idx)    

    idx += 1
      
  timing = time.perf_counter() - start
  
  return (match, nomatch, timing)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

