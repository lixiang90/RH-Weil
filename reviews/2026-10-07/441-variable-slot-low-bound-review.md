# 441 可变槽 low 估计的独立审查

2026-10-07。审查对象为 `notes/441-variable-slot-low-bound-on-the-original-probe.md`，canonical LF SHA256：

`dffcaa1899358d581fe3d6438ee87d075588e5e7e8f41ccd8a629fe5c31be0dd`。

**限定 PASS。** 对固定算术数据、固定目标、固定有限物理槽系统，且 `1/6 <= ell <= 1/5, b=1/8`，441 的 low 结论可由所列通用 [R] 结果及原有限补偿身份推导。正 row loss 被原 tuple 权重支付；没有使用 fixed-geometry low theorem 的结论，也没有添加 zero-free 输入。这里不认证原论文的所有外部依赖、实际 high/capacity、共享轮廓全误差或任何新无零边界。

## 1. 版本和读源范围

独立读取 OpenAI/math 提交 `adc7f1241b42e322a6451854ab7e4b4c146bf78a` 的
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`。
该文件 canonical LF SHA256：

`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。

本次逐前件读取的主要原文位置如下；行号绑定上述版本。

| 身份或通用输入 | 原文位置 | 此次检查 |
|---|---:|---|
| `lem:smooth-calculus` | 1123–1178 | 固定 joint profile、共同 Fourier 密度、固定 polynomial height cost |
| `lem:gaussian-annular` | 1288–1315 | 全 annular 尾、加权 homogeneous seminorm 可求和，无 ell=1/6 前件 |
| `lem:reflection-row-sectors` | 2470–2530 | 全部非零元素行、原 S/非单位零延拓、固定有限字符族 |
| common profile 与 Minkowski | 2540–2609 | kernel scalar 在共同密度中提出，平方后才可扩大 positive row sum |
| `eq:low-separated` | 3456–3479 | 同一 Q 球、Q^{-1/2}、实际 ray/Gauss 系数及单位模 norm powers |
| `eq:compensated-probe-definition` | 6868–6910 | 原窗不改尺度、q_{p_J}^{-3/2}、rescaled/marked 子集的原身份 |
| `cor:marked-reflection` 与 phase 分离 | 7361–7483 | whole-index marks、碰撞零项、完整 reflection sectors、系数独立性 |
| `lem:hybrid-energy` | 7510–7540 | a(P) 与 beta(n,b) 的确切独立性、源共享素数及允许 S-primes |
| `lem:reflected-energy` 及其 block data | 7663–7804 | 任意固定 bounded log-length ranges，actual H、Td 与 fixed-parts 已计数 |
| actual kernel、尾与正扩大 | 7846–7992 | 实际 dyad，先删 genuine kernel 尾，再共密度分离和正扩大 |
| `prop:probe-gram` | 8340–8361 | 任意固定 polynomial Q,Y'，Pa>=1，实际固定系数 |

另读 `hybrid-variable-low-admission-derivation.md` 作交叉核验，其 canonical LF SHA256 为
`ff32e95edd5004362b1468cbd4739aa3549194c0e2b28f4f96da1366b3208e62`。
审查中的数值与前件判断来自独立读原 source；该报告不作为另一条新分析前件。

441 所用的是通用结果的陈述，不是 `lem:probe-row-norm` 或 `prop:probe-low` 的固定几何结论。原文 8125–8137 的 Mellin/Gaussian 身份、8214–8307 的局部长度代数可直接检查，都是参数替换后仍成立的身份；本审查没有从其中 ell=1/6 的最后数值反推新定理。

## 2. 原对象与反射前件

原 finite compensation 在 6868–6910 本来就先固定任意有限正槽长度及互不相交的 underlying physical prime windows，再选最终参数。新的 ell 只改变已固定的长度和 X,Y，未改写 probe 的算术系数或 marks。

固定 J 与 p_J 后，`r_J=q_{p_J}/Z^{d_J}` 在同一固定紧区间。因此

