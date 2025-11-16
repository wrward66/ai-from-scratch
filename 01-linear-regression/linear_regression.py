import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
X = 2 * np.random.rand(100, 1)   # 100 samples, 1 feature
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3x + noise

# Plot the data
plt.scatter(X, y)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Generated Data")
plt.show()

# Initialise parameters
w = np.random.randn(1)
b = np.random.randn(1)
lr = 0.05
epochs = 1000

def predict(X, w, b):
    return X*w + b

def compute_loss(y, y_pred):
    return np.mean((y - y_pred)**2)

def train(X, y, w, b):
    m = len(y)
    loss = []

    for i in range (epochs):
        y_pred = predict(X, w, b)
        lo = compute_loss(y, y_pred)
        loss.append(lo)

        # Computing gradients for weights and bias
        dw = -(2/m)*np.sum(X*(y - y_pred))
        db = -(2/m)*np.sum(y - y_pred)

        # uupdate parameters
        w = w - lr*dw
        b = b - lr*db
            
    return w, b, loss

w_final, b_final, loss = train(X, y, w, b)
print(f"\nTrained parameters: w={w_final[0]:.2f}, b={b_final[0]:.2f}")

# Plot regression line
plt.scatter(X, y, label="Data")
plt.plot(X, predict(X, w_final, b_final), color="red", label="Model prediction")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression Fit")
plt.legend()
plt.show()

plt.plot(loss)
plt.title("Loss over epochs")
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.show()

