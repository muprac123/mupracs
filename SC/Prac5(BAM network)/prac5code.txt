import numpy as np

class SimpleBAM:
    def __init__(self, patterns_A, patterns_B):
        self.weights = np.dot(patterns_A.T, patterns_B)

    def recall_A(self, pattern_B):
        return np.dot(pattern_B, self.weights.T)

    def recall_B(self, pattern_A):
        return np.dot(pattern_A, self.weights)

# Example usage:
if __name__ == "__main__":
    patterns_A = np.array([[1, 1, -1], [-1, 1, 1], [-1, -1, -1]])
    patterns_B = np.array([[1, -1], [-1, 1], [1, 1]]) 
    bam = SimpleBAM(patterns_A, patterns_B)

    # Test recall for pattern B
    test_pattern_B = np.array([1, -1]) 
    recalled_pattern_A = bam.recall_A(test_pattern_B) 
    print("Recalled Pattern A:", recalled_pattern_A)

    # Test recall for pattern A
    test_pattern_A = np.array([1, 1, -1]) 
    recalled_pattern_B = bam.recall_B(test_pattern_A) 
    print("Recalled Pattern B:", recalled_pattern_B)
