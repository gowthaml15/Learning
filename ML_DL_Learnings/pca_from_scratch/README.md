### Theory behind PCA

PCA is a statistical method used for dimensionality reduction while preserving as much variablity (information) as possible. It projects data onto a smaller number of dimensions called Principle components.

```python
data = np.random.randn(100,10)
```

Here’s the step by step process of PCA:

1. Center the data → Before applying PCA, the data needs to be centered, meaning subtracting the mean of each feature from the data.This ensures that the PCA transformation is done around the origin, rather than the data’s mean.
    
    ```python
    # Center the data
    data_centered = data - np.mean(data)
    ```
    
2. Compute the Covariance Matrix → Covariance matrix catures the relationship between the features of the dataset. It shows how the features vary together.
    
    ```python
    # Find the covariance, since rows are observations and columns are features
    cov_matrix = np.cov(data_centered,rowvar=False)
    ```
    
3. Find the Eigenvectors and Eigenvalues → PCA identifies the directions (eigenvectors) that maximize the variance in the data. The corresponding eigenvalues represent the amount of variance in each principal component.
    1. Eigenvectors define the directions of the new feature space.
    2. Eigenvalues represent the ‘importance’ or ‘variance’ explained by each eigenvector.
    
    ```python
    # Find the Eigenvectors and Eigenvalues
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    ```
    
4. Sort Eigenvalues and Eigenvectors → Sort the eigenvalues in descending order and choose the corresponding eigenvectors. The eigenvectors associated with the largest eigenvalues are the principal components that explain the most variance.
    
    ```python
    # Sort the eigenvalues
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvectors = eigenvectors[:,sorted_indices]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    #select the top n_components
    top_eigenvectors = sorted_eigenvectors[:,:n_components]
    top_eigenvalues = sorted_eigenvalues[:n_components]
    ```
    
5. Project the data → Once the principal components(eigenvectors) are identified, the data is projected onto these components to reduce its dimensionality.
    
    ```python
    #Project the data
    final_data = np.dot(data_centered,top_eigenvectors)
    ```
    

### Final Notes

- PCA is effective for reducing high-dimensional data and visualizing it in lower dimensions(usually 2D or 3D)
- It’s important to center the data before applying PCA.
- Eigenvectors with higher eigenvalues are more significant and capture more variance in the data.