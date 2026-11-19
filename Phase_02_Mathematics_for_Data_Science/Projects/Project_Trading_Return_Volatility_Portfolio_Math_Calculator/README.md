# Phase 2 Capstone Project: Return, Volatility & Portfolio Mathematics Calculator

> **Notice / Capstone Reservation Policy:**
> This capstone project is reserved exclusively for the student to build and code directly on PC. Do not place auto-generated scripts here. Follow the specifications below to implement the mathematical engine.

---

## 🎯 Project Overview
Quantitative portfolio management and algorithmic trading models rely heavily on linear algebra, multivariate calculus, and statistical matrices. Without mathematically rigorous return definitions, covariance estimators, and risk metrics, optimization models suffer from garbage-in, garbage-out syndrome (e.g. Markowitz error maximization).

In this capstone project, you will build an **End-to-End Financial Mathematics & Portfolio Risk Engine** in Python from scratch using NumPy and SciPy, executing matrix algebra, eigenvalue decomposition, annualized risk attribution, and Markowitz mean-variance efficient frontier optimization.

---

## 📋 Architecture & Core Requirements

### 1. Mathematical Return Engines
- Compute **Simple Arithmetic Returns**: $R_t = \frac{P_t - P_{t-1}}{P_{t-1}}$.
- Compute **Logarithmic (Continuously Compounded) Returns**: $r_t = \ln(P_t / P_{t-1})$.
- Prove and verify multi-period additivity: $\sum_{t=1}^T r_t = \ln(P_T / P_0)$.
- Convert daily return vectors to annualized expected return vectors ($\mu \times 252$).

### 2. Covariance, Correlation & Matrix Conditioning
- Calculate the sample variance-covariance matrix $\Sigma$:
  $$\Sigma = \frac{1}{N-1} (X - \bar{X})^T (X - \bar{X})$$
- Derive the correlation matrix $C = D^{-1} \Sigma D^{-1}$ where $D = \text{diag}(\sigma_1, \dots, \sigma_n)$.
- Check matrix positive semi-definiteness via **Eigenvalue Decomposition**:
  $$\Sigma v_i = \lambda_i v_i \quad (\text{Ensure all } \lambda_i \ge 0)$$
- Implement Ledoit-Wolf Shrinkage covariance estimation if the sample matrix is ill-conditioned ($\text{cond}(\Sigma) > 1000$).

### 3. Portfolio Variance & Matrix Vectorization
- Implement analytical portfolio variance using quadratic forms:
  $$\sigma_p^2 = \mathbf{w}^T \mathbf{\Sigma} \mathbf{w}$$
- Calculate portfolio expected return: $\mu_p = \mathbf{w}^T \mathbf{\mu}$.
- Calculate portfolio volatility: $\sigma_p = \sqrt{\mathbf{w}^T \mathbf{\Sigma} \mathbf{w}}$.
- Derive marginal contribution to risk (MCR) using partial derivatives:
  $$\text{MCR}_i = \frac{\partial \sigma_p}{\partial w_i} = \frac{(\mathbf{\Sigma} \mathbf{w})_i}{\sigma_p}$$

### 4. Markowitz Mean-Variance Optimization Engine
- Implement the constrained optimization solver using `scipy.optimize.minimize`:
  - **Objective:** Minimize $\mathbf{w}^T \mathbf{\Sigma} \mathbf{w}$
  - **Constraints:**
    1. Fully invested: $\sum_{i=1}^n w_i = 1$
    2. Long-only: $0 \le w_i \le 1$ for all $i$
    3. Target return: $\mathbf{w}^T \mathbf{\mu} = \mu_{\text{target}}$
- Generate the complete Efficient Frontier curve (50 target return points).
- Compute the **Maximum Sharpe Ratio (Tangency) Portfolio**:
  $$\text{SR} = \frac{\mu_p - R_f}{\sigma_p}$$
- Compute the **Global Minimum Variance (GMV) Portfolio**.

### 5. Principal Component Analysis (PCA) on Asset Returns
- Perform PCA on multi-asset market returns to isolate dominant market drivers:
  - First principal component: Systematic Market Factor ($\beta$).
  - Remaining components: Sector and idiosyncratic noise factors.

---

## 🛠️ Recommended Project Directory Structure
```
Project_Trading_Return_Volatility_Portfolio_Math_Calculator/
├── README.md               # Project Blueprint (This file)
├── math_engine/
│   ├── __init__.py
│   ├── returns.py          # Arithmetic & Log return engines
│   ├── covariance.py       # Covariance matrix & eigenvalue checks
│   ├── portfolio.py        # Matrix algebra for weights, volatility, MCR
│   ├── optimizer.py        # SciPy constrained quadratic programming
│   └── pca_analysis.py     # PCA factor extraction
├── tests/
│   ├── test_matrix_math.py # Verify eigenvalues, symmetry, quadratic forms
│   └── test_optimizer.py   # Verify weights sum to 1.0
└── main.py                 # CLI demonstration on multi-asset portfolio
```

---

## 🚀 Execution & Verification
1. Install dependencies: `pip install numpy scipy pandas matplotlib`.
2. Run `python main.py` with 5 sample assets (e.g., AAPL, MSFT, GOOGL, AMZN, JNJ).
3. Confirm:
   - Covariance matrix $\Sigma$ is symmetric and positive definite ($\lambda_{\min} > 0$).
   - Optimal portfolio weights sum exactly to $1.000000$.
   - Analytical risk matches Monte Carlo simulated portfolio risk within $0.01\%$.
