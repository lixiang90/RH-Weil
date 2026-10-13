# 真实晚素数 Sonin 增量：固定源正平方与统一渐近的紧性边界

2026-10-14；C006第一完整迭代，比较基线仍为
`3a72930e9f9f554b03b41d17d8c8002f1813ca82`，起始HEAD `7b6652d`。
状态：proved，范围为固定光滑源的single-p增量，以及冻结源域的统一渐近障碍。
[独立直接推导](../reviews/2026-10-14/c006-late-prime/direct-increment-audit.md)、
[真实端点来源审查](../reviews/2026-10-14/c006-late-prime/source-increment-audit.md)与
[不同组织逆审](../reviews/2026-10-14/c006-late-prime/reverse-audit.md)保留推导及纠错。
不提供完整Weil正性、实际最低态或成长S预算，也不声称世界优先权或外部评议。

## 1. 对象、量词及净结论

实际物理空间H=L²((0,∞),dx)，F的核为2cos(2πxy)，P是真实实位Sonin
cutoff1正交投影。沿[531](531-semilocal-sonin-positive-trace-and-non-hilbert-schmidt-cutoff.md)
及[532](532-actual-sonin-prime-symbol-and-compact-weil-bridge.md)，对实际素数p置

\[
 a=\log p,\ q=p^{-1/2},\ B=I-qU_a,\ C_a=P(U_a+U_{-a})P,
 \quad G=(1+q^2)I-qC_a,\quad P_p=BP G^{-1}PB^*.
\]

其中U_a f(x)=p^(-1/2)f(x/p)，G作用于RanP。
源A_g=∫g(t)U_tdt，正迹T_p(g)=Tr(A_gP_pA_g*)。
原CCM的有限S真实空间及原实位正迹是既有输入，不重复计新。
这里保留全部实际正交化Gram逆，而不是projection product。

冻结源仍是C004的 `b=log(3/2)/4,a₀=log2,μ=13/5`：
g(t)=u(t+a₀/2)+v(t−a₀/2)，u,v∈Cc∞(−b,b)，
每patch满足ℓ₀=ℓ₁/₂=0。记两patch并集为U，合法光滑源的L²闭包为V。
V为L²(U)的有限余维无限维子空间。源相关跨度a₀+2b=log√6<log3，
所以每个p≥3的全部actual primepower项严格0；pole准入亦保持。

令k_s∈RanP为裸unitary Mellin求值的Riesz向量，
κ_s=k_s(1+)，β_s=(Fk_s)(1+)=γ_s\overline{κ_s}，
γ_s=m(−s)，m(s)=π^(is)Γ(1/4−is/2)/Γ(1/4+is/2)。
使用ĝ(s)=∫g(t)e^(−ist)dt，不附unitary因子。

**固定源定理。** 对每个固定g∈Cc∞(U)，特别是每个合法冻结源，实际素数p→∞时

\[
 T_p(g)-T_\infty(g)=p^{-2}\mathcal A(g)+O_g(p^{-5/2}),
 \qquad
 \mathcal A(g)=\frac1{2\pi^2}\int_{\mathbb R}|\widehat g(s)|^2
                   |\kappa_s-\gamma_s\overline{\kappa_s}|^2ds. \tag{1}
\]

首项是有界正源L²型；对每个固定有界U，存在0<c_U≤C_U<∞，使
c_U||g||²≤A(g)≤C_U||g||²。故每个固定非零光滑g最终有严格正增量，
且∑_(p≥3)|T_p(g)−T∞(g)|<∞。这是分别从arch base添加single-p的求和，
不是沿成长S的telescopic增量。

**统一渐近边界。** 令D_p为冻结V上差额T_p−T∞的有界延拓。
每个D_p紧，而A_V=π^(-2)I_V+compact。因此对每个p≥3，

\[
 \|p^2D_p-\mathcal A_V\|\ \ge\ \pi^{-2}. \tag{2}
\]

所以(1)的余项不可能在整个冻结L²单位球上统一o(p^(-2))。
这不排除||D_p||≤Cp^(-2)，或其他∑_p||D_p||<∞的真实预算。
不把固定源的eventual positivity升为统一正算子结论。

## 2. 裸求值的实际端点域

记L为(0,1)投影，H=I−L，K=LFL，R=(I−K²)^(-1)。实位K紧且norm<1，

\[
 P=H-HFLRLFH. \tag{3}
\]

