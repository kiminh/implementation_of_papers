import data_loader as dl
import os
import models
import numpy as np
import accuracy
svd=models.SVD()
svd.fit(dl.loader_100k_1())
estimate=svd.predict(dl.loader_100k_t1())
rmse=accuracy.RMSE(estimate)
print(rmse)
svd.fit(dl.loader_100k_2())
estimate=svd.predict(dl.loader_100k_t2())
rmse=accuracy.RMSE(estimate)
print(rmse)
svd.fit(dl.loader_100k_3())
estimate=svd.predict(dl.loader_100k_t3())
rmse=accuracy.RMSE(estimate)
print(rmse)
svd.fit(dl.loader_100k_4())
estimate=svd.predict(dl.loader_100k_t4())
rmse=accuracy.RMSE(estimate)
print(rmse)
svd.fit(dl.loader_100k_5())
estimate=svd.predict(dl.loader_100k_t5())
rmse=accuracy.RMSE(estimate)
print(rmse)
