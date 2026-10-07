# 固定 balanced cell 的有限比值 Gram 基线与 canonical I–II 延拓

2026-10-07。twisted_research 独立推导。状态：§1–4 为有限公式及无条件上界
[T]；§5 为依赖明确全导子输入 [R] 的 canonical 准入延拓 [T/R]。
范围严格为下述固定 balanced 高 cell、固定 coprime 整数 mask、同一 six-window
feature 和原有限 k。没有证明全部 cells 的 joint response 或 raw o((log X)^4)。

## 1. 原物理对象与本轮比较范围

沿用238-(30)、(38)–(42)和本轮 Type-I 报告的定义。固定常数0<c<C，
令 Y=X^(3/4)、L=log X、整数D=XL+O(1)，并令

\[
 \mathcal A_Y=\{(a,b):cY\le a,b\le CY,\ (a,b)=1,\ m(a,b)\ne0\}.
 \tag{1}
\]

238的D=round(XL)与原AF实际维数d=floor(XL)均逐式适用；以下每次使用所选D
自己的精确有限核，不把两个不同维数的核视为恒等。

mask m 在各 channels 之前固定，包含原 factor/aperture 有限 interval cuts，
0<=m<=1；在 prime-power support 上等于原 distinct-base mask。本节允许任何
满足(1)的此类 bounded mask，不要求其 BV。后面的 canonical 移线另须 Type-I
报告采用的 fixed-b 有限 interval/BV 前件。

令 s_i=log(a/b)，H=L²(R/LZ,dz/L)，F_i 为238和216的原 feature，即

\[
 F_{a,b}(z)=\phi(z+\log(a/b))\phi(z)\phi(\log b-z)^2,
 \qquad \|F_i\|_H\le1.
 \tag{2}
\]

对 r=I,II,Lambda 定义

\[
 c_i^{(r)}=m(a,b)\frac{r(a)\Lambda(b)}{4\pi^2\sqrt{ab}},\qquad
 S_{r,k}=\sum_i c_i^{(r)}e^{i\tau_k s_i}F_i,
 \quad \tau_k=2\pi X+\frac{2\pi k}{L},
 \tag{3}
\]
\[
 G_{rs}=\frac1D\sum_{k=0}^{D-1}\langle S_{r,k},S_{s,k}\rangle_H,
 \qquad A_{rs}=\sum_i c_i^{(r)}\overline{c_i^{(s)}}\|F_i\|_H^2.
 \tag{4}
\]

这里 I=J=mu_{<=U}*1*Lambda_{>V}，II=Lambda-J，U=V=Y^(1/4)，
因为本 cell 的 a>V。全部 composite ghost atoms 都留在同一个 coprime mask 内；
S_Lambda=S_I+S_II 是逐 feature 的精确恒等式。没有取极限 sinc 或删除 carrier。

## 2. 约化比值间距与精确有限 k 核

coprime 的前件使 i->a/b 单射。若 a/b=c'/d' 且两对均约化，则 a=c',b=d'。
对不同 atoms，有非零整数 ad'-bc'，故

\[
 |s_i-s_j|
 =|\log(ad')-\log(bc')|
 \ge\frac{|ad'-bc'|}{\max(ad',bc')}
 \ge\frac1{C^2Y^2}=:\delta_Y.
 \tag{5}
\]

所有 s_i 属于固定长度区间 [-log(C/c),log(C/c)]，所以充分大 X 时
|s_i-s_j|<L/2。原复核的精确几何级数给

\[
 H_D(v):=\frac1D\sum_{k=0}^{D-1}e^{2\pi i k v/L},\qquad
 |H_D(v)|\le\min\left(1,\frac1{D|\sin(\pi v/L)|}\right)
 \le\min\left(1,\frac{C_0}{X|v|}\right).
 \tag{6}
\]

对 v=0 使用1。原 carrier e^(2 pi i Xv)模为1；对精确 cosine 核取实部不增加此界。
D=XL+O(1)和 sin(pi v/L)>=2|v|/L使 C_0 为固定常数。没有变更所选原频率数或 grid。

把 s_i 排序。第 j 个近邻距固定 s_i 至少 j delta_Y（左右最多各一个）。
atom 数 n<=C_1Y²，故

\[
 \sup_i\sum_j |H_D(s_i-s_j)|
 \le 1+2\sum_{j=1}^{n}\min\left(1,\frac{C_0}{Xj\delta_Y}\right)
 \ll_{c,C}1+\frac{Y^2}{X}\log(2Y)=:B_{X,Y}.
 \tag{7}
\]

该有限 harmonic sum 是独立直接证明，不依赖任何零自由输入或 prime-pair 渐近。

## 3. 保留 features 的 Schur 付款

展开(4)，令 v_i=|c_i^(r)| ||F_i||。Cauchy 给
|<F_i,F_j>|<=||F_i||||F_j||，再用(7)和2v_i v_j<=v_i²+v_j²，可得

\[
 0\le G_{rr}\le B_{X,Y}\sum_i|c_i^{(r)}|^2\|F_i\|_H^2
 =B_{X,Y} A_{rr}.
 \tag{8}
\]

这是同一 finite-k 和 Hilbert-valued synthesis 的充分上界，没有把 features
当成互相正交，也没有漏重复 rationals：唯一性恰由两侧 coprime mask 保证。

Dirichlet convolution 的绝对值给

\[
 |J(n)|\le\sum_{r\mid n}\sum_{v\mid n/r}\Lambda(v)
 =\sum_{r\mid n}\log(n/r)\le d(n)\log n,
 \quad |II(n)|\le(d(n)+1)\log n.
 \tag{9}
\]

