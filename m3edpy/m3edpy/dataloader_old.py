import h5py
import numpy as np
import psutil

class DataLoader():
    """
    The DataLoader class points to the desired HDF5 file of the M3ED dataset 
    and allows to load Events, OVC and LiDAR independently

    """
    def __init__(
            self,
            filename: str
            ):
        self.filename = filename
        self.hf = None
        self.events = None
        pass
    def load_events_to_dict(self, timestamp: int):
        """
        Defines an event dictionary structured as 
        events = {t_i : [(x_ij, y_ij, p_ij), ...]}
        
        The idea is that the event vectors are 1-dimensional, if you wanted to
        find all events that happen at the same time you need to do some sort 
        of masking. If you do this "before-hand" and save everything in a dict
        with O(1) access time you can get an array of all events hashed by 
        timestamp. Might make sense to transform the h5py dataset to match 
        this?


            Parameters:
               timestamp (int): milisecond timestamp

        """
        self.hf = h5py.File(self.filename, 'r')
        self.events = {"left": {},
                       "right": {}} 

        for left_or_right in ["left", "right"]: 
            ###create a dict to access each event by timestamp
            t, x, y, p = (self
                          ._parse_events_by_camera(timestamp,
                                                   left_or_right=left_or_right)
                          )
           
            zipped_events = zip (t, x, y,p)
            
            for t, x, y, p in zipped_events:
                if t not in self.events[left_or_right]:
                    self.events[left_or_right][t] = []
                self.events[left_or_right][t].append((x, y, p))
                
                #print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)


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

        #TODO does this +1 here make sense? this is a design choice
        start_idx = hf['prophesee'][left_or_right]['ms_map_idx'][timestamp]
        end_idx = hf['prophesee'][left_or_right]['ms_map_idx'][timestamp+1]

                                                        
        t = np.array(hf["prophesee"][left_or_right]["t"][start_idx:end_idx])
        x = np.array(hf["prophesee"][left_or_right]["x"][start_idx:end_idx])
        y = np.array(hf["prophesee"][left_or_right]["y"][start_idx:end_idx])
        p = np.array(hf["prophesee"][left_or_right]["p"][start_idx:end_idx])
        return (t, x, y, p) 
    





        
