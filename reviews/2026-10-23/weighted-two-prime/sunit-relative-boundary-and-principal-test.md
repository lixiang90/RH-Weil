# 双 prime 算术衰减、真实 S-unit 边界与 frame 共轭方向

2026-10-23；581分支原证明。接580，固定物理源 r=e^{u/2}f、全部 complex S_exp、原 du 与 zero-extension Dlog。本文不写 STATE／cadence；root 独立消费后才构成结论。主要新增是实际 rational-orbit 的完整 imaginary-axis 预算、两种 frame 共轭不可互换的公式，以及有完整原费的 routing／反向共轭 Koszul 计算。它们仍未构造成功的 arithmetic primitive source。

## 1. 算术数据与高度：不以 Q／零点选择

固定 k=Q(sqrt(-7))、p=2、q=11。两者都 split：-7 mod11=4；2的分裂由 O_k 的判别式 -7≡1 mod8 给出。其 local quadratic character 为1，native Haar／Gaussian φ_* 的 norm ν 和 finite μ 不改。置

\[
 x_n=2^j11^k,\quad a_n=2\log x_n,
 \quad e_n=2^j11^k1_{2^jO_2}\otimes1_{11^kO_{11}},
 \quad n=(j,k)\in\mathbb Z^2.
 \tag{1}
\]

其余 finite legs 固定。全部 e_n 都是实际 Bruhat-Schwartz；负下标不因此得到580之外的算术循环定理。normalized finite Gram 为

\[
 G_{n,m}=2^{-|j-j'|}11^{-|k-k'|},\qquad
 \frac5{18}\|z\|_2^2\le\|\textstyle\sum z_ne_n\|^2/\mu
 \le\frac{18}5\|z\|_2^2.\tag{2}
\]

用有限 S-divisor 的总变差定义

\[
 \mathfrak h_S(x_n)=2^{|j|}11^{|k|}
 =\{N(\mathfrak n(x_n))N(\mathfrak d(x_n))\}^{1/2},
 \quad w_n=\mathfrak h_S(x_n)^{-2}=\alpha^{|j|}\beta^{|k|},
 \quad\alpha=\tfrac14,\ \beta=\tfrac1{121}.\tag{3}
\]

这里 n,d 为 K 上互素的分子／分母理想。这是预先固定、对 x↦x^{-1} 对称的算术 divisor 预算；不是通常 rational projective Weil height max(numerator,denominator) 的误记。指数2不拟合源、Q或零点，也没有声称算术结构唯一强制这个指数。

采样仍为580实际Gaussian投影

\[
 c_n(r)=\int r(u)\operatorname{sech}((u-a_n)/2)du,
 \qquad z_n(r)=w_nc_n(r),\qquad |c_n(r)|\le2\|r\|_{du}.\tag{4}
\]

下述精确求和有实际原源费用：

\[
 S_0=\sum_nw_n=\frac{61}{36},\qquad
 S_1=\sum_n(|j|+|k|)w_n=\frac{805}{864}.
 \tag{5}
\]

故 z∈ell1∩ell2，原 Dlog 的 L2 部分也付此费。权不改变每个 c_n 的零集，dense a_n 因 log2/log11 irrational 而给全 S_exp 注入；此注入并非强完成／cycle定理。

## 2. 真实 rational orbit：完整 s、两条常数腿与 Γ 一起协同

设 ω 为同一 adelic Weil representation，D_aφ(x)=e^{a/2}φ(e^{a/2}x)。实际 global rational m(x_n^{-1}) 的全部 local legs 是

\[
 \Omega_n=\omega(m(x_n^{-1}))\Phi_*
       =D_{-a_n}\phi_*\otimes e_n\otimes\text{其余 native legs}.
 \tag{6}
\]

这是 Gaussian 与 finite lattice 同时变化；只移动 finite leg 不是(6)。全局 character／Haar 的乘积公式已包含，p,q split 没有额外符号。规范 section 定义参照[KRY1999 §§1–4作者版](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)；以下是由其 right translation 和 automorphy 定义直接核出的特例，不引用一般 finite Schwartz cycle 定理。

固定原完整 Φ_0(g,s)，采用 **全 s transported section**

