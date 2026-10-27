# 583：完成化模源的全 Faber／native Green 尾与 principal 类门

2026-10-27；C046，G20261027／原冻结0c4f基线。root 对齐三份实际原稿后的数学主稿，独立 fresh 与结算状态另见同目录审查／STATE。≤582、537／552／553与10-27标准容量比较是输入；不能将旧成果再算本轮。

本轮新增的是**同一全物理源的实际系数、整数基 lift 后的全局 Green/current 完成化和关系测试**。结论限于固定复粗曲面，未得经典 Weil 正性或独立 primitive RR；原 strongest-old whole leading4/5 仍为负惯性上预算。

## 1. 同一源、实际模截断和原费用

令 r=e^(u/2)f，允许全部复 S_exp，即每个导数都在每个线性指数权下迅速衰减。定义

\[
 L_r(z)=\int_{\mathbb R}r(u)e^{zu}du,\qquad F_r(\tau)=L_r(j(\tau)),\quad q=e^{2\pi i\tau}.
\]

这里指数为 u j(τ)，全部线性指数矩足够；不混同582的 height 缩放公式。L_r entire，F_r 在 H 全纯、模不变，一般有 essential cusp，因而没有把它直接套入原有限主部乘积定理。

对任意固定0<s<1，取

\[
 K_n(u)=\frac1{2\pi i}\oint_{|q|=s}e^{uj(q)}q^{-n-1}dq,
 \quad A_s=\max_{|q|=s}|\Re j(q)|,\quad p_A(r)=\int|r(u)|e^{A|u|}du.
\]

全部 Laurent 系数为 a_n(r)=∫rK_n，且

\[
 |K_n^{(\ell)}(u)|\le s^{-n}M_s^\ell e^{A_s|u|},\quad
 |a_n(r)|\le s^{-n}p_{A_s}(r),\quad |b_m(r)|\le s^mp_{A_s}(r),\quad b_m=a_{-m}.
 \tag{1}
\]

各固定源的 b_m 超几何衰减；s改变时 p_(A_s)也改变，不能无费用优化半径。fixed 源窗(-L,L)的精确 du dual norm 是 ||K_n||_(L²(-L,L))，可用

\[
 |a_n(r)|\le s^{-n}C_{L,s}\|r\|_{du},\quad
 C_{L,s}^2=(e^{2A_sL}-1)/A_s
 \tag{2}
\]

及 A_s=0 时2L。原 zero-extension Dlog²=(2π)^−1∫log(2+|t|)|r̂(t)|²dt≥log2||r||²，故(2)乘(log2)^−1/2即可。全线用强半范数，不声称 du／Dlog 统一。

用 q 导数定义整数 monic Faber 多项式

