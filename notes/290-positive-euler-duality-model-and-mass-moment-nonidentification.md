# 290. 正整数 Euler、分次对偶与质量相对矩的联合非识别模型

日期：2026-09-06。主线 B1z 第4轮的限额辅助审计。

状态：[T/N] 固定曲线型有理 zeta 模型及联合非识别障碍；
[T] 所有 cutoff、任意正概率频率权的质量相对偶矩界与统一两通道增益；
[O] 真实数域的完整 Weil 桥梁及文献新颖性。
本篇不推进新的有限 Euler 扰动路线，不证明实际曲线、Riemann zeta 或任何
数域 \(L\) 函数违反 RH。它检验的是一组明确列出的结构和响应条件。
本轮主线实际算术削减另见289；本篇仅收束其通往 Weil 目标的逻辑接口。

## 1. 固定模型和主结论

固定整数 \(q\ge5\)；如需有限域风格，可取 \(q\) 为素数幂，但不预设几何实现。
令
\[
 P(t)=1-qt+qt^2=(1-\alpha t)(1-\beta t),\qquad
 Z(t)=\frac{P(t)}{(1-t)(1-qt)},
 \tag{1}
\]
\[
 \alpha=\frac{q+\sqrt{q^2-4q}}2,\qquad
 \beta=\frac{q-\sqrt{q^2-4q}}2.
 \tag{2}
\]
二根满足
\[
 \alpha+\beta=q,\quad \alpha\beta=q,\qquad
 1<\beta<\sqrt q<\alpha<q.
 \tag{3}
\]
例如 \(\beta>1\) 等价于
\(\sqrt{q^2-4q}<q-2\)，平方后即 \(0<4\)；
其余严格关系来自 \(q>4\)、正的判别式和根的乘积。
定义
\[
 N_n=q^n+1-\alpha^n-\beta^n,\qquad
 B_n=\frac1n\sum_{d\mid n}\mu(n/d)N_d .
 \tag{4}
\]
这里 \(\mu\) 是 Möbius 函数；\(N_n,B_n\) 不是数值拟合。

### 定理290-A [T/N]

同一个固定函数(1)具有以下性质。

1. 每个 \(B_n\) 都是正整数，且有真正收敛的正闭点 Euler 乘积
   \[
   Z(t)=\prod_{n\ge1}(1-t^n)^{-B_n}
       =\exp\left(\sum_{n\ge1}N_n\frac{t^n}{n}\right)
       \qquad(|t|<1/q).
   \tag{5}
   \]
2. 它满足曲线 genus-one 形状的精确函数方程
   \(Z(1/(qt))=Z(t)\)，并有有限分次外代数、非退化 Poincaré 配对、
   代数 Hard Lefschetz 同构及对应的超迹/行列式表示。
3. \(Z(q^{-s})\) 的分子零点位于
   \[
   \Re s=\theta:=\log_q\alpha>\tfrac12,\qquad
   \Re s=1-\theta<\tfrac12,
   \tag{6}
   \]
   而不是中心线。不存在与这些 Frobenius 数据相容的正定权1极化。
4. 用本函数自己的正对数导数系数和两个极点的正背景，形成第4节的有限
   prime-power lag 源。对每个共同 cutoff \(K\ge1\)，任意正概率频率测度
   \(\nu_K\)，以及每个整数 \(r\ge1\)，都有
   \[
   \int |\Delta_K(\xi)|^{2r}\,d\nu_K(\xi)
          \le 2^{2r}|\mu_K|^{2r}.
   \tag{7}
   \]
   特别，原 Brownian 物理权给 \(J_{4,K}\le16\mu_K^4\)，对每个 \(K\)
   都成立，不需要选共尾子列。相同两正通道还具有统一的
   common-multiplier Schur 增益。

本定理排除的是：仅凭这组正 Euler/对偶/迹公式数据、这些正权质量相对矩界
及两通道增益，就推出中心线的一般推理。它不排除增加独立几何极化、
真正完整 Weil 正性估计或其他未被模型满足的输入。

