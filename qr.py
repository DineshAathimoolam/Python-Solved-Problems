import numpy as np

def qr_method(A, max_iterations=1000, tolerance=1e-6):
    n = A.shape[0]
    eigenvalues = np.zeros(n)

    for i in range(max_iterations):
        Q, R = np.linalg.qr(A)
        A = np.dot(R, Q)

        # Check if the matrix is already upper triangular
        if np.abs(np.sum(np.tril(A, -1))) < tolerance:
            break

    # Extract the eigenvalues from the diagonal of the upper triangular matrix
    for i in range(n):
        eigenvalues[i] = A[i, i]

    # Compute the eigenvectors using back substitution
    eigenvectors = []
    for eigenvalue in eigenvalues:
        B = A - eigenvalue * np.eye(n)
        eigenvector = np.zeros(n)
        eigenvector[-1] = 1

        for i in range(n-2, -1, -1):
            eigenvector[i] = np.dot(B)
