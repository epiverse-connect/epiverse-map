import numpy as np
from sklearn.metrics.pairwise import cosine_distances
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

def plot_polar_conformal_projection(vectors: np.ndarray, ref_index: int = None, k: int = 20, seed: int = 42):
    """
    Plots a polar projection of the k closest vectors (based on cosine distance) 
    to a reference vector from a high-dimensional space.
    
    Args:
        vectors (np.ndarray): A 2D numpy array of shape (n_samples, n_features)
        ref_index (int): Index of the reference vector. If None, chosen randomly.
        k (int): Number of closest vectors to consider
        seed (int): Random seed for reproducibility
    """
    np.random.seed(seed)
    
    if ref_index is None:
        ref_index = np.random.randint(0, len(vectors))

    reference_vector = vectors[ref_index].reshape(1, -1)
    cosine_dists = cosine_distances(reference_vector, vectors).flatten()
    
    # Exclude the reference vector itself from the list
    indices = np.argsort(cosine_dists)[1:k+1]
    closest_vectors = vectors[indices]
    
    # Combine reference and nearest for projection
    subset_vectors = np.vstack([reference_vector, closest_vectors])
    
    # Use MDS to project to 2D
    mds = MDS(n_components=2, dissimilarity='precomputed', random_state=seed)
    dist_matrix = cosine_distances(subset_vectors)
    projection = mds.fit_transform(dist_matrix)
    
    # Convert to polar coordinates (r, theta)
    origin = projection[0]
    deltas = projection - origin
    r = np.linalg.norm(deltas, axis=1)
    theta = np.arctan2(deltas[:, 1], deltas[:, 0])
    
    # Plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)
    
    # Plot neighbors
    ax.scatter(theta[1:], r[1:], c='blue', label='Nearest neighbors')
    
    # Plot reference
    ax.scatter(theta[0], r[0], c='red', marker='x', s=100, label='Reference')
    
    ax.set_title("Polar Plot of Cosine-Projected Neighbors (MDS)")
    ax.legend(loc='upper right')
    plt.show()

# Generate some synthetic 300D data for testing
np.random.seed(0)
synthetic_data = np.random.rand(100, 300)

# Call the function with the synthetic data
plot_polar_conformal_projection(synthetic_data)
