# 实际变分候选：完整逆缺陷、符号方向与原源范数审计

2026-10-20。本稿为路线图§4的一次来源准入的独立分工；只写本文件。
恢复README/STATE、check/show、同G20261014与冻结0c4f基线、C035/最新决策与宏观前沿后，
核读新路线图§4、560主稿、560的full-inverse-carrier-error §§1–5、571 §§1–2及6、572全文。
不建立C036、不修改STATE/cadence、不计新数学轮、不进行外网检索。

**结论：候选确在实际Sonin原域内；其clipping费可由旧ALL区间carrier输入直接付到cofinal高频。
完整变分身份有两个分别非负的逆缺陷，572的δ正部上界本身不能支付它们。
但保留完整cross-tail后，在固定安全高度θ=16可将两缺陷、actual−window及actual−S的绝对高度均费付清。
更强旧560完整残差／算术尾已足以得到整个|R|≥exp(16e^L)的逐点一致o(1)，572在此甚至非必要。
这只能支付原源的高频Fourier分量，不能报为新独立容量或全源／核心突破。**

## 1. 对象、两个压缩与真实域

H=L²(R,dy)，B=B_F，D=B⁻¹，W=B*B；m=∏(1−p⁻¹/²)>0、M₊=∏(1+p⁻¹/²)，
m²I≤W≤M₊²I。下文以M₊表上界常数，避免与Sonin空间M混名。
P=P_M是实际Sonin正交投影、M=RanP；H_T=1_(0,T)，T始终是完整Γ(R)>0，
w=e^(iRy)1_(0,T)/√(2π)，k=k_R∈M是实际裸求值，二者不相同。

G_M=(PWP)|M、G_T=(H_TWH_T)|H_TH皆为有界、严格正且可逆的压缩；
二者的逆只在各自range上使用。保留560/571的完整双边界

    S_T=H_T(DD*−D L_-D*−D*H_+D)H_T，
    z=S_Tw∈H_TH，y=Pz∈M。

所有项均在原H中有定义；D、D*、P、H_T、B有界，故无额外unbounded-form域责任。
特别是y不需要属于H_TH，z也不需要属于M；不能把y=z或G_M=G_T代入。
这只是物理dy候选的合法性，不等于原Weil源r已进入该映射的像。

## 2. 完整变分账本：上下界方向不可交换

令

    q_M=<k,G_M⁻¹k>，q_T=<w,G_T⁻¹w>，s_T=<w,S_Tw>，
    V_M(y)=2Re<k,y>−||By||²，V_T(z)=2Re<w,z>−||Bz||²。

两个严格正Gram给精确身份

    D_M=||B(G_M⁻¹k−y)||²=q_M−V_M(y)≥0，                 (1)
    D_var=||G_T⁻¹/²(G_TS_T−I)w||²=q_T−V_T(z)≥0。        (2)

S_T自伴，δ_win=q_T−s_T。定义E_clip=V_M(y)−V_T(z)，则没有截逆、删returns或改单边界的
**精确等式**是

    q_M=q_T−D_var+E_clip+D_M
       =s_T+δ_win−D_var+E_clip+D_M。                     (3)

变分原理仅直接给

    q_M≥q_T−D_var+E_clip
       =s_T+δ_win−D_var+E_clip。                        (4)

候选的V_M是actual q_M的下界。不能在(3)中丢掉正D_M后声称actual q_M上界，
也不能丢掉负D_var后声称(4)的有利下界。
δ_win可取两号，572只付|b|²(δ_win)₊；因此它既不是D_var的控制，也不是δ_win负部的控制。

同一身份可整体乘实际|b(R)|²，等价于同时把k,y,w,z乘共同scalar bar b(R)。
这不除b、不改norm；若分别clean左右receiver，仍必须使用572的
J_b=[[I,(bar b/b)K],[(b/bar b)K*,I]]及其完整逆。变分identity不消除这项协同责任。

## 3. 旧clipping付什么，尚留下什么

设e=C_*R⁻¹/⁴、h_T=√(T/(2π))，沿560旧输入

    ||k−w||≤e，||(P−H_T)u_J||≤e

