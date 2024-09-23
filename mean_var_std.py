import numpy as np

def calculate(list):
    # Verifica se a lista tem exatamente 9 números, caso contrário, levanta um ValueError
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Converte a lista em uma matriz 3x3
    matrix = np.array(list).reshape(3, 3)
    
    # Calcula as métricas e organiza em um dicionário com as chaves em inglês
    calculations = {
        'mean': [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()],  # Média
        'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()],  # Variância
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()],  # Desvio padrão
        'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()],  # Valor máximo
        'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()],  # Valor mínimo
        'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]  # Soma
    }
    
    # Retorna o dicionário com os cálculos
    return calculations
