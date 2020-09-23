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
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
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


def sorting(first_list):
    # Sorting Logic
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
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
