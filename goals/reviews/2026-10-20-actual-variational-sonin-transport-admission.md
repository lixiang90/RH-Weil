# 实际变分来源门：完整缺陷的高频运输与停止范围

2026-10-20。执行[修订路线图§4](2026-10-20-generalized-weil-facilities-roadmap-after-572.md)唯一来源门，
不续572的参数预算。同G20261014／0c4f≤538冻结基线；未创建runtime Goal。
这是旧资产的具体候选消费与直接推论核查，0新增数学迭代，不是573，不建C036。

## 1. 结论和准入决定

实际候选P_M S_Tw_R的原域与clipping费用可以闭合。
完整D_var并非在所有成长高度都未知：在一个固定安全高频层

\[
 F_L=\{p<e^{2L}\},\qquad A_L=\exp(16e^L),\qquad |R|\ge A_L,
 \qquad T_R=\Gamma(R),
\]

完整window平方缺陷、actual平方缺陷和实际密度运输均可一致支付，最终有某c>0使

\[
 \boxed{\sup_{|R|\ge A_L}|\epsilon_{F_L}(R)|
       \le \exp(-c e^L/L)\longrightarrow0.}                 \tag{1}
\]

ε是560实际Sonin全密度的完整误差，不是模型δwin；全部Γ、proper powers和双pole保持原定义。
这个安全层甚至无需572的receiver均值：560完整残差＋coercive界和旧ALL区间clipping已足。
572的实际b权费提供另一条较锋利的均值上界，但不能被当成本高层推论的必要新输入。

因此本门的结果不是“只给旧推论加一个完全未知D_var”，也不是独立容量突破。
可消费的是明确的cofinal高频尾和原源高频误差部件；
572整个θ>2e范围的完整运输、低频／危险核心和全源正性仍未支付。
**保存这项旧资产直接合成后停止该入口，不优化16、不续θ/c/β或缺陷参数，不建新数学合同。**

最强旧542＋555→557 whole负惯性上预算leading4/5未改，Goal完成门仍open。
数值16只是一次安全证书，不是必要阈值、实际误差下界或方法类障碍。

## 2. 原对象、完整逆与准确变分方向

H=L²(R,dy)，B=∏_(p∈F)(I−p⁻¹/²U_logp)，D=B⁻¹，W=B*B，Z=DD*=D*D。
令m=∏(1−p⁻¹/²)、M=∏(1+p⁻¹/²)，m²I≤W≤M²I。
P_M为真实实位cutoff1 Sonin投影；实际空间记为\(\mathcal M\)，避免与上界M混淆。
G_M=P_MWP_M在该空间上的限制、G_T=P_TWP_T在P_TH上的限制，是两个不同的完整压缩Gram。

\[
 P_T=1_{(0,T)},\quad L_-=1_{(-\infty,0)},\quad H_+=1_{(T,\infty)},
 \quad T=\Gamma(R)=\Re\psi(1/4+iR/2)-\log\pi>0,
\]
\[
 w_R=e^{iRy}1_{(0,T)}/\sqrt{2\pi},\quad v_T=\|w_R\|=\sqrt{T/(2\pi)},
 \quad S_T=P_T(Z-DL_-D^*-D^*H_+D)P_T,
\]
\[
 z=S_Tw_R\in P_TH,\qquad y=P_Mz\in\mathcal M.
\]

所有算子在对应Hilbert空间上有界，G_M和G_T均严格正可逆，故y属于实际完整变分域。
没有把y当原Weil源r，也没有对整线plane wave施P_M。
裸Mellin求值k_R∈\(\mathcal M\)、w_R、真实receiver和原du／zero-extension Dlog源的角色始终分开。

记q_M=〈k_R,G_M⁻¹k_R〉、q_T=〈w_R,G_T⁻¹w_R〉、s_T=〈w_R,S_Tw_R〉，
V_M(y)=2Re〈k_R,y〉−||By||²，V_T(z)=2Re〈w_R,z〉−||Bz||²。
定义两个**都必须保留**的完整平方：

\[
 D_T=D_{\rm var}=\|G_T^{-1/2}(G_TS_T-I)w_R\|^2=q_T-V_T(z),
\]
\[
 D_M=\|G_M^{-1/2}(G_My-k_R)\|^2=q_M-V_M(y).
\]

令e_clip=V_M(y)−V_T(z)、δwin=q_T−s_T，则精确有

\[
 \boxed{q_M=q_T-D_T+e_{\rm clip}+D_M
             =s_T+\delta_{\rm win}-D_T+e_{\rm clip}+D_M.}    \tag{2}
\]

只用变分不等式丢D_M，得到的是actual密度下界，不是所需误差上界。
只有两个平方都付费后，才可取绝对值作双向运输；572的δ正部不能替代D_T或D_M。

## 3. 完整区间展开和clipping费用

旧532／560输入是ALL有限区间J、位置／长度任意：

\[
 u_J=e^{iRy}1_J/\sqrt{2\pi},\quad e_R=C_*R^{-1/4},\qquad
 \|(P_M-P_T)u_J\|\le e_R,\quad\|k_R-w_R\|\le e_R.           \tag{3}
\]

