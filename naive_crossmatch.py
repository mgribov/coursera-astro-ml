import numpy as np

def hms2dec(h, m, s):
  return 15 * (h + m/60 + s/3600)

def dms2dec(deg, arcmin, arcsec):
  val = abs(deg) + arcmin/60 + arcsec/3600
  
  if deg < 0:
    val = -1 * val
    
  return val

# haversine
def angular_dist(r1, d1, r2, d2):
  r1 = np.radians(r1)
  d1 = np.radians(d1)
  r2 = np.radians(r2)
  d2 = np.radians(d2)
  
  a = np.sin(np.abs(d1 - d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  
  return np.degrees(2*np.arcsin(np.sqrt(a + b)))

def import_super():
  idx = 1
  ret = []
  data = np.loadtxt('crossmatch_data/super.csv', delimiter=',', skiprows=1, usecols=[0, 1])

  for i in data:
    coords = (idx, i[0], i[1])
    ret.append(coords)
    idx += 1
    
  return ret

def import_bss():
  idx = 1
  ret = []
  data = np.loadtxt('crossmatch_data/bss.dat', usecols=range(1, 7))
  for i in data:
    coords = (idx, hms2dec(i[0], i[1], i[2]), dms2dec(i[3], i[4], i[5]))
    ret.append(coords)
    idx += 1
    
  return ret

def find_closest(cat, ra, dec):
  smallest = None
  best = None
  
  for i in cat:
    dist = angular_dist(ra, dec, i[1], i[2])
    if smallest == None or dist < smallest:
      smallest = dist
      best = (i[0], dist)
  
  return best

def crossmatch(cat1, cat2, max_dist):
  match = []
  nomatch = []

  # small optimization to avoid doing it for dup values later    
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)

  for i in cat1:
    best, dist = find_closest(cat2, i[1], i[2])
    
    if dist < max_dist:
      match.append( (i[0], best, dist) )
      
    else:      
      nomatch.append(i[0])    

  return (match, nomatch)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

