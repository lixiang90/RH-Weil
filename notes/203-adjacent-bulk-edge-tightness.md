# 203. Adjacent product bulk edge tightness 与端点消失阶

日期：2026-09-01

分支：MOM-1 / 路线 A

状态：理想 translation-invariant bulk 的 exact-product adjacent edge tightness
及其显式速率为 [T]；真实有限 Gabor 压缩到 bulk 的局部传递为 [O]；数值脚本
只审计有限算术和极限常数，标为 [E]。

## 1. 本轮结论

笔记 201 的 adjacent 通道下一步包含两个逻辑不同的任务：

1. exact-product diagonal 在乘积端点层
   \(X^{1-\delta}<ab\le X\) 的质量是否一致趋零；
2. 真实有限 Gabor 压缩能否以不损失该 tightness 的方式传到理想 bulk。

本轮完成第 1 项。结论只用

\[
 \sum_{n\le x}\frac{\Lambda(n)^2}{n}
 =\frac12(\log x)^2+O(\log x),
\tag{1}
\]

不需要素数对猜想、零密度估计或 RH。若窗口在两个端点具有消失阶
\(\kappa\ge0\)，则 adjacent bulk edge 的绝对质量为

\[
 O_\psi(\delta^{2\kappa+2}).
\tag{2}
\]

平窗给 \(O(\delta^2)\)，端点余弦窗
\(\psi(u)=\cos(\pi u)\mathbf 1_{|u|\le1/2}\) 给
\(O(\delta^4)\)。因此 adjacent 的 arithmetic endpoint mass 本身不是
MOM-1 的剩余硬核；未完成部分已经严格缩成 finite-to-bulk 局部传递误差以及
alternating/Farey ratio Gram。

## 2. 抽象 path overlap

把 \(\psi\) 以零延拓到全线，并定义

\[
 \mathcal W_\psi(s_0,s_1,s_2,s_3)
 =\int_{\mathbb R}\prod_{j=0}^3\psi(u+s_j)\,du.
\tag{3}
\]

假设 \(\psi\) 有界、非负、支撑于 \([-1/2,1/2]\)，且存在
\(C,M<\infty\)、\(\kappa\ge0\) 使

\[
 \|\psi\|_\infty\le M,
\qquad
 \psi(-1/2+x),\ \psi(1/2-x)\le Cx^\kappa
 \quad(0\le x\le1).
\tag{4}
\]

这里 \(\kappa=0\) 只表示有界端点，不声称窗口消失。

### 引理 AEL（endpoint path bound）[T]

若 \(0\le s_1,s_3\le s_2\le1\)，并令 \(\ell=1-s_2\)，则

\[
 |\mathcal W_\psi(0,s_1,s_2,s_3)|
 \le K_{\psi,\kappa}\ell^{2\kappa+1},
\tag{5}
\]

其中

\[
 K_{\psi,\kappa}
 =C^2M^2\,\mathrm B(\kappa+1,\kappa+1).
\tag{6}
\]

#### 证明

因 shifts 包含最小值 \(0\) 与最大值 \(s_2\)，四个支撑的公共交集恰落在
\([-1/2,1/2-s_2]\)，长度为 \(\ell\)。写 \(u=-1/2+x\)，
\(0\le x\le\ell\)。式 (4) 对极端的两个因子给

\[
 \psi(u)\le Cx^\kappa,
 \qquad
 \psi(u+s_2)\le C(\ell-x)^\kappa,
\]

另两个因子至多为 \(M\)。积分即得

\[
 C^2M^2\int_0^\ell x^\kappa(\ell-x)^\kappa dx
 =K_{\psi,\kappa}\ell^{2\kappa+1}.
\qquad\square
\]

## 3. adjacent exact-product edge functional

置 \(X=e^L\)、\(r_n=\log n/L\)。对 \(0<\delta\le1\)，定义一个
adjacent 符号词 \((+,+,-,-)\) 的 exact-product edge 绝对泛函

\[
 \begin{aligned}
 \mathfrak E_{L,\delta}^{\rm adj}(\psi)
 :=\frac1{L^4}
 \sum_{\substack{a,b,c,d\ge2\\ab=cd\\X^{1-\delta}<ab\le X}}
 &\frac{\Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)}{ab}\\
 &\times
 \left|\mathcal W_\psi(0,r_a,r_{ab},r_d)\right|.
 \end{aligned}
\tag{7}
\]

分母确为 \(ab\)，因为在 \(ab=cd\) 上
\(\sqrt{abcd}=ab\)。式 (7) 是 one-cut translation-invariant bulk 中
相应 product-diagonal 的无 \((2\pi)\) 常数版本；所有被略去的全局正规化常数
与 \(\delta\) 无关。

### 定理 AEM（adjacent bulk edge tightness）[T]

在式 (4) 的条件下，令 \(q=2\kappa+1\)。则

\[
 \limsup_{L\to\infty}
 \mathfrak E_{L,\delta}^{\rm adj}(\psi)
 \le
 \frac{K_{\psi,\kappa}}3
 \int_0^\delta t^q(1-t)^3\,dt,
\tag{8}
\]

从而

\[
 \limsup_{L\to\infty}
 \mathfrak E_{L,\delta}^{\rm adj}(\psi)
 \le
 \frac{K_{\psi,\kappa}}{6(\kappa+1)}
 \delta^{2\kappa+2}.
\tag{9}
\]

特别地，

