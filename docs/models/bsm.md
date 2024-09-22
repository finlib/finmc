# Multi-Asset BS

### Model

In a multi asset Black-Scholes model, for asset \(i\), the lognormal stock process \(X^i_t\) is,

$$
dX^i_t = (\mu_i - \frac{\sigma_i^2}{2}) dt + dW^i_s
$$

Where \(dW^1_s, dW^2_s, \dots\) are Weiner processes with covariance matrix

$$
cov = 
\begin{bmatrix}
    \sigma_1^2                  & \rho_{12} \sigma_1 \sigma_2   & \dots  & \rho_{1n} \sigma_1 \sigma_n \\
    \rho_{12} \sigma_1 \sigma_2 & \sigma_2^2                    & \dots  & \rho_{2n} \sigma_2 \sigma_n \\
    \vdots                      & \vdots                        & \ddots & \vdots \\
    \rho_{1n} \sigma_1 \sigma_n & \rho_{2n} \sigma_2 \sigma_n   & \dots & \sigma_n^2
\end{bmatrix}
$$

### Dataset

The model specific component in the dataset (`BSM`) is a dict with the following parameters:

* ASSETS: ordered list of asset names
* COV: the covariance matrix


### Example

This is an example with two assets.

```python
from finmc.models.multi import BSMC
# Covariance matrix
cov = np.array(
    [
        [0.09, 0.03],
        [0.03, 0.04],
    ]
)

# Complete dataset
dataset = {
    "MC": {
        "PATHS": 100_000,
        "TIMESTEP": 1 / 10,
        "SEED": 1,
    },
    "BASE": "USD",
    # assets with discounts and forwards for two years
    "ASSETS": {
        "USD": ("ZERO_RATES", np.array([[2.0, 0.05]])),
        "NVDA": ("FORWARD", np.array([[0.0, 116.00], [2.0, 120.64]])),
        "INTC": ("FORWARD", np.array([[0.0, 21.84], [2.0, 22.70]])),
    },
    "BSM": {
        "ASSETS": ["NVDA", "INTC"],
        "COV": cov,
    },
}

model = BSMC(dataset)
model.advance(1.0)
nvda_spots = model.get_value("NVDA")
intc_spots = model.get_value("INTC")
```