对ALL有限区间J成立，常数独立J/F。完整D/D*展开的每一项仍为interval-carrier；
三项先cohere时，每对log n=a、log m'=b的bulk−left−right恰为一个signed interval：
a+b<T给+(a,T−b)，a+b>T仅给两剪切重叠的负区间，等号为零。因此总绝对系数质量
至多A=m⁻²，W的translation字母质量为M₊²。原展开和区间核在
[域/clipping独稿](candidate-domain-and-clipping.md)§2已逐项核对。
所以，已先在H中绝对收敛再用有界投影，

    ||z||≤A h_T，a:=||y−z||≤A e，
    ||(P−H_T)Wz||≤M₊²A e。                              (5)

不需要发散的word级数求和，也没有用全域plane wave来套P。
由于Pk=k且H_Tz=z，准确的clipping变分差为

    E_clip=2Re<k−w,z>−2Re<Bz,B(y−z)>−||B(y−z)||²。          (6)

故合法绝对费用是

    |E_clip|≤2e||z||+2M₊²||z||a+M₊²a²
       ≤2m⁻²h_Te+2M₊²m⁻⁴h_Te+M₊²m⁻⁴e²。               (7)

乘实际|b|²≤M₊²后仍保全部condition常数。对572的F_L与R∈I_L，
log(M₊⁴m⁻⁴)=(8+o(1))e^L/L，而e≤C exp(−θe^L/4)，T~θe^L。
因此加权clipping费逐R一致趋零；事实上这个旧输入的直接推论对每个固定θ>0均可付清。
这不是新的独立实位来源，也没有证明actual完整逆cofinal接近window完整逆。

令两个完整残差

    r_T=w−G_Tz∈H_TH，r_M=k−G_My∈M。

把二者放回同一ambient H，得到精确而非渐近的式子

    r_M−r_T=(k−w)−(P−H_T)Wz+P W(H_T−P)z。                 (8)

故||r_M−r_T||≤h:=e(1+2M₊²m⁻²)。这里没有把r_T当作M的向量。
再用各自完整inverse，

    D_M=||G_M⁻¹/²r_M||²
       ≤m⁻²(M₊√D_var+h)²，                              (9)

且D_M≥M₊⁻²(m√D_var−h)₊²。特别地，可给actual upper的粗式仍为

    q_M−q_T≤|E_clip|+(M₊²/m²−1)D_var
                  +2M₊m⁻²h√D_var+m⁻²h²。               (10)

(8)付残差的clipping差，(9)–(10)仍须支付r_T/D_var。
即使忽略趋零clipping差，也不能未经证明令D_M=D_var；这等于把两个不同空间的完整逆当成同一个。

## 4. 完整cross-tail可以在固定安全高层支付两平方

560保两边界的完整残差为

    (G_TS_T−I)w=H_T W H_+D L_-D*w
                    +H_T W L_-D*H_+Dw。                  (11)

写v=L_-D*w，u=H_+Dw，V=bar b v、U=b u；真实carrier的反射给||U||=||V||。
不截D、不丢任一边界，仅用||D||=m⁻¹及||W||≤M₊²可得

    |b|²D_var≤m⁻²|b|²||(G_TS_T−I)w||²
       ≤2M₊⁴m⁻⁴(||V||²+||U||²)
       =4M₊⁴m⁻⁴||V||²。                                 (12)

572把av_I ||V||²付到O(L⁴)，因此单用本粗全H运输只给

    av_I |b|²D_var≤O(M₊⁴m⁻⁴L⁴)。                         (13)

该已得upper中的condition因子log(M₊⁴m⁻⁴)~8e^L/L。
右边除T~θe^L仍不趋零；不能将(13)写成O(L⁴)，也不能把condition因子吸收到固定常数。
同理(10)还产生另一层完整inverse条件费用。
这是本粗certificate未付款，**不是actual D_var的下界、不是必然损失、不是实际误差反例**。
本次不能停在这个粗式：下面同一真实receiver的远端像有更强的尾费。

令Q=L_-+H_+、q=H_+Dv+L_-D*u∈QH，则(11)为(G_TS_T−I)w=H_TWq。
因为B H_TG_T⁻¹H_TB*是到BH_TH的正交投影，精确地

    D_var=||Π_(BH_TH)Bq||²≤M₊²||q||²。

