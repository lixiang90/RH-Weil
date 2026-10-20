# 实际变分候选的原域、完整 interval 表示与 clipping 费用

2026-10-20。按572后路线图§4执行一次来源准入；本稿不建C036、不消费cadence、不改公共状态/Git。
对象是实际Sonin候选，不把合法clipping解释为完整actual误差已付。

已恢复README/STATE、check/show、G20261014／0c4f≤538冻结基线、C035、当前路线图§4及前沿。
核读532§§2–3、560的完整inverse/carrier原证明§§1–5和571§§1–3。
旧输入的来源、量词和费用属于原资产；以下只闭合本候选是否落入该输入。

## 1. 三种空间与全逆不变

在物理H=L²(R,dy)上，U_a f(y)=f(y−a)。F先为任意有限prime集，

\[
 B=\prod_{p\in F}(I-p^{-1/2}U_{\log p}),\quad D=B^{-1},\quad
 W=B^*B,\quad Z=DD^*=D^*D,
\]
\[
 m=\prod_{p\in F}(1-p^{-1/2}),\qquad
 M=\prod_{p\in F}(1+p^{-1/2}),\qquad m^2I\le W\le M^2I.
\]

P_M为实际实位cutoff1的Sonin正交投影，M_s=Ran P_M；下标s只为避免与上界M混淆。
G_M=(P_MWP_M)|M_s为有界正可逆算子，原域就是整个M_s，逆的定义域也是整个M_s。
实际裸Mellin求值k_R∈M_s不换成completed求值。

令P_T=1_(0,T)、L_-=1_(-∞,0)、H_+=1_(T,∞)，并保

\[
 T=T_R=\Gamma(R)=\Re\psi(1/4+iR/2)-\log\pi>0,\quad
 w_R=e^{iRy}1_{(0,T)}/\sqrt{2\pi},\quad v_T=\sqrt{T/(2\pi)}.
\]

window中的G_T=(P_TWP_T)|P_TH与实际G_M不同。取完整双边界

\[
 S_T=P_T(Z-DL_-D^*-D^*H_+D)P_T,\qquad
 z_T=S_Tw_R\in P_TH,\qquad y=P_Mz_T\in M_s.                 \tag{1}
\]

D、D*都保留完整因果逆/反因果逆；没有先截掉returns。z_T是window向量，y才是实际Sonin变分域中向量。
其合法性只使用H中的有界算子，未要求physical向量另在Weil源的du／zero-extension Dlog域中。
原Weil源r、裸求值k_R、physical候选y不因同记L²而合并。

532实际Γ相位与Sonin双clipping给唯一旧输入：存在F和区间J均无关的C_*、R_*，
对ALL有限区间J（位置、长度、端点任意）和R≥R_*，

\[
 u_J=e^{iRy}1_J/\sqrt{2\pi},\qquad \varepsilon_R=C_*R^{-1/4},
\]
\[
 \|(P_M-P_T)u_J\|\le\varepsilon_R,\qquad
 \|k_R-w_R\|\le\varepsilon_R.                              \tag{2}
\]

只用有限区间L² carrier；不对整线plane wave施P_M，不把有限Euler的周期相位重新塞进Γ相位定理。

## 2. 全部D/D*展开先合并为一个signed interval

记N_F为含1的F-smooth数，a=log n、b=log m'、c_n=n^-1/2。
为避免m'与下界m混淆，和式中的第二个数始终写m'。
绝对算子范数收敛的完整级数为

\[
 D=\sum_{n\in N_F}c_nU_{\log n},\quad
 D^*=\sum_{m'\in N_F}c_{m'}U_{-\log m'},\quad
 \sum_nc_n=m^{-1}.                                         \tag{3}
\]

对每对(a,b)，bulk、left、right三项有同一phase e^{-iR(a-b)}，区间分别是

\[
 J_0=(0,T)\cap(a-b,T+a-b),
\]
\[
 J_-=(0,T)\cap(a-b,a+\min(0,T-b)),
\]
\[
 J_+=(0,T)\cap(\max(T,a)-b,T+a-b).
\]

准确地，J_-=J_0∩(-∞,a)、J_+=J_0∩(T-b,∞)，a,b≥0。
所以不是给三个独立标签后取平方：

\[
 1_{J_0}-1_{J_-}-1_{J_+}
 =\begin{cases}
 1_{(a,T-b)},&a+b<T,\\
 -1_{J^-(a,b)},&a+b>T,\\
 0,&a+b=T,
 \end{cases}                                               \tag{4}
\]
\[
 J^-(a,b)=(\max(0,a-b,T-b),\ \min(T,T+a-b,a)),
\]
空区间计0。等号端点为零测度，不影响任何H身份。
当a+b<T时(a,T-b)本来就在J_0及(0,T)中；当a+b>T时仅两剪切重叠处留下负号。
这证明每对完整三项可cohere为至多一个signed interval。

定义σ_T(a,b)=+1、−1或0及J_T(a,b)为(4)对应区间，则

\[
 \boxed{z_T=\sum_{n,m'\in N_F}
 c_nc_{m'}e^{-iR(\log n-\log m')}\,
 \sigma_T(\log n,\log m')u_{J_T(\log n,\log m')}.}           \tag{5}
\]

