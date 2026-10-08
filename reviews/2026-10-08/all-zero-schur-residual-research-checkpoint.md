# 全零点稀疏插值、正谱 leverage 与真实相关量

2026-10-08，checkpoint_audit；本轮基线6666ad6。
新结论是实际有限计数的适应性增强，以及可逐项核算的二／三点相关量与内窗残量下界。
前p亏损及去opnorm税Cauchy由root提出；本文独立重推，并补真实核交叉、内窗与两份log费用。
尚未证明任何 N 归一的固定正收益；498 的比例、中心四阶常数与7/8边界均未改变。

## 1. 固定对象与输入

所有身份按 UTF-8、CRLF/lone-CR→LF、保留EOF。499及九点161行本轮全文读；
635行论文及158行旧独审已全文读，本轮重核固定平滑、真实全零点算子和计数段。
453行旧零包源此前全文读，本轮核其(7)局部计数的重数范围。

| 输入 | 行／LF字节 | SHA-256 |
|---|---|---|
| [499](../../notes/499-am-bounded-storage-periodic-ceiling-and-negative-spectrum.md) | 145／8335 | 7378ec659f01dc188ab6322c0578276f64827838d740cd0279bc5eec3570ad37 |
| [正式论文](../../papers/lossless-eight-point-simple-critical-paper.tex) | 635／24829 | 51c3931e3ce3ba54cd4a8441254ea0c8767009aee57e427f7f3492108b1a204c |
| [原有限谱独审](am-storage-and-strip-review-checkpoint.md) | 158／10800 | 6c08f70e88c496243a65b0ef76b24b95f2c982fb3b44c4064ba38a53a1590674 |
| [原局部计数](hybrid-original-squarefree-signed-zero-gram-research-perron.md) | 453／18782 | 0b126138c7bf42e9be3c4352b099a6ab37d88cef93af20593593c8e849aa2a17 |
| [九点lift](am-nine-point-lift-research-high-product.md) | 161／8823 | 88bd93c28ca361a5be70a48504a186378abba57031ac0f149b08eaf5a8acf045 |
| [条件代数程序](../../scripts/am_adaptive_leverage_gain_certificate.py) | 97／4258 | 8d3955001ab59c2622936d969ba84cf18692b36061b34b280070311762551e6d |
| [条件代数输出](../../output/am-adaptive-leverage-gain-certificate.json) | 25／1500 | 4c2e9350449b598a6124cdbc7b92d76cd1cebc7fb3474676f25f1c3d94c46865 |

固定ε，fε为498的偶非负概率密度，ηε=√fε，Kε(t)=∫fε(u)e^(−2πitu)du。
保留0<Imρ≤T的全部重数，zρ=−i(ρ−1/2)logT/(2π)=x+iy。
v_z=ηεe^(−2πizu)，g_z=(v_z+v_barz)/2，h_z=(v_z−v_barz)/(2i)。
在原实不动形式上，A=Σ_real μ_xv_x⊗v_x+2Σ_pairs μ_z(g_z⊗g_z−h_z⊗h_z)。
P只含n个简单实点的单位特征，Q=A−P；重复实点在Q中的权是μ_x，绝非μ_x−1。
指数独立性给p=n_+(Q)=r+k、n_+(A)=n+p、n_−(A)=k。
S=N−n−2p=Σ_repeat(μ−2)+2Σ_pairs(μ−1)≥0。
trA=N、trA²=(C(fε)+oε(1))N，先固定ε令T→∞，随后ε↓0。

## 2. 保留前p正谱的精确亏损

φ₂(t)=t²−(t−2)_+²，J(U)=trφ₂(U)−n；U为简单实点Gram。
令G_−=trA_−²+4trA_−，M_Q=trQ_−，E_Q=1_(Q>0)，L_P=tr(E_QP)≥0。
把A_+的谱按降序填零；minmax仍给λ_(p+j)(A_+)≤λ_j(U)。
前p项均为A的正特征值，H(λ)=4λ−λ²=4−(λ−2)²。
在随后n项用H(t)≤4u−φ₂(u)，其余A_+项为零；完整负谱只扣一次，得到

    trA² ≥2N−n+J(U)+G_−+2S+D_top,
    D_top=Σ_(i=1)^p(λ_i(A)−2)².                              (1)

Ky Fan取同rank p的真实试投影E_Q，而不只使用P≥0，给
Σ_(i≤p)λ_i(A)≥tr(E_QA)=trQ_++L_P=2p+S+M_Q+L_P。
所以Cauchy严格给

    D_top ≥(S+M_Q+L_P)²/p.                                   (2)

p=0时Q≤0、trQ=N−n≥0，故Q=0、N=n；(2)不作除零。
这项L_P可以在离线深度趋零时仍有正值，不必先证明全A的共同Schur残量。
它不是孤立块收益求和：E_Q是完整Q的正谱投影，所有零点耦合仍保留。