常数独立F/J。完整D和D*级数的系数绝对和均为m⁻¹。
每对delay a=log n、b=log n'，三项bulk−left−right先合并，公共phase为e^(−iR(a−b))。
若a+b<T，剩+u_(a,T−b)；若a+b>T，剩一个负区间carrier；等号为零。
负区间为(0,T)∩(a−b,T+a−b)∩(T−b,a)。

因此z的完整signed区间表示总绝对质量≤m⁻²，而非逐三项的粗3m⁻²。
所有区间长≤T，级数在H中绝对收敛，全部尾和有界算子交换合法；
Bz、Wz的全字母质量分别≤Mm⁻²、M²m⁻²。
由(3)得到

\[
 \|z\|\le v_Tm^{-2},\quad\|y-z\|\le e_Rm^{-2},
 \quad\|B(y-z)\|\le Me_Rm^{-2},
\]
\[
 |e_{\rm clip}|\le E_{\rm clip}
 =2e_Rv_Tm^{-2}+2M^2e_Rv_Tm^{-4}+M^2e_R^2m^{-4}.             \tag{4}
\]

实际权始终是|b_F(R)|²，m≤|b_F(R)|≤M，没有除b或改成m²归一。
在572同步窗，(4)乘实际b权一致o(1)；这里只需要任意固定正θ，
因为e_R的log负费为−θe^L/4，所有condition prefactor的log只有O(e^L/L)。
这是旧clipping在指定候选上的直接推论，尚不等于完整实际误差已付。

令r_T=G_Tz−w_R、r_M=G_My−k_R，把它们都置于原ambient H中，精确地

\[
 r_M-r_T=(P_M-P_T)Wz+P_MW(y-z)-(k_R-w_R),
\]
\[
 h_R:=\|r_M-r_T\|\le e_R(1+2M^2/m^2),\qquad
 D_M\le m^{-2}(M\sqrt{D_T}+h_R)^2.                         \tag{5}
\]

此处未交换P_M与B，未混同两个inverse。
由(2)、(4)、(5)，actual–window密度的充分费用为

\[
 |b_F|^2|q_M-q_T|\le |b_F|^2E_{\rm clip}
 +(1+2M^2/m^2)|b_F|^2D_T+2|b_F|^2m^{-2}h_R^2.              \tag{6}
\]

## 4. 完整D_var与真实receiver的关系

v=L_-D*P_Tw_R、u=H_+DP_Tw_R，令q=H_+Dv+L_-D*u。
560的两项完整残差给r_T=P_TWq，两外半线正交，所有returns仍在完整inverse中。
正交投影Π_(BP_TH)=BP_TG_T⁻¹P_TB*给精确身份

\[
 \boxed{D_T=\|\Pi_{BP_TH}Bq\|^2
       \le M^2\tau_F(T)^2(\|v\|^2+\|u\|^2),}\qquad
 \tau_F(T)=\sum_{\log n>T,\,n\in N_F}n^{-1/2}.              \tag{7}
\]

投影的范数1来自同一个完整Gram恒等式，不是假定未知gap。
572实际b权receiver均值确能经(7)进入D_T，再经(5)进入D_M；
但τ及M²/m²必须同时付，不能仅拿O(L⁴)宣布平方已小。
该证书并没有在572的整个θ>2e范围闭合，也不提供该范围的actual lower反例。

两边界的signed身份仍是571完整J⁻¹。
若分别clean V=bar b v、U=b u，必须同步K→(bar b/b)K及J→J_b，
不能独立改相位后读取旧cross。式(7)保留两项后再取上界，没有删除任何边界或return。

## 5. 扣除更强旧残差：固定安全高频层的完整运输

为核是否真有未付平方，本门只取一个安全常数16，不优化阈值。
设E_L=e^L/L、γ=log4/(2L)，并令A_γ=∏_(p∈F_L)(1−p⁻¹/²⁺γ)⁻¹。
572已付moving-exponent PNT/Abel，直接给

\[
 \log M=(1+o(1))E_L,\quad\log m^{-1}=(1+o(1))E_L,
 \quad\log A_\gamma=(4+o(1))E_L.
\]

对T≥Γ(A_L)，τ≤A_γe^(−γT)，起点指数是−d₀E_L+o(E_L)，
d₀=8log4−4>7。
不用572均值，560旧**完整残差和coercive界**已经给

\[
 \|r_T\|\le2M^2m^{-1}\tau_F(T)v_T,\quad
 |b_F|^2D_T\le4M^6m^{-4}\tau_F(T)^2v_T^2.                 \tag{8}
\]

式(8)的最坏指数为(10−2d₀+o(1))E_L；(5)运输到实际D_M后为
(14−2d₀+o(1))E_L<0，clipping余项更小。
此处比较的是旧精确残差短链；只用较弱||S_T−G_T⁻¹||再套条件数，会多损费用，不能作为最强旧对照。
T e^(−2γT)、T e^(−γT)在起点以后递减，√T R⁻¹/⁴亦然。
故这些界对**全部**|R|≥A_L一致，不只是一个有限高度平均。
负频由原实结构运输，不丢复源方向。