设τ_F(T)=Σ_(n∈N_F,log n>T)n⁻¹/²；小于跨窗长度T的delay不可能从左外域送到右外域，
或从右外域送到左外域。两个q分量支撑正交，故完整逆未截掉时仍有

    ||q||²≤τ_F(T)²(||v||²+||u||²)，
    |b|²D_var≤M₊²τ_F(T)²(||V||²+||U||²)。                  (14)

这是完整cross-tail的operator上界，不把任意全H输入费用指派给真实source；实际右端仍是原v/u。
完整证明与独立截尾费用另见[defect独稿](full-defect-and-receiver-control.md)；
本稿独立核了上述投影身份及两支撑正交。

现在只固定一个安全高度，**θ=16、β=1/2**，使用572相同F_L、R₀、I_L、T_R=Γ(R)。
记E_L=e^L/L。统一取α=log4/(2L)，原完整Rankin式

    τ_F(T)≤exp(−αT)∏_(p∈F)(1−p⁻¹/²⁺ᵅ)⁻¹

与572的moving-exponent PNT/Abel同样给

    log τ_(F_L)(T_R)≤−[d₁+o(1)]E_L，
    d₁=8log4−4>7，                                        (15)

于I_L一致。这里partition的权为1，不是572 Euler后权2；T_R始终完整Γ，渐近只用于费用。
log M₊=(1+o(1))E_L、log m⁻¹=(1+o(1))E_L，因而572与(14)–(15)合成

    av_I |b|²D_var≤O(L⁴)exp[(2−2d₁+o(1))E_L]=o(1)。       (16)

再用(9)及clipping的指数余量，**保留actual完整G_M逆**，得到

    av_I |b|²D_M≤O(L⁴)exp[(6−2d₁+o(1))E_L]+o(1)=o(1)。   (17)

于是(3)给真正双向的actual−window绝对费用

    av_I |b|²|q_M−q_T|≤av_I |b|²(|E_clip|+D_var+D_M)=o(1)。 (18)

δ正部不够，但完整D_var还给正确的Cauchy运输

    |δ_win|≤q_T¹/² D_var¹/²，q_T≤m⁻²T/(2π)，
    av_I |b|²|δ_win|
       ≤O(√T L²)exp[(3−d₁+o(1))E_L]=o(1)。                 (19)

所以同一层还给av_I |b|²|q_M−s_T|=o(1)。全部平方与两边界均保留，
没有假设δ或actual ε有有利号，也未免费除b。这一θ=16结论不能外推为572原θ>2e全部范围；
该范围其余高度的完整费用尚须另证。这里不优化阈值。

这已经不同于“旧clipping加永远未知D_var”的结论；必须保存真实闭合的高层范围。
另一方面，不能把(16)–(19)当作最强可消费后果：旧560的原完整残差还直接给更强结论。

### 4.1 扣除旧560完整残差的更强推论：整段高频统一界

现在仅保同一固定安全16，不继续优化任何阈值。令

    R_min(L)=exp(16e^L)，γ=log4/(2L)，E_L=e^L/L，
    d₀=8log4−4>7。

沿旧560完整双残差(11)、||v||/||u||≤m⁻¹h_T及完整τ上界，直接有

    ||r_T||≤2M₊²m⁻¹τ_F(T)h_T，τ_F(T)≤A_γe^(−γT)，
    |b|²D_var≤4M₊⁶m⁻⁴τ_F(T)²h_T²，                       (20a)
    |b|²D_M≤2(M₊²/m²)|b|²D_var+2|b|²m⁻²h²。             (20b)

这里从r_T直接用coercivity，不是先把旧||S−G_T⁻¹||上界套G_T¹/²再损一次M₊。
由旧moving-exponent PNT/Abel，logA_γ=(4+o(1))E_L。
在R=R_min处，τ≤exp[−(d₀+o(1))E_L]；所以(20a)指数系数为10−2d₀<0，
(20b)最坏系数为14−2d₀<0。h²项为R⁻¹/²乘exp[O(E_L)]，亦趋零。
δ的完整Cauchy界相应给

    |b|²|δ_win|≤2M₊⁴m⁻³τ_F(T)h_T²，                    (20c)