## 2. 正整数闭点数与收敛 Euler 乘积 [T]

### 2.1 先证 \(N_n\) 的正性和下界

令 \(x=\alpha/q,\ y=\beta/q\)。则 \(0<x,y<1\)，
\(x+y=1,\ xy=1/q\)。对每个 \(n\ge2\)，
\[
 x^n+y^n\le x^2+y^2=1-\frac2q.
 \tag{8}
\]
所以
\[
 N_1=1,\qquad
 2q^{n-1}+1\le N_n\le q^n+1\quad(n\ge2).
 \tag{9}
\]
所有 \(N_n\) 也是整数：幂和 \(S_n=\alpha^n+\beta^n\) 满足
\(S_0=2,S_1=q,S_n=qS_{n-1}-qS_{n-2}\)。

### 2.2 整性不能从正的点计数直接跳过

首先 \(Z(t)\in1+t\mathbb Z[[t]]\)。对任何这样的整数形式幂级数，
Euler 递归唯一给出整数 \(b_n\)，使
\[
 Z(t)=\prod_{n\ge1}(1-t^n)^{-b_n}
       \quad\hbox{在 }\mathbb Z[[t]]\hbox{ 中}.
 \tag{10}
\]
具体地，假设 \(b_1,\ldots,b_{n-1}\) 已选择，使
\[
 Z(t)\prod_{j<n}(1-t^j)^{b_j}=1+c_nt^n+O(t^{n+1}).
 \]
取 \(b_n=c_n\in\mathbb Z\) 就消掉第 \(n\) 项。
整数次幂的形式二项式系数仍为整数，所以递归合法，且每个系数只涉及有限步。
另一方面，对(1)取形式对数，得到
\(\log Z=\sum_{n\ge1}N_nt^n/n\)。
与(10)的形式对数比较即有
\[
 N_n=\sum_{d\mid n}d\,b_d.
 \tag{11}
\]
Möbius 反演给 \(b_n=B_n\)。这先证明了(4)确为整数，尚未假设其正性。

### 2.3 所有闭点数严格为正

直接算得
\[
 B_1=1,\qquad
 N_2=2q+1,\qquad B_2=(N_2-N_1)/2=q.
 \tag{12}
\]
对 \(n\ge3\)，每个真因子 \(d<n\) 都满足
\(d\le k:=\lfloor n/2\rfloor\)。因为 \(N_d>0\)，由(4)、(9)有
\[
 \begin{aligned}
 nB_n
 &\ge N_n-\sum_{\substack{d\mid n\\d<n}}N_d\\
 &\ge 2q^{n-1}+1-\sum_{d=1}^{k}(q^d+1).
 \end{aligned}
 \tag{13}
\]
而
\[
 \sum_{d=1}^{k}(q^d+1)
   =\frac{q^{k+1}-q}{q-1}+k
   <\frac{q^{k+1}}{q-1}+k
   <2q^{n-1}.
 \tag{14}
\]
最后一步可完全初等核对：\(k+1\le n-1\)，
\(1/(q-1)\le1/4\)，且 \(k\le q^{n-1}\)。
于是右端至多 \((5/4)q^{n-1}<2q^{n-1}\)。
式(13)给 \(B_n>0\)，结合整性即得正整数。

由(11)和全部 \(B_d\ge0\)，还得到
\[
 0<B_n\le\frac{N_n}{n}\le\frac{q^n+1}{n}.
 \tag{15}
\]
故在 \(|t|<1/q\) 内，
\[
 \sum_{n\ge1}B_n\sum_{j\ge1}\frac{|t|^{nj}}j
 \le\frac1{1-|t|}
       \sum_{n\ge1}\frac{q^n+1}{n}|t|^n<\infty.
 \tag{16}
\]
这给 Euler 对数和乘积的局部一致绝对收敛，(5)因此不只是形式等式。
可以把度数 \(n\) 的 \(B_n\) 个标签视为抽象闭点，赋予范数 \(q^n\)；
本篇没有把这些标签宣称为某个有限类型 scheme 的真实闭点。

