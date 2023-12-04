import pickle


with open('./experiments/6/results', 'rb') as f:
    a = pickle.load(f)
    for i in range(-30,0):
        print("================")
        print(a['eval_actions'][i])
        print(a['eval_returns'][i])
        print("================")

    
    
#python main.py --model_name dpm_v2 --n_episode 50 --lr 0.00015 --num_steps 24000 --rolling_steps 50 --nri_d 32 --seed 123 --stocks 0 --smoothing_days 5 --cnn_d 50 --nri_shuffle 20 --nri_lr 0.00015 --cnn_d2 25