其指数系数7−d₀<0。T(R)=Γ(R)对高正R单调，且T e^(−γT)、T e^(−2γT)
在T≥Γ(R_min)均已递减；clipping中的√T R⁻¹/⁴、R⁻¹/²也递减。
由实结构k_−R=bar k_R、Γ偶，负频同样成立。因而旧原件及本候选的直接corollary是

    sup_(|R|≥R_min(L)) |b|²(D_var+D_M+|q_M−q_T|+|δ_win|)=o(1)。 (20d)

actual−S的绝对费也逐点一致o(1)。这些界不使用572的高度平均或receiver的O(L⁴)。
因此572的mean路径虽合法，**并非该安全高层费的必要新输入**。
新的是本次把未曾消费的cofinal参数和候选运输准确闭合；来源／strong-old直接后果不能重复记独立容量。

## 5. actual ε及完整Weil型的系数方向

保原完整Γ与所有proper powers，记

    C_F(R)=[Γ(R)−2Σ_(p∈F,k≥1)(logp)p^(−k/2)cos(kRlogp)]/(2π)，
    e_S(R)=|b(R)|²s_T−C_F(R)。

560的actual密度为ρ_F=|b|²q_M，ε_F=2π(ρ_F−C_F)。所以(3)的actual预算是

    ε_F/(2π)=e_S+|b|²[δ_win−D_var+E_clip+D_M]。             (21)

e_S是S_T的bulk/两个单边界主项与全部尾的真实算术比较余项；它不同于δ_win。
572本身没有支付e_S的cofinal费用。模型完整逆与arithmetic的误差则为e_S+|b|²δ_win，
也不是actual ε。在安全θ=16层，旧560给出的显式余项则足够：

    |e_S|≤C_(F,γ)(1+T)e^(−γT)，
    C_(F,γ)=M₊²{(m⁻¹J_γ+J_0A_γ)/π+A_γ²/(πγ)+M₊²A_γ/(πm³)}，
    A_γ=∏(1−p⁻¹/²⁺ᵞ)⁻¹，
    J_γ=A_γΣ_(p∈F)(logp)p⁻¹/²⁺ᵞ/(1−p⁻¹/²⁺ᵞ)。

对S_T原算术pair余项，这个560给完整逆余项的常数是合法较大上界；
把γ取为log4/(2L)，moving-exponent的同一PNT/Abel给

    logA_γ=(4+o(1))E_L，logJ_γ=(4+o(1))E_L，logJ_0=(1+o(1))E_L，
    logC_(F_L,γ)≤(11+o(1))E_L，γT_R=(8log4+o(1))E_L。

由于8log4>11，旧完整算术尾于|R|≥R_min一致o(1)：(1+T)e^(−γT)在这里亦递减。
结合(20d)–(21)遂给本门的最强高层实际误差结论

    sup_(|R|≥exp(16e^L)) |ε_(F_L)(R)|=o(1)。                 (22)

它蕴含所选I_L上的绝对高度均费o(1)，但本身更强；Γ、全部prime powers并未删除。
它是旧560显式完整残差／算术尾在足够高有利层的强推论加本候选clipping运输，
不能拿更弱“原模型δ+尚不够”的子界当唯一旧对照，宣称新增独立容量。

若仅丢掉正D_M，(21)给ε_F的下界。完整源身份却是

    Q_W(r)=t_F(r)−<r,K_(F,I)r>
       +2|<r,cosh(u/2)>|²−2|<r,sinh(u/2)>|²，             (23)
    <r,K_(F,I)r>=(1/(2π))∫ ε_F(R)|hat r(R)|²dR。

因此由正迹t_F≥0推出Q的有利下界，需要ε_F的上控制，或完整同源signed/relative比较。
仅ε_F下界给(23)的相反侧上控制，不能消费成Q≥0。
同样，δ_win的正部上界在模型端有正向用途，却不能跨越(21)里的actual D_M和负D_var。

这里没有假设双pole矩为零，pole项完整保留；有限Euler μ numerator也没有替代完整prime powers。

## 6. receiver dy／carrier／原du与Dlog三者不能混用

