# 270. 对数cutoff类的质量预算障碍

日期：2026-09-05。路线：NCE-8 / B1w；论文归属：Abel mass obstruction。
状态：[T] 保留完整指数的signed Abel尾；
[N] 更广的连续cutoff类mass-only障碍；
[C] 中心参数预算的RH蕴含；[O] 自由dyadic/cofinal存在性。

## 1. 主定理及和旧结论的区别

固定 \(0<\sigma<1\)、\(\kappa>0\) 和
\[
 0\le b<c_*=0.8476836 .
 \tag{1}
\]
令 \(\Phi\) 在充分大的实区间连续、非减，
\(N(Y)=\lfloor\Phi(Y)\rfloor\) 为有限cutoff，最终 \(N(Y)\ge Y\)。
置 \(L=\log Y,\ h=N(Y)/Y\)。假设最终
\[
 h\ge \frac3\kappa L-b\sqrt L.
 \tag{2}
\]

### 定理270-A [T/N]

若Riemann zeta有非实零点 \(\rho\) 满足 \(\Re\rho>\sigma\)，则
对每个充分大 \(Y_0\)，
\[
 \boxed{
 \sup_{\substack{Y\ge Y_0\\M(Y,N(Y))\ne0}}
 \frac{J_4(Y,N(Y))}{|\mu(Y,N(Y))|^\kappa}=\infty .}
 \tag{3}
\]
当 \(0<\sigma<1/2\) 时此结论无条件成立。
当 \(\sigma=1/2\) 时，若在这样的规则上证明全体充分大实尺度的预算，
就蕴含RH；不声称逆命题。

相比262，本定理不再要求 \(N\le Y^2/8\) 或 \(h/L\to\infty\)。
在本定理的零点假设下（\(\sigma<1/2\) 时无条件），对四次预算已可排除
\[
 N(Y)=\lfloor cY\log Y\rfloor,\qquad c\ge3/4 .
 \tag{4}
\]
这里为覆盖 \(c=3/4\) 的取整误差，在(1)取任意固定 \(b>0\) 即可。
常数 \(3/4\) 是本下界与尾估计给出的充分障碍边界，不是已证明最优阈值。

## 2. 保留 \(e^{-h}\) 的实际signed尾 [T/R]

沿用261的未截断质量 \(M_\infty(Y)\)，固定任意 \(0<d<c_*\)。
Fiori--Kadiri--Swidinsky的已核验定量PNT [R] 给
\[
 |\psi(x)-x|\le C_d x e^{-d\sqrt{\log x}}\qquad(x\ge2).
 \tag{5}
\]
其原对数因子已通过 \(d<c_*\) 吸收，不取端点 \(d=c_*\)。

### 引理270-B

对任意充分大实数 \(Y\)、任意有限整数 \(N\ge Y\)，置 \(h=N/Y\)，有
\[
 \boxed{
 |M_\infty(Y)-M(Y,N)|
 \le C_{\sigma,d}Y^a h^a e^{-h}e^{-d\sqrt L},
 \quad a=1-\sigma .}
 \tag{6}
\]

证明：置 \(w(x)=x^{-\sigma}e^{-x/Y}\)、\(R(x)=\psi(x)-x\)。
prime尾严格取 \(n>N\)，continuum从同一 \(N\) 起积分。
精确Stieltjes公式为
\[
 \begin{aligned}
 M_\infty(Y)-M(Y,N)
 &=\sum_{n>N}\Lambda(n)w(n)-\int_N^\infty w(x)\,dx\\
 &=-w(N)R(N)-\int_N^\infty R(x)w'(x)\,dx .
 \end{aligned}
 \tag{7}
\]
这里 \(R(N)\) 使用包含 \(n=N\) 的右连续值；不能改成左值而遗漏该原子。
无穷边界为零，因 \(R(x)=O(x)\) 与Abel衰减。

