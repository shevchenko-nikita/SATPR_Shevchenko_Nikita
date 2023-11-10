def getMaxCriteria(_matrix, index):
    result = 0
    for alternative in _matrix.keys():
        result = max(result, _matrix[alternative][index])
    return result

def getMinCriteria(_matrix, index):
    result = 100
    for alternative in _matrix.keys():
        result = min(result, _matrix[alternative][index])
    return result
def normalize(_matrix):
    result = {}

    maximize_list = (True, False, True, True, True)

    for alternative in _matrix.keys():
        result[alternative] = {}

        for index in range(len(_matrix[alternative])):
            max_value = getMaxCriteria(_matrix, index)
            min_value = getMinCriteria(_matrix, index)

            if maximize_list[index] == True:
                result[alternative][index] = (_matrix[alternative][index] - min_value) / (max_value - min_value)
            else:
                result[alternative][index] = (max_value - _matrix[alternative][index]) / (max_value - min_value)

    return result

def calcAlternativeUtility(_matrix, weight):
    result = {}
    for alternative in _matrix.keys():
        _sum = 0

        for criteria in range(len(_matrix[alternative])):
            _sum += _matrix[alternative][criteria] * weight[criteria]

        result[alternative] = _sum

    return result

def maximize(_alternatives):
    mx_alternative_name = list(_alternatives.keys())[0]

    for alternative in _alternatives.keys():
        if _alternatives[alternative] > _alternatives[mx_alternative_name]:
            mx_alternative_name = alternative

    return (mx_alternative_name, _alternatives[mx_alternative_name])


def minimize(_alternatives):
    mn_alternative_name = _alternatives.keys()[0]

    for alternative in _alternatives:
        if _alternatives[alternative] < _alternatives[mn_alternative_name]:
            mn_alternative_name = alternative

    return (mn_alternative_name, _alternatives[mn_alternative_name])

def printMatrix(_matrix):
    alternative_names = list(_matrix.keys())
    for name in alternative_names:
        for index in range(len(_matrix[name])):
            print(_matrix[name][index], end=' ')
        print()



first_data = {
    'A1': [3, 7, 2, 9],
    'A2': [8, 3, 6, 7],
    'A3': [4, 8, 3, 5],
    'A4': [9, 6, 5, 4],
}

first_weight = [8, 9, 6, 7]

answer_task1 = maximize(calcAlternativeUtility(first_data, first_weight))

print('Task 1')
print('ANSWER: ', answer_task1[0], ' - ', answer_task1[1])

second_data = {
    'A1': [85, 30, 22, 0.65, 6],
    'A2': [60, 20, 10, 0.6, 7],
    'A3': [30, 12, 5, 0.45, 5],
    'A4': [75, 24, 13, 0.7, 8],
    'A5': [40, 15, 7, 0.55, 7],
}
second_weight = [7, 5, 6, 8, 6]

normalized_matrix = normalize(second_data)

answer_task2 = maximize(calcAlternativeUtility(normalized_matrix, second_weight))

print('Task2')
print('ANSWER: ', answer_task2[0], ' - ', answer_task2[1])