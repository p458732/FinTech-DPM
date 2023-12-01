import numpy as np

t = np.load('./DPM/pgportfolio/data/stock.npy', allow_pickle=True)
coins = ['GOOG', 'NVDA', 'AMZN', 'AMD', 'QCOM', 'INTC', 'MSFT', 'AAPL', 'BIDU']


#stock_cols = ['date', 'high', 'low', 'open', 'close', 'volume', 'quoteVolume']

#python main.py --model_name dpm_v2 --n_episode 50 --lr 0.00015 --num_steps 18000 --rolling_steps 50 --nri_d 32 --seed 123 --stocks 0 --smoothing_days 5 --cnn_d 50 --nri_shuffle 20 --nri_lr 0.00015 --cnn_d2 25 --L2_w 0 --L3_w 0
print(t)