\[
 \Phi_n^{tr}(g,s)=\Phi_0(gm(x_n^{-1}),s),\quad
 E_n^{*,tr}(g,s)=E_0^*(gm(x_n^{-1}),s).\tag{7}
\]

在 s0 的初值恰为 λΩ_n。令 g_v=m(sqrt v)，则 g_v 与 rational m(x_n^{-1}) 交换；左 automorphy 因此精确给

\[
 E_n^{*,tr}(g_v,s)=E_0^*(g_v,s)\quad\text{全部 }s.
 \tag{8}
\]

没有宣称一般 τ 上相同。事实上右 rational diagonal 对 real-part 的作用还在；本结论仅作用于这里实际 Mellin 预算所在的 imaginary axis。

两条 constant legs 也相同：在 N(Q)\\N(A) 的 constant-term 积分中，以 b↦x_n^2b 换元，rational 模长为1，g_v 又可交换，所以 constant term 仍是原 constant。其导数、finite first jets、arch Γ／FP／contact 都随(7)保留。若改用各局部 standard extension，须另加580型明确 δ，其一阶 jet 为 local log-Iwasawa cocycle 的和；同 s0 初值不允许删掉它。

对有限 A⊂Z²，取实际源 V_A(r)=Σ_{n∈A}z_n(r)Ω_n。由(8)，在同一 native v^{-1/2} 读出及两腿 constant subtraction 下，完成化导数／Mellin 预算是

\[
 E^{*,tr}_{V_A}(g_v,s)=C_A(r)E_0^*(g_v,s),\quad
 \mathscr M_{V_A}(z)=C_A(r)\mathscr M_0(z),\quad
 C_A=\sum_{n\in A}z_n,
 \tag{9}
\]

\[
 \mathscr M_0(z)=\Lambda_0(z)\Lambda_\chi(z)
 [\log7+\Lambda'_\chi/\Lambda_\chi-\Lambda'_0/\Lambda_0].
 \tag{10}
\]

因为Σ|z_n|有限，(9)的输出在任意先固定的 v,s compact（避开 poles）一致趋 C_w(r)E_0^*，全部导数亦精确成立；这只定义**输出**的极限，不将无限输入冒称原 Schwartz。全部 Γ、prime powers、poles 未删，但完整预算重新变成一个 scalar

\[
 C_w(r)=\sum_nw_nc_n(r),\qquad
 |C_w(r)|\le\frac{61}{18}\|r\|_{du}.\tag{11}
\]

这是真实协同而非任意 B 因子；它没有从(10) signed 差商独立提取 classical Qζ。

## 3. 405 与 537：预算 scalar 不成为 primitive

405取真实 P=(D²−1/4)H、H>0、H∈S_exp，并保全部平移。580已核出的 exact identity 是

\[
 c_n(\tau_bP)=-\tfrac12\int H(v)
 \operatorname{sech}^3((v+b-a_n)/2)dv<0.
 \tag{12}
\]

由于每个 w_n>0，C_w(τ_bP)<0，absolute 收敛由(11)支付。因此实际 full-s rational 协同预算仍不能把全405认作 principal。

若只以(9)的完整 Mellin／degree scalar 作最终载体，还有不读 Q 选取的537非根。置

\[
 K_w(u)=\sum_nw_n\operatorname{sech}((u-a_n)/2).
\]

它为正、偶（n↔−n）且 smooth；导数在实线一致绝对收敛。任选非零奇 ψ∈Cc∞((-17/16,17/16))，令 r_*=(D²−1/4)ψ。则 r_*≠0，双pole矩0，而 C_w(r_*)=∫r_*K_w=0；537给完整 Qζ(r_*)≥2^{-49162}||r_*||²>0。全 weighted family 本身仍注入；丢失发生在该真实 imaginary-axis budget readout，二者不可混写。

## 4. 真实边界的方向，以及可付 routing 后留下的 charge

令 T_pδ_n=δ_{n+e_p}，物理向量系数为 z，V=Σz_nΩ_n。真实 rational unitary 的作用为 U_pΩ_n=Ω_{n+e_p}，故在 **物理 z 坐标** 上真实 group difference 是 I−T_p（q同理）。若改用衰减 frame E_n=w_nΩ_n、坐标 c，则它变为

