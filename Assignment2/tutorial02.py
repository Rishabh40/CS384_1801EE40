import math
# All decimal 6 places
# function to detect invalid cases


def check(first_list):
    for num in first_list:
        if not isinstance(num, (int, float)):
            return False
    return True


# Function to compute mean
def mean(first_list):
    # mean Logic
    if check(first_list) == False:
        return 0
    if len(first_list) == 0:
        return 0
    mean_value = round(summation(first_list)/len(first_list), 6)
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    if check(first_list) == False:
        return 0
    sorted_list = sorting(first_list)
    median_value = 0
    middle_idx = int(len(sorted_list)/2)
    if len(sorted_list) % 2 == 0:
        median_value = (sorted_list[middle_idx-1]+sorted_list[middle_idx])/2
    else:
        median_value = sorted_list[middle_idx]
    median_value = round(median_value, 6)
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    if check(first_list) == False:
        return 0
    if len(first_list) == 0:
        return 0
    standard_deviation_value = round(math.sqrt(variance(first_list)), 6)
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    if check(first_list) == False:
        return 0
    if len(first_list) == 0:
        return 0
    squared_diff_sum = 0
    mean_val = mean(first_list)
    for num in first_list:
        squared_diff_sum += (num-mean_val)*(num-mean_val)
    variance_value = round(squared_diff_sum/len(first_list), 6)
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    if len(first_list) is not len(second_list):
        return 0
    if check(first_list) == False:
        return 0
    if check(second_list) == False:
        return 0
    if len(first_list) == 0:
        return 0
    rmse_value = round(math.sqrt(mse(first_list, second_list)), 6)
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    if len(first_list) is not len(second_list):
        return 0
    if check(first_list) == False:
        return 0
    if check(second_list) == False:
        return 0
    if len(first_list) == 0:
        return 0
    square_sum = 0
    for idx in range(0, len(first_list)):
        square_sum += (first_list[idx]-second_list[idx]) * \
            (first_list[idx]-second_list[idx])
    mse_value = round(square_sum/len(first_list), 6)
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    if len(first_list) is not len(second_list):
        return 0
    if check(first_list) == False:
        return 0
    if check(second_list) == False:
        return 0
    if len(first_list) == 0:
        return 0
    absolute_diff_sum = 0
    for idx in range(0, len(first_list)):
        absolute_diff_sum += abs(first_list[idx]-second_list[idx])
    mae_value = round(absolute_diff_sum/len(first_list), 6)
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    return skewness_value


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


def sorting(first_list):
    # Sorting Logic
    if check(first_list) == False:
        return 0
    sorted_list = first_list
    mergeSort(sorted_list, 0, len(first_list)-1)
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    if check(first_list) == False:
        return 0
    if len(first_list) == 0:
        return 0
    mean_val = mean(first_list)
    standard_deviation_val = standard_deviation(first_list)
    if standard_deviation_val == 0:
        return 0
    quadratic_sum = 0
    for num in first_list:
        quadratic_sum += ((num-mean_val)/standard_deviation_val)*((num-mean_val)/standard_deviation_val) * \
            ((num-mean_val)/standard_deviation_val) * \
            ((num-mean_val)/standard_deviation_val)
    kurtosis_value = round(quadratic_sum/len(first_list), 6)
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    if check(first_list) == False:
        return 0
    summation_value = 0
    for num in first_list:
        summation_value += num
    summation_value = round(summation_value, 6)
    return summation_value
