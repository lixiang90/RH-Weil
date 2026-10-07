# κ∈[37/50,1] 的 actual count algebra 独立复核

2026-10-07。type_ii_joint。只审 count crossing、strict widths、供给和 κ
feedback 的有限代数，不重复底层 plain proof 的无限 source 逆审。
对主报告相应有限结论给限定 PASS [T/R]；[R] 为另外已明确审查的原 marked
输入、extended plain lemma、actual physical slot/witness 合同。
本报告不认证新最优边界、整条 continuation 或外部 formal kernel。

所审 [hybrid-critical-count-witness-research.md](hybrid-critical-count-witness-research.md)
canonical LF SHA256：

~~~text
a1a6146b8f5e0b82b0e7e642e323398aece00d0a3488cce3d6f146974332dff8
~~~

## 1. crossing 和 adaptive long/short 平衡

独立从两条实际 selected count lines

\[
 A_I(r)=1-\delta\{x+(1-x)r\},\quad
 S_t(r)=1-\delta\{cx+B(t-r)\},
 \quad c=(3\kappa)^{-1},\ B=2-2cx
 \tag{1}
\]

解相等关系，系数为 D=1-x+B=3-(1+2c)x，得

\[
 r_*(t)=\frac{Bt-(1-c)x}{D}.
 \tag{2}
\]

在 t=3/2 时 r_*=1，count为1-δ；其 t-slope 为-δP/D，
P=B(1-x)。故 short envelope准确是

\[
 R_{\rm short}=1-\delta+(\delta P/D)(3/2-t).
 \tag{3}
\]

与 L(t)=1-δ+(α-δ)(t-1)、α=5/6平衡，准确给

\[
 J=(\alpha-\delta)D+\delta P,\quad
 t_*=1+\frac{\delta P}{2J},\quad
 R_*=1-\delta+\frac{(\alpha-\delta)\delta P}{2J}.
 \tag{4}
\]

对0≤δ≤3/4，α-δ≥1/12，故J严格正。
δ>0时1<t_*<3/2；δ=0时连续取t_*=1。没有额外 endpoint、容量折损
或 hidden division byδ。前述两count lines的算术/角色准入仍是明确 [R]，
不是由(1)的有限代数反过来证明。

## 2. 全域 strict widths 与 supply 的独立 sharp 常数

对37/50≤κ≤1，有1/3≤c≤50/111；0≤x≤1/2给

\[
 D\ge455/222>2,\qquad P\ge86/111>3/4.
 \tag{5}
\]

D、P在x上的最小点均为x=1/2；对应在c上的最小值是c=50/111。

在t=1，r_*=[2-(1+c)x]/[3-(1+2c)x]，
其x-derivative为(c-1)/D²<0。
在x=1/2，r_*=(3-c)/(5-2c)，c-derivative为1/(5-2c)²>0。
故准确下界r_*(1)≥8/13在c=1/3、x=1/2达到。
t-r_*(t)随t增加，其t-derivative=(1-x)/D>0；t=1时至少1/3，
t=3/2时为1/2。因此

\[
 r_*\ge8/13,\quad 1/3\le m:=t-r_*(t)\le1/2,
 \quad z_M=(1-r_*)/2\le5/26<1/5,
 \quad z_P=(1-2m)/(6\kappa)\le25/333<1/5.
 \tag{6}
\]

inverse供给相对1/5还保留1/130。
若marked取z≤z_M-ν_0，ν_0>0，则两个实际 widths准确满足

\[
 1-r-2z\ge2\nu_0,\quad
 3-2r-8z=4(1-r-2z)+(2r-1)
 \ge8\nu_0+3/13.
 \tag{7}
\]

这比主稿保守的1/5 lower term更强。plain取z≤z_P-ν_0，
给1-2m-6κz≥6κν_0。主稿 ℓ/d>1/5 的 supply 是足够前件；
它是否在新实际 detector geometry的全部d中成立需新主稿另证。
r≥1、m≥1/2和shrinking-capacity neighborhoods仍使用原 no-slot端点，
不得用(7)把不足容量强行填入positive slots。

## 3. 单调性与 feedback：没有把 reference κ 代入实际 prime 输入

令H=P/D。直接计算

\[
 \partial_cH=-2x(1-x)^2/D^2,
 \quad
 \partial_\kappa R_*=
 \frac{\delta(\alpha-\delta)^2x(1-x)^2}{3\kappa^2J^2}.
 \tag{8}
\]

因此κ降低对x>0、0<δ<α的count严格有利；x=0或δ=0无严格改进。
用J≥(α-δ)D、D≥2、δ≤3/4、
max_(0≤x≤1/2)x(1-x)²=4/27，得

\[
 0\le\partial_\kappa R_*\le625/36963<1/50.
 \tag{9}
\]

后一个strict gap是5713/1848150。所有这些检查用Fraction独立复算，
不是finite网格代替continuous derivative。

旧已证边界θ_0=(1507-2sqrt921)/1653的固定参数
barκ=2θ_0-1=(1361-4sqrt921)/1653确在(37/50,3/4)：
sqrt921<31给barκ>1237/1653>37/50；
(485/16)²<921给sqrt921>485/16，故barκ<3/4。
降低κ排除旧unique equality的结论仍需要旧连续证书确有该unique equality，
本报告不以这些有限常数另证那项几何多项式事实。

在新reference σ_*、κ_*=2σ_*-1 的反证 β_*>σ_* 中，
必须取真实κ_act=2β_*-1，故κ_act-κ_*=2Δ。
若 reference E_(σ_*,κ_*)≤0已另证，且high physical coefficient
0≤d≤h<1，则(9)给实际反馈费用小于Δ/25；
C_b(σ_*)转为C_b(β_*)准确提供-Δ，所以至少剩24Δ/25。
没有双计Δ，也没有将κ_*未经全族前件准入地用于prime界。

## 4. 验收范围

所审有限count formula、strict capacities、1/5 supply前件以及feedback桥
均通过独立代数复算。未发现该范围内错误。
不含：source plain lemma扩域的独立无限证明、新free geometry、全部
principal/outer/error rows、target-independent height orders或新无零边界。
这些前件不得通过本限定PASS省略。