\[
 X'=XZ^{-d_J}/r_J,\qquad Y'=YZ^{-d_J}/r_J,
 \qquad Q=q_{b_*}X'Y'\asymp Z^{M'},
\]

的比较常数一致于 moving tuple。这个 row ball 不依赖幸存 marks 或 dual indices。B 行中的 c,n 可共享素因子；同一身份 `q_{cn^3}=q_cq_n^3` 保留 `q_c^{-1/2}q_n^{-1}`。对所有非零 m 应用 row-sector lemma，而不是先把与 S 相交的行删掉。最终 Cauchy 时原 xi(m) 的绝对值至多一即可，不能将其掩码偷偷加到 B 的通用行范数中。

调用 reflected-energy 时必须完整继承其 block data，而不只继承 E_ref 公式。441 的通用 lemma 引用在以下确切意义下合法：

- 冻结 actual powerful 和 supported row ideals、单位及局部选择。残余 moving row primes 的 exponent 是 j=1；所有其他非槽标签，尤其 j=4，已经冻结。
- 固定 R、P 各自的完整 `M_ref^2` 类；不能只固定 RP，也不能只取较小 reciprocity classes。
- marked/base-prime 碰撞的原项先按零延拓删除。此后仅有源的 `1_(P,R)=1`、`1_(P,b)=1` 和 character zeros；不加 `(n,b)=1` 或额外 S-mask。
- active whole-index marks 是 j=0，故 residual j=1 与 active j=0 的交叉相位为 `(q/p)_3^3=1`。其余相位分别归入 row、tuple 或已冻结标签。
- dual coefficient 是完整 extracted dual index 的函数，独立于 R,P；tuple coefficient 独立于 R,n,b。原 marks 的 product form 仍保留到给 extracted factors 分配 slots 的步骤。

这些条件是所引通用 lemma 的既有定义和反射身份，不是为 441 新设的数论假设。允许 dual n,b 含原反射源所允许的 S-primes，并且允许共享素数，恰好符合 source 7731–7735、7835–7841、7952–7967 的范围。

## 3. 共同 Gaussian 密度与实际 Td/H

同一 profile

\[
 w_{k,J}(x,\boldsymbol\varrho)=
 \chi(\log x)W_G\!\left(e^kx/\prod\varrho_i\right)
 \prod W_i(\varrho_i)
\]

的 logarithmic support 固定，Gaussian 参数的对数为 k 加固定有界量。因此加权 homogeneous Fourier seminorm 可求和，whole-annulus 尾可用原绝对计数先删。有限维度依赖已固定槽数，不需要在槽数趋于无穷或 mesh 趋于零时一致。

保留尺度是 `N_*=1+ell'+theta_N`，其中 `|theta_N|<=kappa_G+O_fixed(1/log Z)`。当前行和 tuple 共用一条 Fourier 密度；不是逐行或逐 tuple 另选一个仅有上界相同的密度。recenter 原 smooth factor 时没有改变 coefficient normalization，因此不出现额外 e^k amplitude。反射 kernel 的 scalar 在这条共同密度中提出，再平方；随后 positive sieve enlargement 只能扩大 separated formula 的非负行和，不能在新增行上重算 kernel argument。

`f=rho=1` 后，每个 moving active non-slot prime 都位于 powerful row part，因而

\[
 H\le M'-O+\epsilon_Z,\quad
 2A_0\le O+\epsilon_Z,\quad N_0\le A_0,\quad z_a\le\ell'.
\]

fixed conductor、support ratios 仅进入 `epsilon_Z=O_fixed(1/log Z)`。actual H 不必等于 M'-O。
原通用公式给

\[
 T_d=2H+2A_0+2z_a-1-\ell'-\theta_N-N_0-3B_0.
\]

由 `M'+ell'-1=-3d_J`，直接得

\[
 T_d-(H-3d_J)
 =H-M'+2A_0+2(z_a-\ell')-N_0-3B_0-\theta_N
 \le2\epsilon_Z+|\theta_N|.
\]

retention `y=v+3ell_b+e_lambda<=Td+epsilon_ref` 和非负 ideal centers、`e_lambda>=-O(1/log Z)` 给 `max(H,v+ell_b)=H+small`。genuine kernel 尾的 discarded dual indices 由全源 lattice shell 计数，不需要在 retained 长度上先套一个行数界。

## 4. 正 row loss、empty marks 与 fixed-parts 计数

令 `Delta_H=M'-O-H>=-epsilon_Z`，`s=min{v,z_a,(v+z_a)/3}`。
若 `s=z_a`，完整 E_ref 给

\[
 E_{ref}\le O/2+H+small
 =M'-O/2-\Delta_H+small
 \le M'-\Delta_H+small.
\]

否则 `s>=v/2-small`，且

\[
 s+\ell_b+2e_\lambda/3+(T_d-y)_+/2
 \ge y/4+(T_d-y)_+/2-small\ge T_d/4-small.
\]

核对 saving 的完整身份：

\[
 O/2+\Delta_H+S_0+B_0+T_d/4
 =\frac{2M'+2z_a-1-\ell'+2\Delta_H-\theta_N}{4}
 +\frac{2A_0-N_0+B_0+4S_0}{4}.
\]