\[
 \partial^{frame}_p=M_w^{-1}(I-T_p)M_w,
 \quad\text{不是 }M_w(I-T_p)M_w^{-1}.
 \tag{13}
\]

Mw 对 ell2(w²)→ell2 是等距；把 c 偷放无权ell2 会改变对象与范数。算术高度不是 unitary character，不允许把 frame 变换当作新 arithmetic principal identity。

在保 constant／theta readout 的 ell1物理系数域，真实 incidence 的 charge 是 Σz_n。对本实际 z=w c，沿每个 n 到原点的两段整格路径逐项 routing，得到显式 edge chain b=(b_p,b_q)，使

\[
 (I-T_p)b_p+(I-T_q)b_q=z-C_w(r)\delta_{0,0},\qquad
 \|b_p\|_1+\|b_q\|_1
 \le\sum_n(|j|+|k|)|z_n|
 \le\frac{805}{432}\|r\|_{du}.
 \tag{14}
\]

有限截断先成立，绝对第一矩给完整链与边界极限；没有未付 finite-height 尾项藏在(14)。故这条具体 routing 能付除了 C_wδ00 的全部系数 primitive，但由(12)该剩余 charge 对每个405平移严格非零。若直接把 δ00 再手添为 boundary，则所有 z 都成为 boundary，537亦全失；不是成功的源商。

这里 charge 不是全 ell2 的连续泛函；在 ell2 取 Hausdorff coinvariants 会把它丢失。那种完成不能与(8)的非零 E／theta readout混用，正如580 point0反测所示。

## 5. 反向共轭的明确有界右逆与 Koszul：合法解析修复会全吞

为了核尽“衰减以后再平移标签”的最便宜修复，另定义

\[
 B_p=M_w(I-T_p)M_w^{-1},\qquad B_q=M_w(I-T_q)M_w^{-1}.
 \tag{15}
\]

这是实际有界解析算子，但由(13)它是**额外 renormalized incidence**，尚非 arithmetic principal 边界。其两个方向 commute，frame cocycle 在每个 plaquette 相消；此零曲率不生成 RR／交数。

对任意物理 z∈ell2(Z²)，固定 k，定义

\[
 (R_pz)_{0,k}=0,\quad
 (R_pz)_{j,k}=\sum_{m=1}^j\alpha^{j-m}z_{m,k}\ (j\ge1),
\]
\[
 (R_pz)_{j,k}=-\sum_{m=j+1}^{0}\alpha^{m-j}z_{m,k}\ (j\le-1).
 \tag{16}
\]

直接代入给 B_pR_p=I。正半轴／负半轴 convolution 的 kernels l1 norm 分别为1/(1−α)、α/(1−α)，源与输出两半分开，故

\[
 \|R_pz\|_{ell2}\le\frac43\|z\|_{ell2},\qquad
 \|R_pz\|_{finite\ Gram}\le\frac{24}{5}
                  \|z\|_{finite\ Gram}.\tag{17}
\]

后者由(2)的 sqrt(condition)=18/5 支付全部 mixed norm。全 Ω_n 的 Gram 另乘 arch correlation sech((a_n−a_m)/2)，Schur product 正性保同样上下界，所以(17)亦可用于 full orbit Hilbert norm。ν／μ原常数并未重标。

因此(15)不是“费用也许发散所以不知”：它有实际原费用可付的 primitive，却把全部 H0 源吞掉。两方向的 Koszul

\[
 0\longrightarrow\mathcal H\xrightarrow{t\mapsto(-B_qt,B_pt)}
 \mathcal H^2\xrightarrow{(y,z)\mapsto B_py+B_qz}\mathcal H
 \longrightarrow0
 \tag{18}
\]

准确满足 H0=H1=0、H2=span{w}。证明：Bp surj；ker Bp={α^{|j|}h_k}，在此核上 Bq 仍 surj且核为 span w。或若 Bpy+Bqz=0，先取t=Rpz，再以ker Bp中的Rq修正 y+Bqt，得到所有1-cycle为2-boundary。唯一 H2 只是预先给定的正权；在 coefficient ell2 orthogonal projection 下的源系数为 Σw²c/Σw²，(12)仍非零且只是 scalar，不给全源 primitive。该 coefficient projection 不冒称非正交实际Gram的orthogonal projection；任何fixed linear投影到这同一一维H2仍只有一个scalar。选取它不等于实际物理源到同对象二次容量。