## 3. 去掉opnorm税的真实二／三点接口

记T_PQ=trPQ、V_PQ=trP Q²=Σ_simple s∥Qv_s∥²≥0。
trPQ≤trP Q_+，Hilbert–Schmidt Cauchy给
(trP Q_+)²≤tr(PE_Q)tr(PQ_+²)≤L_P V_PQ，因Q²=Q_+²+Q_−²。
因此

    L_P ≥[T_PQ]_+²/V_PQ.                                    (3)

V_PQ=0时QP^(1/2)=0，故E_QP^(1/2)=0、L_P=0、T_PQ=0；此时(3)取0。
这个接口不含λ_max(P/Q)的附加费用。它的实际二点量为

    T_PQ=Σ_simple s,repeat x μ_x Kε(x_s−x)²
         +2Σ_simple s,pairs z μ_z Re[Kε(x_s−x_z+iy_z)²].       (4)

V_PQ也完全可核算：令b_i为全部重复v_x、全部g_z和h_z，
D的对应系数为μ_x、2μ_z、−2μ_z；C_ij=〈b_i,b_j〉，a_i(s)=〈b_i,v_s〉，则
V_PQ=Σ_s a(s)^t D C D a(s)。使用完整范数平方，不能删其展开后的signed交叉项。
原全零点pair-correlation付款的是trA²；它不自动支付带simple／repeat／pair标签的(4)，
也不自动给这个真实三点量O(N)上界。

## 4. 已有输入的准确两份log费用

原局部零点计数按重数给#{ρ:|Imρ−t|≤1}≪log(2+|t|)。
故每个rescaled长度1区间的简单实点数≪L=logT，包括完整低高度前缀。
fixedε的光滑紧支撑给|Kε(d)|≪ε(1+|d|)^−2。
简单Gram的绝对行和≪ε L，因而∥P∥op≪ε L、trP²≪ε NL。
Q=A−P和已付trA²≪ε N给trQ²≤2trA²+2trP²≪ε NL，最终

    V_PQ≤∥P∥op trQ²≪ε N L².                                (5)

因此即使另有T_PQ∼tN，(5)仅保证L_P≳ε N/log²T，仍无固定比例收益。
实际可攻的新命题是同一对象的typed二点正下界与typed三点V_PQ≤vN，
而不是将whole HS的O(N)改名为三点付款。这里没有新DirichletL或PCC前件。

## 5. 用固定内窗避免ε常数爆炸

固定偶内窗τ≥0、正于一个开区间，并要求τ≤fε对所有足够小ε。
这可在498允许的标准cutoff族内实现：χε最终在每个固定内区恒为1，取τ≤fAM内支撑。
不把任意仅点态收敛的cutoff族误认成已满足这个逐点支配前件。
M是乘法收缩√(τ/fε)，零分母处τ=0；实际特征逐一满足Qτ=M Qε M。
有限负迹的dual形式trQ_−=sup_(0≤D≤I)−trDQ，使

    tr(Qτ)_− ≤tr(Qε)_−.                                    (6)

因0≤MDM≤I，证明不使用负部的算子单调性。τ可未归一化；
trQτ=mτ(N−n)、mτ=∫τ，不能把Qτ的trace改写成N−n用于(1)。
(6)只供给M_Q的下界；它不宣称L_P在换窗后单调。
这样一个固定Kτ=τhat的实际残量下界可同时供给每个小fixedε，再取外层极限。

## 6. 全部真实核交叉项与两条有限下界

以下所有特征均在τ窗。记m=Kτ(0)、d=x_i−x_j，g_i含重复实点时取y_i=0。
真实实内积准确为

    G_ij=〈g_i,g_j〉=½Re[Kτ(d+i(y_i+y_j))+Kτ(d+i(y_i−y_j))],
    H_ij=〈h_i,h_j〉=½Re[Kτ(d+i(y_i+y_j))−Kτ(d+i(y_i−y_j))],
    X_iz=〈g_i,h_z〉=−½Im[Kτ(d+i(y_z+y_i))+Kτ(d+i(y_z−y_i))]. (7)

σ_i²=G_ii=(Kτ(2iy_i)+m)/2，ν_z²=H_zz=(Kτ(2iy_z)−m)/2>0；X_zz=0。
正特征只有r个重复v与k个g，权d_i分别为μ_x和2μ_z；负权为2μ_z。
令R_ij=G_ij/(σ_iσ_j)，κ_+=max_iΣ_(j≠i)|R_ij|，明确排除diag1。
若κ_+<1，逐向量Schur及R≥(1−κ_+)I给可逐项核算的

    M_Q≥tr(Qτ)_−≥2Σ_z μ_z[ν_z²−Σ_iX_iz²/σ_i²/(1−κ_+)]_+.    (8)