\[
 \begin{array}{c|c|c|c}
 \psi&\kappa&K_{\psi,\kappa}&\text{式 (9) 上界}\\ \hline
 \mathbf1_{[-1/2,1/2]}&0&1&\delta^2/6\\
 \cos(\pi u)\mathbf1_{|u|\le1/2}&1&\pi^2/6&\pi^2\delta^4/72.
 \end{array}
\tag{10}
\]

#### 证明

由于 \(\Lambda(n)\ne0\) 只在素数幂上，满足 \(ab=cd\) 的项分成两类。

**两个不同素数底。** 若 \(ab\) 含两个不同素因子，则必有
\(ab=p^iq^j\)，而 ordered factorization 只有
\((p^i,q^j)\) 与 \((q^j,p^i)\)。因此四个 \((a,b,c,d)\) 选择的总和至多由

\[
 2K_{\psi,\kappa}
 \sum_{\substack{a,b\le X\\X^{1-\delta}<ab\le X}}
 \frac{\Lambda(a)^2}{a}\frac{\Lambda(b)^2}{b}
 \left(1-r_a-r_b\right)^q
\tag{11}
\]

控制；右侧允许同底素数幂，只会增大该非负 majorant。

**单个素数底。** 若 \(ab=p^k\)，则 \((a,b)=(p^i,p^{k-i})\)。这部分在
除以 \(L^4\) 前至多为

\[
 K_{\psi,\kappa}
 \sum_{p^k\le X,\ k\ge2}
 \frac{(k-1)^2(\log p)^4}{p^k}=O_\psi(1),
\tag{12}
\]

因为 \(\sum_p(\log p)^4/p^2<\infty\) 且
\(\sum_{k\ge2}(k-1)^2p^{-k}\ll p^{-2}\)。所以它是 \(o(1)\)。

定义有限测度

\[
 \mu_L=L^{-2}\sum_{n\le X}\frac{\Lambda(n)^2}{n}\,\delta_{r_n}.
\tag{13}
\]

由式 (1)，对每个 \(0\le x\le1\)，

\[
 \mu_L([0,x])=\frac{x^2}{2}+O(L^{-1}),
\tag{14}
\]

故 \(\mu_L\Rightarrow r\,dr\)；于是
\(\mu_L\otimes\mu_L\Rightarrow rs\,dr\,ds\)。固定 \(\delta\) 时，
式 (11) 的归一化极限为至多

\[
 2K_{\psi,\kappa}
 \int_{\substack{r,s\ge0\\1-\delta<r+s\le1}}
 rs(1-r-s)^q\,dr\,ds.
\tag{15}
\]

边界直线对极限测度为零，因此 indicator 不造成 Portmanteau 缺口。令
\(t=1-r-s\)，内层积分为

\[
 \int_0^{1-t}r(1-t-r)dr=\frac{(1-t)^3}{6}.
\]

式 (15) 即化为式 (8)。再以 \((1-t)^3\le1\) 得式 (9)。
\(\square\)

## 4. 公理作用与删除审计

1. **compact support / path extreme**：保证 \(ab\le X\) 且 overlap 长度为
   \(1-r_{ab}\)。删除后，adjacent 乘积可重新具有长度 \(X^2\)，本定理失效。
2. **endpoint envelope**：只负责 \(\delta\) 的幂次。删除端点消失但保留有界性，
   仍有 \(\kappa=0\) 的 \(O(\delta^2)\)；所以端点余弦窗改善速率，却不是
   tightness 本身所必需。
3. **Mertens 型式 (1)**：把有限素数幂权重传到 \(r\,dr\)。只用粗界
   \((\Lambda*\Lambda)(m)\le(\log m)^2\) 会多损失一个 \(L\)，不足以得到
   正确归一化 tightness。
4. **von Mangoldt 的素数幂支撑**：把相同乘积的 factorization 数控制为两个，
   单素数退化项为低阶。对任意稠密非负系数，此结论一般不成立。

上述输入都不编码零点位置或 Weil 完全正性；结论只是一个 prime-side bulk
边界估计，不是 RH/GRH 的改写。

## 5. 尚未证明的桥梁 [O]

定理 AEM **不** 证明笔记 201 式 (28) 的真实有限矩阵版本。仍需证明一个局部化
finite-to-bulk transfer，例如对 edge projector \(\mathbf1_{r_{ab}>1-\delta}\)
建立

\[
 \lim_{\delta\downarrow0}\limsup_{T\to\infty}
 \frac1N\left|
 \mathcal E_{T,\delta}^{\rm finite}
 -\mathcal E_{T,\delta}^{\rm bulk}
 \right|=0.
\tag{16}
\]

该桥梁必须同时处理：

1. finite Gabor 指标集产生的 \(K_{\rm out}\)；
2. \(I^4\) 与 one-cut 时间边界之差；
3. \(\phi^2=\psi(\cdot/L)\) 的两个 \(O(1)\) transition layers；
4. 与 vector-valued Montgomery--Vaughan disintegration 相容的统一常数。

因此 MOM-1 的下一最小引理应改写为式 (16)，而不是再次估计已经闭合的
bulk exact-product edge mass。

## 6. 可复现审计 [E]

`scripts/adjacent_bulk_edge_audit.py` 用 prime-power sieve 与 prefix log moments
计算式 (11) 的有限 \(X\) majorant，并与

\[
 \frac{K_{\psi,\kappa}}3\int_0^\delta
 t^{2\kappa+1}(1-t)^3dt
\]

比较。脚本还检查平窗 \(\delta^2/6\) 和端点余弦窗
\(\pi^2\delta^4/72\) 的符号与常数。该实验不验证式 (16)，也不把有限
收敛升级为 zeta 四矩渐近。
