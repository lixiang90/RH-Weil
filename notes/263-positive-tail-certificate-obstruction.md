# 263. 实际 Abel正源相对尾证书的无条件障碍

日期：2026-09-05。路线：NCE-8 / B1t 至 B1u。
论文归属：Vaughan--Brownian response；本轮仅保存Markdown。

状态：[T] 全cutoff一致的加权PNT质量界及几何必要条件；
[N] 小窗口的绝对正源相对tail证书无条件失败；
[O] 实际带符号响应的相对截断误差。
这是对一个具体充分证书的障碍，不是对实际mass-only预算、Schur增益或RH的否定。

## 1. 对象和待检验的桥梁

固定 \(0<\sigma<1,\ a=1-\sigma,\ Y\to\infty,\ L=\log Y\)。
允许任意有限实cutoff \(N\ge Y\)（包括整数）；两源在同一 \(N\) 匹配：
\[
 \alpha=\sum_{2\le n\le N}\Lambda(n)n^{-\sigma}e^{-n/Y}\delta_{\log n},
 \qquad
 d\beta(\lambda)={\bf1}_{[0,\log N]}e^{a\lambda-e^\lambda/Y}\,d\lambda.
 \tag{1}
\]
记 \(A=\alpha(\mathbb R),B=\beta(\mathbb R),S=A+B,M=A-B,\mu=M/S\)。
令
\[
 I_H=[L-H,L+H],\quad \tau=\alpha+\beta,\quad
 t_H=\frac{\tau(I_H^c)}S,\quad
 \ell_H=\frac{\int_{I_H^c}\lambda\,d\tau}{LS},\quad
 \varepsilon_H=t_H+\ell_H.
 \tag{2}
\]
这些量正是259的relative tail修正所使用的绝对正源majorant。
该修正已经证明（\(D\ge cLS^2\) 时）
\[
 |\sqrt{J_4}-\sqrt{J_4^H}|\le C_c\varepsilon_H.
 \tag{3}
\]
从局部预算推出全源mass-relative预算的一条充分桥梁为
\(\varepsilon_H=O(\mu^2)\)。本轮审计这条桥梁，而不将 (3)误当双边界。

## 2. 连续源给出的几何下界 [T]

### 定理263-A

对所有充分大 \(Y\)、所有 \(N\ge Y\) 和 \(0\le H<L/6\)，有
\[
 \boxed{\quad
 \frac{\mu^2}{\varepsilon_H}
 \le C_\sigma\frac{M^2 e^{aH}}{Y^{2a}}.\quad}
 \tag{4}
\]
这包括 \(M=0\)，不使用PNT，也不需要关于零点的假设。

证明：区间 \(J=[L-H-1,L-H]\) 包含在源支撑内，
除一个零测端点外属于 \(I_H^c\)。在 \(J\) 上
\(e^\lambda/Y\le e^{-H}\le1\)，所以
\[
 \beta(J)\ge
 e^{-1}\int_{L-H-1}^{L-H}e^{a\lambda}d\lambda
 =\frac{e^{-1}(1-e^{-a})}{a}Y^ae^{-aH}.
 \tag{5}
\]
另外 \([Y/2,Y]\) 对应的连续质量给
\[
 S\ge B\ge Y^a\int_{1/2}^{1}u^{-\sigma}e^{-u}du
 =b_\sigma Y^a,\qquad b_\sigma>0.
 \tag{6}
\]
因此 \(\varepsilon_H\ge\beta(J)/S>0\)，于是
\[
 \frac{\mu^2}{\varepsilon_H}
 \le\frac{M^2}{S\beta(J)}.
 \tag{7}
\]
代入 (5)--(6)即得 (4)。\(\square\)

### 推论263-B：全部carrier分离窗口的条件性障碍

如果沿某条cofinal数据要求统一的
\(\varepsilon_H\le K\mu^2\)，则 (4)迫使
\[
 |M|\ge c_{\sigma,K}Y^ae^{-aH/2}
 \ge c_{\sigma,K}Y^{11a/12}.
 \tag{8}
\]
所以若沿某子族 \(M=o(Y^{11a/12})\)，所有 \(H<L/6\) 的这种证书均失败。
这里给的是完整证明的条件蕴含 [T]，其实际质量小量假设尚未无条件证明 [O]。
定性PNT给的 \(M=o(Y^a)\) 本身不足以推出这一强假设。

## 3. 定量PNT的全cutoff Abel转移 [T/R]

