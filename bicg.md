# 共役勾配法による連立一次方程式の解法


## 連立一次方程式

$$

Ax = b

$$

ここで， $ A $ は係数行列， $ x $ は解ベクトル， $ b $ は定数ベクトルである．

$$

\begin{pmatrix} 
    a_{11} & a_{12} & \dots  & a_{1n} \\
    a_{21} & a_{22} & \dots  & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \dots  & a_{nn}
\end{pmatrix}

\begin{pmatrix} 
    x_{1} \\
    x_{2} \\
    \vdots \\
    x_{n}
\end{pmatrix}

=

\begin{pmatrix} 
    b_{1} \\
    b_{2} \\
    \vdots \\
    b_{n}
\end{pmatrix}

$$


## 双共役勾配法 ( BiCG : BiConjugate Gradient )


シャドウ残差 $ r^* $ ，


### 計算手順


$$
\begin{align*}
1. & \; Compute \; r_0 := b - A x_0. \; Choose \; r^*_0 \; such \; that \; ( r_0 , r^*_0) \neq 0.
\\
2. & \; Set \; p_0 := r_0, p^*_0 := r^*_0
\\
3. & \; For \; k=0,1,..., until \; convergence \; Do:
\\
4. & \;\;\;\;\;\; \alpha_{k} := \frac{(r_k, r_k^*)}{(A p_k, p_k^*)}
\\
5. & \;\;\;\;\;\; x_{k+1} := x_k + \alpha_k p_k
\\
6. & \;\;\;\;\;\; r_{k+1} := r_k - \alpha_k A p_k
\\
7. & \;\;\;\;\;\; r_{k+1}^* := r_k^* - \alpha_k A^T p_k^*
\\
8. & \;\;\;\;\;\; \beta_k := \frac{ ( r_{k+1}, r_{k+1}^* )}{ ( r_k, r_k^* ) }
\\
9. & \;\;\;\;\;\; p_{k+1} := r_{k+1} + \beta_k p_k
\\
10. & \;\;\;\;\;\; p_{k+1}^* := r_{k+1}^* + \beta_k p_k^*
\\
11. & \; EndDo

\end{align*}

$$

ここで， $ (a,b) $ は内積であり成分で表すと次式となる．

$$

(a,b) = \sum_n a_n b_n

$$

また， $A^T$ は $ A $ の転置行列である。



## 安定化双共役勾配法 (BiCGStab : Bi-conjugate Gradient Stabilized)

### 計算手順

$$

\begin{align*}
1. & \; Compute \; r_0 := b - A x_0. \; Choose \; r^*_0 \; such \; that \; ( r_0 , r^*_0) \neq 0.
\\
2. & \; Set \; p_0 := r_0
\\
3. & \; For \; k=0,1,..., until \; convergence \; Do:
\\
4. & \;\;\;\;\;\; \alpha_{k} := \frac{(r_k, r_0^*)}{(A p_k, p_0^*)}
\\
5. & \;\;\;\;\;\; s_k := r_k - \alpha_k A p_k
\\
6. & \;\;\;\;\;\; \omega_{k} := \frac{(A s_k, s_k)}{(A s_k, A s_k)}
\\
7. & \;\;\;\;\;\; x_{k+1} := x_k + \alpha_k p_k + \omega_k s_k
\\
8. & \;\;\;\;\;\; r_{k+1} := s_k - \omega_k A s_k
\\
9. & \;\;\;\;\;\; \beta_k := \frac{ ( r_{k+1}, r_0^* )}{ ( r_k, r_0^* ) } \times \frac{\alpha_k}{\omega_k}
\\
10. & \;\;\;\;\;\; p_{k+1} := r_{k+1} + \beta_k ( p_k - \omega_k A p_k )
\\
11. & \; EndDo
\end{align*}

$$



## References