这是区间carrier参数空间上的有限复杂signed原子测度表示，其绝对总变差≤m^-2；
若端点相同再合并，只会减小这个上界。粗逐三项的3m^-2无需使用。
每个区间长度≤T，故(5)在H中绝对Bochner收敛，并且

\[
 \sum_{n,m'}\|\text{对应H项}\|\le v_Tm^{-2},\qquad
 \|z_T\|\le v_Tm^{-2}.                                    \tag{6}
\]

全部无限尾以Σc_n<∞独立支付，允许有界P_M、P_T、B穿过级数；没有未知极限交换。
也可由0≤P_TDL_-D*P_T≤P_TZP_T及右项同界，得
−P_TZP_T≤S_T≤P_TZP_T，因而||S_T||≤m^-2，独立核对(6)。

## 3. Bz的全字母与原clipping费用

有限Euler多项式

\[
 B=\sum_{d\mid\operatorname{rad}(F)}\mu(d)d^{-1/2}U_{\log d},
 \qquad\sum_d d^{-1/2}=M.                                  \tag{7}
\]

逐字母施于(5)仍为有限长度、任意位置的carrier，完整绝对质量≤Mm^-2。
再施B*得到Wz时质量≤M²m^-2。coherent频率、区间碰撞保留；这里的线性绝对上界不把它们当独立正标签。
因此

\[
 \|(P_M-P_T)z_T\|\le\varepsilon_Rm^{-2},\qquad
 \|(P_M-P_T)Bz_T\|\le\varepsilon_RMm^{-2}.                  \tag{8}
\]

第二式只是独立的carrier corollary；实际变分运输不偷用P_MB=BP_M。
由于P_Tz_T=z_T，实际所需的是

\[
 h=y-z_T=(P_M-P_T)z_T,\quad
 \|h\|\le\varepsilon_Rm^{-2},\quad
 \|Bh\|\le M\varepsilon_Rm^{-2},\quad
 \|Bz_T\|\le Mv_Tm^{-2}.                                  \tag{9}
\]

这些是原dy范数；任何除|b_F|、换du、Dlog或全源积分费用均未在(9)中免费发生。

## 4. 实际变分值到window变分值的显式线性费用

令

\[
 V_M(y)=2\Re\langle k_R,y\rangle-\|By\|^2,\qquad
 V_T(z)=2\Re\langle w_R,z\rangle-\|Bz\|^2.
\]

由于k_R∈M_s，〈k_R,P_Mz〉=〈k_R,z〉。令e=k_R−w_R，正好有

\[
 V_M(y)-V_T(z_T)
 =2\Re\langle e,z_T\rangle
  -2\Re\langle Bz_T,Bh\rangle-\|Bh\|^2.
\]

由(2)、(6)、(9)，得到ALL有限F及ALL R≥R_*的完整可用上界

\[
 \boxed{|V_M(y)-V_T(z_T)|\le E_{\rm clip}(F,R)
 =\frac{2\varepsilon_Rv_T}{m^2}
  +\frac{2M^2\varepsilon_Rv_T}{m^4}
  +\frac{M^2\varepsilon_R^2}{m^4}.}                         \tag{10}
\]

实际b_F(R)=∏(1−p^-1/2e^{-iRlogp})无零且m≤|b_F|≤M。因此实际密度权的同对象费用是

\[
 |b_F(R)|^2E_{\rm clip}(F,R)\le M^2E_{\rm clip}(F,R).        \tag{11}
\]

没有改用m²权，没有除b。所有字母、完整D/D*尾、两边界同时在(10)里。
这比560 balanced-word逆运输的对象弱：只比较指定变分试向量，不比较完整G_M^-1与G_T^-1。
所以不能用(10)宣称旧cofinal完整逆运输已经解决。

## 5. 572同步高度中clipping确实可付，但不是新容量

取572的原F_L={p<e^(2L)}、固定θ>2e、2e/θ<β<1、
R_0=exp(θe^L)、I_L=[R_0,R_0+R_0^β]，始终T_R=Γ(R)。
PNT/Abel的旧资产给

\[
 \log M_L=(1+o(1))e^L/L,\qquad
 \log m_L^{-1}=(1+o(1))e^L/L,
\]

Γ(R)=log(R/(2π))+O(R^-2)只用于估计，于I_L一致有v_T=O_θ(e^{L/2})。
因而(10)–(11)最坏一项的log上界是

\[
 -\tfrac14\theta e^L+O(e^L/L)+O(L)\longrightarrow-\infty.
\]

故

\[
 \sup_{R\in I_L}|b_{F_L}(R)|^2E_{\rm clip}(F_L,R)=o(1).       \tag{12}
\]

实际这项clipping证书对任何固定θ>0及固定β∈(0,1)都成立；它无需572的θ>2e。
该扩大只涉及旧clipping的直接推论，不涉及receiver尾、D_var、actual误差或危险核心。
不改变参数优化止损，也不把原F_L依赖埋进O(1)。

## 6. 完整actual residual与两个平方缺陷

完整window变分平方缺陷仍是

\[
 D_{\rm var}(R)=\|G_T^{-1/2}(G_TS_T-I)w_R\|^2
 =\langle w_R,G_T^{-1}w_R\rangle-V_T(z_T)\ge0.               \tag{13}
\]

实际完整逆的正Gram变分身份首先给

\[
 \langle k_R,G_M^{-1}k_R\rangle\ge V_M(y)
 \ge\langle w_R,G_T^{-1}w_R\rangle-D_{\rm var}-E_{\rm clip}.
                                                                    \tag{14}
\]

单独乘实际|b|²后只是actual density下界，不能把它当作actual−model绝对upper。
从Q_W=t_F−K_ε+完整pole作lower比较时，也不能把ε下界自动当作所需上界。
所幸本候选还能不截逆地明确写出第二个平方。令

\[
 r_T=P_TWz_T-w_R=(G_TS_T-I)w_R,\qquad
 r_M=G_My-k_R,
\]
\[
 D_M=\|G_M^{-1/2}r_M\|^2
 =\|B(G_M^{-1}k_R-y)\|^2\ge0.
\]

将两者都看作原ambient H中的向量，精确地

\[
 r_M-r_T=(P_M-P_T)Wz_T+P_MW(y-z_T)-(k_R-w_R).
\]

Wz的完整carrier质量≤M²m^-2和(2)、(9)给

\[
 \|r_M-r_T\|\le\varepsilon_R C_F,\qquad C_F=1+2M^2/m^2,
\]
\[
 \boxed{D_M\le m^{-2}\bigl(M\sqrt{D_{\rm var}}+
                 \varepsilon_R C_F\bigr)^2.}               \tag{15}
\]

这里||r_T||≤M√D_var来自r_T=G_T^(1/2)(G_T^-1/2r_T)，没有将两个压缩Gram逆混同。
由两边完整变分恒等式，准确地

\[
 \langle k_R,G_M^{-1}k_R\rangle-
 \langle w_R,G_T^{-1}w_R\rangle
 =V_M(y)-V_T(z_T)+D_M-D_{\rm var}.
\]

故若另能支付D_var与(15)，便可得到双向actual−window比较；显式可用

\[
 |b_F|^2|a_M-a_T|
 \le |b_F|^2E_{\rm clip}
 +(1+2M^2/m^2)|b_F|^2D_{\rm var}
 +2|b_F|^2m^{-2}\varepsilon_R^2C_F^2.                      \tag{16}
\]

这是原dy域中正确权的充分费用，尚不是原Weil源积分及其du/Dlog费用。

571的δ_window是两个完整Gram之差；572支付其b权正部及receiver原范数平均，
不推出(13)的平方。(15)明确第二平方可由第一平方和clipping控制，不能把两者删去。
若完整D_var仍无新或已付费用，路线图来源门就应停；若另一份完整cross-tail核查
在某固定很高有利层支付它，则应把该层真实direct corollary保存，再扣旧560的operatorS尾强推论。
不得预设D_var永远未知，也不能以更弱receiver子费改善声称whole/core新后果。
本稿至此给旧ALL-J clipping在指定实际候选上的直接corollary，不据此新计数学轮。

完整Γ/contact从未换定义，finite Euler μ不替代−ζ'/ζ的全部素数幂；
完整双pole从未设零，也无额外pole矩消失源条件。现有fixedF fullsource身份可继承，
cofinal all-complex source运输、源du/Dlog范数以及危险核心责任均未由本候选clipping闭合。
没有新独立RR容量、Weil正性或whole4/5后果。本稿无数值、下载或后台过程。

## 7. 消费所用原件

- `notes/532-actual-sonin-prime-symbol-and-compact-weil-bridge.md` §§2–3：actualΓ及ALL-J旧输入、裸求值原域。
- `reviews/2026-10-14/joint-sonin-cross/full-inverse-carrier-error.md` §§1–5：同物理域、旧clipping量词及fixed/cofinal常数区别。
- `notes/571-actual-receiver-two-boundary-signed-comparison-and-growth.md` §§1–3：完整S_T、G_T和两boundary角色。
- `goals/reviews/2026-10-20-generalized-weil-facilities-roadmap-after-572.md` §4：本次明确准入与停止条件。

以上原件的来源费用归原结算。本稿独立出稿须待root对D_var和actual源方向合并审核后消费。
