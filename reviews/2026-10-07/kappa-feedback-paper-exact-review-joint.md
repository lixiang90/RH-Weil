# κ-feedback 正式论文：有限公式、转写与下一研究动作独立审核

2026-10-07。审查者 type_ii_joint。结论：最终版论文的有限公式、
严格有理系数表、实际容量数字和证书说明全部限定 PASS，未发现待修复问题。
本报告不独立重审 plain proof 的无限分析、全族轮廓或无零结论；
这些由新论文的另两份全文审核承担。未重新运行无变化的 49 个有限模型。

## 1. 绑定的最终版本

所审 [正式论文源码](../../papers/kappa-feedback-cubic-boundary-paper.tex)
共 990 行，canonical LF SHA-256：

~~~text
16c0ba50a2917f2ead56843eabf55b62fbbe214e162cff373b4d8554f84315ee
~~~

canonical 规则为 UTF-8 文本 CRLF/CR 统一为 LF，不改其他字符。
最初收到的 978 行版本哈希为
89614f1ff57d97ddc3fdae7232e3f724699d01107fcc80db4f5ac6ca9cb60e47。
审查过程中发现的两处证书术语问题已由主审修正，最终版另明确显示
positive-slot mesh 前件；本报告绑定修订后版本。
未编辑论文、原脚本、JSON、451、math source 或已交付旧论文。

有限数学基础是
[451 exact 独立审查](451-exact-certificate-review-joint.md)，哈希
dbc565341e022e4089eb235f86c6bcbc01658e49b805ccf4934ad280bbce8cc1。
其绑定的脚本和 JSON 仍分别为
e03d6536378fff4b51625ab71fa5eace9fcbf4fe1156ccb6ae048f03bf96bc68 和
309f275701a1d96c245eb067d49b00598df4af8e380d220944de250fd2e9d7ba。
本文核对新稿实际公式，独立检查新附录和额外显示的 count 上下界；
不以旧研究稿通过替代新稿转写检查。

## 2. 根、参数与严格比较