我们只使用一个已发表的无条件外部输入 [R]：
\[
 |\psi(x)-x|\ll x(\log x)^{3/2}e^{-c_*\sqrt{\log x}},
 \qquad c_*=0.8476836,\qquad x>2.
 \tag{9}
\]
出处为 Fiori--Kadiri--Swidinsky 的论文及其正式预印本v3，Corollary 1.4；
这不是对最新常数的宣称，亦不假设完整RH。明确书目见第7节。

### 定理263-C

对每个固定 \(0<d<c_*\)，
\[
 \boxed{\quad
 \sup_{N\ge Y}|M(Y,N)|
 \le C_{\sigma,d}Y^a e^{-d\sqrt L}\quad}
 \tag{10}
\]
于充分大 \(Y\) 成立。特别地，对每个固定 \(K>0\)，
\[
 \sup_{N\ge Y}|M(Y,N)|=O_{\sigma,K}(Y^aL^{-K}).
 \tag{11}
\]

证明：记 \(R_\psi(x)=\psi(x)-x\)，
\(w_Y(x)=x^{-\sigma}e^{-x/Y}\)。
Stieltjes分部积分精确给
\[
 M(Y,N)=w_Y(1)+w_Y(N)R_\psi(N)
             -\int_1^N R_\psi(x)w_Y'(x)\,dx.
 \tag{12}
\]
这里 \(R_\psi(1)=-1\)，故 \(w_Y(1)\) 不可遗漏。
整数端点按 \(\psi(N)=\sum_{n\le N}\Lambda(n)\) 约定处理。

选 \((d/c_*)^2<\theta<1\)，再选
\(d/\sqrt\theta<d_1<c_*\)。
将 (9) 中对数幂吸收到指数余量，得
\[
 |R_\psi(x)|\le C_{d_1}x e^{-d_1\sqrt{\log x}}
 \le C_{d_1}x e^{-d\sqrt L}
 \quad (x\ge Y^\theta).
 \tag{13}
\]
由于
\[
 -w_Y'(x)=
 \bigl(\sigma x^{-\sigma-1}+Y^{-1}x^{-\sigma}\bigr)e^{-x/Y},
\]
高段积分的绝对值至多
\[
 C e^{-d\sqrt L}\int_0^\infty
   \bigl(\sigma x^{-\sigma}+Y^{-1}x^{1-\sigma}\bigr)e^{-x/Y}dx
 \le C_{\sigma,d}Y^a e^{-d\sqrt L}.
 \tag{14}
\]
在endpoint \(N\ge Y\)，也有
\[
 |w_Y(N)R_\psi(N)|
 \le C e^{-d\sqrt L}N^ae^{-N/Y}
 \le C_{\sigma,d}Y^a e^{-d\sqrt L}.
 \tag{15}
\]
低段只需初等 \(|R_\psi(x)|\ll x\log(2x)\)：
其积分与 \(w_Y(1)\) 共计
\(O_\sigma(Y^{a\theta}L+1)\)，被 (10)右侧吸收，因为 \(\theta<1\) 固定。
所有上界与 \(N\) 无关，即得 (10)；(11)是其直接后果。\(\square\)

没有在 (10)中取 \(d=c_*\)。所有参数先固定，再令 \(Y\to\infty\)。
该加权转移是经典分部积分的应用，不将其本身作为新PNT结果。

## 4. 小窗口证书的无条件失败 [N]

### 定理263-D

对每个固定 \(0<k<2c_*/a\)，
\[
 \boxed{\quad
 \sup_{\substack{N\ge Y\\0\le H\le k\sqrt L}}
 \frac{\mu(Y,N)^2}{\varepsilon_H(Y,N)}
 \longrightarrow0.\quad}
 \tag{16}
\]

证明：这些窗口最终满足 \(H<L/6\)。
选 \(ak/2<d<c_*\)，将 (10)代入 (4)，得一致上界
\[
 C_{\sigma,d}\exp\bigl(-(2d-ak)\sqrt L\bigr)\longrightarrow0.
 \tag{17}
\]
\(\square\)

因此对每个固定 \(C>0\)，
\[
 \sup_{\substack{N\ge Y\\0\le H\le C\log L}}
 \frac{\mu^2}{t_H+\ell_H}\longrightarrow0.
 \tag{18}
\]
这无条件命中259每个固定 \(Q\) 的
\(H=(Q+4)a^{-1}\log L\) 窗口，覆盖：

- 任意预先固定的 dyadic尺度 \(Y_m=2^m\)；
- 任意所选cofinal子序列；
- 任意自由选择的 matched cutoff \(N_m\ge Y_m\)，无上界或连续性要求。

若 \(\mu=0\)，因 \(\varepsilon_H>0\)，证书已经失败；
若 \(\mu\ne0\)，(16)等价地使 \(\varepsilon_H/\mu^2\) 一致趋于无穷。
这里不需要连续质量根、相位选择或对未知零点的假设。