## 3. 函数方程、分次代数和准确缺失的极化 [T/N]

### 3.1 曲线型函数方程与离线零点

直接计算
\[
 P(1/(qt))=\frac{P(t)}{qt^2},\qquad
 (1-1/(qt))(1-1/t)=\frac{(1-t)(1-qt)}{qt^2}.
 \tag{17}
\]
所以 \(Z(1/(qt))=Z(t)\) 作为有理函数恒等式成立。
由于 \(1<\beta<\alpha<q\)，分子的两个零点不与分母的
\(t=1,1/q\) 相消。
在 \(t=q^{-s}\) 下，它们具体为
\[
 s=\log_q\alpha+\frac{2\pi i j}{\log q},
 \qquad
 s=\log_q\beta+\frac{2\pi i j}{\log q},
 \qquad j\in\mathbb Z.
 \tag{18}
\]
由 \(\alpha\beta=q\) 有 \(\log_q\beta=1-\theta\)，故(6)成立。

还可直接给出 real-type、阶至多一的整函数作为分子完备函数
\[
 \Phi(s)=q^{s-1/2}P(q^{-s})
        =q^{s-1/2}+q^{1/2-s}-\sqrt q.
 \tag{19}
\]
它满足 \(\Phi(1-s)=\Phi(s)\)，零点正是(18)。
这里没有未构造的 Gamma 因子；这是有限域风格的周期谱模型，不是数域完成函数。

### 3.2 分次外代数、Poincaré 配对和代数 Hard Lefschetz

令 \(V=\mathbb R^2\)，并取定向体积形式
\(\omega(v,w)=v^{\mathsf T}Jw\)，其中
\[
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
 \]
使用外代数
\[
 H^0=\mathbb R,\qquad H^1=V,\qquad H^2=\mathbb R e_2,
 \tag{20}
\]
乘法规定为 \(v\wedge w=\omega(v,w)e_2\)，以 \(1\in H^0\) 为单位。
积分 \(\int_H:H^2\to\mathbb R\) 取 \(\int_H e_2=1\)。
于是 \(H^0\times H^2\) 的乘积配对和 \(H^1\times H^1\) 的交替配对都非退化。

定义
\[
 F_0=1,\qquad
 F_1=\begin{pmatrix}0&-q\\1&q\end{pmatrix},\qquad
 F_2=q.
 \tag{21}
\]
因为 \(\det F_1=q\)，直接有
\[
 F_1^{\mathsf T}JF_1=qJ.
 \tag{22}
\]
故 \(F\) 是分次代数同态，且在顶次积分上乘以 \(q\)；
配对的 Frobenius 对偶关系由乘法保持精确给出。
以 \(e_2\) 相乘定义 Lefschetz 算子 \(L_H\)。则
\[
 L_H:H^0\longrightarrow H^2
 \quad\hbox{是同构},\qquad
 FL_H=qL_HF.
 \tag{23}
\]
在这里的一维曲线型分次中，(23)就是代数 Hard Lefschetz 同构；
它不包含任何尚未说明的正性。

由 \(F_1\) 的特征多项式 \(X^2-qX+q\)，有
\[
 \sum_{i=0}^2(-1)^i\operatorname{Tr}(F_i^n)
      =1-\alpha^n-\beta^n+q^n=N_n,
 \tag{24}
\]
\[
 \prod_{i=0}^2\det(1-tF_i)^{(-1)^{i+1}}
      =\frac{1-qt+qt^2}{(1-t)(1-qt)}=Z(t).
 \tag{25}
\]
因此 Euler 对数、超迹与行列式是同一个函数的三种严格相容表示，
不是分别指定的无关数据。

### 3.3 哪条正性不能补写为既有结构

若在 \(H^1\) 的复化上有正定 Hermitian 型 \(h\)，满足
\[
 h(F_1v,F_1w)=q\,h(v,w),
 \tag{26}
\]
取 \(\alpha\) 的非零特征向量 \(v\) 就会得到
\((\alpha^2-q)h(v,v)=0\)，与 \(\alpha>\sqrt q\) 矛盾。
所以本模型不存在这种相容正极化。

