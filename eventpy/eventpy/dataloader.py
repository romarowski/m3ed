import h5py
import numpy as np
import psutil

class DataLoader():
    """
    The DataLoader class points to the desired HDF5 file of the M3ED dataset 
    and allows to load Events, OVC and LiDAR independently

    """
    def __init__(self, filename: str):
        self.filename = filename
        pass
    def load_events(self, timestamp: int):
        """
        Defines an event dictionary whose strucure is

        events = {t_i : [(x_ij, y_ij, p_ij), ...]}

            Parameters:
               timestamp (int): milisecond timestamp

        """
        self.hf = h5py.File(self.filename, 'r')
        ###create a dict to access each event by timestamp
        t, x, y, p = self._parse_events_by_camera(timestamp,
                                                  left_or_right='left') 
       
        zipped_events = zip (t, x, y,p)
        
        self.events_left = {} 
        for t, x, y, p in zipped_events:
            if t not in self.events_left:
                self.events_left[t] = []
            self.events_left[t].append((x, y, p))
            print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)


        #self.events_left = dict(zip(keys, zip(x, y, p))) 
        pass

    
    def _parse_events_by_camera(self, 
                                timestamp: int, 
                                left_or_right: str) -> tuple:
        """
        Capture event data timestamp t, x, y, polarity p

        Uses the milisecond map, given certain timestamp will grab all 
        available data from the timestamp until the next milisecond 

        """
        hf = self.hf

        start_idx = hf['prophesee'][left_or_right]['ms_map_idx'][timestamp]
        end_idx = hf['prophesee'][left_or_right]['ms_map_idx'][timestamp+1]

                                                        
        t = np.array(hf["prophesee"][left_or_right]["t"][start_idx:end_idx])
        x = np.array(hf["prophesee"][left_or_right]["x"][start_idx:end_idx])
        y = np.array(hf["prophesee"][left_or_right]["y"][start_idx:end_idx])
        p = np.array(hf["prophesee"][left_or_right]["p"][start_idx:end_idx])
        return (t, x, y, p) 
    





        