由(6)得到sup高频|ρ_actual−ρ_window|→0。
若还要比较S_T，Cauchy–Schwarz与q_T≤m⁻²v_T²给
|b|²|δwin|≤2M⁴m⁻³τ v_T²，其指数7−d₀<0；两个完整平方和signed差都已支付。

最后不能漏window到完整Γ／prime-power主项。
560既有误差上界C_(F,γ)(1+T)e^(−γT)中，
J_γ=A_γΣlogp p⁻¹/²⁺γ/(1−p⁻¹/²⁺γ)，满足logJ_γ=(4+o(1))E_L，logJ₀=(1+o(1))E_L。
保所有项后的C指数分别为7、7、10、11，整体至多(11+o(1))E_L。
起点γT=(8log4+o(1))E_L，且8log4>11。
因此完整model主项误差也一致o(1)，与actual–window运输合并得到(1)。

原完整身份为

\[
 2\pi\rho_F(R)=\Gamma(R)
 -2\sum_{p\in F,k\ge1}(\log p)p^{-k/2}\cos(kR\log p)
 +\epsilon_F(R).
\]

Γ只在估计中使用渐近，定义未改；有限Euler numerator不代完整−ζ′/ζ，所有proper powers保留。
本门从未添加pole矩消失条件，完整Weil型的双pole不能设零。

## 6. 原源范数：确实付了哪个部件

对原I=(-L,L)、r∈L²(I,du)，按零延拓取未归一Fourier transform rhat。
560的完整自伴紧误差是K_L=1_I F_unit* M_(ε_F) F_unit1_I。
将它按|R|≥A_L截成高频部件K_L^hi，由(1)可得

\[
 \|K_L^{\rm hi}\|_{L^2(I)\to L^2(I)}\le\eta_L\to0,\qquad
 \eta_L=\sup_{|R|\ge A_L}|\epsilon_{F_L}(R)|,
\]
\[
 \left|\frac1{2\pi}\int_{|R|\ge A_L}
 \epsilon_{F_L}(R)|\widehat r(R)|^2\,dR\right|
 \le\eta_L\|r\|_{du}^2.                                  \tag{9}
\]

这是ALL原复源的高频误差部件，原du范数真实支付；由此继承Dlog源的型连续性，
不另声称K_L^hi保持Dlog图域或给其上的同常数operator界。
Plancherel已把1/(2π)吸收，operator norm是≤η_L，不是≤η_L/(2π)。
**完整K_L还含|R|<A_L的低频部分**，并非每个compact r都可以丢掉它。
完整K_L的全源小费、完整Weil正性或危险核心结论均不能由(9)推出。

这里的A_L远高于旧555有利高频界的大小层，未覆盖θ≤1核心；
也未改最强旧whole4/5预算、补空间coupling或通常Ξ。
572短区间平均本身仍不能代ALL r的频谱积分；本门对原源部件能用的是经旧粗界恢复的uniform实际ε。

## 7. 停止、独立新输入与下一准入

本门已完成，停止继续优化安全高度、τ、m/M或单prime参数。
不是因为证明了D_var在所有成长尺度不可控，而是：
原域／clipping及安全高层缺陷已可由旧资产直接闭合；剩下的完整成长／核心责任没有新的独立输入。
不把较锋利的弱子界或新写出的旧合成登记为新容量、不新增数学轮、不建C036。

重新准入至少需要以下之一的**实际对象和可核费用**：

- 同一actual source层的新Γ-relative／source-adapted联合比较，支付低频、core和coupling，
  或严格削弱现有完整费用前件；仅一个模型δ或全H norm witness不够。
- 一份真实global section→局部评价的map，给kernel、乘法／消失过滤及独立height/collision/RR上界，
  再与完整Γ/pp/pole的all-complex预算比较。正metric、cocycle或按Q反定义容量不够。

新路线图中已定位的O(D)对象仍只是候选；没有新的map／独立估计就不自动执行另一章节来源门。
独立正能量＋完整同源热迹也是有条件备选，经典身份仍欠；不以unknown H/CM延长入口。
长期Goal不因本次停止而完成、暂停或blocked；runtime Goal本轮不存在，未创建新实例。

## 8. 原件与消费范围

[原域／clipping](../../reviews/2026-10-20/variational-admission/candidate-domain-and-clipping.md)、
[完整缺陷／receiver](../../reviews/2026-10-20/variational-admission/full-defect-and-receiver-control.md)、
[actual／原源方向](../../reviews/2026-10-20/variational-admission/actual-source-norm-and-sign-audit.md)
各写独占原证明；最终以fresh逆审与root前件收据为准。
旧输入主要是532 ALL区间clipping、560完整残差和全部模型费用、571双边界、572 moving-exponent账本。
本轮没有新外部文献检索或数值截断，全部inverse与尾均按原对象处理。
