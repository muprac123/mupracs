def hamming_distance(vector1, vector2):
    """Calculate the Hamming distance between two binary vectors."""
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length")
    return sum(el1 != el2 for el1, el2 in zip(vector1, vector2))

def hamming_network(input_pattern, exemplars):
    """Classify input pattern using the Hamming network."""
    min_distance = float('inf')
    classification = None

    for idx, exemplar in enumerate(exemplars):
        distance = hamming_distance(input_pattern, exemplar)
        if distance < min_distance:
            min_distance = distance
            classification = idx + 1  # Class numbering starts from 1
    return classification

# Example exemplar vectors
exemplars = [
    [1, -1, -1, -1],
    [-1, -1, -1, 1]
]

# Example input pattern
input_pattern = [1, 1, -1, -1]

# Classify input pattern
classification = hamming_network(input_pattern, exemplars)
print("Input pattern classified as Exemplar", classification)
