# 完整原四词的连续主密度消去与真实产品长度

2026-10-08，作者 twisted_research。起点只读核到main HEAD `88e86a35`，
工作区干净。只新增本稿，不改冻结docs、scripts、output、papers、math或Git。
状态：新完整推导，待另一作者独立全文审查。

本次支付一个完整范围接口：原high channel可减去连续素数主密度，
其actual high4、31、22及原平方残差q都只改变O((log X)^−2)。
同一结论可传到各自physical四词，但actual/physical比较仅用于包含
主密度的差词，绝不据此删除整个unknown的内部P。
不需要[R]或高第四矩有界前件。

该消去没有缩短尚未付款的atomic两素数产品。它保留了一个准确的
signed-measure joint completion；仍没有净O(N)第四矩或新比例上界。

## 1. 原对象、冻结前件和完整连续channel

保持X=T/(2π)、ell=log X、d=floor(X ell)、I=[−ell/2,ell/2]、
原载波τ_k=T+2πk/ell、interval isometry E、P=EE*、Q=1−P。
R_s f(u)=f(u+s)，在实线上零延拓。原偶C² taperφ与a_ell=
ell^−1||φ||2²保持，a_ell有固定正下界。

\[
 b_p=\frac{\log p}{a_\ell\ell\sqrt p},\quad
 B_H=-\sum_{\sqrt X<p\le X}b_pM_\phi
       (R_{\log p}+R_{-\log p})M_\phi,\quad H=E^*B_HE.
\tag{1}
\]

L指原low matrix；长度始终写ell。原已付输入为
||H||2,d+||L||2,d=O(1)、||H||op≤m_H≪√X/ell、
||L||op≤m_L≪X^1/4/ell，及0≤W≤MI、M=O(1)。

| 冻结来源 | canonical UTF-8 LF SHA-256 |
|---|---|
| [454原二矩](../../notes/454-original-background-and-weighted-prime-mixed-traces.md) | 8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7 |
| [456整个actual重复标签](../../notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md) | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 |
| [465实际W/Γ](../../notes/465-centered-high-square-joint-fourth-budget.md) | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 |
| [463双侧高度](../../notes/463-two-sided-height-stability-for-original-fourth-words.md) | 6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90 |
| [真实P的band crossing](../2026-10-07/hybrid-one-three-finite-band-admission-research.md) | bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f |
| [whole high物理与nearcore](../2026-10-07/hybrid-whole-fourth-compression-upper-research-radial.md) | 0703f66778d49de29e363f7eabede6718ef24fe579e53603ff70db4e6aeacdea |
| [high半区间Gram](../2026-10-07/hybrid-high-parity-gram-and-mobius-completion-research-radial.md) | 3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2 |
| [470新必要下界](../../notes/470-centered-spectral-variance-excludes-small-high-residual.md) | 729ddbed2b2d2af08e21e5f1ebabfb5663f906c702f52b13f81aac224402a93a |

本稿使用这些已付二矩、packet及有限代数；没有使用尚未付款的完整四矩。
定义strong operator integral

\[
 B_0=-\frac1{a_\ell\ell}M_\phi
  \int_{\sqrt X}^{X}x^{-1/2}(R_{\log x}+R_{-\log x})\,dx\,M_\phi,
 \quad C_0=E^*B_0E,\quad \bar H=H-C_0.
\tag{2}
\]

具体说，对每个f∈L²(R)，先取L²-valued Bochner integral：
平移在strong topology连续，且x^−1/2的有限区间积分有限。
这定义一个bounded operator；每个T其operator norm由总变差控制，
||B_0||op≪√X/ell。没有主张平移族在operator norm连续或
B(L²)-valued Bochner可积。后续Fourier表达由逐向量积分得到。
它不是任意新row或目标补偿：正测度dx正是原genuine-prime
Chebyshev测度dϑ(x)=Σ_p log p δ_p的连续主密度。
本稿不要求用PNT把每个microscopic prime fiber换成dx。

## 2. 全部高度的actual C0确实operator-small

取原unitary Fourier，F=𝓕 Mφ E。与(1)完全相同的归一化给

\[
 B_0=M_\phi\mathcal F^{-1}M_{D_0}\mathcal F M_\phi,
 \quad C_0=F^*M_{D_0}F,
\]
\[
 D_0(t)=-\frac{2}{a_\ell\ell}\operatorname{Re}
 \frac{X^{1/2+it}-X^{1/4+it/2}}{1/2+it}.
\tag{3}
\]

这一式是准确积分，不是pointwise prime近似。原J=[T/2,3T]上
ρ_0:=sup_J|D_0|≪X^−1/2/ell，全高度sup≤m_0≪√X/ell。
原packet满足||F||≤1、||1_Jc F||HS²≪T^−2。
由于D_0是frequency乘法，bad项两侧准确都为1_Jc F。因此

\[
 \|C_0\|_{\rm op}
 \le\rho_0+m_0\|1_{J^c}F\|_{\rm op}^2
 \le\rho_0+Cm_0/T^2
 \ll X^{-1/2}/\ell=:\rho .
\tag{4}
\]

