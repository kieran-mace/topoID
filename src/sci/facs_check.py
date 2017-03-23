import numpy as np
from glob import glob
import pandas as pd
import re
from FlowCytometryTools import FCMeasurement
import matplotlib.pyplot as plt
pd.set_option('display.width',180)
np.set_printoptions(precision=2, edgeitems=10, linewidth=180)

# -------------------------------
def sorted_nicely(L):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(L, key=alphanum_key)

def clean_sample(sample):
    ix = (sample['FSC-H'] > 0) & (sample['SSC-H'] > 0) & (sample['FITC-H'] > 0) & (sample['mCherry-H'] > 0)
    # tsample = sample.transform('hlog', channels=['FITC-H', 'SSC-H', 'mCherry-H'] )
    return np.log10(sample.data.loc[ix,'FITC-H']/sample.data.loc[ix,'SSC-H'])

def compute_median_log(dirr):
    files        =  sorted_nicely(glob(dirr + "*.fcs"))
    all_samples  =  [FCMeasurement(ID=f, datafile=f) for f in files]
    x = map(lambda sample: np.median(clean_sample(sample)), all_samples)
    x = np.reshape(x, [8,12])
    x = np.fliplr(x)
    x = np.flipud(x)
    x += 1.
    x = x.T
    x /= x[0,0]
    return (x)

# -------------------------------
# Directory structure
predir = '../../input/fcs/pathway/'
mkk_datadirs = [predir + '967/',
                predir + '969/',
                predir + '968/',
                predir + '966/']

predir = '../../input/fcs/pathway/'
rho_datadirs = [predir + '972/',
                predir + '974/',
                predir + '973/',
                predir + '971/']

# Trial run
datafile = mkk_datadirs[0] + 'Specimen_001_A1_A01.fcs'
sample = FCMeasurement(ID='Test Sample', datafile=datafile)
print sample.channel_names

# Actual run
mkk_kdx = []
for datadir in mkk_datadirs:
    print datadir
    mkk_kdx.append( compute_median_log(datadir) )

rho_kdx = []
for datadir in rho_datadirs:
    print datadir
    rho_kdx.append( compute_median_log(datadir) )


# -------------------------------
(f, ax) = plt.subplots(4, 2, sharex=True, sharey="row", figsize=[8.,11.])
ax[0,0].plot(mkk_kdx[0])
ax[1,0].plot(mkk_kdx[1])
ax[2,0].plot(mkk_kdx[2])
ax[3,0].plot(mkk_kdx[3])

ax[1,1].plot(rho_kdx[1])
ax[0,1].plot(rho_kdx[0])
ax[2,1].plot(rho_kdx[2])
ax[3,1].plot(rho_kdx[3])

f.savefig('../../output/facs_check.py/dose_response.pdf')
plt.show()
