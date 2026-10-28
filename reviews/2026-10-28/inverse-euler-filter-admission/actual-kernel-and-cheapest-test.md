# Actual inverse-Euler filter：剩余Gram核与唯一相对test准入

2026-10-28；`/root/rational_first_gate`当前新任务，非cooling／Gaussian／poly续算。已恢复README／STATE、check→show、同G20261027／原0c4f、Goal／macro frontier／AV及当前已耗尽C052；root随后直接给本次inverse-Euler具体准入。只用项目实际公式及已付proof接口，不web／PDF／源查询／数值，不改STATE／Git／cadence，不预C053／590或新proof合同。

**结论：规则合法，显式Euler因子确可取消，但剩下的是完整weighted Gram逆的reproducing kernel；不是原arch Sonin投影的对角。所核最强旧没有立即判定校准后的g′ ratio。** 本稿给一个明确未付量(R)，而非generic未知K。PNT／既有necessary gain也未给矛盾；校准β必须保留，不能只看原权的最大增益。本稿只到准入，未执行(R)的新估计。

## 1. 有限Euler因子的符号约定先固定

将题设complex变量的有限Euler product记为

\[
 \mathcal D_X(s)=\prod_{p\le X}(1-p^{-s}),\qquad
 d_X(t)=\mathcal D_X(\tfrac12+it)
       =\prod_{p\le X}(1-p^{-1/2-it}).                 \tag{1}
\]

这正是560的b_F(t)及585的D_X(t)，不是ζ有限Euler product的倒数。560 §3另用D=B_F^−1表示causal operator inverse；那是不同字母角色，不能混成(1)。沿原物理酉log坐标，B_X=∏(I−p^−1/2 U_logp)的Fourier symbol为d_X。

每finite X，d_X在real轴无零；置

\[
 m_X=\prod_{p\le X}(1-p^{-1/2}),\qquad
 M_X^+=\prod_{p\le X}(1+p^{-1/2}),
\]

则`0<m_X≤|d_X(t)|≤M_X⁺`。所以bare测度

\[
 d\nu_X^0(t)=\frac{\rho_X(t)}{|d_X(t)|^2}dt
\]

为正tempered测度：560逐X的log密度界乘finite m_X^−2仍有效。一般总质量∞，不能落入Gaussian fixed-finite-mass atom门；对compact smooth原physical源配对有限。原source Fourier为∫r(u)e^(−itu)du，ρ已经含receiver2π。

同一source预处理的Fourier乘子是1/d_X，而不是1/d_X²；其模平方给上述权。每X它是bounded、通常nonlocal的算子；不声称保持compact支撑或把原全部Dlog改成另一域。后续只测试原Cc∞源及其合法谱配对。

## 2. 实际取消后留下什么：basis和weighted norm均不能省

令arch receiver空间M=RanP，在Mellin酉表示的Hilbert measure为dt/(2π)。取raw evaluator k_t满足h(t)=⟨k_t,h⟩，并令

\[
 G_X=(P M_{|d_X|^2}P)|_M,\qquad
 \Pi_X=M_{d_X}P G_X^{-1}P M_{\overline d_X}.
\]

560若采用带1/√(2π)的k_t，则其evaluator norm平方直接为ρ；此处为与589 actual kernel一致，使用未吸收2π的raw evaluator，准确有

\[
 Q_X(t)=\langle k_t,G_X^{-1}k_t\rangle,
 \qquad \rho_X(t)=\frac{|d_X(t)|^2Q_X(t)}{2\pi},
\]
\[
 \boxed{d\nu_X^0(t)=\frac{Q_X(t)}{2\pi}dt.}          \tag{2}
\]

取原M的任意ONB e_j。actual Π_X range的ONB为

\[
 d_X\,G_X^{-1/2}e_j,
\]

所以(2)的对角可写成`(2π)^−1Σ_j |(G_X^−1/2 e_j)(t)|²`。这些G_X^−1/2 e_j只对**weighted norm**

\[
 \|h\|_X^2=\int|d_X(t)h(t)|^2\frac{dt}{2\pi}
\]

构成ONB，不是原unweighted M的ONB。取消外面的d_X不把G_X变成I，也不把算子`P G_X^−1P`变成P。算子在M上的平方为G_X^−2；没有G_X=I前件就不能称它为orthogonal projection。

因此显式Euler幅度取消以后，全部arithmetical dependence仍在G_X^−1和weighted-unit-ball evaluator内。不能声称只剩Γ、原arch kernel或某个已知nested projection。