第二分子非负。代入 `z_a<=ell'` 后得到 441 的第二分支

\[
 E_{ref}\le M'+
 (1+3\ell'-2M'-2\Delta_H+\theta_N)/4+small.
\]

本次几何的分子准确为 `1+3ell'-2M'=5ell-1+d_J`。两分支对 Delta_H 都不增，所以它们的 formal Delta_H=0 上界可用于全部实际 dyads，所需 O(epsilon_Z) 已保留。共同 Fourier Minkowski、Gaussian 求和、finite sectors 和 logarithmic actual dyads 后，正确统一界为

\[
 \sum_{0<Nm\ll Q}|B_m^J|^2
 \ll Z^{M'+(5\ell-1+d_J)_+/4+\epsilon}.
\]

没有把正 loss 删除。E_ref 已包括 powerful ideals 的 O/2 计数和 supported/local choices 的 divisor loss，不能再乘一次 fixed-parts 总数。

empty surviving slots 时 `z_a=0`，`v>=0` 的 unit/positive ideal dyads 直接使 `s=0=z_a`；bounded ramified offsets 只进 small losses。因此得到更强 `M'+epsilon`，无需沿用旧 d_J=1/6 endpoint。这也说明统一较弱 bound 在新的 d_J=ell 端点合法。

## 5. Gram、tuple 权重与 epsilon 一致性

区间最差端点为 ell=1/5、d_J=ell。精确值为

\[
 M'\ge2/5,\qquad l_x-d_J\ge11/80,\qquad
 l_y-d_J\ge21/80,\qquad
 l_y-d_J-11b/6\ge1/30.
\]

故 Q,Y'>=1 最终成立，位于固定 polynomial ranges。
`Pa=Y'^2/Q=q_{b_*}^{-1}Z^b` 不依赖 r_J；最后一个正 gap 正是 `Pa^2/Y' << Pa^{1/6}` 的条件。常数及阈值可以依赖固定 b_*，且一致于当前 rescaled prime labels。

通用 Gram 因而给 `(Q/Y')Pa^{1/6}Z^epsilon` 的实际 A 行二次界。其 fixed polynomial height cost 由原 W_0 Mellin rapid decay 吸收；没有允许任意 row-dependent arithmetic coefficients。原 Q^{-1/2} 与两个二次界在同一 Q 球合并给

\[
 (X')^{1/2}Pa^{1/12}
 Z^{(5\ell-1+d_J)_+/8+\epsilon}.
\]

`Q asy Z^{M'}` 与固定 q_{b_*}、r_J 只带一致的固定常数。rescaled tuples 的原计数 `Z^{d_J+epsilon}`、原系数 `Z^{-3d_J/2}`、`(X')^{1/2} asy X^{1/2}Z^{-d_J/2}` 合成 -d_J；由于 `5ell-1<=0`，

\[
 -d_J+(5\ell-1+d_J)_+/8\le-7d_J/8\le0.
\]

最后得到 `X^{1/2}Z^{b/12+epsilon}=Z^{(1-ell)/4-b/6+epsilon}`。这是由同一原有限补偿身份支付 row loss，不是额外平均或另加抵消项。

epsilon 在固定目标前指定，有限 slot system 固定。先将每次 local/separation/reflection loss 与 kappa_G 分配到所需 epsilon 的有限小份；再固定 Fourier、kernel-tail/Mellin orders；最后选 Z 阈值，吸收 fixed log offsets 和 dyad 数。Gaussian 和 kernel tails 可在任何指定 saving 下支付，所需 seminorm/阈值均不依赖 moving labels。初稿常数“可依赖它们”的歧义已在最终 48–49、178–179 行修正为：只允许依赖已固定 data/target，不依赖 moving tuples、当前行或素数标签。

## 6. 数值复核与结论边界

独立 BigInt 有理算术核对了上述三个最小值及候选的五个身份，8 项断言通过。对 `ell=10003/60000`，

\[
 l_x=42497/120000,\quad l_y=57497/120000,\quad
 h=32503/40000,\quad low=14999/80000.
\]

`Cb(s)=s-11/16` 在 `s=69999/80000` 恰等于 `14999/80000`。该等式只核对 principal/low 指数接口，没有支付 high。

有限指数检查不替代通用 [R] 分析。441 在固定有限槽系统和上述区间中的新 low 推导为 PASS；无重新证明整篇 OpenAI/math、无 Lean 构建/内核认证，也未证明候选无零边界。实际 high counts、adaptive capacity、shared contour 全误差和 continuation 仍须独立完成。