在全部积分变量 \(x\ge N\ge Y\) 上，(5)给
\(|R(x)|\le C_dx e^{-d\sqrt L}\)，而
\(-w'=(\sigma/x+1/Y)w\)。因此右侧绝对值至多
\[
 C_de^{-d\sqrt L}Y^a
 \left[h^ae^{-h}+
       \sigma\int_h^\infty u^{-\sigma}e^{-u}du+
       \int_h^\infty u^ae^{-u}du\right].
 \tag{8}
\]
当 \(h\ge1,\ 0<a<1\)，令 \(u=h+v\)，用
\((h+v)^a\le h^a(1+v)^a\) 及 \((h+v)^{-\sigma}\le h^{-\sigma}\le h^a\)，
两积分均至多 \(C_\sigma h^ae^{-h}\)，即得(6)。\(\square\)

本引理只改进尾项，既不给完整质量下界，也不产生第四矩正性。
若两个源端点不匹配，(7)需增加边界修正；不能照搬(6)。

## 3. 从质量根到有限实际源的证明 [T/N]

261-C已用Mellin恒等式和Landau机制证明：存在上述 \(\rho\) 时，
未截断实际质量有无界根序列 \(Y_j\to\infty\)，即
\(M_\infty(Y_j)=0\)。
该输入是已给证明的质量振荡定理，不是假设所有零点在中心线。

在(1)固定 \(b\) 后，选
\[
 b<d<c_* .
 \tag{9}
\]
令 \(N_j=N(Y_j),\ h_j=N_j/Y_j,\ L_j=\log Y_j\)。
由(6)及 \(S\asymp_\sigma Y^a\)，
\[
 |\mu(Y_j,N_j)|\le C_{\sigma,d}h_j^ae^{-h_j}e^{-d\sqrt{L_j}} .
 \tag{10}
\]
函数 \(h^ae^{-h}\) 在 \(h\ge1\) 上递减。
将(2)的下界代入，注意
\((3/\kappa)L-b\sqrt L\asymp_\kappa L\)，可得
\[
 |\mu(Y_j,N_j)|
 \le C_{\sigma,d,\kappa}
 L_j^a \exp\left(-\frac3\kappa L_j-(d-b)\sqrt{L_j}\right).
 \tag{11}
\]
这一推理不要求 \(h_j=O(L_j)\)：用的是单调上界，而非对实际 \(h_j^a\) 单独粗估。

若有限质量在 \(Y_j\) 也恰为0，则需要从允许 \(M\ne0\) 的尺度趋近。
由 \(\Phi\) 连续非减，每个 \(Y_j\) 右侧都有一小段 \(N(Y)=N_j\)：
连续性使 \(\Phi(Y)<N_j+1\)，单调性使 \(\Phi(Y)\ge\Phi(Y_j)\ge N_j\)。
这也覆盖 \(\Phi(Y_j)\) 恰为整数的情形。
固定有限 \(N_j\) 时，\(M(Y,N_j)\) 是非恒零实解析函数；
非恒零可由 \(Y\downarrow0\) 时从1开始的连续源支配从2开始的prime源验证。
所以能取
\[
 Y_j<Y'_j<Y_j+Y_j^{-1},\quad N(Y'_j)=N_j,\quad M(Y'_j,N_j)\ne0
 \tag{12}
\]
并以连续性保留(11)到固定因子。
由(2)，\(N_j/Y_j\to\infty\)，故同时可保证 \(N_j\ge Y'_j\)。

269-A的全部有限cutoff一致下界给
\(J_4(Y'_j,N_j)\ge c_\sigma (Y'_j)^{-3}\log Y'_j\)。
由 \(Y'_j/Y_j\to1\) 及(11)，得到
\[
 \frac{J_4(Y'_j,N_j)}{|\mu(Y'_j,N_j)|^\kappa}
 \ge c_{\sigma,d,\kappa}
 L_j^{1-a\kappa}\exp\bigl(\kappa(d-b)\sqrt{L_j}\bigr)
 \longrightarrow\infty .
 \tag{13}
\]
故(3)成立。
对 \(\sigma<1/2\)，使用临界线上存在非实零点 [R] 即可；
对 \(\sigma=1/2\)，函数方程将任何离线非平凡零点反射到右半侧，
所以该连续预算若成立便排除所有离线零点。\(\square\)

## 4. 量词、删除及未覆盖范围

- 本定理是全体充分大实尺度上的障碍；所构造的 \(Y'_j\) 不保证是 \(2^m\)。
- 268所选 \(N\in[Y,2Y)\) 不满足(2)，因此没有被本定理否定。
- \(b<c_*\) 和选择 \(b<d<c_*\) 给(13)的严格正指数；没有证明 \(b=c_*\)。
- 若仅用无误差率的定性PNT，本证明不能给 \(-b\sqrt L\) 的明确改进。
  只用绝对尾及269下界仍可排除 \(h\ge(3/\kappa+\varepsilon)L\)。
- 去掉 \(\Phi\) 的局部右侧常值保证，扰动避开有限质量零点的(12)需要另证；
  这里记录证明的失效位置，不宣称连续非减是逻辑必要条件。
- 固定 \(N=cY\log Y\) 类时，一个规则只排除满足相应阈值的 \(\kappa\)；
  不能改写为“任意正幂预算都失败”。\(h/L\to\infty\) 的旧类仍对所有固定 \(\kappa>0\) 失败。
- 没有对 \(N=\infty\) 套用有限均值公式，也没有将离线零点密度或RH作为本定理结论。

Weil接口仍是256所用mass-only充分输入。此障碍阻止在上述连续截断类上
把该输入当作软正性；它不排除更一般的response-specific Schur路线，
也不证明上同调与显式公式型配置等价。

[R] 定量PNT出处：
[Fiori--Kadiri--Swidinsky，v3 Corollary1.4](https://arxiv.org/pdf/2204.02588v3)，
正式发表于JMAA 527(2) (2023), article127426；
版本及常数核验见263。不声称该常数是当前最优。
新颖性与正式论文的外部审计保持[O]。

内部复核记录：两份独立只读审计通过signed尾符号、右连续端点、
\(b<d<c_*\)、无 \(h\) 上界时的单调替换、固定cutoff右侧扰动及中心参数量词；
其中一份另重建261的Landau依赖。已把(4)的零点前提显式写出。
