# 262. 统一截断响应下界与一类质量预算障碍

日期：2026-09-05。路线：NCE-8 / B1t。论文归属：独立 Abel mass obstruction。

状态：[T] 实际系数的双参数响应下界；[N] 一类连续尺度截断规则上的
mass-only预算障碍；[O] 原来的所选 dyadic/cofinal schedule。
本笔记将261的特殊截断推广成一个统一窗口，不宣称得到 RH 或新零密度估计。

## 1. 对象、量词和结果

沿用261-(1)--(3)的实际 von Mangoldt/连续 Abel正源，
固定 \(0<\sigma<1\)，记 \(a=1-\sigma,\ L=\log Y\)。
这里 \(N\) 始终为整数，所有响应与质量在同一个 \((Y,N)\) 计算。

### 定理262-A [T]：双参数下界

存在只依赖 \(\sigma\) 的 \(c_\sigma>0,Y_\sigma\)，使
\[
 \boxed{\quad J_4(Y,N)\ge
 c_\sigma Y^{-6}N^{-3}(\log Y)^{-1}\quad}
 \tag{1}
\]
对每个实数 \(Y\ge Y_\sigma\) 和每个整数
\[
 Y\le N\le Y^2/8
 \tag{2}
\]
同时成立。常数及起点均不依赖 \(N\)。

### 定理262-B [T/N]：连续截断类的障碍

设 \(\Phi\) 在最终实区间连续、非减，令
\[
 N(Y)=\lfloor\Phi(Y)\rfloor,\qquad h(Y)=N(Y)/Y.
\]
假设 (2) 最终成立，并且
\[
 \frac{h(Y)}{\log Y}\longrightarrow\infty.
 \tag{3}
\]
若 zeta有非实零点 \(\rho\) 满足 \(\Re\rho>\sigma\)，则对每个固定
\(\kappa>0\) 和每个充分大 \(Y_0\)，
\[
 \boxed{\quad
 \sup_{\substack{Y\ge Y_0\\\mu(Y,N(Y))\ne0}}
 \frac{J_4(Y,N(Y))}{|\mu(Y,N(Y))|^\kappa}=\infty.\quad}
 \tag{4}
\]

因此 \(0<\sigma<1/2\) 时，这一截断类的连续 mass-only预算无条件失败；
\(\sigma=1/2\) 时，任何一个满足上述假设的规则若有该连续预算，就蕴含 RH。
没有证明逆命题；也没有把“连续尺度”改成“预先固定 dyadic尺度”。

## 2. 双参数下界的完整证明

由 Bertrand定理在 \(\lfloor Y/2\rfloor\) 处的整数形式，取素数
\[
 Y/2<q<Y.
\]
由 (2)，\(q\le N<q^2\)。
令 \(d=\alpha^{\rm ev}-M\delta_0,\ b=\beta^{\rm ev}\)，
故 \(r=d-b\)。测度 \(\eta=r*r*p\) 的原子部分为 \(d*d*p\)，
绝对连续部分为 \(g(x)\,dx=-2d*b*p+b*b*p\)。

在 \(x_0=3\log q\) 处有精确原子系数
\[
 w=\frac18\bigl((\log q)q^{-\sigma}e^{-q/Y}\bigr)^3
 \ge c_\sigma L^3Y^{-3\sigma}.
 \tag{5}
\]
因为每个因子的非中心原子只在 signed prime-power lags处，
且 \(q^2>N\)，每个因子的 \(q\)-valuation至多1。
要得到总valuation 3，三个因子必须都是正向 \(q\)。
中心原子、负向原子及其他素数幂均不能参与，故无原子抵消。

任意其他原子位置为 \(\log(u/v)\)，其中正整数 \(u,v\le N^3\)。
若该位置不同于 \(3\log q\)，则 \(u\ne vq^3\)，并且
\(\min(u,vq^3)\le N^3\)，故
\[
 |\log(u/v)-3\log q|\ge\log(1+N^{-3})\ge(2N^3)^{-1}.
 \tag{6}
\]
取 \(\delta=(8N^3)^{-1}\)。

