# 原 prime 四词的双侧 height 逃逸：无需 full-fourth 的频带稳定性

2026-10-07。作者 twisted_research。状态：完整新稳定性证明，待独立全文审查。
只新增本文件，不改之前 physical13、finite-band桥、low4稿、旧notes/
论文/脚本/output/math/Git。

本次把单侧 `sqrt d/T` 的粗费用改为真正的双侧 `T^{-2}`，证明原载波附近
频带截断对**任何一个 prime 四词**的 finite trace与 physical trace均稳定。
全 genuine-prime fourth的 normalized费用为 `O(X^{-1}L^{-5})=o(1)`。
不需要 [R]、whole fourth有界或新 prime cancellation。原内部 P 的删除
仍是另一个问题，不能由此自动完成31、distinct22或高 all-distinct项。

## 1. 原 packet、原 P 与辅助频带

沿 [原13/31模型](hybrid-one-three-mixed-prime-sector-research.md)，
canonical LF SHA256 `5db2c614ab9d009a15a70f4e0639b95df2d59a6b56bd752216537fcf71e2b405`。
之前 [finite-band桥](hybrid-one-three-finite-band-admission-research.md)
SHA256 `bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f`
的单侧证明保持原样；本报告另证更强的双侧结论，不更新其已绑定源。

\[
 X=T/(2\pi),\quad L=\log X,\quad d=\lfloor XL\rfloor,
 \quad\tau_k=T+2\pi k/L\in[T,2T),\quad I=[-L/2,L/2].      \tag{1}
\]

E的columns为 `L^{-1/2}1_I exp(i tau_k u)`，`P=EE*` 是原interval
zero-extension finite-carrier projection。令unitary Fourier为 mathscr F，
原 phi及phi²的二阶导数 L¹ uniformly bounded，0<=phi<=1、support I。
`hat`仍表示 nonunitary integral transform。

\[
 V=\mathscr F M_\phi E,\qquad
 K=\mathscr F M_{\phi^2}\mathscr F^{-1},\qquad
 J=[T/2,3T],\quad J_0=[9T/10,21T/10].                     \tag{2}
\]

V columns是 `(2pi L)^{-1/2}hat phi(t-tau_k)`；K kernel是
`(2pi)^{-1}hat(phi²)(t-s)`。P未变成全局 Fourier band，也不要求它
与频率 multiplier交换。J、J0仅为此证明辅助频带。

对range R的真实genuine-prime乘子，置

\[
 D_R(t)=-\frac1{a_LL}\sum_{p\in R}\frac{\log p}{\sqrt p}
            (p^{it}+p^{-it}),\quad
 B_R=M_\phi\mathscr F^{-1}M_{D_R}\mathscr F M_\phi,
 \quad C_R=E^*B_RE.                                      \tag{3}
\]

定义 `D_R^g=D_R1_J`、`D_R^b=D_R1_Jc`，Bg、Cg相应替换。
所有raw/good/bad multiplier的 op至多 `m_R=||D_R||_infty`。
这里只用全高度 absolute bound。若 R全部p<=X，`m_R<<sqrt X/L`；
high/low分开则 `m_H<<sqrt X/L`、`m_L<<X^{1/4}/L`。

## 2. 两端 packet 尾与单矩阵 traceclass

C² Fourier尾及原 E normalization给

\[
 \|V\|\le1,\quad\|V\|_2\le\sqrt d,
 \quad\|\mathbf1_{J^c}V\|_2+\|\mathbf1_{J_0^c}V\|_2\ll T^{-1}.
                                                               \tag{4}
\]

确切平方计算是 `(d/L) int_|v|>=cT |hat phi(v)|²dv<< (d/L)T^{-3}`，
而 d/L~T，所以为 `O(T^{-2})`。不把每列norm误当未归一化。

\[
 C_R-C_R^g=V^*D_R^bV
  =(\mathbf1_{J^c}V)^*D_R^b(\mathbf1_{J^c}V),
 \quad\|C_R-C_R^g\|_1\ll m_R/T^2.                       \tag{5}
\]

这是 traceclass界，不只是 `m_R/T` 的HS界。Dbad为signed或complex时，
`||A* D A||_1<=||D||||A||_2²`仍成立，无需正性。
对有序R1,...,R4，逐因子 raw/good telescoping、其余 compressed factors
op<=m_R，得到

\[
 \left\|C_{R_1}\cdots C_{R_4}
       -C_{R_1}^g\cdots C_{R_4}^g\right\|_1
 \ll T^{-2}\prod_{i=1}^4m_{R_i}.                          \tag{6}
\]

因此其 trace差同界，不依赖未知四迹大小。

## 3. 任意短链逃逸的实际 HS bound

固定eta=1/100。将K按 convolution difference拆分为near/far：
near取 `|t-s|<=eta T`，far取其余。C²尾给