这比全A投影减少n个简单列，却仍包含所有实际Q正特征，不能另删远点。
另一条不要求消去正特征的dual试投影是Π_H，投到全部h的span。
写Qτ=B−C，B=Σ_i d_i g_i⊗g_i、C=2Σ_z μ_z h_z⊗h_z。
M_Q≥[trC−trΠ_HB]_+。若κ_H=max_zΣ_(w≠z)|H_zw|/(ν_zν_w)<1，则

    M_Q≥[2Σ_z μ_zν_z²
          −Σ_i d_iΣ_z X_iz²/ν_z²/(1−κ_H)]_+.                 (9)

Π_H C=C，规范h Gram逆≤(1−κ_H)^−1I证明(9)。自身g_z/h_z精确正交减少泄漏。
κ条件是充分的真实有限核条件，未由7/8或whole pair-correlation证明；κ≥1时不使用该式。
k=0时Q≥0、M_Q=0，(8)–(9)取0，不求空Gram逆。
普通条带只给|y|≤3logT/(16π)，不提供这些绝对行和、深度或正密度下界。

## 7. 真正可消费的平均命题与极限

例如，若每个小fixedε先有liminf_T T_PQ/N≥t−oε(1)>0、
limsup_T V_PQ/N≤v+oε(1)、0<v<∞，则(3)给liminf L_P/N≥t²/v−oε(1)。
若固定内窗(8)或(9)另外有liminf_T下界qN，(6)给每个小ε的liminf M_Q/N≥q。
这些都是actual ζ全部所需typed sums的命题，当前没有证明t>0、v有限或q>0。
若最终δ=liminf_(ε↓0)liminf_(T→∞)(M_Q+L_P)/N>0，
由p/N≤(1−n/N)/2、(1)–(2)及498得到，对r=liminf n/N<1，

    (1−c)r≥A₀−B+2δ²/(1−r)，A₀=.67216841.                   (10)

r=1时结论已强于目标。没有交换ε/T顺序或把有限的正残量当成N归一δ。

## 8. 九点lift的独立范围核对

High161行数学限定PASS：两完整相邻8帧各取½，另加跨度8权2。
s≤7仍各付原跨度≤2，s=8恰2，b′=10⁻⁸(14449,43085,66399,78242,78242,66399,43085,14449)。
Σb′=B，旧reward仍仅c；新c+δ需全连续[.8,∞)⁸证明，并保持c+δ<1/40近对合同。
正压力尾精确付S≥2870483/72245（目标δ=10⁻⁶），不等于整个紧核心已付。
两个旧低余量frame的T₂δ cover、真实左右兼容交集及全span核下界尚未建立。
作者Arb指定盒的(6.85,6.87)µ仅为该盒余量；本轮读106行诊断代码，未重跑定位／诊断。
九点32dε滑窗误差及m−8端项可沿498消费，但任何δ>0仍未准入。
本轮未写新实验或数值覆盖，不改任何冻结输入／Git；实际边界与比例保持原值。

## 9. 条件代数证书的独审

97行程序与25行JSON本轮全文读。独立标准库Fraction重推顶点与负残差，未import程序自证；
实际readonly `--check` 退出0：`PASS conditional adaptive leverage algebra and committed report`。
令h=(M_Q+L_P)/N，γ=1−c、p₀=66812491/99194997。
直接对每个fixedε的(1)–(2)与498作有限T预算：γ_ε=1−c+42dε、bε=2−C(fε)−B，
2h_T²≤[γ_εr_T−bε+oε,T(1)](1−r_T)，其中r_T=n/N；p=0时两边的h／尾因子皆为0。
对全部r_T∈[0,1]先用凹式上界(γ_ε−bε)²/(4γ_ε)，再T→∞、ε↓0；
原有限预算及r_T≤1亦保证0≤γ−(A−B)，A≥A₀使上述上界不大于γ(1−p₀)²/4，故

    limsup_(ε↓0)limsup_(T→∞)h²≤262156673710009/19838999400000000<.114954². (11)

这也沿原fixedε能量及dε→0得到，并非把liminf改写成limsup。
若另有未付输入liminf_(ε↓0)liminf_(T→∞)h≥3/2000，目标r*=67356/100000处
γ(r*−p₀)(1−r*)−2(3/2000)²=−17817139237/62500000000000000<0；
其在[p₀,r*]的导数下界404749045517/1250000000000>0，因而条件下严格r>r*。
r*>499固定range7方法ceiling，但没有证明h的正lower，故不是新的实际比例。
JSON将归一正输入、有限谱引理与解析运输的proves范围均设为false，范围正确；
程序只验证有理后果、身份与报告一致性，不认证无限ζ命题或九点紧域证书。