使用未截断正源作为上界，初等求和与密度极大值给
\[
 S\le C_\sigma Y^aL,\qquad
 \|db/dx\|_\infty\le C_\sigma Y^a.
\]
其中 \(x\) 是 additive lag坐标。
\(\|d\|_{\rm TV}\le2S,\ \|p\|_{\rm TV}\le2A,\ \|b\|_{\rm TV}=B\)
给
\[
 \|g\|_\infty\le10S^2\|db/dx\|_\infty
 \le C_\sigma Y^{3a}L^2.
 \tag{7}
\]
由 (2)、(5)，
\[
 \frac{\delta\|g\|_\infty}{w}
 \le C_\sigma\frac{Y^3}{N^3L}
 \le C_\sigma L^{-1}.
 \tag{8}
\]
故对与 \(N\) 无关的充分大 \(Y\)，该值至多 \(1/4\)。
\(F_\eta\) 在 \(x_0\) 跳跃 \(w\)，其一侧极限绝对值至少 \(w/2\)。
该侧长度 \(\delta\) 的区间没有其他原子，连续变化至多 \(w/4\)，因此
\[
 P^2\ge\|F_\eta\|_2^2\ge\delta w^2/16
 \ge c_\sigma N^{-3}L^6Y^{-6\sigma}.
 \tag{9}
\]

Brownian minimum-kernel恒等式及 \(\log N\le2L\) 给
\[
 D\le\tfrac12(\log N)(A^2+B^2),\qquad
 S^4D\le C_\sigma Y^{6a}L^7.
 \tag{10}
\]
除以分母，并使用 \(6a+6\sigma=6\)，得到 (1)。\(\square\)

这里需要的是 \(\log N\asymp\log Y\)，不是比值趋于1。
例如 \(N=\lfloor Y^{3/2}\rfloor\) 的比值趋于 \(3/2\)，完全在定理范围内。

## 3. 连续截断类障碍的完整证明

由261-C的 Mellin/Landau论证，存在未截断质量根 \(Y_j\to\infty\)。
记 \(N_j=N(Y_j),\ h_j=N_j/Y_j,\ L_j=\log Y_j\)。

初等上界 \(\Lambda(n)\le\log n\) 及递减尾积分比较给，对 \(h=N/Y\ge1\)，
\[
 |M(Y,N)-M_\infty(Y)|
 \le C_\sigma Y^a(L+h+1)e^{-h}.
 \tag{11}
\]
具体地，对从 \(N\) 起的积分代换 \(x=Yu\)，并用
\(u^{-\sigma}\le1,\ \log u\le u\)，即得右侧。
对充分大 \(Y\)，原被积函数在 \(x\ge N\ge Y\) 递减。
由于 \(N\ge Y\)，连续源在 \([Y/2,Y]\) 上的质量至少 \(c_\sigma Y^a\)。
于是
\[
 |\mu(Y_j,N_j)|\le C_\sigma(L_j+h_j+1)e^{-h_j}
 \le e^{-h_j/2}
 \tag{12}
\]
最终成立；最后一步只用 \(h_j/L_j\to\infty\)。

每个 \(Y_j\) 右侧有一个 \(N(Y)=N_j\) 的区间：
连续性保证 \(\Phi(Y)<N_j+1\) 于足够短的右区间，
非减性保证 \(\Phi(Y)\ge\Phi(Y_j)\ge N_j\)。
这也覆盖 \(\Phi(Y_j)\) 恰为整数的情形。

固定 \(N_j\) 时，\(M(Y,N_j)\) 是非恒零实解析函数。
非恒零可从 \(Y\downarrow0\) 时连续源从1开始而素数源从2开始验证。
所以可在同一右区间选
\[
 0<Y'_j-Y_j<Y_j^{-1},\qquad M(Y'_j,N_j)\ne0
