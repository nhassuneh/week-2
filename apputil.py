import numpy as np


# update/add code below ...

def ways(n):
    """
    Calculate the number of ways to make change for n cents using pennies (1 cent) and nickels (5 cents).
    
    Args:
        n: The amount in cents to make change for
        
    Returns:
        The number of different combinations of pennies and nickels that sum to n
    """
    if n < 0:
        return 0
    
    return n // 5 + 1

def lowest_score(names, scores):
    """
    Returns the name of the student with the lowest score.
    
    Args:
        names: numpy array of student names
        scores: numpy array of corresponding test scores
        
    Returns:
        The name of the student with the lowest score
    """
    # Use argmin to find the index of the minimum score
    min_index = np.argmin(scores)
    
    # Return the name at that index
    return names[min_index]

def sort_names(names, scores):
    """
    Returns student names sorted in descending order of test scores.
    
    Args:
        names: numpy array of student names
        scores: numpy array of corresponding test scores
        
    Returns:
        numpy array of names sorted by scores (highest to lowest)
    """
    # Use argsort to sort the indices
    # Then reverse with [::-1] to get descending order
    sorted_indices = np.argsort(scores)[::-1]
    
    # Return names in the sorted order
    return names[sorted_indices]