没有忽略t≈0的连续principal峰；该峰由两个外packet同时付款。
P仍是原interval finite carrier，没有与1_J交换。
本式不使用零自由性、H⁴ bounded或scalar fourth mean value。

## 3. entire actual四词及Γ的统一误差

normalized Schatten记号||A||p,d=d^−1/p||A||Sp。
任意有序四词若一个因子为C_0、其余来自H、L、bar H、C_0，
每个因子的S2,d为O(1)，op≤C m_H。
给C_0用op ρ，给另一因子用op C m_H，另外两个用S2,d，
非交换Schatten Hölder直接给

\[
 |\tau(A_1A_2A_3A_4)|\ll\rho m_H=O(\ell^{-2}).
\tag{5}
\]

因子顺序任意，不假设这些矩阵交换。若有多个C_0，仍有同一upper。
对第四次方或各原mixed word逐因子telescoping，所以

\[
 \begin{gathered}
 \tau\bar H^4-\tau H^4=O(\ell^{-2}),\qquad
 \tau\bar H^3L-\tau H^3L=O(\ell^{-2}),\\
 \tau\bar H^2L^2-\tau H^2L^2=O(\ell^{-2}),\qquad
 \tau\bar HL\bar HL-\tau HLHL=O(\ell^{-2}),\\
 \tau(\bar H+L)^4-\tau(H+L)^4=O(\ell^{-2}).
 \end{gathered}
\tag{6}
\]

这不是仅凭S4,d距离小就对可能增长的第四迹作连续性判断。
(5)专门使用已付second与raw op，只需两个S2因子。
它覆盖完整high范围、全部labels/signs以及原实际所有内部P。

还可保持原W而定义bar Γ=bar H²−W。

\[
 \|\bar\Gamma-\Gamma\|_{2,d}
 \le2\rho\|H\|_{2,d}+\rho^2=O(\rho),\quad
 \|\Gamma\|_{2,d}\le\|H\|_{\rm op}\|H\|_{2,d}+M=O(m_H).
\]

因此包括未知Γ增长的交费为

\[
 |\|\bar\Gamma\|_{2,d}^2-\|\Gamma\|_{2,d}^2|
 \le2\|\Gamma\|_{2,d}\|\bar\Gamma-\Gamma\|_{2,d}
        +\|\bar\Gamma-\Gamma\|_{2,d}^2
 =O(\ell^{-2}).
\tag{7}
\]

同一U-even/U-odd投影为HS contraction，也给q_e、q_o各自O(ell^−2)差。
于是470的必要下界及gap仍对bar Γ成立，不能靠此消去绕过q_*。
weighted second及ΓW中心化也只改变o(1)，因为W op有界、H S2,d有界、
C_0 S2,d≤ρ。原commutator k用(6)的两个四词亦只改变O(ell^−2)。

## 4. 只对含principal的差词支付全部physical crossing

为明确它没有隐藏actual/physical切换，取同一J的good versions。
原packet给每个C_i−C_i^g的trace norm≤Cm_i/T²。
连续D_0同样有该式，因为证明只使用bounded multiplier与packet。
因而H^g、L^g的S2,d仍O(1)，C_0^g op≤ρ_0。

原band-crossing来源(13)–(16)只用global sup，允许sharp J和任意
bounded D^g：l_i,l_i*≤C√ell ||D_i^g||∞。
对至少一个B_0^g的四词，以原three internal P的closed two-crossing
引理得到

\[
 d^{-1}\left|\operatorname{Tr}E^*B_1^gB_2^gB_3^gB_4^gE
       -\operatorname{Tr}C_1^gC_2^gC_3^gC_4^g\right|
 \ll\frac{\ell\rho_0m_H^3}{d}=O(\ell^{-4}).
\tag{8}
\]

全部六个crossing配对都含同一principal的小sup；左右伴随同界。
不是对剩余四prime词用此式免费删P。
其finite词由(5)为O(ell^−2)。

回到所有height时，463的proof对D_0也逐字成立：每个physical
replacement在一个bad frequency multiplier处切开；左右各至多三个
K=𝓕 Mφ²𝓕^−1，两个first-far HS都是O(T^−1)乘其余raw norms。
proof没有用离散prime分布，只用C² kernel和bounded multipliers。
每个physical或actual四词的raw/good差因此均为

\[
 d^{-1}O(T^{-2}m_0m_H^3)=O(X^{-1}\ell^{-5} ).
\tag{9}
\]

所以(6)还传到相同顺序的physical四词，以O(ell^−2)误差成立。
physical各placements没有被免费循环；每个差词各自支付(8)–(9)。
这是完整principal subtraction，仍未支付不含principal的原内部P余额。

## 5. 真实signed-measure completion保留全部有限walk

定义原高区间的signed测度

\[
 d\nu_H(x)=\sum_{\sqrt X<p\le X}\log p\,\delta_p(dx)
               -1_{[\sqrt X,X]}dx,\qquad
 d\eta_H(x)=\frac{d\nu_H(x)}{a_\ell\ell\sqrt x}.
\tag{10}
\]

