# 273. 实际素数乘积的逆最近间距预算：异常邻点与行列式筛

日期：2026-09-05。主线：NCE-8 / B1y；论文归属：Vaughan--Brownian response。
本篇给完整 Markdown 证明，暂不排版 PDF。

状态：[T] 一般最近间距局部化、异常邻点删除、有限 Selberg 二次型；
[R] Chebyshev 上界、Bettin--Chandee 固定行列式公式；
[T/R] 实际 prime-product 的加权逆最近间距上界；
[O] 更低频实际联合响应和完整 Weil 配置。
不声称 RH/GRH、零点比例改进或文献新颖性已经完成。

## 1. 主定理

固定 \(0<\sigma<1/2\)，令 \(Y\) 为充分大的实数，
\(N\) 为任意满足 \(Y\le N\le2Y\) 的整数。置
\[
 L=\log Y,\quad W=\log(2L),\quad
 a_n=\mathbf1_{2\le n\le N}\Lambda(n)n^{-\sigma}e^{-n/Y},
 \quad b_k=\sum_{uv=k}a_ua_v.
 \tag{1}
\]
所有乘积纤维先精确聚合。对有限正支撑 \(\mathcal K=\{k:b_k>0\}\)，定义
\[
 \delta(k)=\min_{\substack{l\in\mathcal K\\l\ne k}}
                   |\log k-\log l|,\qquad
 \mathcal G(Y,N)=\sum_{k\in\mathcal K}\frac{b_k^2}{\delta(k)}.
 \tag{2}
\]
大 \(Y\) 下支撑至少有两点。

### 定理273-A [T/R]

对上述全部有限 cutoff 一致有
\[
 \boxed{\quad
 \mathcal G(Y,N)\ll_\sigma Y^{4-4\sigma}\log(2\log Y).
 \quad} \tag{3}
\]
特别，272-(G) 的单对数预算成立；实际上 (3) 比它更强。
这不是由平均支撑密度或有限实验推出的结论。

证明分为四项：小 product、远间距、高幂及其邻点污染、纯素数近碰撞。
前三项只需初等结构与267的系数预算；第四项重建一个可独立核验的
固定行列式上界筛，而不直接将旧221--233的内部标签作为证明。

## 2. 一般最近间距的局部化 [T]

设 \(\mathcal S\) 为至少含两点的有限正整数集，\(c_k\ge0\)，
\[
 d(k)=\min_{l\in\mathcal S,l\ne k}|k-l|,\quad
 B_j=\sum_{k\in\mathcal S}k^jc_k^2\quad(j=0,1).
\]
最近整数邻点和最近 log 邻点不必相同；但总有
\[
 \delta_{\mathcal S}(k)\ge\log(1+d(k)/k),\qquad
 \delta_{\mathcal S}(k)^{-1}\le1+k/d(k)\le2k.
 \tag{4}
\]
第一式对右邻点显然；左邻点满足
\(-\log(1-u)\ge u\ge\log(1+u)\)。
第二式用 \(\log(1+x)\ge x/(1+x)\)，最后用整数 \(d(k)\ge1\)、\(k\ge1\)。

对 \(H\ge1\) 定义正的近碰撞账本
\[
 E_H=\sum_{k\in\mathcal S}kc_k^2
       \sum_{\substack{l\in\mathcal S\\0<|l-k|\le H}}\frac1{|l-k|}.
 \tag{5}
\]
按 \(d(k)>H\) 或 \(d(k)\le H\) 分开，由 (4) 得
\[
 \sum_k\frac{c_k^2}{\delta_{\mathcal S}(k)}
 \le B_0+B_1/H+E_H.
 \tag{6}
\]
同样可只对一部分被计权的 \(k\) 求和，邻点集合仍保持 \(\mathcal S\)。
这是单向充分账本；不把 \(E_H\) 与真实最近间距能量称作等价。

267-D的实际系数预算为
\[
 B_0\ll_\sigma Y^{2-4\sigma}L^2,\qquad
 B_1\ll_\sigma Y^{4-4\sigma}L^2.
 \tag{7}
\]
固定
\[
 K=Y^2/L^4,\qquad H=\lceil L^2\rceil.
 \tag{8}
\]
小 product 的**被计权项**由 (4) 支付
\[
 \sum_{k\le K}\frac{b_k^2}{\delta(k)}
 \le2KB_0\ll_\sigma Y^{4-4\sigma}L^{-2}.
 \tag{9}
\]
远间距部分在 (6) 中只需 \(B_0+B_1/H\ll_\sigma Y^{4-4\sigma}\)。
这里并未从 gap 支撑删掉小 product。

