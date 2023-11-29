import numpy as np

def encode_to_spikes(data, threshold, max_spike_rate):
    """
    Преобразует данные в последовательности спайков.
    
    :param data: Входные данные (временные ряды)
    :param threshold: Порог для генерации спайков
    :param max_spike_rate: Максимальная частота генерации спайков
    :return: Последовательности спайков для каждой характеристики
    """
    num_samples, num_features = data.shape
    spike_sequences = []

    for feature_idx in range(num_features):
        feature_data = data[:, feature_idx]
        spike_sequence = []

        for value in feature_data:
            if value >= threshold:
                # Рассчитываем частоту генерации спайков на основе значения
                spike_rate = (value - threshold) / (max_spike_rate - threshold)
                # Генерируем спайк с вероятностью, соответствующей частоте
                spike = np.random.uniform(0, 1) < spike_rate
                spike_sequence.append(spike)
            else:
                spike_sequence.append(False)

        spike_sequences.append(spike_sequence)

    return spike_sequences

# Пример использования
data = np.random.rand(100, 4)  # Пример данных (100 временных отсчетов, 4 характеристики)
threshold = 0.5  # Порог для генерации спайков
max_spike_rate = 0.9  # Максимальная частота генерации спайков
spike_sequences = encode_to_spikes(data, threshold, max_spike_rate)

# В spike_sequences теперь содержится последовательность спайков для каждой характеристики
