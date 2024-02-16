# 反復法による連立一次方程式の解法


## 連立一次方程式

$$
Ax = b
$$

ここで， $A$ は係数行列， $ x $ は解ベクトル， $ b $ は定数ベクトルである．

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


##  ヤコビ法 ( Jacobi method )

係数行列 $ A $ を対角成分 $ D $ とそれ以外の成分 $ L+U $ に分解する．

$$

A = D + L + U

$$


$$

D = 
\begin{pmatrix} 
    a_{11} & 0 & \dots  & 0 \\
    0 & a_{22} & \dots  & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \dots  & a_{nn}
\end{pmatrix}

\\

L+U =
\begin{pmatrix} 
    0 & a_{12} & \dots  & a_{1n} \\
    a_{21} & 0 & \dots  & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \dots  & 0
\end{pmatrix}

$$

分解した係数行列を連立一次方程式に代入し整理する．

$$

\begin{align*}
Ax &= b \\
(D+L+U)x &= b \\
x &= D^{-1} ( b - (L+U)x ) \\
\end{align*}

$$

ここで，右辺の解ベクトル $ x $ を $ k $ ステップ目，左辺の解ベクトル $ x $ を $ k+1 $ ステップ目とすることで現ステップから次ステップの解ベクトル $ x $ を更新する．

$$

x^{k+1} = D^{-1} ( b - (L+U)x^{k} )

$$


また，対角行列 $D$ の逆行列は対角成分の逆数とすればよいので簡単に求められる．

$$

D = 
\begin{pmatrix} 
    \frac{1}{a_{11}} & 0 & \dots  & 0 \\
    0 & \frac{1}{a_{22}} & \dots  & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \dots  & \frac{1}{a_{nn}}
\end{pmatrix}

$$


成分で記述すると次式となり，この式を繰り返して連立方程式の解を求める．

$$

x^{k+1}_i = \frac{1}{a_{ii}} ( b_i \sum_{j \neq i} a_{ij} x^{k}_{j} )

$$





## ガウス・ザイデル法

$$

x^{k+1}_i = \frac{1}{a_{ii}} \left( b_i - \sum^{i-1}_{j=1} a_{ij} x^{k+1}_j - \sum^{n}_{j=i+1} a_{ij} x^k_j \right)

$$


## SOR法

$$

x^{k+1}_i =
( 1 - \omega ) x^k_i +
\omega \frac{1}{a_{ii}} \left( b_i - \sum^{i-1}_{j=1} a_{ij} x^{k+1}_j - \sum^{n}_{j=i+1} a_{ij} x^k_j \right)

$$



## 収束判定

### 相対残差

反復法の収束判定には次式の相対残差 norm(b-A*x)/norm(b) を用いる． $ \varepsilon $ は許容誤差である．

$$

\frac{{\lVert b - A x^k \rVert}_2}{{\lVert b \rVert}_2} < \varepsilon

$$

ここで，2-ノルムの定義は以下である．

$$

{\lVert x \rVert}_2 = {\left( \sum^n_{i=1} {| x_i |}^2  \right)}^{\frac{1}{2}}

$$
