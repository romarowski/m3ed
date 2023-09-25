from tonic.dataset import Dataset

from typing import Callable, List, Optional, Union

class M3ED(Dataset):
    """`M3ED <https://m3ed.io/>`_
        ::


            @InProceedings{Chaney_2023_CVPR,
            author    = {Chaney, Kenneth and Cladera, Fernando and Wang, Ziyun and Bisulco, Anthony and Hsieh, M. Ani and Korpela, Christopher and Kumar, Vijay and Taylor, Camillo J. and Daniilidis, Kostas},
            title     = {M3ED: Multi-Robot, Multi-Sensor, Multi-Environment Event Dataset},
            booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
            month     = {June},
            year      = {2023},
            pages     = {4015-4022}
            }

        Parameters:
            save_to (string): Location to save files to on disk.
            recording (string or list): Name of the recording(s) to load.
            transform (callable, optional): A callable of transforms to apply to the data.
            target_transform (callable, optional): A callable of transforms to apply to the targets/labels.
            transforms (callable, optional): A callable of transforms that is applied to both data and
                                         labels at the same time.
            
        

    """
    base_url = "https://m3ed-dist.s3.us-west-2.amazonaws.com"
    dataset_list_url = ("https://raw.githubusercontent.com/"
                        "daniilidis-group/m3ed/main/dataset_list.yaml")

    def __init__(
            self,
            save_to: str,
            recording: Union[str, List[str]],
            transform: Optional[Callable] = None,
            target_transform: Optional[Callable] = None,
            transforms: Optional[Callable] = None,
    ):
        super().__init__(save_to, transform, target_transform, transforms)
        self._check_integrity()
        self._load_metadata()