对405，反向共轭的 formal algebraic charge Σz/w=Σc 确实发散：每个 j 选 k 最近于−j log2/log11，a_n落在固定 compact，(12)在该 compact 上≤−δ_b；对|j|≤N有2N+1点，所以 partial charge≤−(2N+1)δ_b。**这不否定(16)的合法 ell2 primitive**；它说明该 primitive 穿过原无衰减 charge 的强域。不能用“charge发散”否认付过费的解析修复，也不能将此解析修复偷称 arithmetic boundary。

## 6. 常数 S-unit 的真实 principal divisor 不是特殊循环的 level edge

先钉住输入域：fixed-arch J_w(r)=φ_*⊗Σz_ne_n 与(6)的 V_w(r)=Σz_nΩ_n 是不同对象。σ2的finite point0绝对费不能自动支付后者的arch Schwartz半范数。在finite origin，两处finite因子 d=x_n 与D_{-a_n}振幅d^{-1}恰相消，故 V_w(r)(y,0,0)为 Σ_nw_nc_n(r)φ_*(y/x_n)。对非负非零compact r，固定k0、j→+∞时 c_{j,0}(r)~2μ_+(r)2^{-j}，取y=2^j后该单项为常数倍2^{-3j}，全部项同号。所以这条实际arch函数至少有固定幂次尾，不是Schwartz；Gaussian正性使这里不存在藏掉lower bound的mixed抵消。此反测仅针对该非负源与该补偿orbit sum，不排更快算术权／源适应抵消／付费不同完成。即使(9)输出极限完备，也不能反推原域与cycle已扩展。

在CM算术base上，常数 x_n=2^j11^k 确有 principal Arakelov divisor：finite 部分只支撑2、11，arch correction 的总量−2log|x_n|，由乘积公式 degree0。这个真实 principal 身份并不产生 e_0−e_{1,0} 的特殊循环身份。

直接在 n=1 检验：580实际 split 可除性给 Z_{0,0}(1)=Z(1)、Z_{1,0}(1)=0，前者为 char7 的非零cycle、degree2log7。任何常数 S-unit divisor 的 finite support 都在2、11，不能以 arch constant 抹去这个 char7 分量。因此最便宜的 principal S-unit divisor 不实现所需 level-cycle edge。需要新的实际 isogeny／modular-function／relative transgression，给同一模型全部 finite 与 arch divisor；finite containment或手添格边均未提供它。

负level算术cycle、full infinite Ω 的 Green／cycle延拓、一般 source-dependent 变复形／额外原源边界在本文均 open，不由上述 support 反测排除。

## 7. 连续与函数域对照；净结果

continuous d=±1/16 的同一 odd compact源，在native完整Weil型异号，但(1)–(5)局部体积／权／Gram与其分布参数无关。(17)的 positive Hilbert预算不能因此支付 signed complete Weil型；未构造 continuous→CM 比较，故不把continuous反例冒称反驳所有KRY几何。

函数域的真实 principal 函数有**同一曲线全部places**的零极点和，不是手添格 incidence；primitive 双degree扣除后，C×C的混合交数／RR／实际截面乘法给正号。580已付完整Frobenius returns／aliases及H0,H2 poles。上述(18)的H2一维权向量既不依点数，也不是该 primitive Hodge；(10)仍是 signed KRY差商，不是同对象Weil二次型。

新可消费输入：固定算术divisor衰减的完整norm／first-moment routing；真实 rational-orbit imaginary-axis 全s与两条constant腿预算；frame conjugation方向；反向修复的明确有界 primitive、完整Koszul同调与537失守；常数S-unit principal support反测。它们不改善strong-old542+555→557 whole4/5负惯性UPPER，不付独立Weil正性／实际q费／成长core／Xi。

本具体边界入口停止：真实weighted rational读出仍留非零Pan charge；额外反向conjugate incidence则全吞非根。下一可准入的独立输入必须给不同于这些标签平移的实际relative／regulator公式，读取额外原源并支付原Schwartz域、完整finite／arch／constant尾费、405 principal与537 coverage；然后才是同一整模型的mixed RR／quadratic capacity。不能仅以完整Q拉回新完成、以零点坐标或已知源商定义边界。
