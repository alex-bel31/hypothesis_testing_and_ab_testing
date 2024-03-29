import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

def generate_data_and_collect_metrics(X, mean_A, mean_B, std_A, std_B):    
    avg_A_list = []
    avg_B_list = []
    p_value_list = []
    
    for day in range(1, X + 1):
        sample_A = np.random.normal(mean_A, std_A, size=day)
        sample_B = np.random.normal(mean_B, std_B, size=day)

        avg_A = np.mean(sample_A)
        avg_B = np.mean(sample_B)
        
        _, p_value = stats.ttest_ind(sample_A, sample_B)
        
        avg_A_list.append(avg_A)
        avg_B_list.append(avg_B)
        p_value_list.append(p_value)
    
    data = pd.DataFrame({
        'Day': range(1, X + 1),
        'Avg_A': avg_A_list,
        'Avg_B': avg_B_list,
        'p-value': p_value_list
    })
    
    return data


def plot_metrics_and_pvalue(data, num_days):
    plt.figure(figsize=(10, 6))
    
    plt.plot(data['Day'], data['Avg_A'], label='Группа A')
    plt.plot(data['Day'], data['Avg_B'], label='Группа B')
    
    plt.axvline(x=num_days, color='r', linestyle='--', label='Количество дней')
    
    plt.xlabel('День')
    plt.ylabel('Среднее')
    plt.title('Средние показатели в группах A и B')
    plt.legend()
    plt.grid(True)

    plt.figure(figsize=(10, 6))
    plt.plot(data['Day'], data['p-value'], label='p-value')
    plt.axvline(x=num_days, color='r', linestyle='--', label='Количество дней')
    plt.axhline(y=0.05, color='g', linestyle='--', label='Уровень значимости афльфа')

    plt.xlabel('День')
    plt.ylabel('p-value')
    plt.title('Динамика p-value')
    plt.legend()
    plt.grid(True)
    plt.show()


def generate_p_values_on_last_day(X, mean_A, std_A):
    p_values = []
    
    for _ in range(1000):
        sample_A = np.random.normal(mean_A, std_A, size=X)
        _, p_value = stats.ttest_1samp(sample_A, mean_A)
        p_values.append(p_value)
    
    return p_values
