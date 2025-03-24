from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd

# 파일에서 모델 로드
with open('./manhattan_model.pk1', 'rb') as f:
    model = pickle.load(f)

print(model.coef_)
print(model.intercept_)
data = [[2, 2,]]
sample = pd.DataFrame()