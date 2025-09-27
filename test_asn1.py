from asn1_function_sheet import age_splitter, cohenEffectSize, effectSizer, cohortCompare, CohortMetric
import pandas as pd
import numpy as np
import pytest

def test_age_splitter_1():
    df = pd.DataFrame({
        'age': [25, 30, 35, 40, 45],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
    })
    df_below, df_above_equal = age_splitter(df, 'age', 40)
    assert df_below.shape[0] == 3
    assert df_above_equal.shape[0] == 2

def test_age_splitter_2():
    df = pd.DataFrame({
        'age': [18, 22, 27, 29, 31, 35],
        'name': ['A', 'B', 'C', 'D', 'E', 'F']
    })
    df_below, df_above_equal = age_splitter(df, 'age', 30)
    assert all(df_below['age'] < 30)
    assert all(df_above_equal['age'] >= 30)

def test_cohen_effectsize_1():
    group1 = pd.Series([1, 2, 3])
    group2 = pd.Series([4, 5, 6])
    d = cohenEffectSize(group1, group2)
    assert isinstance(d, float)
    assert d < 0  # group1 mean < group2 mean

def test_cohen_effectsize_2():
    group = pd.Series([1, 2, 3])
    d = cohenEffectSize(group, group)
    assert d == 0 # Equal

def test_effectsizer_1():
    df = pd.DataFrame({
        'score': [10, 20, 30, 40],
        'group': ['A', 'A', 'B', 'B']
    })
    d = effectSizer(df, 'score', 'group')
    assert isinstance(d, float)

def test_effectsizer_2():
    # Invalid Category
    df = pd.DataFrame({
        'score': [1, 2, 3],
        'group': ['A', 'B', 'C']
    })
    with pytest.raises(ValueError):
        effectSizer(df, 'score', 'group')

def test_cohort_compare_1():
    df = pd.DataFrame({
        'age': [20, 25, 30],
        'salary': [1000, 1500, 2000]
    })
    results = cohortCompare(df, ['age', 'salary'])
    assert isinstance(results, dict)
    assert 'age' in results
    assert 'salary' in results
    assert isinstance(results['age'], CohortMetric)
    assert results['age'].statistics['mean'] == df['age'].mean()
    assert results['salary'].statistics['max'] == df['salary'].max()