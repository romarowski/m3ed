import matplotlib.pyplot as plt
import pdb
from matplotlib.figure import Figure

class EventFigure():
    """
    A figure for the prophesee event camera
    """
    def __init__(self, dataloader):
        self.dataloader = dataloader
    

    def plot(self, timestamp):
        timestamp = timestamp * 1e3 #convert to microseconds
        fig, (axl, axr) = plt.subplots(1, 2)
        fig.suptitle(f"Prophesee events at timestamp {timestamp} microseconds")

        axl.set_title("Left events")
        axr.set_title("Right events")

        left = self.dataloader.events['left'][timestamp]
        right = self.dataloader.events['right'][timestamp]

        xl, yl, pl = self._unpack_events_for_plotting(left)
        xr, yr, pr = self._unpack_events_for_plotting(right)

        axl.plot(xl, yl, s=4, c=pl)
        axr.plot(xr, yr, s=4, c=pr)

        plt.show()

        
        pass
    def _unpack_events_for_plotting(self, event_array):
        x = []
        y = []
        p = []
        for event in event_array:
            x.append(event[0])
            y.append(event[1])
            p.append("blue" if event[2] == 0 else "red")

        pdb.set_trace()
        return x, y, p


