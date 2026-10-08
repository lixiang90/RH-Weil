# 长内层 ζ 四矩、原乘积 Perron 与完整误差：不同作者全文审查

2026-10-08，checkpoint_audit。
**结论：相对所列明确前件的数学 PASS；没有当前实质阻断。**

本审查完整读取 perron_reviewer 的最终研究源全部 505 行，逐步重推新增
Euler/Abel 尾、长内层与 ζ′ 四矩、共同有限乘积截断及实际分区。
批准的无限估计范围是原 Type I、原 short Λ/μ 子项和由它们合成的完整误差；
其中无条件版本为 3/5，普通 [R7/8] 下版本为 9/17。
完整 159/238 传递另依赖已冻结 476 的同对象 whole 5/7 输入。
这不批准新的 whole 上界、常数级中心矩、零点比例、RH 或新的无零边界。

## 1. 最终身份及实读范围

唯一审查研究源为
[最终作者源](hybrid-original-extended-inner-zeta-fourth-perron-research-perron.md)。

- canonical UTF-8 LF SHA256：
  54d39f22b370be40a780fac6fe80968e24c014fc48d1156ab87248d5310a2549
- 505 行，21073 canonical bytes；只统一 CRLF/lone CR，不 trim、不改 EOF。
- 先全文读过 477 行的 0e9a3f8d6d9adfd675754a576430c832343f9e98c491dff78383133803a787d1。
  随后再次全文读最终 505 行；反向删除新 §10 并还原旧节号，精确恢复这个旧 SHA。
  因而最后变化仅为无条件推论的 28 行和后节编号。

本轮重新全文读取 484、451、476 的笔记，核对其条件、原函数和既有输入范围。
下面其他证明已在同一连续研究轮全文读取并重推；本轮重新核其全部 canonical 身份。
其中 482 的有限 Perron 和 481 的完整 tail 是本审查作者此前写出的证明，
故本次不同作者审查所针对的是 perron_reviewer 的新长因子证明，
不把本作者自己的旧源称为新的独立作者证据。

