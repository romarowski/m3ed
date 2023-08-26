import h5py
import numpy as np

class DataLoader():
    """
    The DataLoader class points to the desired HDF5 file of the M3ED dataset 
    and allows to load Events, OVC and LiDAR independently

    """
    def __init__(self, filename: str):
        self.filename = filename
        pass
    def load_events(self):
        """
        Defines an event dictionary whose strucure is

        events = {t_i : [(x_ij, y_ij, p_ij), ...]}

        """
        hf = h5py.File(self.filename, 'r')
        ###create a dict to access each event by timestamp
        t, x, y, p = _parse_events_by_camera(left_or_right='left')

        self.events_left = {} 
        for t, x, y, p in zip (t, x, y,p):
            if t not in self.events_left:
                self.events_left[t] = []
            self.events_left[t].append((x, y, p))


        #self.events_left = dict(zip(keys, zip(x, y, p))) 

    
    def _parse_events_by_camera(left_or_right='left'):
        """
        Capture event data timestamp t, x, y, polarity p
        """
        t = np.array(hf["prophesee"][left_or_right]["t"])
        x = np.array(hf["prophesee"][left_or_right]["x"])
        y = np.array(hf["prophesee"][left_or_right]["y"])
        p = np.array(hf["prophesee"][left_or_right]["p"])
        return t, x, y, p 
    





        
