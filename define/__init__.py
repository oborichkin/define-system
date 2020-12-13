import os
from .utils import dict_from_csv as _dfcsv
from .utils import list_from_csv as _lfcsv

train_example = _dfcsv(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "train.csv"))
test_example = _lfcsv(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data", "test.csv"))

from .main import make_qmt, classify, poisk, my_poisk
from .utils import mw, mw_advanced, randomly
