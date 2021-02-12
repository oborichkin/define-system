from define import test_example, train_example, make_qmt, classify
from define.algo import Step

print(classify(train_example, test_example, make_page=True))

make_qmt(train_example)
