# 下一连接候选：实际系数的独立计算

2026-09-21。原始共同工具回包保存为[f1-split-transfer-full-review.raw.json](f1-split-transfer-full-review.raw.json)；正文仅作标题、路径及行末空白整理。

**原定义下成立：\(K\) 使 \(e,v,u\) 平行，而压缩提升 \(T\) 留下属于 \(I\) 的有界残差；该残差确实可以非零。** 以下直接使用 [414](../../notes/414-f1-deep-boundary-unitary-and-time-defect.md) 的实际系数，不依赖抽象角内酉关系。未读取或重审 416，未修改文件、未运行 Git。

1. **先计算 \(K\) 与关键的角内导数。**

记
\[
c_n(t)=c(t-nL),\quad d_n(t)=c'(t-nL),
\]
\[
c_{n,M}(t)=c(t-nL-M),\quad
d_{n,M}(t)=c'(t-nL-M).
\]
平方分割及其导数给出
\[
\sum_n c_n^2=1,\qquad \sum_n c_nd_n=0,
\tag{1}
\]
并且在 \(t-M\) 处同样成立。求导合法：这些平移和局部有限。

交叉积乘法约定为
\[
(fU_g)(bU_r)=f(t)b(t-\ell_g)U_{g+r}.
\]
直接求第 \(n\) 个 \(p\)-系数：
\[
(\delta e\,e)_n
=\sum_m(d_0c_m+c_0d_m)c_mc_n=d_0c_n,
\]
\[
(e\,\delta e)_n=c_0d_n.
\]
故
\[
\boxed{
K=[\delta e,e]
=\sum_n\kappa_n(t)U_p^n,\qquad
\kappa_n=d_0c_n-c_0d_n.
}
\tag{2}
\]

现在计算 \(\delta v\)，其 \((n,1)\) 系数为
\[
(\delta v)_{(n,1)}=d_0c_{n,M}+c_0d_{n,M}.
\]
由 (1)，
\[
(e\,\delta v)_{(n,1)}
=\sum_m c_0c_m
  (d_mc_{n,M}+c_md_{n,M})
=c_0d_{n,M},
\]
\[
(\delta v\,e)_{(n,1)}
=\sum_m(d_0c_{m,M}+c_0d_{m,M})
 c_{m,M}c_{n,M}
=d_0c_{n,M}.
\]
再右乘 \(e\)，得到
\[
\boxed{
(e\,\delta v\,e)_{(n,1)}
=c_0c_{n,M}\sum_m d_{m,M}c_{m,M}=0.
}
\tag{3}
\]
这就是需要的实际系数验证；没有从 \(v^*v=vv^*=e\) 反推它。

甚至可以直接核准交换子：
\[
(Kv)_{(n,1)}
=\sum_m(d_0c_m-c_0d_m)c_mc_{n,M}
=d_0c_{n,M},
\]
\[
(vK)_{(n,1)}
=\sum_m c_0c_{m,M}
(d_{m,M}c_{n,M}-c_{m,M}d_{n,M})
=-c_0d_{n,M}.
\]
因此
\[
\boxed{\delta v=[K,v].}
\tag{4}
\]
同一计算给
\[
(Ke)_n=d_0c_n,\qquad(eK)_n=-c_0d_n,
\]
故
\[
\delta e=[K,e],\qquad
\boxed{\delta u=[K,u].}
\tag{5}
\]

这里真正使用的是 \(c\) **实值**及平方分割；非负性并非这些消去等式额外需要的条件。

2. **\(K\) 的位置、反自伴性与光滑性。**