## 3. 校准及唯一尚未判定的actual量

记

\[
 \mathcal T_X(r,s)=\int\widehat r(t)\overline{\widehat s(t)}
                         Q_X(t)\frac{dt}{2\pi},
 \qquad a_X=\mathcal T_X[g].
\]

同587 literal g非零，a_X finite且strict positive。完整目标q₀=Q_W[g]>0，故按题意取

\[
 \beta_X=q_0/a_X,\qquad
 d\nu_X(t)=\beta_X\frac{Q_X(t)}{2\pi}dt.             \tag{3}
\]

这是exact g校准；也可允许渐近校准，但不能忽略其β费。对g′的必要测试恰为

\[
 \boxed{R_X:=
 \frac{\displaystyle\int t^2|\widehat g(t)|^2
                      \langle k_t,G_X^{-1}k_t\rangle\,dt}
      {\displaystyle\int |\widehat g(t)|^2
                      \langle k_t,G_X^{-1}k_t\rangle\,dt}
 \ \stackrel{?}{\longrightarrow}\ R_*:=q_1/q_0>0.}   \tag{R}
\]

2π在ratio中精确消去，g′的Fourier因子it给t²。实际calibrated test为`W_X[g′]=q₀ R_X`。q₁使用537完整Γ／FP-contact、所有Λ(p^k)=logp和双pole，g′ mean0不等于polefree。

这就是本稿冻结的**一个**未付量：同一actual G_X、同一fixed g上的归一化second moment。证明R_X与R_*有非消失差即可停止本规则；证明R_X→R_*只让它通过这两个fixed tests，不等于完整D′身份，更不独立支付经典正性。没有把它改名generic K预算或未知正H。

等价地，`dπ_X(t)=|ghat(t)|²Q_X(t)dt/(2πa_X)`是实际probability measure，(R)就是`∫t²dπ_X`。这份π_X不是原ν_X，也没有由π_X质量1免费得到second-moment uniform integrability；未付量因此有明确对象／norm／可判目标。

## 4. 最强旧为何尚未直接给(R)

已核560实际全Gram公式、585 trial／cofinal范围、587 actual derivative Gram及589原upper／localization的必要接口；在这些原件中未定位到适用于`P G_X^−1P`的cofinal monotonic-projection定理。不是由名字判定没有定理：actual对象已由(2)精确给出，旧projection是Π_X，移去M_d后的正算子不是同一个projection。

添加一个新prime p时，Gram中的实际因子是

\[
 I+p^{-1}I-p^{-1/2}(U_{\log p}+U_{-\log p}),
\]

夹在B_X及P之间。这个identity不自带Loewner单调号或nested range前件。本稿不据oscillating symbol就宣判actual compressed difference不定，也不另造反例／证明；只是不从未给出的order推(R)。

旧585／587下界直接控制的是`|d_X|²Q_X`配原source，不是当前Q_X；两个下界不能相除给ratio。589 headline的fixed-source mean-rank1同样属于原ρ_X，不覆盖先乘1/|d_X|²再校准的规则。

必须扣除更强的paid real-axis资产：C052上游原审§3的Hardy／反射／strip证明给全部weighted-unit h以`|h(t)|≤C(1+|t|)||h||_X`，故

\[
 Q_X(t)\le C(1+t^2)\qquad(t\in\mathbb R),             \tag{4a}
\]

C独立X。这不是只依X的m_X^−2粗费。另一个已付接口，对每first-fixed B及|t|≤ℓ^B，给

\[
 Q_X(t)\le\exp[(-4+o(1))A],\quad
 A=\sqrt X/\ell,\quad\ell=\log X.                  \tag{4}
\]

这可直接消费，而不读未消费的反向6.9／sharp段。(4a)与(4)联合确实控制当前**bare**测度的全线：对S中的任一有界集，(4a)使一个先fixed大T以外的测试尾统一小，(4)使|t|≤T的贡献趋0。因此

