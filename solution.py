def longest_substring_k_unique(s: str, k: int) -> int:
    '''
    If string is empty, return 0
    Integer default should be 0 otherwise
    Min Window size is K, string length must be min K long to count...
    but start with window size = to length of string. That way we can return immediately if conditions met (only K unique chars)
    If we get to min window size and there are not K unique chars...return 0.
    '''

    # String empty? Return 0.
    if str == "":
        return 0
    
    longest = 0
    window_size = len(str)

    return 0