式(26)仅用于**核验模型缺失什么**，不能将它倒写成未经解释的结构公理，
然后把“归一化后酉”再次作为 RH 的证明。
模型已经具有非退化对偶和代数 Lefschetz；没有的是能与 Frobenius 相容、
并真正约束其增长的正 Hodge/极化来源。
随意另选一个正内积不会修复这种相容性。

[078](078-ihara-ramanujan-hodge-structure.md)的一般 companion 定理在
\(A=[q]\) 时已经包含这里的二次根失纯性与 Hodge 型一正一负结论；
本篇不将这部分登记为新的结构定理。

## 4. 同一模型的实际正 lag 源和所有质量相对偶矩 [T]

固定 \(0<\sigma<1/2\)。对每个整数 \(K\ge1\)，取
\[
 Y=q^K,\qquad \tau=K\log q,\qquad
 w_Y(x)=x^{-\sigma}e^{-x/Y}.
 \tag{27}
\]
两个源使用完全相同的 cutoff \(1\le n\le K\)：
\[
 a_n=N_n(\log q)\,w_Y(q^n),\qquad
 b_n=(q^n+1)(\log q)\,w_Y(q^n),\qquad u_n=n\log q.
 \tag{28}
\]
这里 \(a_n\) 来自(5)的真实模型对数导数：
\[
 -\frac{d}{ds}\log Z(q^{-s})
       =(\log q)\sum_{n\ge1}N_nq^{-ns}\qquad(\Re s>1).
 \tag{29}
\]
背景 \(b_n\) 来自分母的两个极点 \(1,q\) 的迹 \(1+q^n\)。
它是**离散 pole/lattice 背景**，不是277中数域的
\(x^{-\sigma}e^{-x/Y}dx\) 连续背景。

置一侧有限正测度
\[
 \mathsf a_K=\sum_{n=1}^Ka_n\delta_{u_n},\qquad
 \mathsf b_K=\sum_{n=1}^Kb_n\delta_{u_n},
 \quad A=\mathsf a_K(\mathbb R),\ B=\mathsf b_K(\mathbb R),\
 S=A+B,\ M=A-B,\ \mu=M/S .
 \tag{30}
\]
因为 \(q^n+1-N_n=\alpha^n+\beta^n>0\)，有
\[
 \eta_K:=\mathsf b_K-\mathsf a_K\ge0,\qquad \eta_K(\mathbb R)=|M|>0.
 \tag{31}
\]
这是一条从同一固定模型逐项证明的有符号性质，不是改变源以后强制的平衡。

使用原居中核与 Fourier 约定
\[
 k_u=(\delta_u+\delta_{-u})/2-\delta_0,\qquad
 \widehat\omega(\xi)=\int e^{-i\xi u}\,d\omega(u),
 \]
\[
 p_K=\int k_u\,d\mathsf a_K(u),\quad
 c_K=-\int k_u\,d\mathsf b_K(u),\quad
 r_K=p_K+c_K=-\int k_u\,d\eta_K(u).
 \tag{32}
\]
定义
\[
 W_p(\xi)=\sum_{n=1}^Ka_n(1-\cos(\xi u_n)),\qquad
 W_c(\xi)=\sum_{n=1}^Kb_n(1-\cos(\xi u_n)),
 \quad \Delta_K=(W_p-W_c)/S.
 \tag{33}
\]
中心项完整保留，精确有
\[
 0\le\widehat r_K(\xi)=W_c(\xi)-W_p(\xi)
       =\int(1-\cos(\xi u))\,d\eta_K(u)\le2|M|.
 \tag{34}
\]
因此对每个频率，\(|\Delta_K(\xi)|\le2|\mu|\)。
对任意正概率测度积分，就得到(7)；\(\nu_K\) 可以随源、cutoff 和响应而变化。
证明不需要该概率测度是 Lebesgue 密度，也不需要它不依赖算术数据。

### 4.1 原 Brownian 物理权确实包含在内

