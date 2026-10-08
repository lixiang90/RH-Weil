# 条件带权 Möbius 平方自由归约：不同作者全文数学审查

2026-10-08，perron_reviewer。审查者与419行被审源作者不同。
本审查只新增此文件；没有修改研究源、旧审查、检查器、输出或 Git。

**结论：限定数学 PASS。** 已 FULL READ 冻结研究源全部419行，
并独立重推带权 Euler 修正、无限 Perron 截断、局部掩码求和、
真实 Type I 乘积、共同外 Perron 的全部分区与指数账本。
在源声明的整个普通 zeta 半平面前件 \([R_\theta]\)、
固定 \(1/2<\theta<1\) 下，完整归约误差
\(c_\theta=1-1/(2\theta)\) 成立；名义 \(\theta=7/8\) 给
\(3/7\)，消费476既有完整增长输入后给完整矩传递 \(9/14\)。
该 PASS 不包含新的 whole 增长界、常数预算、零点比例或无零区域。

## 1. 冻结绑定与实际审查范围

被审对象：
[条件带权 Möbius 源](hybrid-original-weighted-mobius-squarefree-perron-research-high-product.md)。
419行、17999 canonical LF bytes，SHA256：
`426e0e72e9234e6a9eccbe9a82e3055e7bbbc1669956ae78b9c4a6f82e9799b6`。
canonical 规则仅将 CRLF/lone CR 转 LF，不 trim。

另 FULL READ 根作者汇总
[note490](../../notes/490-original-weighted-mobius-squarefree-conditional-remainder.md)
全部118行、4987 LF bytes，绑定 SHA256
`a5bf40493c864774da5f8fbecce8d257bc21176a78b16ff1841c89843d4924ef`。
其总误差、真实主项、端点排除和研究范围均与419源一致。

本轮重新全文读395源，重新核读484及113源的真实复参数接口；
505、324、401、476已在本研究链全文读取，并对本次消费的段落复核。
这些是解析证明输入，不把文件哈希或有限算式当成无限估计证明。

