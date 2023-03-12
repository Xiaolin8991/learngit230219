#电影数据分析
import json
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
#pd.set_option('display.max_columns',None)#显示所有列

#导入数据
credits_file='D:/wzl/kaggle/the movies/archive_new/tmdb_5000_credits.csv'
movies_file='D:/wzl/kaggle/the movies/archive_new/tmdb_5000_movies.csv'
credits=pd.read_csv(credits_file,encoding='utf-8')
movies=pd.read_csv(movies_file,parse_dates=['release_date'])#parse_dates 将release_date列设为日期格式
#print('credits:',credits.shape,'movies:',movies.shape)

#查看信息
print(credits.head(),movies.head())