对零质量紧支撑测度用 \(F_\omega(x)=\omega((-\infty,x])\) 表示 primitive。
置
\[
 D_K=\|F_{p_K}\|_2^2+\|F_{c_K}\|_2^2
     =\frac1{2\pi}\int_{\mathbb R}
         \frac{W_p(\xi)^2+W_c(\xi)^2}{\xi^2}\,d\xi .
 \tag{35}
\]
有限 lag 保证原点处 \(W_p,W_c=O(\xi^2)\)，无穷远处有界，所以积分有限；
又 \(b_1>0,u_1>0\)，故 \(D_K>0\)。
于是
\[
 d\nu_K^{\rm raw}(\xi)
     =\frac{W_p(\xi)^2+W_c(\xi)^2}{2\pi\xi^2D_K}\,d\xi
 \tag{36}
\]
是正概率测度。定义原完整物理积分
\[
 J_{4,K}=\frac1{S^4D_K}\frac1{2\pi}
 \int_{\mathbb R}
   \frac{|\widehat r_K(\xi)|^4
         (|\widehat p_K(\xi)|^2+|\widehat c_K(\xi)|^2)}
        {\xi^2}\,d\xi .
 \tag{37}
\]
代入(32)--(36)，它正是
\(\int|\Delta_K|^4d\nu_K^{\rm raw}\)。所以
\[
 \boxed{\qquad J_{4,K}\le16\mu_K^4
       \quad\hbox{对每个整数 }K\ge1.\qquad}
 \tag{38}
\]
这是全频积分结论，不是有限采样、不只是大高度尾，也不依赖共尾选择。

作为独立归一化检查，正 min-kernel 恒等式给
\[
 \|F_{r_K}\|_2^2
   =\frac12\iint\min(u,v)\,d\eta_K(u)d\eta_K(v)
   \le\frac{\tau M^2}{2}.
 \tag{39}
\]
结合(34)还有
\[
 Q_{\mathbb R}(r_K)
 :=\frac1{2\pi}\int\frac{|\widehat r_K|^4}{\xi^2}\,d\xi
 \le4M^2\|F_{r_K}\|_2^2\le2\tau M^4.
 \tag{40}
\]
此外，\(B\asymp_{q,\sigma}Y^{1-\sigma}\)，最后一项
\(b_K=(Y+1)(\log q)Y^{-\sigma}e^{-1}\asymp_{q,\sigma}Y^{1-\sigma}\)。
由于 \(A\le B\)，正 min-kernel 的最后一项和全部支撑的上界给
\[
 \frac{\tau b_K^2}{2}\le D_K\le\frac{\tau(A^2+B^2)}2,
 \qquad D_K\asymp_{q,\sigma}S^2\log Y .
 \tag{41}
\]
几何和同样给
\[
 |M|\asymp_{q,\sigma}Y^{\theta-\sigma},\qquad
 |\mu|\asymp_{q,\sigma}Y^{\theta-1}\longrightarrow0.
 \tag{42}
\]
这里 \(\theta-\sigma>0\)；下界保留 \(\alpha^K\) 的末项，上界用
\(\beta^n\le\alpha^n\) 与公比 \(q^{\theta-\sigma}>1\) 的有限几何和。
因此模型确实渐近平衡，预算不是靠 \(|\mu|\) 远离零而变成空话。
式(38)本身不需要(39)--(42)，故不隐藏对277连续通道定理的调用。

### 4.2 甚至统一两通道 Schur 增益也成立

由(9)有逐项比较
\[
 c_q:=\frac1{q+1}\le\frac{N_n}{q^n+1}\le1
          \quad(n\ge1).
 \tag{43}
\]
在 \(n=1\) 取等；\(n\ge2\) 时
\(N_n/(q^n+1)\ge2/q>1/(q+1)\)。
因此
\[
 c_qW_c(\xi)\le W_p(\xi)\le W_c(\xi)\quad\hbox{对全部 }\xi.
 \tag{44}
\]