| 输入 | canonical LF SHA256 |
| --- | --- |
| [395原平方自由 Euler/Perron](hybrid-original-squarefree-core-euler-perron-research-perron.md) | 2f25a678b0c38c95a40469c41a757506c6f1fe64343bed327c7effe298e980c0 |
| [484条件 prefix 汇总](../../notes/484-original-double-perron-conditional-remainder.md) | 38c94314687ccddf1cda08b2d7611c0e1409927b0fb62fdfb0760b32256d1cad |
| [484的427行解析源](hybrid-original-double-log-derivative-perron-research-checkpoint-audit.md) | 8673c02894a1503a8e4bb9e25bfe1c693347ddfc1f5acb070b55a64b3c275b27 |
| [113 buffered reciprocal](hybrid-short-mobius-twist-and-vaughan-zero-residue-research-radial.md) | a970366e68b8d3526c0dadac49b8ee8f4a7b6984e763712a851f8b6d353a291d |
| [505长内因子与 Type I](hybrid-original-extended-inner-zeta-fourth-perron-research-perron.md) | 54d39f22b370be40a780fac6fe80968e24c014fc48d1156ab87248d5310a2549 |
| [324原 Vaughan 分区](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 |
| [401平方丰满尾](hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md) | 66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab |
| [476完整增长输入](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |
| [451既有条件边界](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |

审查对象是419源的新条件证明。395与505的原作者也是本审查者；
本报告不充当这两个旧源的第二作者审查，也不改变它们既有独审状态。
新源从旧全体原系数出发，保留真实 \(b_V(k)\)、原负号、
共同 \(Y<mk\le X\)、全部局部 masks，并允许外 prime \(m\mid k\)。

## 2. 带权 Euler 级数的连续控制

源§2的真实系数为
\[
 d_{r,w}(a)=1_{a\ \mathrm{squarefree},(a,r)=1}\,
       \mu(a)\prod_{p\mid a}(1+p^{-w})^{-1},
 \qquad w=\tfrac12+c-i\tau.
\]
它不是普通 Möbius 系数，不能直接使用无权 prefix 定理。
独立相乘每个 Euler 因子得到
\[
 H_r(z,w)=\frac{K_r(z,w)}{\zeta(z)},
\]
\[
 K_r(z,w)=
 \prod_{p\nmid r}\left(1+
 \frac{p^{-z-w}}{(1+p^{-w})(1-p^{-z})}\right)
 \prod_{p\mid r}(1-p^{-z})^{-1}.
\]
当 \(\Re z\ge\theta+\delta\)、\(\theta\ge1/2\) 时，
\(\Re z+\Re w>1+\delta\)。分母由相应实部下界控制，
第一个乘积绝对、局部一致收敛；不需要声称它无零或估计其倒数。
第二个有限乘积统一为 \(\ll_\eta r^\eta\)：有限小素数归入常数，
大素数满足 \(-\log(1-p^{-1/2})\le\eta\log p\)。
故源(7)的局部损失合法，不遗漏 \(r\) 的素因子。

初线另须绝对收敛，不能把 \(|d(a)|\ll a^\eta\) 带到无穷。
独立核其绝对 Euler 因子：
\[
 \sum_{a\ge1}|d_{r,w}(a)|a^{-1-c}
 \le\prod_p\left(1+\frac{p^{-1-c}}{1-p^{-1/2}}\right)
 \ll\zeta(1+c)\ll L.
\]
对数展开的一阶主项为 \(\sum_p p^{-1-c}\)，
与该项的差由 \(\sum_p p^{-3/2-c}/(1-p^{-1/2})\) 绝对控制。
常数对 \(r,w,c\) 统一；这才支付无限远尾。

## 3. 内部 Perron：全部无限尾、近整数及真实高度

源§3用 \(x^\sharp=\lfloor x\rfloor+1/2\)，
精确保持原整数条件 \(a\le x\)。初始相对实部 \(\kappa=1/2\)
使绝对 Euler 参数 \(\Re(w+\xi)=1+c\)；固定内部高度为 \(T/32\)。
标准截断误差的正包络是
\[
 \sqrt{x^\sharp}\sum_{a\ge1}|d(a)|a^{-1-c}
 \min\{1,(K|\log(x^\sharp/a)|)^{-1}\}.
\]
对 \(a\notin(x^\sharp/2,2x^\sharp)\)，上节绝对 Euler 和直接给
\(O(\sqrt x\,L/T)\)，包含 \(a>2x^\sharp\) 的整个无限尾。
近段只在有限 \(a\asymp x\) 使用 \(a^\eta\)，
半整数距所有整数至少 \(1/2\)，谐和求和给
\(O_\eta(x^{1/2+\eta}T^{-1}\log(2x))\)。
它不是有限枚举，也没有以 \(a^\eta\) 替代初线绝对级数。

左相对实部 \(\lambda=\alpha-c>0\)，
\(\alpha=\theta-1/2+\delta\)，使真实参数 \(w+\xi\)
恰在 \(\Re=\theta+\delta\)。最终 \(c<\alpha\) 且
\(\alpha-c<1/2\)，可作固定矩形移线。
整个内部高度区间为 \([3T/32,133T/32]\)。
113源 buffered reciprocal 的全高度次幂界在此连续区间适用。
\(K_r\) 全纯，\(1/\zeta\) 在 \([R_\theta]\) 下无极点；
\(\zeta\) 的极点成为 reciprocal 的零点，核 \(\xi=0\) 也不被跨越。
因此没有遗漏零点或极点留数。

左边界费用为 \(r^\eta x^\alpha T^\rho L^C\)，
两水平线为 \(r^\eta\sqrt x\,T^{-1+\rho}L^C\)。
先选择近段的 \(\eta\)，把 \(x^\eta\le T^\eta\) 吸收到所预留
\(T^\rho\) 后，得到源(13)；\(1\le x<2\) 由唯一 \(a=1\) 直接付。
当 \(x\le V\) 时，上式中的第二项对固定合法参数是负幂误差，
不影响主费用。

## 4. 全部局部掩码与外部移线范围

源§4从395的真实除数恒等式使用
\[
 F_{V,r}(w)=\prod_{p\mid r}(1+p^{-w})^{-1}
   \sum_{e\mid\operatorname{rad}r,\ e\le V}
           \mu(e)S_{r,w}(V/e).
\]
这里确实没有 \(e^{-w}\)：\(e\) 是实际 \(b_V(sr)\) 的除数部分，
原 \(r^{-w}\) 已承担其整数重量。实际截断 \(ae\le V\)
和 \((a,r)=1\) 都保留，不把局部 mask 放大后当成 signed 单调域。
逐个 \(e\) 的上界只产生合法 \(r^{2\eta}\tau(r)\)。

平方丰满 dyadic 计数 \(\#\{r\asymp R\}\ll\sqrt R\)
给 \(\sum_{2\le r\le H}r^{-1/2}\ll\log H\)。
先固定小局部损失，把 \(r\le H\le X\) 的损失分配到最终
\(\epsilon\)，可得 \(C_{\ge2}\ll V^\alpha T^\rho X^\epsilon L^C\)
及已付款的负幂项。全部 \(2\le r\le H\) 的项都在求和中。

该条件 bound 仅证明在 \(\Re w=1/2+c\) 的外垂直线。
源明确继续用395已有的无条件 \(\sqrt V X^\epsilon L^C\)
控制外部水平线。此安排合法：没有把未证明的条件带权 prefix
强行推广到整条横向复参数区间。

## 5. 真实 Type I、prime 定义及共同外 Perron

源§5消费484两个真实 \(+c\) prefix，并用 Abel 保持该实部。
\(F_{\Lambda,U}\)、\(G_V\) 均为 \(O(U^\alpha T^\rho L^C)\)，
\(U=V\)。484内 \(\Lambda\) 的 pole 与截断小项在本参数下可吸收。
\(F_U^{\rm prime}\) 必须减掉有限 proper-power prefix；
其 normalized 绝对费用为 polylog，故相同点值 bound 成立。

实际 Type I 系数满足精确有限多项式恒等式
\(\Gamma_{U,V}=-F_{\Lambda,U}G_V\)。
两 Type I 直接在有限外 Perron 的 \(c+i\omega\) 使用
\(\Gamma W_N\)、\(G_VW_{\log,N}\)，无需水平移线。
取505已证 \(N=\lfloor10T\rfloor\)；最大有限乘积长度
\(UVN\asymp X^{1+2v}<X^2\)。所有附加 \(n>X\) 系数及
两个半整数端点的截断误差仍由505的完整正包络付款。
不能删除长内因子的这些系数。

505的统一 \(\zeta^4\) 及由 Cauchy 得到的 \((\zeta')^4\)
只产生对数费用。先对共同 \(\omega\) 作 Minkowski，再消费
相同真实点值与连续高度 guard，得 Type I2 的 \(8\alpha v\)
和 Type I3 的 \(4\alpha v\) 第四矩指数。
没有误把 \(|\zeta\zeta'|^2\) 当作 \(|\zeta'|^4\)。

§6两个生成函数保留395的全部真实系数：
\[
 {\cal H}_{\ge2}
 =\frac{[\zeta'+(Q_{\rm pp}+F_U^{\rm prime})\zeta]C_{\ge2}}
          {a_LL\zeta(2w)},\qquad
 {\cal H}_{\rm pp}=-\frac{Q_{>U}(\zeta G_V-1)}{a_LL}.
\]
\(Q_{\rm pp}\) 是全部 proper powers，\(Q_{>U}\) 是仅 \(m>U\)
的 proper powers，而 \(F_U^{\rm prime}\) 只含低 prime；没有双扣。
初线的无限远尾仍使用395精确 \(n^{-1-c}\) 的 \(\zeta^3\) 对数导数预算，
不是将 \(n^\eta\) 带到无穷。外部矩形不跨 kernel 极点或
\(\zeta\) 极点；取消后的表达式在该有高度 guard 的区域全纯。
全部水平费用仍无条件为负幂 \(X^{-1/2+v+\epsilon}\)。
新的条件 prefix 只在外垂直线被消费，得小 squarefull 族
\(8\alpha v\)、全部 proper-power 族 \(4\alpha v\) 的第四矩费用。

## 6. 完整参数账本与传递

源§7的精确分区保留全部 proper powers、全部 \(r>H\) prime尾、
全部 \(2\le r\le H\) prime族和真正未付的平方自由 prime 主项。
401尾界允许实际 \(M_0=U\)，不要求改成其它 prime 截断；
费用为 \(1-4v\)。低段费用仍为 \(2y-1\)。
对任意最终 \(\epsilon>0\)，先取足够小的 \(\delta,\rho,\eta\)
并分配日志损失，设 \(\beta=2\theta-1\)，完整费用确为
\[
 \max\{2y-1,4\beta v,1-4v,0\}.
\]
Type I3 与 proper powers 的 \(2\beta v\) 已被 \(4\beta v\) 支配。
\(v=1/(8\theta)\)、\(y=1-1/(4\theta)\) 对固定 \(\theta>1/2\)
满足严格 \(v<1/4\)、\(y>1/2\)、\(y-2v=1-1/(2\theta)>0\)；
三项主费用等于 \(c_\theta\)。floor只产生固定常数。
源明确排除 \(\theta=1/2\) 的不合法参数端点；其 prefix lemma
可在带固定 buffer 的该端点成立，不等于达成零误差指数。

独立有理运算核准 \(\theta=7/8\) 下
\[
 v=1/7,\quad y=5/7,\quad
 (2y-1,4\beta v,2\beta v,1-4v,0)
       =(3/7,3/7,3/14,3/7,0).
\]
新参数改变真实主项；完整函数 Minkowski 给继承的 \(5/7\) 界，
随后四阶差的 Hölder 给 \([3(5/7)+3/7]/4=9/14\)。
相对旧 \(1/2,37/56\) 的节省分别为 \(1/14,1/56\)；
相对486的 \(9/17,159/238\) 分别为 \(12/119,3/119\)，均精确。
有限 Fraction 运算只检查上述代数，不替代连续解析估计。

## 7. 零点包和最终范围

真正平方自由生成函数仍是
\(B_{\rm sf}=\zeta(w)F_{V,1}(w)/\zeta(2w)-1\)。
有限 \(F_{V,1}\) 在 \(\Re w>0\) 全纯；对 \(\Re\rho>1/2\)，
\(1/\zeta(2\rho)\) 解析，故 \(B_{\rm sf}(\rho)=-1\)。
prime 因子 \(A_U=-\zeta'/\zeta-Q_{\rm pp}-F_U^{\rm prime}\)
仍有留数 \(-m_\rho\)，所以 \(-A_UB_{\rm sf}\) 的留数也是
\(-m_\rho\)。两个原 sharp 端点核仍完整保留该零点包。

此独审没有发现需修改419源的数学缺口。限定 PASS 准入其真实
完整条件误差归约及已明确前件下的完整矩传递；不把它扩大为
新的无零前件、whole 界、常数级 \(o(1)\)、零点比例或独立零点包消去。

## 8. note490 的既有边界应用

note490§3是一般 \(c_\theta\) 的合法应用，不是419源新增无零区域。
451已经全文读取，本轮核对其最终哈希及明确的完整依赖：
445原 \([R]\) 输入包、450的 lower-\(\kappa\) 输入和既有
whole finite-order Hecke \(7/8\) bootstrap。不能把它缩减成
单一普通 \([R_{7/8}]\)，也不能把新的误差归约倒推成新前件。

独立 Fraction 算式（未导入任何项目检查器）复核
\(p(e)=657e^3-954e^2+21e+20\) 在
\(e_- =0.16683858898627\)、\(e_+ =0.16683858898628\)
的严格正、负符号。\(p'<0\) 在 \([1/6,0.167]\)，
故该根区间唯一；\(\theta_*=11/12-e_*/4\) 严格在 \((5/6,7/8)\)。
476的 \(B_I(\theta)=4\theta-3+3(1-\theta)/(2\theta)\)
因此在自己的合法区间被消费。

\(c_*=1-1/(2\theta_*)=(5-3e_*)/(11-3e_*)\)。
\(c_\theta\) 和 \(B_I(\theta)\) 在此均严格递增，
代入两个有理根端点后独立得到
\[
 0.4285433582424544<c_*<0.4285433582424561,
\]
\[
 0.6427843417753810<
       (3B_I(\theta_*)+c_*)/4<0.6427843417753854.
\]
note490两段包络正确，并保留451全部引用条件。
这些是有限代数核验；新的带权复 Euler 收敛、移线、共同截断
和完整分区的 PASS 来自本报告§2–7的连续审查。
note490所链接的新检查器与保存输出不在本数学独审的执行范围中。