## 3. 高幂自身和邻点污染的幂次节省 [T]

写 \(a=P+Q\)，其中 \(P\) 仅支撑在素数，\(Q\) 仅支撑在
\(p^j,\ j\ge2\)。乘法卷积满足
\[
 b=b_P+e,\qquad b_P=P*P,\quad e=2P*Q+Q*Q.
 \tag{10}
\]
\(b_P\) 的支撑上 \(\Omega(k)=2\)，\(e\) 的支撑上 \(\Omega(k)\ge3\)，
二者不交；所以 \(b_k^2=b_P(k)^2+e(k)^2\)，没有遗漏两部分交叉项。
\(e\) 内部的交叉仍须控制。

记 \(Q_{1,P}=\sum nP_n^2,\ Q_{1,Q}=\sum nQ_n^2\)。Chebyshev 给
\[
 Q_{1,P}\ll_\sigma Y^{2-2\sigma}L,\qquad
 Q_{1,Q}\ll_\sigma Y^{3/2-2\sigma}L.
 \tag{11}
\]
后一个界可直接由
\[
 \sum_{\substack{n\le X\\n=p^j,\ j\ge2}}\Lambda(n)
 =\sum_{2\le j\le\log_2X}\vartheta(X^{1/j})
 \ll\sqrt X+X^{1/3}\log X\ll\sqrt X
 \tag{12}
\]
推出：\(n\le2Y\)，\(1-2\sigma>0\)，并用
\(\Lambda(n)^2\le\log(2Y)\Lambda(n)\)。

每个“素数 × 高幂”的指定次序表示唯一，故
\[
 \sum_k k(P*Q)(k)^2=Q_{1,P}Q_{1,Q}.
 \tag{13}
\]
对 \(Q*Q\)，异素数底的有序分解至多两个。
同底链的加权系数为
\((\log p)p^{(1/2-\sigma)j}e^{-p^j/Y}\)，\(2\le j\le\log_pN\)；
267-C的几何尾/单峰证明在这个连续指数段仍给
\(\|\text{chain}\|_1\ll_\sigma\|\text{chain}\|_2\)。
Young不等式遂给
\(\sum k(Q*Q)(k)^2\ll_\sigma Q_{1,Q}^2\)。
结合 \((2u+v)^2\le8u^2+2v^2\)，得到
\[
 \sum_k ke(k)^2\ll_\sigma Y^{7/2-4\sigma}L^2.
 \tag{14}
\]
因此高幂被计权点在**完整支撑 gap**下的贡献也是 (14) 的规模。

还需单独控制低权重异常点改变纯点最近邻的影响。
Chebyshev素数计数给
\[
 |\operatorname{supp}P|\ll Y/L,\qquad
 |\operatorname{supp}Q|\ll\sqrt Y/L,
 \quad |\mathcal E|:=|\operatorname{supp}e|\ll Y^{3/2}/L^2.
 \tag{15}
\]
第二式用
\(\pi(\sqrt{2Y})+O(Y^{1/3}\log Y)\ll\sqrt Y/L\)；
第三式只数可能的乘积对，允许重复。

令 \(\delta_P(k)\) 是全部纯 prime-product 支撑自身的 gap。
若某纯点有 \(\delta(k)<\delta_P(k)\)，它在完整 log 排序中的某个相邻点必属
\(\mathcal E\)。每个异常点至多相邻两个纯点，因此受污染纯点不超过
\(2|\mathcal E|\)。纯点上
\[
 b_P(k)\le2\log^2(2Y)\,k^{-\sigma},\qquad
 \frac{b_P(k)^2}{\delta(k)}
 \le2k b_P(k)^2\ll_\sigma Y^{2-4\sigma}L^4.
 \tag{16}
\]
于是包括高幂自身和污染在内，严格有
\[
 0\le\mathcal G-
       \sum_{k\in\operatorname{supp}b_P}\frac{b_P(k)^2}{\delta_P(k)}
 \ll_\sigma Y^{7/2-4\sigma}L^2.
 \tag{17}
\]
这才允许转到纯 prime-product gap。不能只因异常点权重小而删除它们。

## 4. 有限 Selberg 权：主二次型的一致下界 [T]