取任意具有有限总变差、紧支撑的复 Borel 测度作为 common multiplier \(R\)，令
\(U_p=F_{p_K*R},U_c=F_{c_K*R}\)，并记
\(P_R=\|U_p\|_2^2,C_R=\|U_c\|_2^2,z_R=\langle U_p,U_c\rangle\)。
Plancherel 和 \(\widehat p_K=-W_p,\widehat c_K=W_c\) 给
\[
 -z_R=\int W_pW_c\,\frac{|\widehat R|^2}{2\pi\xi^2}\,d\xi,
 \qquad
 P_R+C_R=\int(W_p^2+W_c^2)
                    \frac{|\widehat R|^2}{2\pi\xi^2}\,d\xi .
 \tag{45}
\]
在非零能量点令 \(v=W_p/W_c\in[c_q,1]\)。因为
\(v/(1+v^2)\) 在 \([0,1]\) 递增，若 \(P_R+C_R>0\)，便有
\[
 \boxed{\qquad
 \frac{-z_R}{P_R+C_R}\ge
      \frac{c_q}{1+c_q^2}>0.
 \qquad}
 \tag{46}
\]
两个 symbols 同时为零的点没有贡献。证明适用于源依赖的多项式 common
multiplier，也适用于256所讨论的同类有限 degree-two multiplier。
若 transformed diagonal 为零，则相应比值不定义，只保留未归一化不等式。
这里不需要 fixed-core capture，也不借用数域 PNT。

所以本模型同时通过“质量相对偶矩有某个尺度一致的有限常数”和“统一两通道
Schur 增益”两项测试，仍有(18)的离线零点。

## 5. 联合障碍的最小输入、删除位置与适用范围

| 结构或输入 | 实际证明中的作用 | 不能自动替代的东西 |
|---|---|---|
| 固定 \(q\ge5\) 与二次多项式(1) | 产生分离的实 reciprocal 根 | 不是实际几何构造 |
| 整数形式级数和 Euler 递归 | 证明全部闭点数整性 | 仅 \(N_n>0\) 一般不给 \(B_n\in\mathbb Z_{\ge0}\) |
| (9)及真因子几何和 | 证明全部 \(B_n>0\) 与收敛乘积 | 不是只检查有限个 Euler 系数 |
| 同一个外代数和 Frobenius | 对偶、Lefschetz、超迹和行列式严格相容 | 代数 HL 不是相容正极化 |
| 极点迹背景与逐项 \(b_n-a_n>0\) | (34)及所有质量相对正权矩界 | 不能推广为一般有符号 discrepancy 的同一结论 |
| 正概率测度 | 从逐点界积分得到(7) | 带符号权或未控制总质量的权不在此推论内 |
| 逐项比例(43)及共同 multiplier | 所有 cutoff 的统一 Schur 增益 | 两个不同 multiplier 的相位不能用(45)处理 |

特别须保留以下范围限制。

1. 本篇是抽象正闭点 Euler 数据与函数域风格的周期 zeta 模型；
   没有构造真实有限类型曲线，也不把分次向量空间命名为已经存在的几何上同调。
2. 原数域 Abel 连续背景不是(28)。因此本模型不是实际 von Mangoldt
   prime--continuum 源的反例，不替代287或289的实际算术任务。
3. 即使 \(q\) 是素数幂，抽象度数闭点的 Euler 乘积也不应被误称为具有数域
   自守 \(L\) 函数全部局部/全局公理。本篇只使用(5)精确证明的乘积。
4. 与288不矛盾：本背景的迹为 \(q^n+1\)，不是288中固定的幂和上限 \(m\)；
   本篇没有将288有限多项式定理推广到有理或无限 Euler 变形。
5. 非识别针对的是(7)、(38)、(46)这种**某个有限统一常数存在**的测试。
   它不排除另一个经独立证明、具有额外结构或特殊尖锐阈值的判据；
   更不等于“任何可能的质量归一化方法都不能证明 RH”。

## 6. 返回194/195/256：准确的既有桥梁和当前停止点

### 6.1 不能说已经没有任何 response-to-Weil 映射

