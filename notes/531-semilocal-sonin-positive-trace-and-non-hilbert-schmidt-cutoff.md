# 真实半局部 Sonin 正迹与截断 Fourier 的正则性断点

2026-10-13；C005首轮。状态：proved / obstruction，限下面的真实对象。
相对启动基线 `3a72930e9f9f554b03b41d17d8c8002f1813ca82`。
本轮不证明完整 Weil 正性、源差额的符号或最低态排序。

## 1. 原件输入与两种参数

[Connes–Consani–Moscovici, arXiv2310.18423v2](https://arxiv.org/html/2310.18423v2)
的 (57)–(58)、Proposition4.7及Theorem4.6给真实半局部 Sonin 稳定性。
其映射θ_S是有界可逆的 Hilbert 同构；内积随S改变，不能当作酉映射。
这个旧输入不重记新成果。[来源审查](../reviews/2026-10-13/c005-semilocal/source-audit.md)
保存版本、原PDF编号及核读范围，HTML的部分 proposition 标题未正常渲染。

固定 Sonin cutoff 为1；完整型源支持仍用 C005 冻结的
`a=log2,b=log(3/2)/4,μ=13/5,λ_source=√μ`。
Sonin cutoff 与 source 支持不是同一个参数。
先对真实 `S={∞,p}` 推导，再消费实际首素数p=2；没有增加数值样本。

把物理Hilbert空间通过原件的unitary w/F_μ识别到实位偶空间，
再把偶空间unitary识别为 `H=L²((0,∞),dx)`。
写 `a=log p,q=p^{−1/2}`、`U_a f(x)=p^{−1/2}f(x/p)`。
U_a是unitary dilation，`F U_a=U_a* F`；F为实位cosine Fourier，核 `2cos(2πxy)`。
原θ_S在这个共同物理范数下恰为

\[
 B=I-qU_a,\qquad
 (1-q)\|f\|\le\|Bf\|\le(1+q)\|f\|,
 \quad B^{-1}=\sum_{n\ge0}q^nU_a^n.
\]

原件的η_S对应 `(B*)^{-1}`，mixed pairing θ*η=I，
并不是 θ*θ=I。它们的作用与unitary scaling相交换，但固定Sonin空间不由scaling保持。

## 2. 真实正交投影及同源有限正迹

令P为实位Sonin cutoff1的正交投影，M=RanP。
原稳定性给半局部Sonin空间在此unitary识别下为 BM。
设

\[
 W=B^*B=(1+q^2)I-q(U_a+U_a^*),\quad
 G=(PWP)|_M,\quad (1-q)^2I_M\le G\le(1+q)^2I_M.
\]

**同源投影定理。** 真实半局部正交投影与源正迹为

\[
 P_p=BP G^{-1}PB^*,\qquad
 T_p(h)=\operatorname{Tr}(A_hP_pA_h^*)
       =\|BA_hP G^{-1/2}\|_{HS}^2<\infty,
 \quad A_h=\int h(t)U_tdt,\ h\in C_c^\infty(\mathbb R).
\]

证明：`V=B|_M G^{-1/2}`为M到BM的等距映射，P_p=VV*。
实位正迹原定理给A_hP∈HS；A_h与B交换，有界B及G^{-1/2}保HS。
所有cross产品于是trace class，可在同一源上极化。
不能用B P B*或B P B^{-1}冒充正交投影，也不使用非正投影乘积。

令 `Z_h=A_h*A_h`。保留所有物理正交化费用，有精确的边界通量身份

\[
 T_p(h)-T_\infty(h)
 =\operatorname{Tr}_M[G^{-1}PW(I-P)Z_hP]
 =-q\operatorname{Tr}_M[G^{-1}P(U_a+U_a^*)(I-P)Z_hP].
\]

迹合法性：P W Z_h P由HS夹心为TC，G P Z_h P亦TC，
它们的差就是此完整cross块。没有假设各个未夹紧的ambient块TC。
这个身份是实际来源的消费接口，不是已经支付的prime比较。
粗范数界 `κ^{-2}T∞≤Tp≤κ²T∞`，κ=(1+q)/(1−q)，仅为相对Gamma费用。

## 3. 新的实际正则性定理

在同一物理表示中，原半局部Fourier为

\[
 F_p=BFB^{-1}.
\]

W与F交换（F把U_a与U_a*互换），故F_p是自伴unitary involution。
固定任意L>0，令C_L为区间(0,L)乘法投影，`K_{p,L}=C_LF_pC_L`。

**定理。** 对每个真实素数p、每个L>0，K_{p,L}紧、自伴、范数严格小于1，
但不属于Hilbert–Schmidt。其特征值ν_j满足

\[
 \sum_j|\nu_j|^2=\infty,
 \qquad \sum_j\frac{|\nu_j|}{\sqrt{1-\nu_j^2}}=\infty.
\]

证明先在operator norm中展开：

\[
 F_p=(1-q^2)\sum_{n\ge0}q^nU_{-na}F-qU_aF.
\]

每个区间夹心具有光滑有界核而为HS；截断到n=N的operator norm尾≤
`(1−q²)q^{N+1}/(1−q)`。因此K_{p,L}是紧算子。
这是opnorm收敛，不是HS或trace-norm收敛。

精确的分布核是

\[
 k_p(x,y)=2\left[(1-p^{-1})\sum_{n\ge0}\cos(2\pi p^nxy)
                  -p^{-1}\cos(2\pi xy/p)\right].
\]

在远离xy=0的紧支光滑测试上，逐x分部积分支付分布级数的收敛。
取非零χ≥0光滑，紧支于(0,L)²且远离两坐标轴，
`c_n(x,y)=cos(2πp^nxy)`，`φ_N=χ Σ_{n=0}^N c_n`。
非驻相分部积分给

\[
 \int\chi c_n^2=\tfrac12\int\chi+O(p^{-n}),\qquad
 \sum_{m\ne n\ge0}\left|\int\chi c_mc_n\right|<\infty.
\]

因为 `|p^m−p^n|≥(1−p^{-1})p^{max(m,n)}`，
每个交叉积分为O(p^{−max(m,n)})，双和由 `Σ k p^{−k}<∞` 控制。
对χ²同样有效，故 `||φ_N||₂=O(√(N+1))`，而

\[
 \langle k_p,\phi_N\rangle
 =(1-p^{-1})(\int\chi)(N+1)+O(1).
\]

若k_p局部L²，Cauchy–Schwarz将右边约束为O(√N)，矛盾。
HS积分核的唯一性因此排除K_{p,L}∈HS；不是仅以不收敛的点值级数作推断。

最后η=(B*)^{-1}及η^{-1}=I−qU_a*均保持(0,L)的低支持，
且 `F_pη=ηF`。若非零f与F_pf都低支持，g=η^{-1}f与Fg亦同时紧支，
违反实位Fourier整延拓唯一性。紧contraction若范数为1会达到该范数，
产生这样的非零f，故范数<1。紧自伴谱定理再给两个发散式。

这些逐L的严格gap不是统一成长预算。嵌套cutoff的绝对Rayleigh上确界给
`||K_{p,L}||` 随L不减；C_L强趋I、F_p unitary给 `||K_{p,L}||→1`。
所以不存在对全部L统一的正gap。这里L仍为ambient Sonin cutoff，
不能把它与冻结源支持λ_source混同。

## 4. 对真实prime桥的消费与限制

对冻结p=2两patch源，pole严格0，其他primepower相关严格0，
[530](530-archimedean-sonin-prime-compact-repair-boundary.md)给

\[
 Q_W-T_2=-E_\infty-w_2\mathrm{Swap}-(T_2-T_\infty),
 \qquad w_2=\log2/\sqrt2.
\]

新正迹是真实、有限、同源的；但最后的边界通量尚未算成所需
`−w2Swap`及可支付剩余误差。不能把positive Gram直接当成完整型下界。

新增严格边界是：实位有限Fourier的快速衰减、HS和绝对prolate系数测试
不能原样搬到任何真实单素数半局部cutoff。上面的绝对系数和实际发散，
即使每个ν_j仍严格在(−1,1)。这与固定S空间同构、514全素数尾或辅助H边界不同。
它不证明ε_p不连续、不证明诱导的源差额非紧，也不排除有符号抵消。
这些是未付前件，不能从“非HS”越级推断。

尚可作的合法工具：在M上令C=P(U_a+U_a*)P，
`G^{-1}=(1+q²)^{-1}Σ_{m≥0}(qC/(1+q²))^m`。
p=2时ρ=`2q/(1+q²)=2√2/3<1`，对应源迹级数的tail≤
`[(1+q)²/((1+q²)(1−ρ))] ρ^{N+1}T∞(h)`。
这个相对Gamma预算并非uniform源L²质量/紧差额证书；不据它宣布已吸收prime。

## 5. 宏观结算与唯一下一动作

本轮新输入是实际半局部正迹的合法构造/完整通量身份，以及每p/每L的
compact但nonHS严格断点；来源与投影独立审查已对齐，重大regularity结论另逆审。
[不同组织逆审](../reviews/2026-10-13/c005-semilocal/reverse-audit.md)
从真实θ/η和内部测试重建，未消费ε_p符号；
[投影审查](../reviews/2026-10-13/c005-semilocal/projection-transport-audit.md)
另核全部迹类、级数和预算对象。
基线511有Fourier相位、514有不同源卷积边界HS费用，均没有本cutoff断点。
内部审查不等于外部评审或世界优先权认证。

“独立正来源→同一完整型”这一箭头现在有可消费的真实projection/trace接口，
而非只有非酉同构。但宏观完整signed正性、低端排序和增长支持费用仍未解决。
精确尚未付的是边界通量的算术主项与剩余费用，长期Goal保持active。

停止：原样移植实位快速谱/绝对系数误差证明，以及只用粗范数运输晋级。
重准入：实际signed通量身份、直接弱零源评估或可验证的源L²误差控制。
唯一下一动作仍属C005最后一轮：在冻结两patch上直接评估真实通量的
非紧prime主项；若只余unknown比较或relativeGamma尾，按合同停止，不继续加条件名。