### 推论263-E：可行证书的必要窗口尺度

如果任意实际schedule上的统一证书
\(\varepsilon_{H_m}\le K\mu_m^2\) 成立，则必须
\[
 \liminf_{m\to\infty}\frac{H_m}{\sqrt{\log Y_m}}
 \ge\frac{2c_*}{1-\sigma}.
 \tag{19}
\]
证明：对任意更小的 \(k\)，(16)排除满足 \(H_m\le k\sqrt L_m\) 的无界子列；
若 \(H_m\ge L_m/6\)，该比值自动趋于无穷。随后令 \(k\) 逼近边界。\(\square\)

这是外部PNT输入所给的必要下界，不声称最优，亦不声称达到它便有证书。
更强的独立PNT误差可加强窗口下界；无需为本轮结论追求最佳常数。

## 5. 明确的停止边界和剩余算术任务

本轮证明的逻辑链是
“actual PNT使质量很小 + positive continuum尾仍大”
导致“绝对正源majorant不足”。它不提供
\[
 \left\|(F_{r*r*p},F_{r*r*c})
 -(F_{r^H*r^H*p^H},F_{r^H*r^H*c^H})\right\|
 \tag{20}
\]
的下界；\(\varepsilon_H\) 不是这个差的等价范数。
所以不推出 \(J_4\ne O(\mu^4)\)，也不排除256的实际capture/Schur增益。
261--262的连续尺度预算障碍与本轮的离散证书障碍是不同命题，不可混写。

**B1u 下一最小引理 [O]**：选定实际schedule，直接比较 (20) 与
\(M^2\sqrt D\)，保留两discrepancy因子的符号；并分别控制
\(|M_H|\) 相对 \(|M|\)。若要转移局部预算，一条清楚的充分组合为
\[
 \text{(20)}=O(M^2\sqrt D),\qquad |M_H|=O(|M|).
 \tag{21}
\]
实际中心窗口可先保留 \(H=O(\log L)\)，但不再用正源TV去闭合 (21)。
另一选择是允许更宽窗口并重审carrier几何；仅将 \(Q\) 换成另一个固定常数
已被 (18)排除。让 \(Q\) 随尺度增长也不能静默沿用固定 \(Q\) 的误差常数。

## 6. 公理用途、删除审计和模型范围

独立输入及作用：

1. 连续Abel源的正性及低lag密度给 (5)，正bulk给 (6)；
2. matched endpoint使 (12)没有未记账的endpoint mismatch；
3. 外部无条件定量PNT (9)给统一 (10)，不是由compactness产生正性；
4. 绝对正源tail定义使 \(\varepsilon_H\ge\beta(J)/S\)；
5. 最终统一的 \(O\)-常数使反证可用于任意cofinal子列。

删除时：若仅有定性PNT，(16)的明确尺度不能推出；
若改为signed response误差，(5)不再是其下界；
若continuum被重新缩放或endpoint不匹配，需要另写质量恒等式；
若window覆盖全部低lag区，(5)不适用，但此时已不在所排除的小窗口类。
这些是失效位置，不全部宣称为已构造反例。

实际Riemann正源适用；其他正系数谱模型只要独立满足同型bulk、tail和PNT估计，
可复用证明。复Dirichlet/自守系数的Hermitian替代需另证。
cohomological Weil结构与Gamma-complete显式公式未由本证书连接。

## 7. 文献、审计与结果状态

[R] A. Fiori, H. Kadiri, J. Swidinsky,
*Sharper bounds for the Chebyshev function \(\psi(x)\)*,
Journal of Mathematical Analysis and Applications 527(2) (2023), article 127426.
[期刊 DOI](https://doi.org/10.1016/j.jmaa.2023.127426)；
[arXiv v3, Corollary 1.4](https://arxiv.org/pdf/2204.02588v3)；
[作者出版目录](https://www.cs.uleth.ca/~fiori/publications.html)。
本轮阅读v3的定理及假设，并核验发表信息；期刊正文接口未能打开。
v3正文前因子为9.22022，摘要页面仍显示较旧数值；本笔记只用指数常数及存在的隐常数。
不将这个外部已证明定理的有限高度验证误写为假设完整RH。

独立逆向审计确认 (12)的 \(x=1\) 边界项、所有 \(N\ge Y\) 的一致性、
\(d<c_*\) 的严格不等式、(16)的零质量点以及证书/实际误差的逻辑区别。
本轮没有以数值实验支撑任何渐近结论。新颖性及可发表性仍需外部文献审查 [O]。