[194](194-brownian-primitive-energy-cauchy-certificate.md)已证明，
对有限 canonical response \(q_{\rm resp}\)，
\[
 \left|\int e^{-|u|}\,dq_{\rm resp}(u)\right|
       \le |T_{q_{\rm resp}}|+\sqrt{\mathcal E_B(q_{\rm resp})}.
 \tag{47}
\]
[195](195-response-specific-vaughan-brownian-gram.md)又给完整 common
divided-difference channelization：
\(\mathcal E_B(q_{\rm resp})=\mathbf1^*G_{\rm resp}\mathbf1\)。
结合187的合法 polynomial soft-effect 近似和完整 current/divisor 识别，
194-AHD 的条件证书要求
\[
 \sup_n\left\{
 |T_{q_n}|+\sqrt{\mathcal E_B(q_n)}
 +2\rho_n+5\epsilon_n\tau_n(|H_n|)+\eta_n
 \right\}<\infty.
 \tag{48}
\]
其中 \(\eta_n\) 包括必须独立核查的 Gamma、quadrature、tail 和识别误差。
所以存在明确的**条件桥梁**；问题不是完全没有公式。

### 6.2 256终点是相对两通道增益，不是(48)

[256](256-quartic-discrepancy-capture-and-conditional-schur-gain.md)
从质量相对四阶预算及其附加 fixed-core hypotheses 推出
\[
 -z_n\ge\varepsilon_*(P_n+C_n),\qquad
 \|U_{p,n}+U_{c,n}\|_2^2
       \le(1-2\varepsilon_*)(P_n+C_n),
 \qquad \varepsilon_*>0.
 \tag{49}
\]
这里 \(P_n+C_n\) 是**经过 degree-two multiplier 后**的
response diagonal；它不是(35)的 raw \(D_K\)。
式(49)没有给这个 diagonal 的绝对有界或跨 block 可和估计。
固定比例缩减一般不把一个发散正账本变为有界账本。

加入 Gamma 也不能只把旧 multiplier 下的一个新向量附在后面：
195的 multiplier 本身依赖完整 signed symbol、总质量和参数。
必须在同一构造中明确识别完整 \(q_n\) 与两通道 reduced \(q_n\)，
并估计它们的 constant mode、primitive 能量及其他误差。
此外，284/286/287/289使用固定 \(\sigma<1/2\) 和新的整数对角记录；
主 Weil current 的右半平面偏移、截断与 Cauchy trace 量词必须另行匹配。
本篇不把重新编号当作完成这个识别。

### 6.3 当前固定二阶软证书的显式发散项

[254](254-balanced-core-multiplier-degeneracy-and-energy-reweighting.md)
固定了
\[
 \rho=S/3,\qquad S=A+B.
 \tag{50}
\]
对实际 Abel 正源的共尾尺度，\(S\to\infty\)；例如固定
\(0<\sigma<1/2,\ Y\le N\le2Y\) 时连续 bulk 已给
\(S\gg_\sigma Y^{1-\sigma}\)。
因此若不改变这套固定二阶参数，直接试图使用(48)，其非负左端至少为
\[
 2\rho=2S/3\longrightarrow\infty .
 \tag{51}
\]
这已经阻止该**特定充分证书**自动闭合，即便另有理想的两通道相对增益。
固定 degree-two 的 polynomial approximation error
\(5\epsilon_n\tau_n(|H_n|)\) 也没有因此得到一致控制。

式(51)不是负迹真的发散、RH为假、或所有 Weil 桥梁不可能的证明。
它只说明必须提供新的低代价 one-sided certificate，或改变
\(\rho\)/逼近次数并重新审计 actual multiplier 和四阶归约；
不能继续将(48)中的软化代价当作已经消失的小误差。

同理，256没有给出197的实际压缩 Weil 矩阵 \(G\) 的
\(\operatorname{tr}G\)、\(\|G\|_{\rm HS}^2\) 或惯性改善。
Brownian 的 \(\int\Delta^4d\nu\) 和该矩阵的
\(\operatorname{tr}G^4\) 是不同对象；同为“四阶”不是迹公式。
欲改进简单/互异零点比例，仍需一条保持归一化、误差和同一尺度的显式矩阵映射。