\[
 \|K_{\rm far}\|\ll T^{-1},\quad\|K_{\rm near}\|\le2,
 \quad\|K_{\rm far}\mathbf1_{J'}\|_2\ll T^{-1}            \tag{7}
\]

对任何长度O(T)的interval J'一致；最后界为
`|J'| int_|v|>etaT |hat(phi²)(v)|²dv/(2pi)²<<T^{-2}`。
Knear支持传播每步至多etaT。这里单用 far op而乘sqrt d会损失新结论。

令mathcal A为至多三个K及若干bounded frequency multipliers M_i组成的
交替链，起点为V。各 multipliers只改变值，不改变频率支持。则

\[
 \boxed{\|\mathbf1_{J^c}\mathcal A V\|_2
       \ll T^{-1}\prod_i\|M_i\|.}                        \tag{8}
\]

证明逐步保留原 operators：先把V分为 `1_J0 V`及其HS尾。
尾项用 (4)与bounded链付同型界。对 `1_J0 V` 展开至多三个K。
all-near词的support位于 `J0+[-3etaT,3etaT] subset J`，所以其 escape
准确为零，不是假定 small op。
其余词取从右数第一个far。它之前的near链仍在一个长度O(T)的interval
J'，op至多固定2的幂乘相应multiplier norms。用 (7)的HS；其之后的
operators取各自bounded op。因此每词为 (8)，有限词数吸入固定常数。

该证明允许每个M_i任取raw/good multipliers，允许使用其adjoints；
complex conjugate multiplier仍保同一norm与支持传播。r=0时就是 (4)。
不引用canonical height主区估计，也没有去掉任意principal/ghost峰。

## 4. Physical四词的双侧guard，含正确左伴随

原物理四词的准确frequency形式为

\[
 E^*B_{R_1}B_{R_2}B_{R_3}B_{R_4}E
   =V^*D_{R_1}K D_{R_2}K D_{R_3}K D_{R_4}V.              \tag{9}
\]

raw/good difference逐因子telescoping，每项只有一个Dbad，其左prefix
取good、右suffix取raw（其他约定亦同界）。对第i项写

\[
 V^*\mathcal L_i D_{R_i}^b\mathcal R_i V
   =G_{\rm left}^*D_{R_i}^bG_{\rm right},\qquad
 G_{\rm left}=\mathcal L_i^*V,\quad
 G_{\rm right}=\mathcal R_iV.                             \tag{10}
\]

左G必须用prefix的 **adjoint与reverse order**，不能把L_i V直接当左链。
它含i−1个K，右G含4−i个K；两侧均至多三个。端点 i=1或4的空链也由
(4)覆盖。Dbad在Jc，故两侧可准确guard为 `1_Jc G_left/right`。
(8)分别给

\[
 \|\mathbf1_{J^c}G_{\rm left}\|_2
 \ll T^{-1}\prod_{j<i}m_{R_j},\quad
 \|\mathbf1_{J^c}G_{\rm right}\|_2
 \ll T^{-1}\prod_{j>i}m_{R_j}.                            \tag{11}
\]

两个HS的order与同一个T完全一致。于是Schatten HS–HS给

\[
 \|G_{\rm left}^*D_{R_i}^bG_{\rm right}\|_1
 \ll T^{-2}\prod_{j=1}^4m_{R_j}.                          \tag{12}
\]

有限四项相加，得到physical压缩word矩阵的traceclass稳定性（因此trace
也稳定）：

\[
 \boxed{\left\|E^*(B_{R_1}\cdots B_{R_4}
        -B_{R_1}^g\cdots B_{R_4}^g)E\right\|_1
        \ll T^{-2}\prod_{i=1}^4m_{R_i}.}                 \tag{13}
\]

不能将一侧escape与另一侧的sqrt d packet恢复成旧粗界；(11)两侧都是
outside-J escape。无需循环physical trace或假称P与D1_J交换。

## 5. 全 genuine-prime第四迹及mixed sectors

取全部genuine primesp<=X的B、C、Bg、Cg。`m_all<<sqrt X/L`，
故由 (6)、(13)，两种fourth trace（finite与physical分别）原/good差满足

\[
 |\operatorname{Tr}C^4-\operatorname{Tr}(C^g)^4|
 +|\operatorname{Tr}(E^*B^4E)-\operatorname{Tr}(E^*(B^g)^4E)|
 \ll m_{\rm all}^4/T^2\ll L^{-4}.                       \tag{14}
\]

Normalized为 `O(X^{-1}L^{-5})=o(1)`。13、22、31各个有序fourword
也按其真实product m_R获得 (6)、(13)；不靠whole F先有界。
所有threshold随原T/X、sharp prime cut及finite floor保留。

本结果只比较 raw与高heightband的两个**同类型对象**：原actual与band
actual，原physical与bandphysical。它不比较actual与physical。
原内部P crossing另须付款；good/globalop若用canonicalinput则仍要其[R]，
其31的two-crossing envelope目前仍有正幂。双侧尾界没有自动提供该budget。

此处未做时间padding、proper-power replacement、background/gamma替换，
也未以全heightprime envelope当作净arithmetic saving。它是新的明确稳定性
接口，无新无零边界、比例常数或RH claim。等待对 (8)、(10)及source
normalization的独立全文复核。