本节重证所需有限筛代数，使 \(h\) 的统一性不隐藏在某个渐近定理常数中。
设 \(h\ne0,\ z\ge3\)，\(P(z)=\prod_{2<p\le z}p\)，并在奇素数上定义
\[
 g_h(p)=\frac2p-\frac{\mathbf1_{p\mid h}}p,\qquad
 t_h(p)=\frac{g_h(p)}{1-g_h(p)},\qquad
 \mathfrak S_2(h)=\prod_{\substack{p\mid h\\p>2}}\frac{p-1}{p-2}.
 \tag{18}
\]
将 \(g_h,t_h\) 乘法延拓到 \(P(z)\) 的 squarefree 因子。
取截断参数 \(\mathscr D\)，置
\[
 J(\mathscr D)=\sum_{\substack{d\le\mathscr D\\d\mid P(z)}}t_h(d).
 \tag{19}
\]
在 \(\lambda_1=1\)、\(\lambda_d=0\) 除非 \(d\le\mathscr D,d\mid P(z)\) 的
实系数中，精确有
\[
 \min_\lambda\sum_{d,e}\lambda_d\lambda_e g_h([d,e])
   =J(\mathscr D)^{-1},
 \qquad \text{可取全部 }|\lambda_d|\le1.
 \tag{20}
\]

证明：令 \(x_r=\sum_{r\mid d}\lambda_dg_h(d)\)。由 squarefree 乘法性，
该二次型等于
\(\sum_r x_r^2/t_h(r)\)，而 \(\sum_r\mu(r)x_r=\lambda_1=1\)。
Cauchy给下界 \(1/J\)，取 \(x_r=\mu(r)t_h(r)/J\) 达到它。
Möbius反演给
\[
 \lambda_d=\frac{\mu(d)}J
   \prod_{p\mid d}(1+t_h(p))\,
   J_d(\mathscr D/d),\qquad
 J_d(u)=\sum_{\substack{q\le u\\q\mid P(z)\\(q,d)=1}}t_h(q).
 \tag{21}
\]
将 \(q\le\mathscr D/d\) 及所有 \(e\mid d\) 映到互异的
\(eq\le\mathscr D\)，得到
\(J\ge\prod_{p\mid d}(1+t_h(p))J_d(\mathscr D/d)\)，故 \(|\lambda_d|\le1\)。
\(\square\)

令 \(\mathscr D=z^s\)，其中 \(s\) 是下述足够大的固定绝对常数。
Euler有限乘积
\[
 \mathcal E_h=\prod_{2<p\le z}(1+t_h(p))
            =\prod_{2<p\le z}(1-g_h(p))^{-1}
 \tag{22}
\]
使 \(t_h(d)/\mathcal E_h\) 成为 \(d\mid P(z)\) 上的概率。
其 \(\log d\) 期望为
\(\sum_{2<p\le z}g_h(p)\log p\le C_0\log z\)，
其中 \(C_0\) 绝对，来自 \(g_h(p)\le2/p\) 及 Chebyshev 分部积分。
固定 \(s>2C_0\)，Markov给 \(J(\mathscr D)\ge\mathcal E_h/2\)。

另一方面
\[
 \mathcal E_h=
 \frac{\prod_{2<p\le z}(1-2/p)^{-1}}
      {\prod_{2<p\le z,\ p\mid h}(p-1)/(p-2)}
 \ge \frac{c(\log z)^2}{\mathfrak S_2(h)}.
 \tag{23}
\]
因为 \(1-2/p\le(1-1/p)^2\)，且全素数 Euler 乘积
\(\prod_{p\le z}(1-1/p)^{-1}\ge\sum_{n\le z}1/n\ge\log z\)；
删除素数2仅损失固定因子。故
\[
 \boxed{\ J(\mathscr D)^{-1}\ll
           \mathfrak S_2(h)/(\log z)^2.\ } \tag{24}
\]
此证明对全部 \(h\ne0\) 一致，不要求 \(h\) 固定，也不使用筛的下界或破奇偶输入。

若非负有限序列 \(u_n\) 的除数和
\(A_q:=\sum_{q\mid n}u_n\) 满足 \(A_q=g_h(q)X+r_q\)，点态平方权及 (20) 给
\[
 \sum_{(n,P(z))=1}u_n
 \le X/J+\sum_{d,e\le\mathscr D}|r_{[d,e]}|.
 \tag{25}
\]
这是本篇使用的全部 Selberg 上界形式；序列可以带非整数非负权。

## 5. 纯素数固定行列式 incidence [T/R]

