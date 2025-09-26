
import pandas as pd
import numpy as np
import math

def age_splitter(df, col_name, age_threshold):
    """
    Splits the dataframe into two dataframes based on an age threshold.

    Parameters:
    df (pd.DataFrame): The input dataframe.
    col_name (str): The name of the column containing age values.
    age_threshold (int): The age threshold for splitting.

    Returns:
    tuple: A tuple containing two dataframes:
        - df_below: DataFrame with rows where age is below the threshold.
        - df_above_equal: DataFrame with rows where age is above or equal to the threshold.
    """
    # Using .copy() to ensure a seperate data frame is created.

    df_below = df[df[col_name] < age_threshold].copy() # Select the Rows in Col_name that are lower than the threshold
    df_above_equal = df[df[col_name] >= age_threshold].copy() # Select the Rows in Col_name that are greather than or equal to the threshold
    return df_below, df_above_equal # Return both of the dataframes as a tuple
    
def effectSizer(df, num_col, cat_col):
    """
    Calculates the effect sizes of binary categorical classes on a numerical value.

    Parameters:
    df (pd.DataFrame): The input dataframe.
    num_col (str): The name of the numerical column.
    cat_col (str): The name of the binary categorical column.

    Returns:
    float: Cohen's d effect size between the two groups defined by the categorical column.
    Raises:
    ValueError: If the categorical column does not have exactly two unique values.
    """
    unique_values = df[cat_col].unique() # Grab all the unique values in the cat_col
    if len(unique_values) != 2: # Ensure two unique values
        raise ValueError("Categorical column must have exactly two unique values.")

    # Assign the Two Groups
    group1_val = unique_values[0]
    group2_val = unique_values[1]
    
    group1 = df[df[cat_col] == group1_val][num_col] # Select numerical values corresponding to the first group
    group2 = df[df[cat_col] == group2_val][num_col] # Select numerical values corresponding to the second group

    return cohenEffectSize(group1, group2) # Calculate and return Cohen's d effect size between the two groups

def cohenEffectSize(group1, group2):
    # You need to implement this helper function
    # This should not be too hard...

    diff = group1.mean() - group2.mean() # Calculate the difference in means

    # Calculate the pooled standard deviation
    n1, n2 = len(group1), len(group2) # Number of observations in each group
    s1, s2 = group1.std(), group2.std() # Get the Standard Deviation of Each Group

    # Formula for Pooled Standard Deviation: sqrt [ ((n1-1)*s1^2 + (n2-1)*s2^2) / (n1 + n2 - 2) ]
    pooled_std = math.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))
    d = diff / pooled_std
    
    return d # Return the Effect Size


def cohortCompare(df, cohorts, statistics=['mean', 'median', 'std', 'min', 'max']):
    """
    This function takes a dataframe and a list of cohort column names, and returns a dictionary
    where each key is a cohort name and each value is an object containing the specified statistics
    """
    pass
  

class CohortMetric():
    # don't change this
    def __init__(self, cohort_name):
        self.cohort_name = cohort_name
        self.statistics = {
            "mean": None,
            "median": None,
            "std": None,
            "min": None,
            "max": None
        }
    def setMean(self, new_mean):
        self.statistics["mean"] = new_mean
    def setMedian(self, new_median):
        self.statistics["median"] = new_median
    def setStd(self, new_std):
        self.statistics["std"] = new_std
    def setMin(self, new_min):
        self.statistics["min"] = new_min
    def setMax(self, new_max):
        self.statistics["max"] = new_max

    def compare_to(self, other):
        for stat in self.statistics:
            if not self.statistics[stat].equals(other.statistics[stat]):
                return False
        return True
    def __str__(self):
        output_string = f"\nCohort: {self.cohort_name}\n"
        for stat, value in self.statistics.items():
            output_string += f"\t{stat}:\n{value}\n"
            output_string += "\n"
        return output_string
