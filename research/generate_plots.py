import json
import numpy as np
import matplotlib.pyplot as plt


VIEW_TYPE = 'label'
VIEW_TYPES = [
    'label',
    'image',
    'text_field',
    'button',
]


def obtain_label(view_type):
    if view_type == 'label':
        return 'Комп. отображения текста'
    elif view_type == 'image':
        return 'Комп. отображения изображения'
    elif view_type == 'text_field':
        return 'Комп. поля ввода строки символов'
    elif view_type == 'button':
        return 'Комп. кнопки'


if __name__ == '__main__':
    for view_type in VIEW_TYPES:
        x = []
        y = []

        with open(f'results/time_to_process_rules/{view_type}s_results.json', 'r') as f:
            data_dict = json.load(f)

        for key in data_dict:
            x.append(float(key))
            y.append(float(data_dict[key]))

        x = np.array(x)
        y = np.array(y)
        plt.plot(
            x, 
            y, 
            label=obtain_label(view_type=view_type),
        )


    # plt.xticks(range(0, 101, 10))
    plt.xlabel('Кол-во объектов структуры правил отображения')
    # plt.ylabel('Время создания объектов классов графических компонент (с)')
    plt.ylabel('Время обработки правил отображения (с)')
    # plt.title('График времени обработки правил отображения графических компонент для разных типов графических компонент')
    plt.legend()

    plt.savefig(f'plots/time_to_process_rules.png')