import matplotlib.pyplot as plt
from matplotlib.colors import TABLEAU_COLORS, to_rgb
import numpy as np
COLORS = np.array([to_rgb(v) for k,v in TABLEAU_COLORS.items()])
print(COLORS)
def hist2D(x,y,bins,r,c,norm=False,gain=1):
    h = np.histogram2d(x,y,bins,range=r)[0].T.reshape((bins,bins,1))
    H = np.concatenate((h*c[0],h*c[1],h*c[2]),axis=2)
    
    if norm:
        H = (H/H.max())**(1/gain)
        H[H>1]=1
        return H
    return H

def histplot(x, 
             y, 
             labels, 
             bins=100, 
             normalize_each_label=False, 
             range=None, 
             colors=None,
             gain = 1):
    
    # label_idxs = {l:i for i,l in enumerate(set(labels))}
    # label_idxs = [label_idxs[l] for l in labels]
    colors = COLORS
    

    # If Range is not specified set it to the min and max of x and y respectively
    if range==None:
        range=np.array(((x.min(),x.max()),(y.min(),y.max())))
    else:
        range = np.array(range)
        if not range.shape == (2,2):
            raise ValueError('range should be array-like with shape (2,2). {} is not valid'.format(range))
    
    
    # Initiallize RGB image to zeros
    H = np.zeros((bins,bins,3))
    
    
    # Add each label's histogram to H
    for i,l in enumerate(list(set(labels))):
        idxs = np.where(labels==l)[0]
        H = H + hist2D(x[idxs],
                       y[idxs],
                       bins,
                       range,
                       colors[i%len(colors)],
                       normalize_each_label,
                       gain
                      )
    
    # Normalize and apply gain
    im = H/H.max()
    im[im.sum(2)==0]=1
    
    # Plot image
    plt.imshow(np.flip(im,0)) # Must be flipped because vertex is at top left for images
    
    
    # Draw axes
    range_x = np.round(np.linspace(range[0][0],range[0][1],bins),2)
    range_y = np.round(np.linspace(range[1][0],range[1][1],bins),2)
    _ = np.arange(0,bins-1,(bins-1)//5)
    plt.xticks(_, range_x[_])
    plt.yticks(_, range_y[-_-1])
    
    # Show image
    plt.show()