bar B_H的准确表达就是以η_H替换(1)的高prime权重。
ν_H有限T的总质量未必零；本稿不把其PNT误差设为零。
测度总变差经Chebyshev控制为∫|dη_H|=O(√X/ell)，
所有entry与有限矩阵乘法均有定义。

对s=±logx，仍令a_s(u)=φ(u)φ(u+s)，
entry准确为e^{iτ_k s} a_hat_s(j−k)。
原[finite walk公式](../2026-10-07/hybrid-one-three-mixed-prime-sector-research.md)
(28)–(30)可对η_H积分：保持n_1+…+n_4=0、
r_j=Σ_{i≤j}n_i、span(r)<d及原核

\[
 \Gamma_{d,r}(S)=d^{-1}
    \sum_{k=r_{\max}}^{d-1+r_{\min}}e^{i\tau_k S}.
\tag{11}
\]

所有ν原子、连续变量、signs、原载波和三个内部P均在同一公式中。
有限T时C² a_s的Fourier ℓ¹ bound与有限测度总变差给绝对可积majorant，
所以这次Fubini合法。没有改成长度d的K_d，或另一个residue-row family。

在physical空间，连续high support同样使每步长度>ell/2，
其正方向块Abar=Π_- Abar Π_+，Abar²=0。
这条bipartite结构只对physical成立，不对压缩后E*AbarE宣称nilpotence。
atomic same-prime diagonal仍是原W：ν⊗ν的连续及混合部分在x=y上
没有原子，只有prime×prime同p部分产生local zero translation。
这提供一个保持原diagonal的具体centered ratio completion。

## 6. 支撑没有缩短尚未付款的atomic near量

physical high4只有+-+-及−+-+，其五点支持给
S=log(pr/(qs))满足|S|<ell/2，故没有±ell alias。
但它不蕴含pr、qs≤X。冻结whole-high源§7已构造
p,q,r,s∈[αX,βX]、四distinct、|pr−qs|≤δX的真实非空路径；
这里pr,qs∼X²、K_d的实部正，endpoint overlap为常数/ell。
原atomic restricted nearcore≥cX/ell^5。

主密度消去没有降低这一atomic计数或系数：η_H在每个prime上的
原子仍为b_p。乘积测度的prime×dx及dx×dx部分是绝对连续，
不会改变两prime产品的离散原子。
令c_H(n)=Σ_{pq=n,p,q high}b_pb_q，则整个atomic Hilbert energy仍准确为

\[
 \sum_n n|c_H(n)|^2
 =2\left(\sum_{p\in H}p b_p^2\right)^2
          -\sum_{p\in H}p^2b_p^4
 \asymp X^2/\ell^2.
\tag{12}
\]

上界由Chebyshev，下界只需冻结nearcore来源使用的固定比例区间PNT。
故高度长度X上的标准weighted-MV误差仍有X/ell²量级的normalized费用，
不能因已减连续主项就免费把它改成O(1)。
正nearcore依然只是restricted signed sum，不是bar H⁴或bar B_H⁴的下界。
各含连续密度的四词完整净和由§3–4为o(1)，并不表示它们在每个
microscopic determinant shell也小。若在shell内先作density replacement，
就重新索取尚未付款的joint prime correlation。

31的two+/two− near实际满足HH产品≤2Xsqrt X，因为另一侧是HL；
这是整个near的正确X^3/2长度，仍大于X。
full high4的两侧则仍可为X²。22的HL ratio products可到Xsqrt X，
same-sign physical部分的产品≤X也不能自动限制actual Q-crossing。
因此principal subtraction保留相位与coupled窗口，却没有给新的integer
spacing、TypeII长度或marked Möbius-family准入。

## 7. 真实进展与未完成的一步

本稿确证：可在整个actual high-square/31/22 joint budget中先减连续
principal channel，误差O(ell^−2)，所有高度、范围、载波与P已付。
物理对应也只对这些差词支付o(1)，不把未知whole physical量等同actual。
这是净主密度消去，并且同一个signed measure保留原same-prime diagonal。

尚未付款的是η_H的原atomic two-product相互作用与coupled path/walk
在真实X²或X^3/2产品范围的净upper。独立prefix [R]只能控制完整
canonical多项式；它没有将(12)或每个moving determinant fiber变成短列。
470已排除旧Q=1/350，任何新whole上界还必须容许q≥q_*。
进一步，flat原high的已付重复标签union为19/240+o(1)。若D_T表示
原actual四distinct标签的完整signed union，则456与已付ΓW中心化给

\[
 \tau H^4=19/240+D_T+o(1),\qquad
 q=19/480+D_T+o(1).
\tag{13}
\]

所以接近q_*的可达upper必须证明四distinct部分的净负相消；只证
D_T=o(1)会留下q→19/480。连续主密度消去保留(6)–(7)，故没有
改变这个原actual目标。这里未把含连续变量的词硬分到原重复标签union。
本稿没有给可达数值Q，也没有新的O(N)四矩、实际比例或无零边界。
