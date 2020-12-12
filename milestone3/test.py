# -*- coding: utf-8 -*-
import random
import pickle

# for _ in range(5):
#     print(random.randint(1,2))


model_file = 'ytong10.model'
policy_param = pickle.load(open(model_file, 'rb'),
                                       encoding='bytes')