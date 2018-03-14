import glob
import os
import sys
import numpy as np
from PIL import Image
import librosa
import librosa.core

def invert_spectogram(S, filename):
  #S = S.T
  S = np.expm1(S)
  # add clipped freqncies back in (as zeros)
  # could predict these...
  if S.shape[0] != 1025:
    S = np.concatenate([S, np.zeros((1025-S.shape[0], S.shape[1]))], axis=0)
  y = librosa.core.istft(S)
  librosa.output.write_wav(filename, y, 44100, norm=True)

np.seterr(all='raise')
print('Looking in folder', sys.argv[1])
files = glob.glob(os.path.join(sys.argv[1], '*.png'))

for f in files:
  S = np.array(Image.open(f)) / 255
  print(S)
  #print(s.shape)
  outname = os.path.split(f)[-1].split('.')[0] + '.wav'
  print(outname)
  invert_spectogram(S, os.path.join(sys.argv[1], outname))