以下下界范围显式取 \(Y/(4L^4)\)，不沿用较窄的 \(Y/(4L)\)。
设四个素数 \(a,b,c,d\) 分别在 dyadic 箱 \(A,B,C,D\) 中，所有箱
落在 \([Y/(4L^4),2Y]\) 的固定倍数扩大内，且
\[
 AD\asymp BC\asymp R,\qquad 0<|h|\le H=\lceil L^2\rceil.
 \tag{26}
\]
端点 sharp cutoff 可由固定个非负光滑 majorants 覆盖；
两个未光滑坐标保留真实 prime 系数和原 cutoff。
所有涉及的素数最终均大于 \(|h|\) 和筛素数。

### 引理273-B

存在固定 \(c>0\)，一致于上述全部箱和 \(h\)，有
\[
 \sum_{\substack{ad-bc=h\\a,b,c,d\ {\rm prime}\\\text{四个箱中}}}
       (\log a)(\log b)(\log c)(\log d)
 \ll R\,\mathfrak S_2(h)+Y^{2-c}.
 \tag{27}
\]
常数不依箱端点、\(N\) 或 \(h\)；范围中的固定对数幂4是固定参数。

外部输入 [R] 为 Bettin--Chandee, *Trilinear forms with Kloosterman fractions*，
[Corollary 1，公式(1.4)](https://arxiv.org/pdf/1502.00769)。
正式发表信息：[Advances in Mathematics 328 (2018)](https://www.sciencedirect.com/science/article/pii/S0001870815304965)。
对 \(m_1n_2-m_2n_1=h\)，两个光滑权 \(f,g\) 和任意系数 \(\alpha,\beta\)，
主项是
\[
 \sum_{(n_1,n_2)\mid h}\frac{(n_1,n_2)}{n_1n_2}
 \alpha_{n_1}\beta_{n_2}
 \int f((x+h)/n_2)g(x/n_1)\,dx,
 \tag{28}
\]
误差为
\[
 O_\varepsilon\!\left(
 (\eta\mathcal R)^{3/2}\|\alpha\|_2\|\beta\|_2
 (N_1N_2)^{7/20}(N_1+N_2)^{1/4+\varepsilon}
 (M_1M_2)^\varepsilon\right),\quad
 \mathcal R=\frac{M_1N_2}{M_2N_1}+\frac{M_2N_1}{M_1N_2}.
 \tag{29}
\]
这里 \(\eta\) 控制固定光滑权的导数，所需规模条件与原文一致。

证明 (27)：先不在 \(a,c\) 上放 \(\log\) 权，而用光滑 \(w_A(a),w_C(c)\)
覆盖相应箱；\(b,d\) 仍为 prime，权为 \((\log b)(\log d)\)。
对 squarefree \(q_1,q_2\le\mathscr D^2\)，只含 \(p\le z\) 的奇素因子，
令 \(A_{q_1,q_2}(h)\) 是附加 \(q_1\mid a,\ q_2\mid c\) 的和。
取
\[
 a=q_1m_1,\ c=q_2m_2,\ n_1=q_2b,\ n_2=q_1d.
 \tag{30}
\]
对应原文的函数和系数为
\(f(u)=w_A(q_1u),\ g(v)=w_C(q_2v)\)，
\(\alpha_{q_2b}=\log b,\ \beta_{q_1d}=\log d\)，其余系数为零，
且 \(b,d\) 保持各自 sharp prime 箱及原 cutoff。
尺度为 \(M_1\asymp A/q_1,\ M_2\asymp C/q_2,\ N_1\asymp q_2B,\ N_2\asymp q_1D\)。
原文公式适用，\(\mathcal R\asymp1\)，\(\eta\) 一致有界。
当 \(b\ne d\)，因 \(b,d\) 是大于所有筛素数的不同素数，
\((q_2b,q_1d)=(q_1,q_2)\)。当 \(b=d\)，该素数大于 \(|h|\)，
行列式等式和 (28) 的 gcd 条件都排除这一对。
因此定义**显式去除 \(b=d\)** 的共同主量
\[
 X_h=\sum_{\substack{b,d\ {\rm prime}\\b\ne d\\\text{各自箱中}}}
 \frac{(\log b)(\log d)}{bd}
 \int w_A((x+h)/d)w_C(x/b)\,dx
 \ll R.
 \tag{31}
\]
最后的上界：积分长度 \(O(R)\)，除以 \(bd\asymp BD\)，
两次 Chebyshev 加权 prime 和为 \(O(BD)\)，不损失对数 aspect 因子。
光滑函数的两个参数在 (30) 后精确消去 \(q_1,q_2\)，故
\[
 A_{q_1,q_2}(h)=
 \mathbf1_{(q_1,q_2)\mid h}\frac{(q_1,q_2)}{q_1q_2}\,X_h
       +r_{q_1,q_2}(h).
 \tag{32}
\]
范数上界 \(\|\alpha\|_2\|\beta\|_2\ll YL\)，
\(N_1\le Cq_2Y,\ N_2\le Cq_1Y\)，所以
\[
 |r_{q_1,q_2}(h)|\ll_\varepsilon
 Y^{39/20+C\varepsilon}L
 (q_1q_2)^{7/20}(q_1+q_2)^{1/4+\varepsilon}.
 \tag{33}
\]
这里 \(C\) 是固定数；所有固定 polylog 因子也可吸收进任意小的 \(Y^\varepsilon\)。

对单序列 \(n=ac\) 筛，而不是对两个坐标各放一套平方权。
每个 \(p\mid q\) 的恒等式
\(\mathbf1_{p\mid ac}=\mathbf1_{p\mid a}+\mathbf1_{p\mid c}
 -\mathbf1_{p\mid a,\ p\mid c}\)
给至多 \(3^{\omega(q)}\) 个 (32) 的组合，主密度恰为 (18) 的 \(g_h(q)\)。
取
\[
 \mathscr D=Y^{1/1000},\qquad z=\mathscr D^{1/s},
 \tag{34}
\]
其中 \(s>2C_0\) 已固定。
所有 \(q_1,q_2\le\mathscr D^2\) 都远小于 \(Y/L^4\)。
展开 (25) 只有 \(O(\mathscr D^2)\) 对筛除数；
由 \(3^{\omega(q)}\ll_\varepsilon q^\varepsilon\) 及 (33)，总误差至多
\[
 Y^{39/20+C\varepsilon}L\,
         \mathscr D^{39/10+C\varepsilon}.
 \tag{35}
\]
指数 \(39/20+(39/10)/1000=1.9539<2\)。
先固定充分小的 \(\varepsilon>0\)，再吸收固定 log 因子，
即使补上 \((\log a)(\log c)\ll L^2\)，误差仍为 \(O(Y^{2-c})\)
（可缩小 \(c\)，例如取 \(c=1/100\)）。
由 (24)、\(\log z\asymp L\)、\(X_h\ll R\)，筛主项为
\(O(R\mathfrak S_2(h)/L^2)\)；补上两份 log 权即得 (27)。\(\square\)

此处采用的外部定理只是固定行列式带权公式。
有限筛二次型、局部密度、除数级别及 \(h\) 的统一性已在上文重建。
它不假定四素数相关渐近，不要求 RH 或 GRH。

## 6. 保留 product 权后的箱求和与主定理证明

先只用纯 prime-product 支撑，gap 邻点保留其全部纯点。
对 \(k>K\)、\(0<|l-k|\le H\)，有 \(l\ge K/2\)，
且 \(k,l\) 的每个 prime 因子均至少 \(Y/(4L^4)\)，因为另一个因子不超过 \(2Y\)。
故引理273-B的范围覆盖全部近碰撞，而不只覆盖固定 balanced 比例。

写 \(k=ad,\ l=bc\)。四个素数的 log 均 \(\asymp L\)，
prime-product 的表示重数至多2，于是每个近碰撞被计权项可上界为
\[
 k b_P(k)^2
 \ll k^{1-2\sigma}(\log a)(\log b)(\log c)(\log d).
 \tag{36}
\]
Abel指数在这个上界中仅被界为1。对 \(a=d\) 或 \(b=c\) 的 square products
重数更小，仍适用；不要求四个素数互异。

对固定 \(h\) 将四个因子作 dyadic 分箱，只有 \(AD\asymp BC\) 的箱可非空。
若直接数箱会损失 \((\log L)^4\)；本证明保留每箱 product 权 \(R^{1-2\sigma}\)。
写箱大小为固定倍数的
\[
 A=Y2^{-i},\quad D=Y2^{-j},\quad
 B=Y2^{-u},\quad C=Y2^{-v},\qquad i,j,u,v\ge0,
 \tag{37}
\]
有限个最顶部常数倍箱吸收到固定倍数中。
相容性给 \(u+v=i+j+O(1)\)。
固定 \(t=i+j\) 的相容箱数量 \(O((t+1)^2)\)，从而
\[
 \sum_{\rm compatible\ boxes}R^{2-2\sigma}
 \ll_\sigma Y^{4-4\sigma}
       \sum_{t\ge0}(t+1)^2\,2^{-(2-2\sigma)t}
 \ll_\sigma Y^{4-4\sigma}.
 \tag{38}
\]
这个几何求和是避免虚假的 \((\log L)^4\) 主项损失的具体一步。
误差则可粗数 \(O((\log L)^4)\) 个箱，并用
\(k^{1-2\sigma}\ll_\sigma Y^{2-4\sigma}\)。

奇异因子的 harmonic 平均有完整初等界
\[
 \sum_{1\le|h|\le H}\frac{\mathfrak S_2(h)}{|h|}
 \ll \log(2H).
 \tag{39}
\]
证明：展开
\(\mathfrak S_2(h)=\sum_{d\mid h,\ d\ {\rm odd\ squarefree}}
 \prod_{p\mid d}(p-2)^{-1}\)，交换正项求和，得到上界
\[
 C\log(2H)\prod_{p>2}\left(1+\frac1{p(p-2)}\right)<\infty\cdot\log(2H).
 \tag{40}
\]
负 \(h\) 同样处理。

将 (27)、(36)、(38)--(39) 合成，纯高 product 的近账本满足
\[
 E_{H,\,k>K}^{P}\ll_\sigma
 Y^{4-4\sigma}\log(2H)
 +Y^{4-4\sigma-c}(\log L)^4\log(2H)
 \ll_\sigma Y^{4-4\sigma}W.
 \tag{41}
\]
最后加上 (9) 小 product、(6)--(8) 的远间距和 \(B_0\)，以及 (17) 高幂误差，
全部被 (3) 控制。所有估计一致于原有限 \(N\in[Y,2Y]\)。\(\square\)

## 7. 删除审计、失效路线与模型范围

| 输入 | 具体用途 | 删除后的失效位置 |
|---|---|---|
| 实际整数 product、先聚合纤维 | (4)和 \(\Omega=2/\ge3\) 的支撑分离 | 任意实频率可任意靠近；同频未聚合时最近间距无定义 |
| \(0<\sigma<1/2\)、\(N\le2Y\) | 加权链、(16)、(36)的幂次和 finite prime 计数 | 此证明不覆盖中心参数或任意大的 cutoff；常数不在端点一致 |
| 异常点排序邻接计数 | (17)同时控制低权重邻点污染 | 只删其自身能量不能保证剩余 gap 不变 |
| BC 的严格幂次 saving [R] | (35)支付正幂筛除数级别 | 仅有无 saving 的格点误差不能完成该筛法证明 |
| 单序列 \(n=ac\) 筛、精确 \(X_h\) | 两个 log saving及 \(\mathscr D^{39/10}\)账本 | 分别放两套平方权不能沿用这个level账本；含 \(b=d\) 的 \(X_h\) 不给所写精确密度 |
| 每箱 \(R^{1-2\sigma}\) 权、相容 product | (38)让主项不损失箱总数 | 先统一取最大权再数箱只能得到较弱的迭代log界 |
| 272物理响应归一化与271质量选择 | 将 (3)接到274的频带归约 | 最近间距上界本身不是完整响应预算，更不是Weil正性 |

仅有平均稀疏度不足：可将 \(M\) 个单位权频率放在整数对
\(\{jQ,jQ+1\}\) 中，令 \(Q\to\infty\)。平均整数间距很大，仍有每点最近间距1；
因此不能以平均密度替换加权逆最近间距。这是抽象模型障碍，不是实际素数反例。

本轮没有使用固定频率 PNT 代替增长频带估计，也没有假定负指数有界或酉谱。
结论目前仅在 Riemann 的正 \(\Lambda\) 源核验。一般复 L 系数、
Dedekind prime ideals、函数域 degree 乘积需要另证适合的纤维和 incidence；
不能自动推广，亦不建立两类 Weil 结构的等价。

274给 Weil 型响应接口、复现数据和下一最小引理。
内部定稿复核：carrier_audit 独立检查行列式参数、共同主量、筛级别与带权分箱；
gap_exception_audit 独立检查全部证明，并重读BC原始 Corollary 1 及第9节。
两份复核均通过；按共同反馈把(25)中的原序列权 \(u_n\) 与整除和 \(A_q\)
明确区分，且补出(30)后的外部定理逐项对应。
旧221-(15)也显式去除 \(b=d\)，以保证所写共同主密度精确。
上述是独立代理的内部审计，不是外部同行评审；新颖性及外部评审仍 [O]。
