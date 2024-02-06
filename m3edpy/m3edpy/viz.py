import matplotlib.pyplot as plt
import pdb
import numpy as np
from matplotlib.figure import Figure

class EventFigure():
    """
    A figure for the prophesee event camera
    """
    def __init__(self, dataloader):
        self.dataloader = dataloader
    

    def plot(self, timestamp: int):
        """
        Polarity is encoded as blue = 0; red = 1 

            Parameters:
               timestamp (int): millisecond timestamp of the events to plot 
            Returns:
                fig (Figure): 
                axl (Axes): left camera events axes
                axl (Axes): right camera events axes

        """


        hf = self.dataloader.hf 

        timestamp = timestamp * 1e3 #convert to microseconds
        
        fig, (axl, axr) = plt.subplots(nrows=1, ncols=2, 
                                       figsize=(16, 9),
                                       dpi=300)
        fig.subtitle(f"Prophesee events at timestamp {timestamp} microseconds")

        axl.set_title("Left events")
        axr.set_title("Right events")

        left = self.dataloader.events['left'][timestamp]
        right = self.dataloader.events['right'][timestamp]

        xl, yl, pl = self._unpack_events_for_plotting(left)
        xr, yr, pr = self._unpack_events_for_plotting(right)

        resolution_left = hf['prophesee']['left']['calib']['resolution']
        resolution_right = hf['prophesee']['right']['calib']['resolution']

        width_l, height_l = resolution_left[0], resolution_left[1]
        width_r, height_r = resolution_right[0], resolution_right[1]

        axl.scatter(xl, yl, s=4, c=pl,)
        axr.scatter(xr, yr, s=4, c=pr,)

        axl.set_xlim(0, width_l)
        axl.set_ylim(0, height_l)
        
        axr.set_xlim(0, width_r)
        axr.set_ylim(0, height_r)
        
        plt.show()

        
        return fig, axl, axr 
    def _unpack_events_for_plotting(self, event_array):
        x = []
        y = []
        p = []
        for event in event_array:
            x.append(event[0])
            y.append(event[1])
            p.append("blue" if event[2] == 0 else "red")


        #return np.array(x), np.array(y), np.array(p)
        return x, y, p