正文的
\[
p(e)=657e^3-954e^2+21e+20,\quad
L=16683858898627/10^{14},\quad
H=16683858898628/10^{14}
\]
与已独立证明的隔离证书一致：
\(1/6<L<H<167/1000,\ p(L)>0>p(H)\)，且 \(p'<0\) 遍及该区域。
参数 \(b,\kappa_*,\sigma_*\) 的转写及
\(\kappa_*=2\sigma_*-1,\ 37/50<\kappa_*<3/4\) 正确。
从 e 的区间得到明确的严格 σ 区间
\[
\frac{262487105826029}{300000000000000}
<\sigma_*<
\frac{1049948423304119}{1200000000000000}.
\]
独立展开有
\[
p(11/3-4\sigma)
=-\frac{16}{3}(7884\sigma^3-18819\sigma^2+14643\sigma-3686),
\]
故抽象中的指定三次方程及根口径正确。

旧 \(e_0=(33+8\sqrt{921})/1653\) 确满足
\(1653e_0^2-66e_0-35=0\)，并且
\[
11/12-e_0/4=(1507-2\sqrt{921})/1653=\sigma_0.
\]
其有理隔离上端严格低于 L，所以新边界严格更小。
正文的 e、κ、b、σ 和新旧差值小数均与精确结果一致，
仅作为方向说明；没有让小数承担不等式证明。

## 3. 连续证书与 Appendix 系数逐项核对

正文将 x 改为 \(y=1/2-x\) 后的 D/P，
\(K_0,W,E_*,A,B,C,Q\) 与独立符号运算完全相同。
\(-2JE_*=A\delta^2-B\delta+C\) 是一般有理函数恒等式；
先定义 cleared polynomial，再在 \(J\ne0\) 域内转回 E 的说明准确。

一般 \(Q_0\) 的 \(b^2\) 系数、optimizer 及极大值 factor 式均逐项吻合。
\(\rho(\kappa)=3312\kappa^2-936\kappa+67\) 的 discriminant
确为 \(-11520\)，leading coefficient 正；
因此实际非零 κ 上严格凹性成立。
\(\kappa=5/6-e/2\) 的方括号为 \(-p(e)\)，
b 模 p 的化简为 \((-5181+156335e-387630e^2)/81941\)，正确。

新 Appendix 的显式系数也另用一般符号核对。设
\[
D=D_0+D_1y,\quad P=P_0+2y+2cy^2,\quad
P-D=T_0+T_1y+2cy^2,\quad W-h=-b/2-ey .
\]
直接乘法得到
\[
\begin{aligned}
A_0&=bT_0+hP_0,& A_1&=bT_1+2eT_0+2h,\\
A_2&=2bc+2eT_1+2hc,& A_3&=4ec,\\
B_0&=2K_0T_0-5bD_0/6+5hP_0/6,\\
B_1&=2K_0T_1-5bD_1/6-5eD_0/3+5h/3,\\
B_2&=4K_0c-5eD_1/3+5hc/3,\\
C_0&=-5K_0D_0/3,& C_1&=-5K_0D_1/3 .
\end{aligned}
\]
新稿全部九个系数无转写错误。
\[
Q_j=4\sum_{r+s=j}A_rC_s-\sum_{r+s=j}B_rB_s
\]
在缺项取零时，五个系数 \(Q_0,\ldots,Q_4\) 与直接展开完全相同。
JSON 的全部 A/B/C/Q 坐标已由独立 QQ remainder/inverse 重建一致。

正文 table 十个严格区间与已独立 Bernstein 证明的表完全一致：
\[
\begin{array}{c|cccc}
j&0&1&2&3\\ \hline
A_j&(47/100,48/100)&(121/100,122/100)&(86/100,87/100)&(29/100,30/100)
\end{array}
\]
\[
C_0\in(7/100,8/100),\quad C_1\in(6/100,7/100),
\]
\[
Q_1\in(4/100,5/100),\ Q_2\in(19/100,20/100),\
Q_3\in(26/100,27/100),\ Q_4\in(7/100,8/100).
\]
\(Q_0=0\) 是 exact identity。
由系数正性证明所有 \(y\ge0\) 的连续平方完成，
再利用实际 rectangle 的 \(J>0\) 得 \(E_*\le0\)，逻辑正确。
唯一等号 \(y=0,\delta_*=(5-9e)/(6+18e),R=2/3\) 正确；
\(1/3<\delta_*<7/18\) 已蕴含正文的实际 δ 区间。

## 4. Counts、strict capacities 和 plain proof 数字

新稿 D/P 与两条 count lines 的 crossing、short/long balance
和 \(t_\kappa,R_{*,\kappa}\) 均与独立结果一致。
新增的 \(J\le5/2\) 也可连续证明：
\[
D-P=1+x-2cx^2>0,\quad D\le3,\quad
J=(5/6)D-\delta(D-P)\le5/2 .
\]
在 \(1/3\le c\le50/111,\ 0\le x\le1/2\)，
D/P 的 x-derivatives 均负，所以
\[
D\ge455/222>2,\quad P\ge86/111>3/4,\quad J\ge35/48>0.
\]
实际 \(\delta\ge1/50\) 给 \(1<t_\kappa<3/2\)。

独立求导与端点计算给
\[
r_*(1)\ge8/13,\quad r_*(3/2)=1,\quad
1/3\le t-r_*(t)\le1/2.
\]
所以 \(z_M\le5/26<1/5,\ z_P\le25/333<1/5\)。
inverse 的第二 width 实际更强为
\(8\nu_0+3/13\)；正文保守写 \(8\nu_0+1/5-o(1)\) 充分。
plain width \(6\kappa\nu_0\) 及容量零区间另走原 endpoints 的口径正确。

plain proof 中新增 lower endpoint 的所有显示数字另用 Fraction 检查：
\[
s_\kappa\ge87/100,\quad
z\le25M/111,\quad \kappa z\le M/6,\quad
6\kappa-1\ge86/25,
\]
\[
z<25M/516<M/20,\quad
1/20-25/516=1/645,
\]
\[
3/2-5/6+1/10=23/30,\quad
5/2-2(5/6)+1/10=14/15.
\]
因此显示的比较 margin 为 \(1/15\)，数字正确。
最终版 Proposition 显示 \(\max_i z_i\le\eta_{\rm mesh}\)，
physical \(w_i\le2\ell_i\) 与先 mesh 后 K 的顺序相配。
本审核仅核这些有限前件；没有由这些数字单独认证整个 source induction。

## 5. Geometry、feedback 与会计转写

已付的全部 20 个 geometry 坐标和严格 margin 原样正确转写。
新稿另外显示的 middle endpoint
\[
-73/300+(13/50)e-(49/300)b
+\delta(1/6+3e/4-b/4)
\]
在 \(\delta=3/4\) 正确化为论文的 middle bound。
δ 系数严格正。floor、small、Gram、Euler-domain 和 principal m_w/m_z
数值与独立区间审核一致。
principal min 中选择的分支正确，原四个 local error exponents
在 residue 的最弱 decay 是 σ，不是另一个更强未证值。

另作一般符号核对，得到：

- \(C_b(s)=s+l_x/2-1+h/6=s-2/3-b/6\)；
- \(l_x/2+b/12=(1-e)/4-b/6=C_b(\sigma_*)\)；
- 原始 high expression 与正文 fullE 精确相等；
- outer \(B_0=l_x/2+1+l_y=7/4-3e/4+b/4\)。

whole-slot gain eq 及 conductor deficit 未在转写中重复计费。
feedback 导数、\(625/36963<1/50\)、κ_act 的实际准入和 \(2\Delta\)
费用与独立连续计算一致。
高侧 d-斜率下界 \(57/200>0\)、上界 \(<2\)，ζ 费用及
\(359\Delta/400\) 算术正确。
\(\zeta=\Delta/32\le(e-1/6)/128<1/384000\) 与
\(e/(h+\zeta)>1/5\) 保持实际供给 margin。

## 6. 附录证据说明的验收

最终版明确写 149 counted checks，其中 98 项 identity checks 在
49 个有限 points，另有 uncounted internal arithmetic assertions。
它没有把 require 计数误称为程序所有 assert 总数，
也没有把取样模型用作连续证明。

最终版明确写 source-hash 字段是 fixed metadata，
脚本不读取或 authenticate 外部 source 或 Note 451；
实际版本绑定由 independent reviews 和 build manifest 另作。
这与真实代码一致。本报告只实际绑定所审源码及上述有限证据文件；
PDF 的编译、哈希和逐页视觉 QA 由主审 manifest 承担。

## 7. 下一 proof plan 建议

边界线方面，单纯继续下调 plain lemma 的 κ 下端不会改变本稿已经使用的
reference envelope。当前 \(\kappa_*=2\sigma_*-1\) 已严格在合法区间内，
一般 optimizer 和 Q0 条件仍回到同一个三次式。
更有效的验收对象是实际临界邻域：
\[
(\delta,x)\approx(\delta_*,1/2),\qquad
q=\delta x\text{ 是全部原 physical slots 的平均}.
\]
先证明保留同一角色、witness、自然 masks 和全部 physical slots 的联合
count 在该邻域比当前 \(R_{*,\kappa}\) 有严格 exponent decrement，
或证明该邻域受到一个新的严格联合约束。
不能把 certificate 等号直接解释成坏行实际达到等号。

此计划的连续配套已有依据：actual rectangle 紧致，certificate 只有一个
等号点，且 J 正且有上下界；任何固定等号邻域外都已有严格统一 margin。
因此应先支付该邻域内的新实际算术改进，再靠连续稳定性重新选 geometry，
随后复核邻域外、strict capacities、low normalizer、Euler/principal/outer
和原 Δ→mesh→K→μ→target→height→external-tail 量词。
若新联合 count 未证明，只记录未完成，不能先改三次根宣布边界改善。

比例方面，保留原 actual frequency shell 与 joint Möbius/divisor fiber 的
研究线更有价值；下一结果必须估计 moving reciprocal-residue weights，
或真实联合 h 平均，而非再次重排 gq|h。
fixed-cell \(X^{1/2+\eps}\) 或 canonical \(X^{3\theta/2+\eps}\) 上界仍远大于
所需 raw \(o((\log X)^4)\) budget。
需在全部 divisor blocks 合并后的同一 physical response 支付
six-window、carrier、sharp masks、tails、cross-cell/alias 与共同 centering；
新 strip 改善没有提供这项四阶常数预算。
这是后续研究目标，不是本有限公式审核已经证明的新 saving。
