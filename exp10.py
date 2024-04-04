def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    # Iterate through the text
    for i in range(n - m + 1):
        
        # Check if the pattern matches the substring starting at position i
        
        for j in range(m):
            if text[ j+i] != pattern[j]:
              
                break
        # If the pattern matches, add the starting index to the list of occurrences
        if (j == m-1):
            occurrences.append(i) # Pattern found at index i
    
    return occurrences

# Example usage:
text = "AABAACAADAABAABA"
pattern = "AABA"
print("Text:", text)
print("Pattern:", pattern)
print("Occurrences found at indices:", naive_string_matching(text, pattern))