\[
 -\frac{qj'(q)}{j(q)-z}=1+\sum_{m\ge1}P_m(z)q^m,\qquad
 J_m=P_m(j)=q^{-m}+O(q),\quad c_0(J_m)=0.
\]

真正模截断为 F_(r,N)=a0(r)+Σ_(m≤N)b_m(r)J_m；普通负 Laurent 多项式不能代替。对每个 compact A⊂C，可取小0<s<R<1使 j(q)的R圈反向包围A、G(q,z)=−qj′/(j−z)在闭R盘对 z∈A全纯。令 D_(A,R)=max|G|，则 Cauchy换元给完整重构及尾

\[
 L_r(z)=a_0(r)+\sum_{m\ge1}b_m(r)P_m(z),\qquad
 \|L_r-a_0-\sum_{m\le N}b_mP_m\|_{C(A)}
 \le D_{A,R}p_{A_s}(r)\frac{(s/R)^{N+1}}{1-s/R}.
 \tag{3}
\]

fixed窗可替换 p_(A_s)为 C_(L,s)||r||du，给真正 operator tail；增厚A后也给任意固定阶导数。源窗、target height和两圈不得无声共变。若全部b_m=0，(3)使L_r常值；虚轴Fourier衰减迫常值0，唯一性给r=0。因此扣a0后的**解析**完成化仍注入全部源，尤其保全部非零Pan，不能冒称已作关系商。

上述证明和完整源核见[解析原稿](../reviews/2026-10-27/cusp-transport/fourier-kernels-and-faber-tails.md)。

## 2. 逐个整数输入的实际 native 产品

固定 M=II_(2,2)，有序群SL2(Z)×SL2(Z)，粗紧化 X=P¹_C×P¹_C、开部U=A²。先对每个整数基J_m使用[Borcherds作者稿 Theorem13.3](https://math.berkeley.edu/~reb/papers/aut/aut.pdf)，再只在divisor／Green数据复化。任意complex源或其截断不是原整输入。

令 D_m=σ1(m)，实际全isogeny norm为

\[
 R_m(j(z_1),j(z_2))=
 \prod_{ad=m}\prod_{0\le b<d}
 \left[j(z_1)-j\left((az_2+b)/d\right)\right].
 \tag{4}
\]

陪集置换、有限处全纯和cusp有限极点给R_m∈C[X,Y]；roots of unity的Galois置换及整数q三角消元给R_m∈Z[X,Y]。它对第一变量monic，bidegree(D_m,D_m)。记零除子为T_m，闭包为Tbar_m，B=B1+B2为两条无穷边界，则

\[
 Z_m=\operatorname{div}_X R_m=\overline T_m-D_mB,
 \quad T_m=\sum_{k^2\mid m}T_{m/k^2}^{\rm prim}.
 \tag{5}
\]

后式按matrix entries最大公因数分解给出，保全部非cyclic重复；m不是经典prime-power指标。

原文Problem16.5并未证明一般Hecke等变。本例逐m身份另付：原定理的负primitive vector／倍数除子与(5)相同；c0=0使weight0并在有序群上给实际unitary character，其12次方平凡。原product在q1→0、z2固定compact的chamber中有有限阶，正第一指数因子整体趋1；交换方向同理。故Ψ_m^12在generic两边界亚纯，corner余codim2由meromorphic Hartogs延拓，在P¹×P¹上为有理函数。Ψ_m^12/R_m^12在A²无零极除子，是rational unit，故常数。原unimodular cusp前因子模长1，再与monic q1^(−D_m) leading对照，给

\[
 \Psi(J_m)=C_mR_m,\quad |C_m|=1,\quad
 \rho_{m,1}=-D_m,\quad\rho_{m,2}=0,\quad
 \Phi_m=-4\log|R_m|.
 \tag{6}
\]

Weyl向量只限该chamber；不是从Example13.5的“essentially”忽略随m变化的实归一化。完整有限cusp、normal convergence及除子论证见[native原稿§2–3](../reviews/2026-10-27/cusp-transport/native-products-and-green-tail.md)。

常数输入1必须独立保留。原公式为

\[
 \Phi(F)=-4\log|\Psi(F)|-2c_0(F)
 (\log|Y_M|+\Gamma'(1)/2+\log\sqrt{2\pi}),
 \tag{7}
\]

并有c0/2权及character／line；不能把Φ0=Φ(1)替成weight0 rational log。下文全局L1/mass目标只针对**balanced**尾；a0Φ0作为带原line/metric/constant规范的固定腿保留，未用未估的Φ0 norm冒充已付目标。

## 3. 尖点边界也付款的实际全尾

fixed interior compact上的Hecke root满足log(1+|α|)≤C_Km：reduced height≤max(v,1/v)≤C_Km。holomorphic局部有限阶分解给uniform ∫log^-|j−α|≤C_K，故local ||log|R_m|||1≤C_KmD_m。

全X不能直接由local界推出。本轮另付：在固定|X|=|Y|=1 torus上，Y的reduced j-preimages在共同compact，所有Hecke roots满足同一logheight≤Cm。二维Cauchy给R_m各coeff模长≤exp(CmD_m)。对P¹的probability FS measure μ，

\[
 \log^+|R_m|\le CmD_m+2\log(D_m+1)
                   +D_m\log^+|X|+D_m\log^+|Y|.
\]

各末项可积。对每个有限Y，monic分解和dμ≤π^−1dA给∫log^-|R_m(X,Y)|dμ(X)≤D_m/2。因此

\[
 \|\log|R_m|\|_{L^1(X,\mu^2)}\le C_XmD_m.
 \tag{8}
\]

用ω=π1*ωFS+π2*ωFS，mass(Tbar_m)=2D_m、mass(B)=2，mass(Z_m)≤4D_m。给定0<s<t<1，以mD_ms^m≤C_(s,t)t^m及(1)合并，可得

\[
 \|\sum_{m>N}b_m\log|R_m|\|_{L^1_X}
 \le C_XC_{s,t}p_{A_s}(r)\frac{t^{N+1}}{1-t},
 \quad
 \operatorname{mass}(\sum_{m>N}b_m[Z_m])
 \le C'_{s,t}p_{A_s}(r)\frac{t^{N+1}}{1-t}.
 \tag{9}
\]

Tbar和boundary scalar D(r)=Σb_mD_m的尾亦绝对收敛。fixed源窗给原du→fixed globalL1／mass的operator尾，再乘相应Dlog常数；全S_exp在同p_(A_s)有界族上一致。没有cofinal算术height、跨零点log sup或smooth Green断言。

固定dd^c=(i/2π)∂bar∂，有ddc log|f|²=[div f]。定义

\[
 Z(r)=\sum_{m\ge1}b_m([\overline T_m]-D_m[B]),\qquad
 G(r)=-4\sum_{m\ge1}b_m\log|R_m|.
\]

则L1对distributional ddc连续，给

\[
 dd^cG(r)=-2Z(r). \tag{10}
\]

ordinary principal pair是(Z_m,−log|R_m|²)，native尺度为(2Z_m,Φ_m)；(Z_m,Φ_m)不是同一规范。无限输出是合法L1／mass completion，未宣称ordinary locally finite divisor、单值复幂乘积或原定理扩展到essential cusp。

## 4. 全部重复系数与 raw 可见性

真正primitive cyclic raw coefficients为

\[
 A_N(r)=\sum_{k\ge1}b_{Nk^2}(r),\qquad
 b_N(r)=\sum_{k\ge1}\mu(k)A_{Nk^2}(r).
 \tag{11}
\]

两重和由Σd(h)s^(Nh²)<∞付绝对性，不能删掉Nk² aliases。各不同primitive curves只在离散点相交，绝对mass使其measure restrictions彼此奇异，所以raw current可读到每个A_N。全A_N为零由(11)给全b_N为零，再由(3)给r=0。因此balanced raw current同样注入全部源；它同时保非零Pan与537。该结论是测量层的可见性，不是正定／有效性／primitive类非零。

## 5. 真实关系的必要费用与类商的净门

令A(u)=K0(u)=CT exp(uj)，V=A″−A/4。j=q^−1+744+Σ_(n>0)c_nq^n各c_n>0，故u≥0时

\[
 V(u)\ge(744^2-1/4)e^{744u}.
\]

对405真实noncompact p=(D²−1/4)H、H>0且H∈S_exp，全部b∈R有精确式

\[
 a_0(\tau_bp)=\int H(v)V(v+b)dv.
\]

v∈[0,1]给c_H exp(744b)，v<−b的负尾由固定q圈与H的全部线性指数矩给任意C_Nexp(−Nb)，其余正半线不减。因此所有充分大正b有a0(τ_bp)>0且≥c exp(744b)。原du／Dlog范数平移不变，故此读出没有全线统一原norm费用。这是实际必要下界，不是将(1)粗upper反向使用。各Faber截断保同一a0，N增大不能修weight腿。

同一537窗内取足够小偶φ≥0，r*=(D²−1/4)(uφ)。其双pole moments精确零、r*≠0，旧537给Qζ(r*)>0；V′(0)=CTj³−744/4>0给a0(r*)>0。这证明constant通道也读到非根，但它并未消关系。实际尾和小支撑证明见[关系原稿](../reviews/2026-10-27/cusp-transport/principal-relations-and-nonroot-test.md)。

合法扣a0不丢解析信息，却有两个不同的后续门：

* **raw函数／current记录：** 全b与A仍注入，所以全部非零Pan也非零，尚无正确下降。
* **full principal pair的连续类商：** 每个有限(2Σb_mZ_m,Σb_mΦ_m)是复化principal pair；在对本轮L1×mass topology连续、杀掉这些finite principal span的商中，(9)使整个无限像为零。于是405和537都被杀掉。它只是在指定连续完成化商中的结论，没有给一般ordinary Pic／算术Chow的未定义无限类赋值。

只保2Σb_mTbar_m时会留下2D(r)B；它是明确boundary记录，不能删去同时声称principal。按同bidegree扣掉boundary／degree line后的标准primitive pair则全principal。不同relative/higher读出、非闭／更强拓扑或另一个非零primitive载体仍合法，但须提供实际新公式、关系和费用；本轮不靠名称补出它们。

## 6. root 前件闭合与最强旧比较

| 消费项 | 本轮实际范围 |
|---|---|
| 对象／domain-range | ALLcomplex physical S_exp → actual Faber coeffs → 逐整数基原lift后复化 → fixed X的balanced L1 Green及mass current；a0Φ0单列line标签 |
| 源与增长量词 | 每fixed s<t、source窗L与fixed FS几何；强p_(A_s)或fixed窗du/Dlog；不代cofinal算术height、成长L或频高 |
| 依赖与误差 | 原Th13.3整输入／权／character／Weyl；本轮逐m身份、全coefficient-height、FS lognegative及mass证明；误差仅(3)/(9)明确几何upper，无数值代定理 |
| 系数／符号方向 | a_−m=b_m；全部A_N=Σb_(Nk²)；Φ=2g、ddcG=−2Z；任意复／signed源不保有效性，无Hermitian positivity身份 |
| 关系／physical／商 | 原map注入保Pan；raw constant大平移非零；连续principal闭商杀全部源。两者均未给同时消405并保537的primitive来源 |
| 仍欠coverage／coupling | 算术整模型、有限位原special-cycle／vertical修正、同源整过滤／section乘法／mixed RR、完整Bζ signed身份及actualq/core/coupling/Ξ |
| strongest-old净值 | 标准essential/Baire、有限rank、552高频、553旧稠密不重计；新项为实际全S_exp模系数与native全global尾／boundary／关系必要费用。542＋555→557 whole4/5UPPER未改善 |

复杂Hecke degree和固定复曲面的bidegree不是Weil所需的同源mixed预算。完整经典Γ/contact、properpowers及双pole仍属于原完整Bζ，未识别为本轮m项或删掉；537只作真实非根，非本轮新正性。全局复Green可运输这一局部设施瓶颈改变，**独立primitive容量及经典主瓶颈未改变**。

本合同一轮止该完成化principal recipe，不续N/radius/j常数/level/同product-paper。若另有具体relative公式或完整signed输入，应先按cycle16扣强旧准入；本轮完成不complete长期Goal。
