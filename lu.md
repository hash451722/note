# 直接法による連立一次方程式の解法


## LU分解 ( LU decomposition )


$$
\begin{align*}
\begin{pmatrix}
    a_{11} & a_{12} & a_{13} & a_{14} \\
    a_{21} & a_{22} & a_{23} & a_{24} \\
    a_{31} & a_{32} & a_{33} & a_{34} \\
    a_{41} & a_{42} & a_{43} & a_{44}
\end{pmatrix}

&=

\begin{pmatrix}
    1 & 0 & 0 & 0 \\
    l_{21} & 1 & 0 & 0 \\
    l_{31} & l_{32} & 1 & 0 \\
    l_{41} & l_{42} & l_{43} & 1
\end{pmatrix}

\begin{pmatrix}
    u_{11} & u_{12} & u_{13} & u_{14} \\
    0 & u_{22} & u_{23} & u_{24} \\
    0 & 0 & u_{33} & u_{34} \\
    0 & 0 & 0 & u_{44}
\end{pmatrix}

\\
\\
&=

\begin{pmatrix}
    u_{11} & u_{12} & u_{13} & u_{14}
    \\
    l_{21} u_{11} &
    l_{21} u_{12} + u_{22} &
    l_{21} u_{13} + u_{23} &
    l_{21} u_{14} + u_{24}
    \\
    l_{31} u_{11} &
    l_{31} u_{12} + l_{32} u_{22} &
    l_{31} u_{13} + l_{32} u_{23} + u_{33} &
    l_{31} u_{14} + l_{32} u_{24} + u_{34}
    \\
    l_{41} u_{11} &
    l_{41} u_{12} + l_{42} u_{22} &
    l_{41} u_{13} + l_{42} u_{23} + l_{43} u_{33} &
    l_{41} u_{14} + l_{42} u_{24} + l_{43} u_{34} + u_{44}&
\end{pmatrix}

\end{align*}

$$

以上より， $ u_{ij} $ と $ l_{ij} $ をまとめる． 

$$

u_{ij} = a_{ij} - \sum_{k=1}^{i-1} l_{ik} u_{kj}
\\
l_{ij} = ( a_{ij} - \sum_{k=1}^{j-1} l_{ik} u_{kj} ) / u_{jj}

$$



## Solve

$$

A \vec{x} = \vec{b}
\\
LU \vec{x} = \vec{b}

$$

ここで， $ y = U \vec{x} $ とすると，

$$

L \vec{y} = \vec{b}
\\
U \vec{x} = \vec{y}

$$

を順番に解いて，解ベクトル $ x $ を求める．


### Step 1.  $ Ly=b $

$$

\begin{pmatrix}
    1 & 0 & 0 & 0 \\
    l_{21} & 1 & 0 & 0 \\
    l_{31} & l_{32} & 1 & 0 \\
    l_{41} & l_{42} & l_{43} & 1
\end{pmatrix}

\begin{pmatrix}
    y_1 \\ y_2 \\ y_3 \\ y_4
\end{pmatrix}

=

\begin{pmatrix}
    b_1 \\ b_2 \\ b_3 \\ b_4
\end{pmatrix}

$$

$$

\begin{align*}
y_1 &= b_1 \\
l_{21} y_1 + y_2 &= b_2 \\
l_{31} y_1 + l_{32} y_2 + y_3 &= b_3 \\
l_{41} y_1 + l_{42} y_2 + l_{43} y_3 + y_4 &= b_4
\end{align*}

$$

$$

\begin{align*}
y_1 &= b_1 \\
y_2 &= b_2 – l_{21} y_1 \\
y_3 &= b_3 – l_{31} y_1 – l_{32} y_2 \\
y_4 &= b_4 – l_{41} y_1 – l_{42} y_2 – l_{43} y_3
\end{align*}

$$

$$

y_i = b_i – \sum_{j=1}^{i-1} l_{i j} y_{j}

$$


### $ Ux = y $

$$

\begin{pmatrix}
    u_{11} & u_{12} & u_{13} & u_{14} \\
    0 & u_{22} & u_{23} & u_{24} \\
    0 & 0 & u_{33} & u_{34} \\
    0 & 0 & 0 & u_{44}
\end{pmatrix}
\begin{pmatrix}
    x_1 \\ x_2 \\ x_3 \\ x_4
\end{pmatrix}
=
\begin{pmatrix}
    y_1 \\ y_2 \\ y_3 \\ y_4
\end{pmatrix}

$$

$$

\begin{align*}
u_{44} x_{4} &= y_4 \\
u_{33} x_3 + u_{44} x_4 &= y_3 \\
u_{22} x_2 + u_{23} x_3 + u_{24} x_4 &= y_2 \\
u_{11} x_1 + u_{12} x_2 + u_{13} x_3 + u_{14} x_4 &= y_1
\end{align*}

$$


$$

\begin{align*}
x_4 &= \frac{1}{u_{44}} y_4 \\
x_3 &= \frac{1}{u_{33}} \bigl( y_3 – u_{44} x_4\bigr) \\
x_2 &= \frac{1}{u_{22}} \bigl( y_2 – u_{23} x_3 – u_{24} x_4 \bigr) \\
x_1 &= \frac{1}{u_{11}} \bigl( y_1 – u_{12} x_2 – u_{13} x_3 – u_{14} x_4 \bigr)
\end{align*}

$$


$$

x_i = \frac{1}{u_{ii}} \bigl( y_i – \sum_{j=i+1}^{n} u_{i j} x_j \bigr)

$$


