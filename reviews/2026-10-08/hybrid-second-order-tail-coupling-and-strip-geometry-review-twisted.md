# 二阶可加谱尾与固定条带几何的独立全文审查

2026-10-08，twisted_research。结论：**限定 PASS**。
独立FULL READ最终292行，逐式复算有限谱槽位、计数消元、效果对偶、
κ₂恢复与实际low/row方向；实读197、304相关证明及AF v2原PDF
pp.4–7的归一化、列范数、trace/tail proof。不改被审稿或冻结材料。

## 1. 最终绑定

被审文件：
[hybrid-second-order-tail-coupling-and-strip-geometry-research-compression.md](hybrid-second-order-tail-coupling-and-strip-geometry-research-compression.md)。
canonical UTF-8 LF SHA-256：
`e5c21e3a8bb0cb52e9e3131259a52dbb42051d7eb514ca8a65b083128b88d444`；
14464 bytes，292行。规范化仅CRLF/lone CR→LF，不trim。

七个输入链接/绑定逐个重算相符。AF PDF按原始bytes计算，
`6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444`；
其余Markdown按canonical LF。使用197/304已有账本与mixed cubic的
准确域，未引入全Weil正性或未付fourth upper。

## 2. 有限谱槽位与可加性

置F(t)=4t−t²。正文κ₂给

\[
 F(t)+\kappa_2(t)=
 \begin{cases}0,&t<0,\\4t-t^2,&0\le t\le2,\\4,&t>2.\end{cases}
\tag{1}
\]

故前b个谱槽位均≤4；之后Weyl/minimax的λ_{i+b}(A)≤p_i
对P≥0、n_+(Q)≤b成立，不要求Q≥0。λ≤p的槽位上，(1)至多
φ(p)=2p+1−j(p)。超过s的p_i=0，于是相应槽位值为0。
连Gram的zero eigenvalues一并保留，Σφ(p_i)=2p+s−trj(G)。
这准确证明(2)，不交换P、Q，不丢负谱，也不用operator convexity。

j在非负轴凸且2-Lipschitz；不能在全实轴如此使用。κ₂在全实轴
凸非负、[0,2]上零，正文最终已明确两个函数的不同域。
negative quadratic/linear tail、positive quadratic tail与j来自同一
槽位恒等式，所以可加。其他对同一j的几何下界仍不能重复相加。

## 3. 原计数与simple Gram恢复

p+2b≤N+E₀将4b+2p换成2N+2E₀，得到(4)。
对于(5)，p≤s、s+2b≤N+E₁、D≥s+b依次给
4b+2p+s≤4b+3s≤N+E₁+2D。没有使用不成立的
D≥(N+s)/2。304的p=s、trA=N于是给(6)；其原三点合同
0<μ<2保证(7)除以1−μ/2合法，原μ没有被重新优化。

AF原a=||φ||²/L为有限L的实际归一化。无限same-simple Gram减
carrier压缩Gram为漏出列的PSD Gram；两矩阵同维，Weyl单调使
排序特征值距离的ℓ¹和恰为其trace。结合j的非负轴Lipschitz，
得到(8)的2倍trace-loss，不能只由条目误差推全Gram trace norm。

outside-I的collar列数O(√T logT)，每simple列泄漏≤1；inside-I
用原C² packet及单位高度计数，故总trace-loss=o(N)。MT kernel
O(1/L)误差只用于固定三点块，每块有限条目、块数O(N)，费用
O(N/L)。正文没有把这个局部比较扩大成完整Gram trace-norm接近。

## 4. 非交换效果对偶与二矩恢复

在A谱基中，PSD B的非对角条目只增加trB²，最优positive-tail
平方由B=(A−2I)_+达到；negative-tail平方由C=A_-达到。
0≤D≤I的线性最优值由D=1_{(-∞,0)}(A)达到。三份变量独立，
所以(9)准确同加，任意已验证PSD/contraction效果给严格下界，
不要求实际选定效果与A交换。

rayleigh方向Jensen只是一条可计算finite lower，未证明正密度
多向量越过0或2。以未知谱作最优效果不等于已经付款算术收益。
全heightν含unbounded Γ log multiplier，但有限C² packet的
square tail为O(|t|^−4)，log-weight可积，故(10)是准确finite
form pullback；没有非法宣称整个Γ multiplier bounded。

标量导数界与Hoffman–Wielandt、Cauchy给(11)的normalized S2
常数，不需要S4。AF trace-norm小tail因此恢复κ₂/d；flat的
实际Gamma/pole/proper-power恢复同样只用已付second。MT需保留
实际bounded background，正文没有将它冒称I。

## 5. 条带、单对特征与误差量纲

|β−1/2|≤3/8在304的z坐标只给|Imz|≤3logT/(16π)，
不是fixed-width或o(1)窄带。simple-real Gram的实间距没有因此
变小，μ没有自动提高。

对normalized real-even η，cosh/sinh的odd积分给g⊥h；
两norm为(M+1)/2、(M−1)/2，因此未压缩单对的谱确为
m(M+1)、−m(M−1)。M≤cosh(dL)，只有dL=o(1)才保证M−1=o(1)。
原AF η_L(s)=φ(Ls)/√a的固定物理endpoint区间给固定d>0时
M≥c_d e^(dL)/L；304固定ηδ切去端部，最终正文正确限定
该指数lower仅属于AF的随L profile。

原carrier压缩可破坏g/h正交，多个pair谱也不相加；因此这些
单对值不等于整个trA_-的下界。MT非可去simple实根处，Taylor
给ReK(a+iy)²=−y²K′(a)²+O(y⁴)，确实排除任意非零条带的
termwise positivity，但未声称真实零点位于该点。

AF packet square的X^(1/2)改为X^(3/8)，保持√T collar，
tail变为O(T^−5/8)、trace error O(X^(3/8)L²)，另有
O(√T L)collar计数。所有仍为o(N)，只改速度，不改主比例。

## 6. 已付实际效果方向与最终范围

flat A=I+H+L的已付second/cubic给(13)。其两个quadratic forms
的矩阵分别为

\[
 \begin{pmatrix}1&1/6\\1/6&1/6\end{pmatrix},\qquad
 \begin{pmatrix}-1&1/6\\1/6&-1/6\end{pmatrix}.
\tag{2}
\]

第一个positive definite，第二个negative definite，Schur gap均
为5/6；再减effect-square成本不能提供正主项。对fixed nonnegative
row mark，prime first trace的endpoint overlap抵消csc alias denominator，
两-P cross为o(1)，所以positive/negative线性收益也无正主项。
这是原same-coefficient trace计算，不是generic array反例。

含H的linear-square effect需保留未知high fourth成本；在
a_T=o(L²)时已付relative cubic才是o(1)，其三变量线性Schur gap
2/3仍不为正。没有此growth前件不能删掉该relative error。
qstar的high第四矩lower也不直接付款完整A在[0,2]外的κ₂尾。

未发现final正文的数学阻断。限定PASS仅认证完整finite可加谱尾、
原计数/恢复及实际已付方向检验。正密度tail lower、其他效果的
positive arithmetic收益、whole fourth upper、新比例和新无零边界
均未获得，不以本有限证书取代它们。