\]
并由连续性保留 (12) 到固定因子，譬如 \(2e^{-h_j/2}\)。
定理262-A适用于这些实际有限源，且
\[
 J_4(Y'_j,N_j)\ge c_\sigma (Y'_j)^{-12}(\log Y'_j)^{-1},
\]
因为该规则满足 \(N_j\le(Y'_j)^2/8\)。
因此
\[
 \frac{J_4(Y'_j,N_j)}{|\mu(Y'_j,N_j)|^\kappa}
 \ge c_{\sigma,\kappa}
 \frac{\exp(\kappa h_j/2-12L_j)}{L_j}\longrightarrow\infty,
 \tag{13}
\]
其中 \(Y'_j/Y_j\to1\)，且 \(h_j/L_j\to\infty\)。
这证明 (4)，不需要将未截断响应转移到有限响应。\(\square\)

## 4. 适用规则与未覆盖的量词

- [T/N] 每个固定 \(b>1\) 的 \(N(Y)=\lfloor Y(\log Y)^b\rfloor\) 满足262-B；
  由262-A更精确地有 \(J_4\ge c_{\sigma,b}Y^{-9}L^{-1-3b}\)。
- [T/N] 每个固定 \(0<\varepsilon<1\) 的
  \(N(Y)=\lfloor Y^{1+\varepsilon}\rfloor\) 同样满足262-B，
  下界为 \(c_{\sigma,\varepsilon}Y^{-9-3\varepsilon}L^{-1}\)。
- [T] 对固定 \(0<b\le1\)，上述下界仍成立，但262-B的条件 (3) 不成立；
  不能据此宣告所有正幂预算失败。
- [O] 本文未覆盖任意大 \(N\ge Y\)、非规则跳动的 cutoff、
  固定 dyadic尺度或原256中自由选择的 cofinal schedule。

对任意所选 dyadic/cofinal数据，只要每个点满足 (2)，若在非零质量点有
\(J_{4,m}\le C|\mu_m|^\kappa\)，则262-A强迫
\[
 |\mu_m|\ge(c_\sigma/C)^{1/\kappa}
 Y_m^{-6/\kappa}N_m^{-3/\kappa}L_m^{-1/\kappa}.
 \tag{14}
\]
这是必要条件，不是充分条件，也没有证明实际 dyadic质量会违反它。
原 B1o-q4允许自由选择 \(N_m\ge Y_m\)，因此不能以这一部分窗口的障碍
否定整个存在性目标。抽取 \(m_j\) 时仍保留原物理归一化 \(t=m_j\xi\)。

## 5. 最小输入、删除审计及下一路线

独立输入及用途：实际 prime-power支撑与 Bertrand提供孤立原子；
正源 TV和有界连续密度控制跳跃两侧；(2)使原子唯一且分母统一；
Abel指数尾与 (3)给超多项式小质量；261的 Mellin非实极点及正实轴全纯性
给无界质量根；连续非减 \(\Phi\) 使非零质量扰动留在同一cutoff cell。
没有使用 RH、统一 Weil正性、PNT误差或非构造完备化。

删除或减弱时的失效位置：(2)上界删除后，\(q^2,q^3\) 原子可能出现，
valuation唯一性不再按本证明成立；允许任意原子支撑时也失去这一唯一性。
密度控制删除后，单个跳跃不保证统一区间能量。仅有绝对tail趋零时，
它未必小于响应的多项式下界。缺少cutoff cell性质时，固定 \(N_j\)
解析扰动不能自动对应同一实际规则。仅检验离散尺度时，根的位置可能全被错过。
这些是证明失效位置，不将其全部伪称为已构造反例。

与 Weil配置的接口仍是256的实际 capture/Schur条件；这里只处理
prime/continuum二通道，Gamma-complete与上同调结构的桥梁仍为 [O]。
其他数域/函数域模型的适用性需另证正源、原子间距和 Mellin实轴条件。

下一最小引理 B1t：冻结一个具体 dyadic cutoff，比较实际 \(E_1,E_2\)
与质量项，并核验相对 \(\mu^2\) 截断误差；同步检验 (14) 的必要分离界。
仅证明质量分离不能晋级。若实际质量沿非零子序列小于 (14) 的尺度，
只停止那个schedule；完整能量预算及相对误差同时闭合才晋级。
停止继续寻求262-B这类连续族上的软 mass-only公理。

后续263--264：小窗口的正源绝对相对tail证书已被定量PNT无条件排除，
包括任意dyadic/free-cutoff族；这不是full-source mass-only预算的no-go。
局部预算经最优能量平方不等式缩为单一 \(E_{2,H}=O(LM_H^4)\)。
B1u剩余接口为实际signed响应差、\(|M_H|=O(|M|)\) 与该局部能量预算。

## 6. 审计、复算与文献边界

独立复核确认了 (1) 中 \(N\)-一致常数、实数 \(Y\) 的Bertrand选取、
\(\log N\asymp L\) 而非错误的渐近等价，以及右侧cutoff cell和非零质量扰动。
精确有限复算沿用 scripts/abel_prime_atom_audit.py：
24案例、126原子系数及567180整数间距检查通过 [E]。
这只交叉检查代数，渐近定理由第2--3节证明，不由有限数据升级。

Landau机制属于经典结果，不主张其新颖性；外部复核入口为
[Mahatab--Mukhopadhyay, arXiv:1512.03144v4, Theorem 3.1](https://arxiv.org/pdf/1512.03144v4)。
该预印本还讨论更强的振荡测度结果，本笔记没有借用其更强结论。
261已独立重建所需的非负 Mellin边界论证。
尚需系统比较既有 Abel平滑振荡文献及响应障碍文献，不能把内部复核
当作发表价值、新颖性或外部同行评审的认证。

交付复核：独立论文连续两次 pdflatex编译，最终7页已逐页渲染检查；
公式编号、控制字符及最终LaTeX日志检查通过。复算命令：

```powershell
python scripts/abel_prime_atom_audit.py
python scripts/abel_mass_discrepancy_probe.py --tail-factor 40 --skip-e1
python scripts/abel_mass_discrepancy_probe.py --max-m 10
```

最后一条另检查 E1的6点/10点Gaussian求积路径；它仍只是浮点交叉证据。
