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

        with open(f'results/{view_type}s_results.json', 'r') as f:
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

    plt.xlabel('Кол-во объектов структуры правил отображения')
    plt.ylabel('Время создания объектов классов графических компонент')
    # plt.title('График времени обработки правил отображения графических компонент для разных типов графических компонент ')
    plt.legend()

    plt.savefig(f'plots/result_plot')