## 7. 贡献范围与审计状态

本篇新增的联合测试在于：正整数闭点 Euler 数据、完整的曲线型分次/对偶/迹公式、
所有正权质量相对偶矩及统一两通道 Schur 增益，可以在同一个固定离线谱模型中共存。
缺失的正极化相容性被明确定位，没有藏入“广义 Weil 配置”名称。

其中二次 reciprocal 根、companion 极化失正、Brownian min-kernel、
正权积分界、Schur 比例界、有限 Euler 递归和标准矩不等式都是初等或既有机制。
078已经含有 companion/Hodge 部分；本篇不把这些组成步骤分别包装为
新的可发表定理。联合障碍的文献新颖性、足够一般的论文定位与外部同行审查仍[O]。
对本研究 Goal，内部完整证明和联合反例不自动等于阶段成果验收。

### 7.1 可复现有限检查 [E]

主代理新增并运行
[positive_euler_weil_model_probe.py](../scripts/positive_euler_weil_model_probe.py)；
carrier_audit 另行完整阅读脚本并独立复跑：

    python -B scripts/positive_euler_weil_model_probe.py

标准库检查通过，约0.04秒。脚本不写文件、不使用网络，也没有执行整个 CI。

- 对 \(q=5,7,8,9,16\)，精确整数运算检查 \(n\le80\) 的闭点整性、正性及
  点/闭点反演；独立形成 Euler 乘积的前20项并与(1)相乘验证。
  对偶矩阵、幂迹和 reciprocal 函数方程另以整数/有理算术核对。
  例如 \(q=5\) 时 \(B_1,\ldots,B_6=(1,5,25,110,500,2215)\)。
- Fraction 分支使用**几何权** \(w_n=2^{-n}\)，在
  \(K=2,4,6,8\) 检查物理偶矩 \(2,4,6,8\)。
  它通过实际卷积 \(r^j*p,r^j*c\) 的 primitive 平方范数求全频量，
  不是采样 Fourier 频率；所有有理不等式
  \(J_{2j}/|\mu|^{2j}\le2^{2j}\) 精确通过。
  几何权不是(27)的 Abel 权；它只复核(31)--(38)中仅使用正权的代数机制。

原 Abel 权则在单独的浮点分支使用 \(q=5,\sigma=1/4\)，结果为：

| \(K\)，\(Y=5^K\) | 完整 \(J_4/\mu^4\) | \(-\langle F_p,F_c\rangle/D_K\) |
|---:|---:|---:|
| 4 | 3.15663088786 | 0.456404381096 |
| 8 | 5.28950769195 | 0.497400290195 |
| 12 | 6.23915358217 | 0.499812860942 |
| 16 | 6.68240921869 | 0.499986009328 |
| 24 | 7.10115044354 | 0.499999920442 |

共同的系数因子 \(\log q\) 和 lattice spacing \(\log q\) 在这些齐次比值中
消去，脚本相应使用单位格点。表中 Schur 数值取 common multiplier
\(R=\delta_0\)，不是对所有 multiplier 的数值验证；
(46)的全 multiplier 量词由解析证明给出。
浮点 Abel 分支不是区间认证；它与 Fraction 几何权分支严格区分。
尽管 primitive 算法避免了数值频率截尾，浮点结果仍只标[E]。
本篇全 \(n\)、全 \(K\)、全矩次的结论均来自证明，不从上述有限范围外推。

完整正文由 carrier_audit 写出并逐段自审；主代理和 gap_exception_audit
另行完成全文独立定稿复核，结果通过。审计覆盖全 \(n\) 的 Euler 整性/正性、
对偶与极化区别、完整物理概率权、所有 common multiplier 的量词，以及
194/195/254/256 中原有条件桥梁与特定软证书的停止点。
有限复算通过不代替该数学审计，内部复核也不证明文献新颖性。
