import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class EventFigure(Figure):
    """
    A figure for the prophesee event camera
    """
    def __init__(self, *args, 
                 events_dict=None,
                 events_to_plot=None, **kwargs):
        super().__init__(*args, **kwargs)

        if events_to_plot == "both":
            figtitle = "Prophesee"
            markersize = 4
            nrows = 1
            ncols = 2