设 \(\operatorname{supp}c\subset[a,b]\)。因为 \(c'\) 也支持于该紧集，\(\kappa_n\ne0\) 必须有
\[
|n|L\le b-a.
\]
所以 \(K\) 只有有限个 \(p\)-群次数，没有 \(q\)-次数，且每个系数属于 \(C_c^\infty(\mathbb R)\)。

由实值性，
\[
\kappa_{-n}(t-nL)=-\kappa_n(t),
\]
这正是交叉积伴随公式所需的关系。因此
\[
K^*=-K,\qquad
\|K\|\le\sum_n\|\kappa_n\|_\infty<\infty.
\tag{6}
\]

必须区分两个代数中的位置：

- 在边界代数中，\(K\in B=C_0(\mathbb R)\rtimes p^{\mathbb Z}\subset A_D\)。
- 经 414 的表示进入原交叉积后，\(K\in M(A)\)，**实际上 \(K\notin A\)**。

后一断言可直接验证。首先
\[
\sum_n\kappa_n(t)c_n(t)=c'(t).
\]
所以 \(K=0\) 将迫使 \(c'=0\)，与非零紧支平方分割矛盾。任一非零 \(\kappa_n(t)\) 拉回 \(Y\) 后都在 \(j,k\) 方向常值，不能属于 \(C_0(Y)\)；例如沿 \(j\to-\infty\) 不衰减。因此有限 Fourier 系数唯一性排除 \(K\in A\)。

所有迭代 \(\delta^rK\) 仍有相同的有限群支、紧时间支集和有界系数。\(e,v,u,K,T\) 都对时间作用范数光滑。注意符号：
\[
\beta_s f(t)=f(t-s)
\quad\Longrightarrow\quad
\left.\frac{d}{ds}\beta_s\right|_{s=0}=-\delta.
\]

在 414 的共同 Hilbert 空间上，取
\[
\operatorname{Dom}D_c
=H^1(\mathbb R_t;\mathcal H_{\mathrm{rad},p}
 \otimes\mathcal H_{\mathrm{rad},q}),
\qquad
D_c=\partial_t-K.
\]
有限光滑系数与平移保证上述算子保持此定义域，并且
\[
[D_c,a]=\delta a-[K,a].
\]
于是
\[
[D_c,e]=[D_c,v]=[D_c,u]=0.
\tag{7}
\]
此外 \(D_c\) 是 \(\partial_t\) 的有界反自伴扰动，仍在该定义域上反自伴。这里的平行性是协变导数为零，并非原时间作用 \(\beta\) 下固定。

3. **\([K,Q]\in I\)，而裸 \([K,Q_p]\notin A\)。**

写
\[
H(j)=\mathbf1_{\{j\ge0\}\cup\{\infty\}},\qquad
Q_p=H(j),\quad Q_q=H(k).
\]
由于 \(K\) 只有 \(p\)-群支，
\[
[K,Q_q]=0,\qquad
[K,Q]=[K,Q_p]Q_q.
\]
具体系数为
\[
\boxed{
[K,Q]
=\sum_n\kappa_n(t)
 \bigl(H(j-n)-H(j)\bigr)H(k)\,U_p^n.
}
\tag{8}
\]
其中
\[
H(j-n)-H(j)=
\begin{cases}
-1,&n>0,\ 0\le j<n,\\
+1,&n<0,\ n\le j<0,\\
0,&\text{其他情形，包括 }j=\infty.
\end{cases}
\tag{9}
\]
因此每个系数支持于
\[
\{\text{有限多个整数 }j\}
\times\bigl(\mathbb Z_{\ge0}\cup\{\infty\}\bigr)
\times\{\text{紧时间集}\}.
\]
这是 \(Y\setminus D\) 内的紧集，故
\[
\boxed{[K,Q]\in C_c(Y\setminus D)\rtimes_{\rm alg}\Gamma\subset I.}
\tag{10}
\]

若去掉 \(H(k)\)，系数便沿全部 \(k\) 常值，在 \(k\to-\infty\) 时不衰减。又 \(\kappa_0=0\) 而 \(K\ne0\)，所以至少有一个非零 \(\kappa_n,\ n\ne0\)，相应的 (9) 也非零。因而在当前假设下，实际有
\[
\boxed{[K,Q_p]\notin A,}
\]
不只是“尚未证明属于 \(A\)”。

4. **压缩提升的准确残差。**

令
\[
R=[K,Q]\in I,\qquad a=u-1,\qquad T=1+QaQ.
\]
由于 \(\delta Q=0\)、\(\delta a=[K,a]\)，直接展开得到
\[
\begin{aligned}
[D_c,T]
&=Q\delta aQ-[K,QaQ]\\
&=-RaQ-QaR.
\end{aligned}
\]
所以
\[
\boxed{
[D_c,T]
=-[K,Q]\,(u-1)Q-Q(u-1)[K,Q]\in I.
}
\tag{11}
\]
这是定义域上交换子的有界延拓。乘子乘法保持闭理想 \(I\)；也可以逐系数检查：有限群平移只把 (8) 的紧支集移到另外的紧支集。

残差仍只有有限群支，时间系数光滑紧支，所有时间导数仍属于 \(I\)。

5. **两个明确反例，限定可加强的范围。**

首先，原定义内确有
\[
[D_c,T]\ne0.
\]
取 \(0<\varepsilon<L/4\)，选光滑非降函数 \(\theta\)，在 \(r\le-\varepsilon\) 为 \(0\)，在 \(r\ge\varepsilon\) 为 \(\pi/2\)，端点平坦。定义合法平方分割
\[
c(t)=
\begin{cases}
0,&t<-\varepsilon,\\
\sin\theta(t),&-\varepsilon\le t\le\varepsilon,\\
1,&\varepsilon\le t\le L-\varepsilon,\\
\cos\theta(t-L),&L-\varepsilon\le t\le L+\varepsilon,\\
0,&t>L+\varepsilon.
\end{cases}
\]
在 \(t=L+r,\ |r|<\varepsilon\)，仅有
\[
c(t)=\cos\theta(r),\qquad c(t-L)=\sin\theta(r)
\]
这两个非零平移，且
\[
\kappa_1(t)=-\theta'(r).
\]
将 \(u-1=-e+v\) 代入 (11)，其 \(q\)-次数零部分为
\[
ReQ+QeR.
\]
在 \(j=k=0,\ t=L+r\)，该部分的单位群系数直接等于
\[
\boxed{
([D_c,T])_{(0,0)}(0,0,L+r)
=2\theta'(r)\sin\theta(r)\cos\theta(r).
}
\tag{12}
\]
选过渡内部 \(\theta'(r)>0\) 的点便严格为正。含 \(v\) 的项具有 \(q\)-次数 \(1\)，不能抵消它。这给出原定义范围内的非零残差。

其次，若离开原来的具体 \(v\)，角内酉关系确实不足。令
\[
f(t)=e^{2\pi it/L},\qquad \widetilde v=f(t)v.
\]
由于 \(f\) 是 \(L\)-周期函数，它与 \(e\) 交换，因而
\[
\widetilde v^*\widetilde v
=\widetilde v\widetilde v^*=e.
\]
但
\[
\boxed{
e\,\delta(\widetilde v)\,e
=\frac{2\pi i}{L}\widetilde v\ne0.
}
\tag{13}
\]
这个例子仍具有有限群支和光滑紧时间系数，说明 (3) 必须依赖原始 \(c(t)c(t-nL-M)\) 的具体计算。

上述结果只建立原交叉积中的连接、平行性及 \(I\)-值压缩缺陷；没有引入或假定规范算术读出、相对 Chern 特征。