\[
 \nu_X^0\longrightarrow0\ \text{于strong }S',\quad
 a_X\to0,\quad\mathcal T_X[g']\to0,\quad\beta_X\to\infty.
                                                               \tag{4b}
\]

这一最强裸旧后果不能漏记，也不需再假设bare D′收敛。但(3)是以未知速率的a_X作除法；两个趋0量不能相除定(R)。**bare tails已控，β-relative尾／π_X的相对shape尚未控**；不能把(4b)无声运输成校准后仍0，或再次写成裸全尾未知。

另一个域区别也保留：fixed-X的原source inverse为`B_X^−1g=Σ_(n为F_X-smooth)n^−1/2 τ_logn g`，是合法nonlocal L¹／Schwartz预处理。对非空F_X及g>0，Tonelli却给`μ_+(B_X^−1g)=μ_+(g)Σ_n1=∞`。所以不能把完整双pole Q身份直接套到该filtered source并称所有项已合法抵消。新ν规则是在**原compact g／g′**上作positive谱配对，仍合法；它不需要filtered source先落完整Weil的该强域。

## 5. PNT与必要gain：必须保β，当前并不矛盾

原Gram有精确比较

\[
 m_X^2I\le G_X\le(M_X^+)^2I,
\quad (M_X^+)^{-2}I\le G_X^{-1}\le m_X^{-2}I.
\]

令`T_arch[g]=∫|ghat|²||k_t||² dt/(2π)>0`为fixed arch Sonin正迹，便得

\[
 \frac{T_{arch}[g]}{(M_X^+)^2}\le a_X
       \le\frac{T_{arch}[g]}{m_X^2},
\quad
 \frac{q_0m_X^2}{T_{arch}[g]}\le\beta_X
       \le\frac{q_0(M_X^+)^2}{T_{arch}[g]}.            \tag{5}
\]

这也支付a_X strict positivity。标准PNT给

\[
 \log m_X=-(2+o(1))A,\qquad
 \log M_X^+=(2+o(1))A;
\]

高次展开只多O(loglogX)或更小项，不作零自由区优化。原unscaled inverse权的global最大精确为`m_X^−2`（t=0取到），即`exp[(4+o(1))A]`。**全局最大不证明fixed-away band已有所需增益，更不能单独判不可达；实际权还要乘β_X。** (5)只把logβ夹在±(4+o)A之间。

假如(3)真趋完整Wζ于D′，已付positive-D′谱vague必要桥与q₁>0给某个fixed away0 χ≥0，其谱质量最终≥m>0。将(4)作用于该fixed support，有

\[
 m\le\beta_X\int\chi(t)Q_X(t)\frac{dt}{2\pi}
       \le C_\chi\beta_X e^{(-4+o(1))A}.
\]

于是`liminf logβ_X/A≥4`；再用(5)，得到这份full-D′假设下的必要条件

\[
 \log\beta_X/A\longrightarrow4.                    \tag{6}
\]

它与已知upper的leading指数**兼容**，不是矛盾、同scale可达或sharp结论。若另行证明β在一个cofinal子列的指数严格小于4，则这条已付必要门足以拒绝full逼近；本稿没有执行那项新估计。(6)也使原source滤波乘子`√β_X/d_X`的global L² operatornorm在该假设下为`exp[(4+o(1))A]`，但大费用本身不构成失败证明。

## 6. 三句准入、停止与版本

**Input：** finite inverse-Euler common positive filter已由(1)–(3)实际定义，保完整Gram；它不是某个未知target谱除以ρ的后验选择，亦没有新增独立算术／primitive来源。

**Test：** 唯一未付首检为(R)，或用已经证明的(6)必要条件作便宜排重；当前旧bounds没有给(R)的极限或非消失缺陷。不得把取消显式D当取消Gram，不得忽略β或未控全尾。这里停止准入审，不另开proof、数字试算、参数／source或590。

**Net：** 若(R)失败，只止这份确定的inverse-Euler＋g校准规则；若通过，仅保留一个full coverage尚未付的非poly／nonlocal候选。其positive D′层不必逐层消405 Pan，固定degree坍缩、finite-mass atom门和CCM source-through-image零均不能错套。未有whole4/5UPPER改善、Q负源、完整signed核心／primitive／principal／mixed／Ξ新后果，Goal门open。

实际主要绑定：560为9263 bytes／LF SHA `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3`；585为7857／`5dca916d978eef599587ff4c6ce34144f814ddec0567a4c1b2314dcd71cd01af`；589原localization审为11459／`809bc7ffc6f1fbf4dd24af0d710af05fb7ca1bc259992430c3fd6760912ffcb1`。必要monotonic／kernel scope只在这些项目旧原件及相应full-inverse／fixed-test记录中核，未读新PDF／来源。当前直接定义及PNT／gain比较属标准旧消费，但**没有**把尚未判定的(R)标成旧0失败或新已证结果。cadence3/history53/latest589/formal17保持，本稿不代root消费／结算。