用 d(n)<<_eps n^eps 及 sum_(b~Y) Lambda(b)²/b<<log²(2Y)，对每个
r=I,II,Lambda 都有 A_rr<<_eps X^eps。这里 eps 可先减小后重新命名。
Hilbert 空间 H^D 上的 Cauchy 和同原子 Cauchy 分别给

\[
 |G_{rs}|\le\sqrt{G_{rr}G_{ss}},\qquad
 |A_{rs}|\le\sqrt{A_{rr}A_{ss}}.
 \tag{10}
\]

所以本固定 balanced cell 上，无条件地

\[
 \boxed{|G_{rs}|+|G_{rs}-A_{rs}|\ll_\epsilon X^{1/2+\epsilon},
 \qquad r,s\in\{I,II,\Lambda\}.}
 \tag{11}
\]

它包含 I–II mixed；也保留同 atom reference 的扣除。仍有 power 级预算，不能
用(11)独立相加获得 raw o(L^4)。共同 shell centering 含另一项 linear mass
projection，也不能从(11)不加账本地认定每个 centered channel entry 同界。

## 4. 与 Type-I contour 界的准确比较

本轮 Type-I 报告证明 G_(I,I)<<X^(21/16+eps)，相对于最粗
coefficient l1 平方预算 X^(3/2+eps)改善3/16。这一比较本身正确，但(11)更强。
因此该 contour 结果不应表述成此固定 cell 的最佳 Gram 预算或新的算术幂 saving。
其有用内容是 canonical J 的实际 natural-mask 准入、uniform U/V/q/height、
sharp prefix、真实 ghost double pole 和 high-height 峰的完整付款。

本结论没有否定238的“full-band Bessel不是必要条件”反例。(8)是一个粗充分界，
没有声称它必要、无损或足以 closure；其 X^(1/2)费用正显示它仍远离目标。

范围不能扩大：若删 coprime mask，会有相同比值的重复 pairs，应先合并其
Hilbert feature/coefficient，不能仍用(5)单射。若跨全部 cells 的 log-ratio 跨度
达到 L，则 v/L 可接近非零整数而发生原 grid 的 alias；本固定 O(1)区间
论证不提供 global all-cells 界。

## 5. 在同一 mask 中升级 canonical I–II，但不重复使用 b 的相消

现假定所涉 primitive Dirichlet 全导子 family 在 Re s>theta 无零，并有原
source1531–1620/global reciprocal、deleted-Euler logarithmic control [R]。
固定 theta<sigma<1，fixed gap 先于 X、b、U、V、k。

对固定 b，full Lambda 的 natural zero extension chi_b(a)=1_(a,b)=1
有 generating function D_b(s)=-L_b'(s)/L_b(s)。在 Type-I 同一 shifted Perron
合同内，其 sharp normalized prefix 为

\[
 \sum_{n\le x}\frac{\Lambda(n)\chi_b(n)}{\sqrt n}n^{i\tau}
 =\mathbf1_{\rm principal}\frac{x^{1/2+i\tau}}{1/2+i\tau}
 +O_{\sigma-\theta,\epsilon}(Y^{\sigma-1/2}X^\epsilon),
 \quad x\asymp Y,\ \tau\asymp X.
 \tag{12}
\]

删除 Euler factors 不改变 D_b 在s=1的留数1。此处是 full Lambda 的 simple pole，
不是 J 的 ghost double pole。固定 b 的实际 Hilbert BV/finite interval cuts，
以及原 denominator sum_(b~Y) Lambda(b)/sqrt b<<sqrt Y，遂给

\[
 \|S_{\Lambda,k}\|_H+\|S_{I,k}\|_H
 \ll Y^\sigma X^\epsilon+(Y/X)\log^{C_2}(2X).
 \tag{13}
\]

两项在对 b 取绝对值之前，各自独立完成其 canonical a-prefix 估计。
随后只用精确 S_II=S_Lambda-S_I，得到同样的 S_II 上界，故

\[
 \boxed{|G_{I,II}|+G_{II,II}\ll_\epsilon X^{3\theta/2+\epsilon}.}
 \tag{14}
\]

任意小 eps 吸收 sigma-theta、height/conductor 小幂和 logs；所有固定多项式
范围及 gap 常数先确定。没有将已经依赖 b 的 a-error 再解释成 b 的
canonical sequence；没有对 determinant fiber 的第二个 prime form 施加独立 PNT。

若使用已提交69999论文明确假定的 package R，theta1=69999/80000，(14)指数为

\[
 \frac{3\theta_1}{2}=\frac{209997}{160000}=1.31248125.
 \tag{15}
\]

若另引用447自己的 R 前件和完成的条件 continuation，theta_c=7/8-t_c/4，
指数为21/16-3t_c/8；不是从69999论文自动得到critical theorem。
这些 canonical 指数均比(11)弱。它们量化了此单因素移线接口对 strip 的依赖，
不证明“无零边界对所有联合相关估计均无作用”。

## 6. 可保存的成果和仍需支付的算术接口

可以保存：真实 canonical convolution 准入及 ghost 费用；低 Lambda 实际
full-compression 的四范数小量；此固定 cell 的有限比值 Gram 基线；以及
在同 mask、同 finite k 中合法但较弱的 conditional mixed 延拓。

仍需支付：原238 physical vector上的 G-A净相消、239共同 shell centering后的
determinant/prime-pair signed average、跨 cells 与 alias账本。不能把(11)或(14)
分别相加接入四矩常数，也没有从平均零点比例推出无孤立零。

本推导仅新增本文件，不编辑旧notes/math，不运行构建或Git。相关原版本及全报告
最终哈希由本轮 `type-i-and-low-lambda-full-response-review.md` 统一绑定。
