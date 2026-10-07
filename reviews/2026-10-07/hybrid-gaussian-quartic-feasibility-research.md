# Gaussian quartic theta 与原 cubic probe 的接口核查

日期：2026-10-07。作者：mixed_path_check 独立核验。

本稿仅新增研究记录。原 math 源、旧 reviews、脚本、输出、Goal、Git 均未修改。
固定比较源为 `E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，
commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，canonical LF SHA-256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。
本稿不重新认证该源全部证明，也不改变现有 zero-free-region 数值结论。

结论：Q(i) 的 quartic 候选并非被 Gauss 信号排除。按下面明确的归一化，所有 odd primary
squarefree c 都满足
\[
 \gamma_1(c)^2=\mu(c)\alpha(c),\qquad \alpha(c)=c/|c|.
\tag{G}
\]
quartic 有限核也确实允许所需的 \(j=1\mapsto2\) quadratic 终端。
缺口是将这两个接口同时装入一个实际 probe：已知 quartic theta 的闭式 Gauss 系数位于平方指标，
而原 cubic probe 使用线性 squarefree 指标；现有公式没有提供原稿所需的完整任意 row 反射、
全素数幂 reciprocal Euler 恒等式及其 marked/plain 长度账本。不能据此给出 Gaussian 新无零域。

## 1. 所用原始结果与版本边界

主要原始论文为 David–Dunn–Hamieh–Lin,
[Quartic Gauss sums over primes and metaplectic theta functions, arXiv:2306.11875v5](https://arxiv.org/html/2306.11875v5)，
版本日期 2026-01-30。核查 §3 的 Gauss 定义和 (3.5)、(3.8)–(3.11)，
§4 的实际 theta、(4.26)、(4.28)、(4.35)–(4.41)，以及 Lemma 9.2。
以下称 DDHL。其 §4.5 给出真实 quartic theta 原始结果，故这里不是依据泛称 metaplectic theta 猜测可迁移。

Suzuki 的原论文为 *Some results on the coefficients of the biquadratic theta series*,
J. Reine Angew. Math. 340 (1983), 70–117。该文原始扫描在本次工具中未成功取得；
本文对其定理的使用严格限于 DDHL §4.5 所明确记录、采用 DDHL 的符号归一化的公式，
不声称另行通读了 Suzuki 原扫描。
Diaconu 的 [原出版社页面](https://link.springer.com/article/10.1007/s00222-004-0363-6)
核对了 *Mean square values of Hecke L-series formed with r-th order characters*,
Invent. Math. 157 (2004), 635–684；具体函数方程使用 DDHL 的 (4.28)，
不从该文摘要推出更强 uniform reflection。

初始曾读 [v3](https://arxiv.org/html/2306.11875v3)。其 (3.11) 少一个因子，
且 (3.8) 给了较强的 inert 定号；这些不能作为当前归一化依据。第 3 节记录可复验的 q=5 分歧。
v5 是本稿最终引用版本。

## 2. Gauss–Jacobi 信号：逐素数证明与 squarefree 扩展

置 \(\lambda=1+i\)，primary 指 \(c\equiv1\pmod{\lambda^3}\)。采用
\[
 \chi_\pi(x)=(x/\pi)_4,
 \quad \check e(z)=\exp(2\pi i(z+\bar z)),
 \quad G_j(\pi)=\sum_{x\bmod\pi}\chi_\pi(x)^j\check e(x/\pi),
 \quad\gamma_j=G_j/\sqrt q.
\]
所有角色在 nonunit 处按零延拓。这里 \(G_1\) 对应 DDHL 的 \(g_4\)，
\(G_2\) 对应其 \(g_2\)；避免将下标 4 与角色幂 4 混用。

令 \(J_\pi=\sum_x\chi_\pi(x)\chi_\pi(1-x)\)。直接将 \(G_1^2\) 的两个变量按
\(t=x+y\) 分组，\(t\ne0\) 时写 \(x=tu,y=t(1-u)\)，得到
\[
 G_1^2=J_\pi G_2,
 \qquad \frac{\gamma_1^2}{\gamma_2}=\frac{J_\pi}{\sqrt q}.
\tag{2.1}
\]
\(t=0\) 项为 \(\chi_\pi(-1)\sum_{x\ne0}\chi_\pi(x)^2=0\)。
这证明所用 Gauss–Jacobi 关系，并明确它的归一化。

先取 degree-one prime \(\pi=a+bi\)，\(q=p=a^2+b^2\) 为 rational prime。
primary 条件给 a 奇、b 偶、p≡1 mod4。定义
\[
 \epsilon_\pi=\chi_\pi(-1),\qquad
 \kappa_\pi=(\bar\pi/\pi)_4^{-2}.
\]
DDHL v5 (3.9)、(3.11) 的实际输入为
\[
 G_2=\epsilon_\pi\sqrt p,\qquad
 G_1^2=-\epsilon_\pi\kappa_\pi\sqrt p\,\pi.
\tag{2.2}
\]

现独立简化新增因子。模 π 有 \(\bar\pi=2a\)，角色的 -2 次幂等于二次角色，故
\[
 \kappa_\pi=(2a/p)_2=(2/p)_2(a/p)_2.
\]
\(\gcd(a,b)=1\)。若 \(|a|>1\)，二次互反律、p≡1 mod4 和 Jacobi 乘法性给
\[
 (a/p)_2=(p/|a|)_2=(b^2/|a|)_2=1.
\]
a<0 不增加符号，因为 \((-1/p)_2=1\)；a=±1 单独也等于 1。
因此
\[
 \kappa_\pi=(2/p)_2=(-1)^{(p-1)/4}=\epsilon_\pi.
\tag{2.3}
\]
这一步将看似移动的 \((\bar\pi/\pi)_4^{-2}\) 降成有限 ray 符号；不能在 degree-two
prime 处直接代入这个 quotient，那里 \(\bar\pi\) 本身被 π 整除。
由 (2.1)–(2.3)，degree-one 处
\[
 J_\pi=-\epsilon_\pi\pi,
 \qquad \gamma_1(\pi)^2=-\alpha(\pi),
 \qquad \gamma_1(\pi)^2/\gamma_2(\pi)=-\epsilon_\pi\alpha(\pi).
\tag{2.4}
\]
注意 quotient 的 -epsilon 不能删；最方便的 reciprocal 信号候选是平方本身。

再取 inert rational prime p≡3 mod4，primary generator 是 π=−p，q=p²。
v5 (3.8) 仅保证 \(|G_1|=|G_2|=p\)，本稿不假设 \(G_1=p\)。
在 \(\mathbb F_{p^2}\) 上，Frobenius x↦\(\bar x=x^p\) 给
\(\chi(\bar x)=\chi(x)^p=\overline{\chi(x)}\)，且 additive trace 对共轭不变。
另有 \(\chi(-1)=1\)。于是
\[
 \overline{G_1}
 =\sum_x\overline{\chi(x)}\check e(-x/\pi)
 =\sum_y\chi(y)\check e(y/\pi)=G_1,
\]
其中使用 x=−\(\bar y\)。所以 \(G_1\) 是实数，由其绝对值得 \(\gamma_1^2=1\)。
同时 \(\alpha(\pi)=-1\)，仍有 \(\gamma_1^2=-\alpha(\pi)\)。这不确定 Gauss sum 的正负号，
也无需确定它。

对互素 odd primary a,b，CRT 与 quartic reciprocity 的 cross factor 为
\[
 \gamma_1(ab)=\gamma_1(a)\gamma_1(b)
 (a/b)_4(b/a)_4,
 \quad (a/b)_4(b/a)_4\in\{1,-1\}.
\]
平方使 cross factor 消失。primary 生成元乘法相容，所以对任意 odd primary squarefree c
逐素数相乘即得 (G)。它是严格可用的全 squarefree signal；它并不评价一般 prime-power
probe 里的其他变量，也不是整个 reciprocal Euler quotient。

若改变 additive character 为 \(\check e(r x/\pi)\)，\((r,\pi)=1\)，则
\(G_j(r)=\chi(r)^{-j}G_j(1)\)。因此 quotient \(\gamma_1^2/\gamma_2\) 不变，
而平方信号被 \(\chi(r)^{-2}\) 乘上一个二次符号。实施新 probe 时必须保留这一项。

## 3. v3 的遗漏可在 q=5 精确复验

取 \(\pi=-1+2i=1+\lambda^3\)，\(q=5\)，在 residue field 中 i=3。
对 x=1,2,3,4，quartic values 为 1,−i,i,−1。因此
\[
 J_\pi=\sum_{x\in\mathbb F_5}\chi(x)\chi(1-x)=-1+2i=\pi,
 \quad \epsilon_\pi=-1.
\]
v3 (3.9)、(3.11) 印刷式联合会给 J=−π，与这个整数计算冲突。
v5 加上 \(\kappa_\pi=(\bar\pi/\pi)_4^{-2}=-1\) 后，(2.2) 与有限和一致。
因此这是版本更新所解决的归一化问题，不能据旧 v3 式宣称新 signal 为统一 \(-\alpha\) quotient。

memory-only 独立核查表：

| q | primary π | 精确 J | epsilon |
|---:|---|---|---:|
| 5 | −1+2i | −1+2i | −1 |
| 13 | 3+2i | 3+2i | −1 |
| 17 | 1+4i | −1−4i | +1 |
| 29 | −5+2i | −5+2i | −1 |

按 \(\check e(x/\pi)\) 直接计算 Gauss 和，(2.1) 的浮点余差小于 \(10^{-12}\)。
这些是有限一致性检查，完整论证是第 2 节，不靠样本推广。

## 4. rho=1：精确有限核与真正全局条件

对 \(\mathbb F_q\) 上 quartic χ 和非平凡 additive ψ，置
\[
 \tau_j^{\pm}=q^{-1/2}\sum_{h\ne0}\chi(h)^j\psi(\pm h),
\]
以及明确的有限核
\[
 K_j(x)=q^{-1}\sum_{h,v\ne0}
 \chi(h)^j\chi(v)^{-1}\psi(-hv+x/v).
\tag{4.1}
\]
先对 h 求和，再置 t=1/v。对 j=1,2 得精确恒等式
\[
 K_j(x)=\tau_j^-\tau_{j+1}^+\chi(x)^{-j-1}.
\tag{4.2}
\]
在 x=0 时，两边都按零延拓为零。特殊分支同样明确：
\[
 K_3(x)=q^{-1/2}\tau_3^-(-1+q1_{x=0}),\qquad
 K_0(x)=-q^{-1/2}\tau_1^+\chi(x)^{-1}.
\tag{4.3}
\]
因此 rho=1 的全部四个 local exponent 分支均有合法有限公式；j=1 在 (4.2) 中就是 χ²。
q=5 的全部 j=0,1,2,3 与 x=0,1,2,3,4 共 20 个有限和已在内存核对。

(4.1) 是本稿直接定义并证明的有限核。它证明 local arithmetic 兼容，
**不宣称 DDHL 已为原 probe 给出了以此核为全部 moving-prime dependence 的全局反射定理**。
具体 quartic Kubota multiplier 的确是四次 residue multiplier，见 DDHL §4.3；
但从这个 multiplier 到原稿任意 row、共同 profile 的完成反射还需逐 cusp 推导。

一般 order d=2m 若需保持原平方自由 residual row j=1 为 quadratic，则
\(-1-\rho\equiv m\pmod{2m}\)，即 \(\rho\equiv m-1\pmod{2m}\)。
所需 theta multiplier 的角色阶数为
\[
 \frac{2m}{\gcd(2m,m-1)}=
 \begin{cases}m,&m\text{ 奇},\\2m,&m\text{ 偶}.\end{cases}
\]
故 d=6 用 rho=2 的 cubic multiplier；d=4 需要 rho=1 的 quartic multiplier。
使用 quadratic theta χ4² 会得到 \(-1-2\equiv1\pmod4\)，仍为 quartic，不能满足终端。

## 5. 已有具体 quartic theta 如何接入，哪里不接入

DDHL §4.5 给真实 24-cusp theta、Bessel \(K_{1/4}\)，及以下 Suzuki 系数接口。
令 m 为 squarefree primary、\((m,\nu)=1\)，β 为两个 mod4 sector：
\[
 \psi_\beta(m^2\nu)=N(m)^{-3/4}\overline{g_4(\nu,m)}\,
 \begin{cases}
 \psi_\beta(\nu),&m\equiv1\ (4),\\
 (-1)^{(N(\beta)-1)/4}\psi_{\beta(1+\lambda^3)}(\nu),&m\equiv1+\lambda^3\ (4).
 \end{cases}
\tag{5.1}
\]
第四幂有周期性，互素非平凡 cube factor 使系数消失。
general exponent-one core 的 prime coefficient 尚无闭式；其平方与 Gauss sum 的关系仍是 conjectural。
这些是可用接口的具体边界，而非本稿证明的新 theta 定理。
[DDHL v5 §4.5](https://arxiv.org/html/2306.11875v5#S4.SS5)

下面是本稿对 (5.1) 的接口分析。若 ν=1，已知线性 Gauss weight 在 theta 指标 m²，
其尺度是 \(N(m)^{-1/4}\overline{\gamma_1(m)}\)，加固定 sector 切换。
原 fixed source 的 completed cubic reflection 使用 sf n 的 **线性指标 n**，
并将其和 cube b³ 完成为 \(nb^3\)，允许 n,b 共素因子。
把 quartic 的已知 square formula 直接代替它，会改变为 square / fourth-power 指标，
而不是把 3 在原式中简单换成 4。

若所有角色都作用于 theta 的全指标 \(m^2b^4\)，则在 residual m 处
\(\Psi(m^2)=\prod\chi_p(m)^{2j_p}\)，只含 even exponent。
原来的 arbitrary quartic row \(\prod\chi_p(m)^{j_p}\)，尤其 j=1，不能通过这一步保持。
这是该直接替换的角色奇偶障碍；并非所有 Gaussian 新 probe 的全局不可能性。

同一问题也落在 **target family**，不只是 moving row。若照原稿将任意目标 ray character η
作用于已知完整 theta 指标 \(n^2b^4\)，则
\[
 \eta(n^2b^4)=\eta(n)^2\eta(b)^4.
\tag{5.2}
\]
因而 squarefree 信号若读出 reciprocal，潜在目标已经变成 η²，不能保持原任意 η。
同一固定 ray-character 群上的平方映射不必满射：例如固定群为 C4 时，image 只有
1 与 quadratic，不能取得原 quartic generator；照用一个 order2 目标时平方直接成为 trivial。
因此在原固定有限字符合同内，选择 η 的 square root 不是对所有目标合法的修复。
若增大 ray modulus 寻找 square root，仍须另证存在性及新的 conductor、profile、
natural-zero uniformity；这个有限群例子没有断言可变导子的全 Hecke 字符群永远不存在根。
若改为只给 root n 加 η(n)，则权重已经不是 full-index theta character，
需要证明一个新的 root-weight reflection theorem。这个明确障碍仅针对 literal square-index design，
不排除其他 quartic 完成设计。

若反而坚持线性 sf 指标来保留 odd row，则需要完整的 exponent-one core 系数；
(5.1) 没有评价它。平方未知 Fourier coefficient 也不是线性 theta Fourier 展开，
对 theta 函数求平方得到的是 additive convolution，不能凭一条猜想自动获得 desired Euler series。

另外，若直接令 probe modulus A=m²，则原 residue symbol χA=χm² 已为 quadratic。
在 modulus π² 的 additive Gauss 计算中，unit numerator 下和为 0；numerator valuation 1 时
才出现 \(qG_2(\pi)\)，而非 \(qG_1(\pi)\)。这是 prime-power 局部核直接可算的后果。
因此 (G) 虽然能提供 signal，也不能仅凭已知 square-index theta 断言 Poisson 又产生第二个 γ1。

## 6. 真实 Voronoi formula 的 quadratic 接口及其限制

已有 DDHL Lemma 9.2 的 numerator 是
\(\xi\,(\alpha/m)^2\)，其中 m|α，\(\xi=(-1)^a\lambda^{2b}\) 属固定局部项。
其相应 Gauss 列为
\[
 \widetilde g_4\big(\xi(\alpha/m)^2,c\big).
\tag{6.1}
\]
在 \((\alpha/m,c)=1\) 时，直接换元给
\[
 \widetilde g_4\big(\xi(\alpha/m)^2,c\big)
 =(\alpha/m\,/c)_2\,\widetilde g_4(\xi,c).
\tag{6.2}
\]
这是真正具体的 quadratic family 入口，故 Gaussian quartic theta 的研究路线具有实质可用部分。
若 m 与 c 有共素因子，不能用 (6.2) 擅自除 mask；须保留 (6.1) 并用实际 prime-power 表处理。
[DDHL v5 Lemma 9.2](https://arxiv.org/html/2306.11875v5#S9)

此公式中的输入本身是 square-numerator / level α 的专门完成，含 m|α 的 divisor sum。
它不是原 fixed source proposition 对每个任意 quartic \(j_p\) 给出的统一完成恒等式。
从 (6.2) 可以支付某个具体 square-numerator bilinear block；不能反推原 odd row 的全部反射已经成立。

同一原始结果的 Dirichlet-series completion 使用
\[
 Z_{i1}(s,\nu,\ell)=\zeta_{K,\lambda}(4s-3,\ell)\psi_{i1}(s,\nu,\ell),
\]
\[
 G_\infty(s,\ell)=\prod_{a\in\{3/4,1/2,1/4\}}\Gamma_{\mathbb C}(s+|\ell|/2-a),
\]
并以 \(N(\nu)^{1-s}\) 和 24×24 固定 cusp matrix 反射到 2−s。
[DDHL v5 (4.24)–(4.28)](https://arxiv.org/html/2306.11875v5#S4.SS4)

本稿由此作出的限制判断是：固定 cusp 数不使该路线本身不可能，但必须跟踪共同测试 profile、
ramified rational factors、pole contributions 和 matrix entries。不能将 cubic 的两 Gamma 比值
\(R(t)=\prod_\pm\Gamma(1+t\pm1/6)/\Gamma(1-t\pm1/6)\) 原样搬来。
theta 本身的 K1/4 Mellin 核，与这里 Gauss Dirichlet series 的三 Gamma completion 也不是同一个对象；
不能混用后只更改 ±1/6。

## 7. 对 fixed source 的准确替换账本

| 原 fixed source 调用 | 本稿所得 Gaussian 状态 |
|---|---|
| 766–835 的 prime Gauss phase；841–1039 的 sf signal | 有新严格 signal (G)，需改用 γ1²，保持 additive normalization |
| 1676–1881 的 completed reflection、共同 profile、全部 local branches | local rho=1 核已证明；原 probe 的全局同形完成尚未给出 |
| 1945–2009 的完整 cusp coefficient 公式与 sf/cube support | square/fourth-power 部分有已知接口；exponent-one core 未闭合 |
| 2640–2737 的 terminal quadratic large sieve | 若真正生成 (4.2) j=1 或 (6.2) 且付 masks，则可调用；尚非整个反射 block 已付 |
| 3806–3820、4032–4058 的同一 probe 的 reciprocal Euler identity | (G) 只提供 sf phase；全部 prime-power、completion、mask 仍需新计算 |
| 9250–9340 的 marked actual invariant / reflected energy | 未迁移；column 指标及长度已经改变 |
| 12531–12600 的 plain moment 与 capacity 条件 | 未迁移；原 numeric slopes 不能自动保留 |
| 12362–12455 的 sixth-power amplification | 形式 order4 amplification 可独立给 3/4 slope，但其 raw moment 前提仍待建立 |

所谓 reciprocal quotient 需要的是一个从 **同一实际 probe** 推导出的、在绝对收敛区域验证的
\(\zeta_K(4z)L_K(w,\chi_u)/L_K(x,\eta\bar\chi_u)\) 型恒等式及可控 Euler remainder。
(G) 本身虽能产生 \(1-\eta(\pi)\bar\chi_\pi(u)q^{-x}\) 的候选线性信号，
却没有定义、支付实现该线性项的 theta completion 和全部非线性 local terms。
不是“多一个固定符号”就能完成原稿全 Euler 商。

## 8. 有限 no-go 与下一步可检验目标

已明确排除的是三种直接替换：保留 χ² theta 时 terminal 仍为 quartic；
用已知 square-index theta 但坚持 all characters 作用于全指标时 odd row 丢失；
凭 sf signal 省略 prime-power Euler 计算。它们不构成所有 Q(i) 方法的绝对 no-go。

可检验的下一阶段应先做一个 good prime π 的 **实际新 probe**：明确选 linear-index core、
square-index projection，还是别的完成对象；列出四个 row exponent、所有 numerator/modulus valuations、
zero masks 和 additive normalization。首要成功条件是同时复现 sf signal (G) 与 rho=1 的终端，
且来自同一完成对象。若该步骤成功，再推 24-cusp 同 profile 反射及 prime-power reciprocal Euler 表。
只有这两步闭合后，重算 marked/plain moment 的 dual norm 长度、kernel seminorm 与 amplifier，
才有依据优化无零域指数。

本次新增可用接口是全 sf signal (G)、新增 v5 phase 的 fixed-ray 简化、完整四分支 local rho=1
有限核、以及已有 square-numerator Voronoi 的具体 quadratic 列。未支付费用是 core coefficients /
实际 completion、完整 reciprocal Euler 商和实际 marked/plain moment。