物理receiver范数是||V||²_H，变分候选y在实际M中，w只是频率R的Γ-window载波。
原Weil输入另为r∈L²(I,du)，zero-extension的自然域是Dlog，采用

    hat r(R)=∫r(u)e^(−iRu)du，
    ||r||²=(1/(2π))∫|hat r(R)|²dR，
    ∫log(2+|R|)|hat r(R)|²dR<∞。

560已对每个固定F/I支付ordinary trace与原Dlog core；F覆盖p<e^(2L)后全部支撑外相关exact0。
本门不重复计这项域桥，也不把旧每fixedL紧误差升级为成长费用。
要从(21)消费ALL复r，须对(23)的同一加权Fourier积分给原du或Dlog预算，
并覆盖低频／危险core及核心—补空间coupling。

572及本次中间mean路径的av_I是长度R₀^β区间上的未加权高度平均；它没有给逐R或全部局部调制源的乘子上界，
亦没有给与每个|hat r|²的相关费。compact源仍可调制到该长区间的局部片段；
长区间平均小本身不排除局部集中，更不覆盖所有R或所有r。
除||w||²~Γ/(2π)的模型相对费只有在另付合法uniform/相关运输后，才能变为原Dlog的相对费。
不能把载波范数本身当作源范数，也不能从平均费免费除b。

本门更强(22)确可合法运回**原源的高频误差分量**。令δ_L=sup_(|R|≥R_min)|ε_F(R)|→0，
K_hi=1_I F_unit* M_(1_(|R|≥R_min)ε_F) F_unit1_I，则

    ||K_hi||_(L²(I,du)→L²(I,du))≤δ_L，
    |(1/(2π))∫_(|R|≥R_min) ε_F(R)|hat r(R)|²dR|
       ≤δ_L||r||²。                                       (24)

这是ALL原du源的同一高频压缩误差，因而对Dlog源也成立。Plancherel的1/(2π)
已在未归一hat积分中；相应F_unit算子范数是δ_L，不能再次除2π。
它不是整个K的小费：低频部分|R|<R_min完全保留，没有由(24)支付。
非零compact源不可能同时完全Fourier支撑在高频，不能把(24)写成全r误差o(1)。
此处源的高／低频分解是误差乘子账本，不把band-limited分量称仍在同一compact源域。

θ>2e仍在旧555的有利高频大小层；本门付清的clipping直接推论虽可覆盖固定θ>0，
没有把572的receiver尾估计或(21)的完整误差覆盖推进到θ≤1危险core。

## 7. 来源门结论与独立新输入的准确缺口

本门付清候选的原H/M域、旧clipping的同源cofinal显式费用及完整符号账本；
不能在粗(12)–(13)处误停，完整tail已在安全θ=16层支付D_var、D_M及actual误差，
最强旧残差推论还给整段高频逐点一致o(1)与原du高频误差的operator小费。
这不是“该层D_var永远未知”，也不是原572所有θ>2e／原源／危险核心已闭合。
剩余原源责任未因足够高的误差tail改变，现有完整算术／残差尾须计为旧强后果。
故本来源门保存高层直接合成即止，不由它新建C036或续θ/β/γ阈值优化。

重新准入至少须下列之一是独立证明，而非把目标当定义：

1. 在实际receiver像／候选残差上，保全部returns和两边界的D_var或D_M−D_var新signed估计，
   其中condition损失及原源相关费用确可付，且给超出旧fixed-F结论的actual净后果。
2. S_T全部bulk/两单边界的同一Γ/prime-power比较尾、实际k_R/G_M的cofinal运输，
   与ALL原complex du/Dlog源、核心及coupling共同闭合。
3. 同一真实global section/kernel/评价对象上的独立局部消失与全局height/RR容量，
   再以完整Γ/prime-power/pole身份运输到目标型；正J或变分恒等式本身不提供该容量。

直接假设完整Weil Grams PSD，或假设足够强且无独立来源的domination，仍是目标／等价终点。
本次来源门不改变542+555→557的strongest-old whole leading4/5，不改变独立global容量、
危险核心、全源coupling或通常Ξ的宏观瓶颈。没有运行中的计算、下载或后台进程。