R−I=KRK有光滑cosine-even核J：J(t,u)=〈K(t,·),RK(u,·)〉。
固定R的有界性与cosine rows的各阶导数给J的全部有限阶核界，
不依赖prolate系数换和。

不能对不属于L²的全域Mellin power直接应用P。
先置e_s(x)=x^(-1/2+is)/√(2π)，在distribution意义Fe_s=γ_s e_(-s)，
再取低forcing r_s=LFHe_s=γ_s Le_(-s)−LFLe_s∈L¹，L¹范数统一于实s。
K²r_s光滑并属于L²，故v_s=r_s+RK²r_s合法，且
k_s=H[e_s−FLv_s]。此表达也与532的截断L²求值极限相符。

homogeneous Fourier恒等式消去power尾；smooth低核在0的odd derivatives为0，
剩余来自x=1。外部cosine积分至少三阶分部积分给

\[
 k_s(x)=-\frac{\beta_s\sin(2\pi x)}{\pi x}
         -\frac{(Fk_s)'(1+)\cos(2\pi x)}{2\pi^2x^2}
         +O_s(x^{-3}). \tag{4}
\]

直接稿曾把第二项写成正号，逆审已纠正；首项及(1)不受影响。
每个所需有限阶尾及导数误差常数随s至多多项式增长。
κ_s、β_s在实轴连续有界；weighted Mellin积分对smooth低核一次分部积分还给
κ_s=1/√(2π)+O(1/|s|)，β_s=γ_s/√(2π)+O(1/|s|)。
这是实际求值端点，不是一般Sonin L²向量的点值定理。

## 3. 实际整数p、两branch及完整Gram逆

令M_j(s)=〈k_s,C_a^jk_s〉，ρ∞=||k_s||²。实际整数p满足cos(2πp)=1。
将(4)代入〈k_s,U_a k_s〉，变x=py并在y=1分部积分，得到

\[
 M_1=-\frac{p^{-3/2}}{\pi^2}\Re(\beta_s\overline{\kappa_s})
             +O_s(p^{-5/2}). \tag{5}
\]

第二cos项另付一次非驻相，第三阶尾绝对可积；仅O_s(x^(-2))尾不足以识别此系数。
任意实p的端点会留cos(2πp)，不能偷换实际素数位置。

再令t=HU_(-a)k_s、t_F=HU_(-a)Fk_s。两者尾norm²分别为
|β_s|²/(2π²p)+O_s(p^(-2))和|κ_s|²/(2π²p)+O_s(p^(-2))。
低Fourier泄漏为O_s(p^(-3/2))，因频率p±y在0<y<1不驻相；(3)支付实际投影误差。
Fk_s=γ_s\bar k_s及FU_a=U_(-a)F给两个return branch。
将branch cross按x≤p/2与x>p/2分开：前区Fourier振荡抑制，后区直接尾L²界，
cross=O_s(p^(-3/2))，没有假定正交。因此

\[
 M_2=\|C_ak_s\|^2=\frac{|\kappa_s|^2}{\pi^2p}+O_s(p^{-3/2}). \tag{6}
\]

设r=q/(1+q²)。实际密度精确为
ρ_p=(1−2r cos(as))∑_(j≥0)r^jM_j。
分子与Gram逆的1+q²把裸q²ρ∞质量**精确消去**。
对j≥2，|M_j|≤2^(j−2)M₂，且p≥3保证2r<1有统一gap。
故全部j≥3尾以及分子cross均已付，得到

\[
 \rho_p-\rho_\infty=-2r\cos(as)\rho_\infty
       +\frac{p^{-2}}{\pi^2}\bigl(|\kappa_s|^2-
                    \Re(\beta_s\overline{\kappa_s})\bigr)
       +O_s(p^{-5/2}). \tag{7}
\]

第一项pointwise仍是O(q)，不能删除；必须对同一个实际源配对。

## 4. 同源大移位项的真实抵消及余项费用

实际外部核为P(x,y)=δ(x−y)−(FLRLF)(x,y)，x,y≥1。
R=I+J中的bare FLF沿scaling-diagonal给
sin(2π(ρ−1)x)/(π(ρ−1)x)+sin(2π(ρ+1)x)/(π(ρ+1)x)。
此式与primary Connes–Consani作者版printed page4 Eq(10)一致：

\[
 \delta(\rho)=\frac{\sqrt\rho}{\pi}
 \left[\frac{\operatorname{Si}(2\pi(\rho+1))}{\rho+1}
       +\frac{\operatorname{Si}(2\pi(\rho-1))}{\rho-1}\right].
\]

把Si替成π/2产生ρ^(-1/2)/(1−ρ^(-2))，恰抵消actual Gamma的相反off核。
这里Gamma仍按2θ′；不是只抵消一个1/p项，而是整个非振荡代数核。
原件版本及字节见C004 receipt，本文重新目检了该页公式。

J光滑且cosine-even，沿第一个低坐标反复积分只留endpoint1振荡；
endpoint0的odd derivatives为0。对ρ=pe^v，**先**用固定光滑自相关R_g(v)配对，
每个phase在x≥1有|∂_v phase|≥c_U px。反复非驻相并保留深阶核余项，
使x积分绝对可控，得到对任意固定N

\[
 \int|\widehat g(s)|^2\cos(s\log p)\rho_\infty(s)ds
       =O_{g,N}(p^{-N}). \tag{8}
\]

全过程取合法source夹心TC trace的分布；不对未夹源的U_ρP取独立发散迹。
(7)的s误差常数至多多项式，ĝ Schwartz可积分；联合(8)即(1)。
具体余项受Cp^(-5/2)∫(1+|s|)^M|ĝ(s)|²ds及
C_Np^(-N)R_g的有限光滑seminorm控制。固定支持的足够高Sobolev有界集上可统一，
整个L²单位球上没有这些导数费用。未利用ζ零点位置或数值拟合。

## 5. 首项的源L²强制后果和不交换的极限

κ−β在实轴real analytic（低forcing在|Im s|<1/2的L¹域解析），且非恒零：
κ趋于非零实常数，γ的Gamma相位持续旋转。其零集测度零，故A在非零L²源上严格正。
单位Fourier规范下A的乘子为

\[
 \ell(s)=\pi^{-1}|\kappa_s-\beta_s|^2
         =\pi^{-2}(1-\Re\gamma_s)+O(1/|s|).
\]

γ的inverse Fourier是smooth log-cosine核（反演选择只交换t与−t），
在固定有界U−U上有界，故压缩Reγ为HS；C₀误差压缩紧。
于是A_U=π^(-2)I+compact。正性、无kernel及Fredholm谱定理给c_U>0；
该常数不以unknown最低谱定义一个新正来源。对V限制亦成立。

532已经给每个固定p的Δ_p为negative actual prime型加源紧型。
冻结域p≥3的prime型为0，故D_p紧；这是差额的有界L²延拓，
不是宣称两个独立positive traces都在任意L²源上有限。
取V内norm1的光滑弱零carrier（每patch用D(D+1/2)η保持两矩零），
则对固定p有D_p(g_R)→0而A(g_R)→π^(-2)。这证明(2)，也可选联合R(p)见证。
固定g先p→∞与固定p先carrier→∞确实不交换。

严格停止统一o(p^(-2))算子渐近/统一首项正下界的尝试；
允许逃逸是有界但不norm收敛的p²D_p、统一绝对上界、带Sobolev费用的源族，
或新的base-S有符号输入。不能用(2)反推∑||D_p||发散。

## 6. 宏观影响、未付前件与唯一下一动作

新增独立输入是实际晚整数prime端点与正交化return的联合平方，
在真实非空源域给p^(-2)正增量及固定源可求和后果。
比532固定p紧性更强，也识别了便宜q²质量项精确相消。
同轮消费既有compact桥得到统一渐近边界，不另计研究轮。

改变的是成长费用的局部准入：fixed smooth single-p已付，whole源L²预算仍未付。
低域完整overlap符号、base S={∞,2}/一般finiteS cross、成长U、真正lowest/prolate均开放；
没有实际ζ谱带/零点限制，整个Goal未达到完成门槛。比例/无零区域及已降级路线保持。

唯一下一动作是C006最后一轮：在原冻结V上直接审实际D_p的
**可求和源L²上界**，检验||D_p||≤Cp^(-2)或较弱∑_p||D_p||<∞，
保留joint carrier/p范围。优先便宜联合carrier反例；不再追已不可能的norm渐近，
不在single-p预算未付前自动运输base-S。若只有generic relativeΓ或旧unknown条件，
合同止损，保存实际未付输入与重新准入条件。