| 冻结输入 | 行数 | canonical UTF-8 LF SHA256 |
|---|---:|---|
| [484 原摘要](../../notes/484-original-double-perron-conditional-remainder.md) | 194 | 38c94314687ccddf1cda08b2d7611c0e1409927b0fb62fdfb0760b32256d1cad |
| [原 Λ/μ 双因子 source](hybrid-original-double-log-derivative-perron-research-checkpoint-audit.md) | 427 | 8673c02894a1503a8e4bb9e25bfe1c693347ddfc1f5acb070b55a64b3c275b27 |
| [其同行审查](hybrid-original-double-log-derivative-perron-review-peer.md) | 350 | 1f05daa4c005b8e8363f985d31468188e312b1615fff2f1123bb227646a66f02 |
| [482 摘要](../../notes/482-original-conditional-mobius-perron-remainder.md) | 139 | c0abff933a180f5591412f82772634091f8db0e2079f846772f8a7047ed4a912 |
| [482 有限 product Perron](hybrid-original-optimized-type-ii-remainder-research-checkpoint-audit.md) | 477 | 2d43aa69d79bde9a3aeac00ff4c9ee79696640f816df28eba051011ab255b25d |
| [481 全参数摘要](../../notes/481-original-type-ii-squarefull-tail-and-optimized-moment-transfer.md) | 239 | 4ce3ea2ac087d734142c8788607c1c54fc6887bcf535c806c88097447afdc63e |
| [完整 squarefull tail](hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md) | 401 | 66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab |
| [原 Vaughan 与 Type I](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | 324 | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 |
| [479 最大 prefix、疏项](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | 524 | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 |
| [原 scalar proper-power 迁移](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | 370 | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [476 whole 输入](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 96 | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |
| [451 原完整相对依赖](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 244 | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |

12 个输入身份均实际重新计算并相符；本审查没有执行旧检查器或重型 coverage。

另外绑定 [486 最终数学摘要](../../notes/486-original-padded-perron-fourth-mean-remainder.md)：
193 行、7868 canonical bytes，SHA256
5e98058d6d47545aedb98b6e70f66f4e11a904b623351903e3846e01bbe7eaf7。
先全文实读183行数学正文，再实读新增§7的10行（含分隔空行）；
精确切去追加段恢复旧SHA58c890b7273b02d64da40f8c780589f9af41f26a2e1ec6cb35a6b5801dc44dd6。
摘要的条件、无条件、旧band及未付范围与本次批准范围一致。
§7只描述有限检查的范围，本审查未执行该新检查器或认领其实际PASS。
上述身份核对不能代替下面的数学重推，也不重新认证 451 所列外部 [R] 全输入包。

## 2. 经典输入与真实实部、正高度

实际打开并读取
[Montgomery–Vaughan 原书 III，Theorem 26.23](https://personal.science.psu.edu/rcv4/Vol3/Vol3.pdf)
的 statement 和完整显示证明，PDF 第151页、印刷第143页。
该合同是统一于 \(|\sigma-1/2|\le2/\log U\) 的第四均值上界，
不是固定 \(\sigma>1/2\) 的渐近公式。原证明通过平滑 approximate functional equation、
有限多项式均值和 divisor 能量获得所需日志上界；这里只消费其定理，不认证整本书。

令 \(c=1/L,\ U=5T\)。充分大 T 时 \(3/(2L)\le2/\log(5T)\)。
对 \(|\omega|\le T/8,\ t\in[T/4,4T]\)，真实
\[
 s=1/2+c-i(t-\omega)
\]
的绝对高度在 \([T/8,33T/8]\)。
半径 \(c/2\) 的 Cauchy 圈实部在
\([1/2+c/2,1/2+3c/2]\)，小虚部偏移后仍处于 \((0,5T)\) 的绝对高度。
负虚部通过 ζ 的 conjugation 转到正高度，因此原归一化 L4 合同对全部共享 ω 统一。

以 ζ 本身的 Cauchy 公式及 L4 Minkowski 得
\(\|\zeta'\|_{4,T}\ll c^{-1}\|\zeta\|_{4,T}\ll L^2\)。
这是合法的 ζ′ fourth 上界；没有误用 \(|\zeta\zeta'|^2\) 的均值。
这里不需要任何无零前件，Cauchy 圈也不包含 ζ 的 pole 1。

## 3. Euler、Abel 与完整无限尾

对同一个固定整数 \(N=\lfloor10T\rfloor\)，源式(8)的整数端点符号正确：
\[
 \zeta(s)=W_N(s)+\frac{N^{1-s}}{s-1}
 -\frac12N^{-s}-s\int_N^\infty\psi(u)u^{-s-1}\,du.
\]
在 \(\Re s>1\) 由计数积分得式，再续延到 \(\Re s>0,\ s\ne1\)；
积分在显示实部范围绝对收敛。
主极点项没有删除：\(|\tau|\asymp T,\ N\asymp T\) 给
\(N^{1-\sigma}/|s-1|=O(T^{-\sigma})\)。

ψ 的 Fourier 不能无条件绝对换序。源先取周期 Poisson/Abel 平均
\(\psi_r\)，固定 \(r<1\) 时 Fourier 绝对收敛，
\(\sup|\psi_r|\le1/2\)，且在非整数点趋于 ψ。
原积分由 \(u^{-\sigma-1}\) 可积 domination 保证取限合法。

逐 \(h\ne0\) 的相位
\(\Phi_h=2\pi hu-\tau\log u\) 在全部 \(u\ge N\) 上满足
\(|\Phi_h'|\ge\pi|h|\)，因为 \(N\ge9T,\ |\tau|\le5T\)。
边界项和 amplitude/phase′ 的导数积分分别给
\[
 \left|\int_N^\infty u^{-\sigma-1}e^{i\Phi_h(u)}du\right|
 \ll N^{-\sigma-1}/|h|.
\]
乘 ψ 系数 \(1/|h|\) 后是完整可求和的 \(h^{-2}\)；
随后乘 \(|s|=O(T)\)，得到 \(O(T^{-\sigma})\)。
这支付了整个无限 u-tail，并非把未知尾截断成 polylog 误差。

在所有实际 \(c/2\) 圈上，\(W_N-\zeta\) 解析，N 固定，
\(T^{c/2}=O(1)\)。对这个完整差使用 Cauchy 得
\(W_{\log,N}=-\zeta'+O(T^{-\sigma}L)\)，含主极点项的导数费用。
因此源(13)的两个统一 normalized L4 上界成立。

## 4. 延长后仍是原共同 sharp 函数

原整数 j 被延至 N，新增 \(j>X\) 在二因子或三因子中都产生 \(n>X\)。
这仅证明 n≤X 的系数保持；新增项仍必须经过有限 Perron，
不能在积分前免费丢弃。
两个端点 \(x^\sharp=\lfloor X\rfloor+1/2,\ y^\sharp=\lfloor Y\rfloor+1/2\)
恢复原整数集合 \(Y<n\le X\)。

对全部 product 系数，包括 n>X，
\(|\gamma_n|\le C_\phi\tau_3(n)/\sqrt n\)，支撑 \(n\le Z\ll X^z,\ z<2\)。
逐系数有限 Perron 的近端 half-integer harmonic 和远端和给
\[
 O_{\phi,\eta}\!\left(X^{2\eta}
 \{\sqrt Z/T+\sqrt X\,T^{-1}\log(2X)\}\right).
\]
远端完整包括额外 j、额外 n，以及产品尾；固定 N/X 的变化只改变常数。
外核绝对积分 \(O(L)\)，共享 ω 的一次 L4 Minkowski 合法。
外层 integrand 是有限全纯 product，不涉及 ζ 的零点移线。

短项 \(Z=AVN\asymp X^{1+a+v}\) 的远端指数为
\(-1/2+(a+v)/2+2\eta\)，近端为 \(-1/2+2\eta\)。
Type I 两项分别 \(Z_2=UVN,\ Z_3=VN\)，远端指数
\(v-1/2+2\eta,\ (v-1)/2+2\eta\)。
源的固定余量保证先选小 η 后全部为真负幂。

## 5. 原短项与 Type I 费用

条件短项保留原 \(\Lambda(m)q(m),\mu(d)\)、负号与共同 \(Y<mk\le X\)。
\(q(m)=1\) 或 genuine-prime 指示通过原 prefix/prime-power 差接口，
并未升级为任意 signed 子集。
\(AV<Y\) 保证原 m-band 的 k>V 自动成立；
展开 \(b_V(k)\) 后仍恢复完整 product cut。

在同一真实 +c 和 guard 上，冻结双 Perron 供应
\(F\ll A^\alpha T^\rho+\sqrt A/T+\text{内部尾}\)，
\(G\ll V^\alpha T^\rho\)。
Λ 的主 pole 和内部无限 Perron 尾明确存在；
pole 乘 G 后的 norm 指数 \(a/2-1+v\alpha+\rho<-1/2+\rho\)。
只有 F、G 使用已证 pointwise sup，长 W 使用第四均值。
分配 δ、ρ、日志及 η 于任意给定 ε 后，短项 fourth 为
\(X^{2\beta(a+v)+\epsilon}\)，\(\beta=2\theta-1\)。

Type I 的真实 \(g=-\Lambda_{\le U}*\mu_{\le V}\) 不变。
其加权绝对质量 \(\ll\sqrt{UV}\log(2U)\)，
另一条 μ 外质量 \(\ll\sqrt V\)。
分别消费 \(W_N,W_{\log,N}\) 和同一共同 Perron，
得 I2 norm \(X^vL^C\)、I3 norm \(X^{v/2}L^C\)，合成 fourth 为 \(X^{4v+\epsilon}\)。
Type I 本步无条件，没有额外声称 Möbius 相消。

## 6. 分区、费用最优性与 complete transfer

原 low、large proper m、完整 r>H 尾保持既有无条件合同；
新主分区仍取 \(H=V^2\)，费用为
\[
 C=\max\{2y-1,4v,2\beta(a+v),1-2a,1-4v,0\}.
\]
\(C\ge1/2\) 来自 4v 与 tail，亦吸收独立 squarefull-k 的 1/2 费用。
从 proper/tail 得 \(a\ge(1-C)/2,\ v\ge(1-C)/4\)；
代入短费给 \(C\ge3\beta/(2+3\beta)\)。
源显示的 θ≤5/6、θ≥5/6 两组参数分别达到这两个下界。
所有一般量词、y 下界和固定幂前件成立，接合点一致。
该 optimality 仅针对列出的费用族。

主参数 a=2v 时，精确 floors 给 \(V^2\le\lfloor X^{2v}\rfloor=A\)。
r≤H 的 pure-squarefull k 全部 bV=0；非零剩余保留 s(k)≥2，
而不是换成 odd squarefree kernel。
prime m>A 与 r 互素，但没有添加 m 与 s 互素的假掩码。
最终 R 保留原所有 aspect ratios、Λ、bV、负号和两端共同 cut。

θ=7/8 的五费逐项为 \((9/17,8/17,9/17,9/17,9/17)\)。
有限次 Minkowski 得 E=P_H−R 的 9/17 fourth；
只在另外消费 476 同对象 whole 5/7 后，R 才继承该幂。
完整 Hölder 差随后给
\[
 (3(5/7)+9/17)/4=159/238,\qquad 5/7-159/238=11/238.
\]
不存在未知主项 lower 的使用，不是 relative equivalence 或常数级 o(1)。

## 7. 无条件推论、旧固定 bands 和 θ* 依赖

源新 §10 不使用 [Rθ]：真实 F、G 的绝对质量给 \(\sqrt{AV}L^C\)，
消费相同无条件长 W fourth，短费为 2(a+v)。
取 \((v,a,y)=(1/10,1/5,4/5)\) 时五费
\((3/5,2/5,3/5,3/5,3/5)\)，完整 E0 fourth 无条件为 3/5。
此 R0 与条件主参数 R 是不同配置。
本结论不附带无条件 whole 上界或无条件 159/238 传递；
相对 481 的无条件误差节省 \(2/105\) 精确正确。

固定旧484配置时，62/225 的新 m 截断 short 费用为43/75；
固定旧482配置时，74/243 的新截断 short 费用为49/81。
各自先付完整 k-band，再直接以同 m-mask 付 r>H tail，
两完整函数之差支付 r≤H band，保持旧 bV、V、Y。
允许 a2>1/4，因为原 Λ prefix 合同实际覆盖全部 N≤X；
μ 的 v<1/4 和 a+v<y 仍满足。
这没有使用 signed norm 的子集单调性。

θ* 用途必须接受 451 全部相对输入及其 ordinary ζ transfer。
把它压缩成仅 [R7/8] 的输入是无效的。
对 476 已给的 5/6<θ≤7/8 域，
\(c_\theta\le9/17<19/30\le B_I(\theta)\)，
故 source(31) 的完整传递合法。
由 451 根区间独立 Fraction 重算 c*、v*、a*、y*；
两处显示十进制外包围均为严格有理外包围。
这些有限计算核代数，不认证 451 的无限外部前件。

## 8. 审查边界和冻结

原完整 C4 的 generating function 与 ζ 零点 residue \(-m_\rho\) 保持；
有限长 W 的延伸不为该 residue 添加小因子。
普通 ζ fourth 仅消费一个真实无权因子的均值。
balanced prime/squarefree signed mixed4、whole 5/7 的改进、
实际中心四阶常数以及高产品次弧 joint F·G 仍未付款。

有限证据仅包括 12 个 canonical 输入与本源身份、唯一 append diff、
本地链接和少量独立 Fraction 恒等式/严格包围；没有执行未知外部代码、
旧 coverage、有限素数实验、Lean 或新检查器。
数学 PASS 的依据是上述逐步分析与明确经典/冻结前件，
不能由 hash 或未来有限 checker 的 PASS 替代。
本审查只新增此文件；没有修改任何研究源、旧文件、输出或 Git。
