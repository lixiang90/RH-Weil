# Anchored原载波的完整fourth P差：独立全文审查

2026-10-08，twisted_research。结论：**限定 PASS**。
全文实读最终413行，并独核整条高度轴MV、准确outside e基公式、
联合L² Minkowski、完整positive gap、16个ordered words及q_sq夹界。
只新增本审查，不改作者正文、旧源、脚本、输出、论文、math或Git。

## 1. 最终正文与引用范围

被审：
[hybrid-anchored-carrier-averaged-fourth-projection-gap-research-radial.md](hybrid-anchored-carrier-averaged-fourth-projection-gap-research-radial.md)。

canonical UTF-8 LF SHA-256：
`c0e874ab9061982c8ef4365c8e9313eeac77eeddb756dc0b455cab3349f99dd8`；
16479 bytes，413行。仅CRLF/lone CR→LF，不trim。
六项冻结输入的链接与SHA均从磁盘重算相符。

独立读取228的moving grid、padded block、N(symmetric difference)
及uniform second接口。作者只从223取finite scalar MV、从228取
零侧moving-block transfer，不借225的旧signed first mean或旧fourth
算术闭合。这一范围限制准确且必要。

## 2. 全height的scalar second及实线e基

Chebyshev给Σb_p²=O(1)、Σp p b_p²=O(X/ell)。连续MV在任意
shifted interval长s上有sΣb²+CΣp p b²；起点被吸收到unit phases，
常数确实不依赖起点。正负符号用二项Cauchy均可包含，故(6)为
O(1+X/(ell s))，t≈0 coherent peak没有被排除。
必须保留Σp p b²里的ell分母，否则后续O(ell+X/s)会少一因子。

原unitary Fourier配nonunitary hatφ，(7)前因子1/(2πell)正确。
输出被φ支撑在I，所以Q的相关输出正是完整interval basis的outside
j；对固定n=j−k，inside k而outside j的数目准确为min(d,|n|)。
不能把这个P当作全实线frequency projection。

对任意ξ令ν=ξ/h，|n|≤|n−ν|+|ν|。near、middle、far三段
分别给O(1)、O(logell)、O(1)的weighted lattice能量；|ν|项
给O(ell|ξ|)。包括ν接近整数的情形，故(9)uniform。C² Fourier
衰减又给∫|hatφ|≪1+logell、∫√|ξ||hatφ|≪1，所以(10)的
O(√ell)成立；没有使用可能粗界发散的∫|ξ||hatφ|。

## 3. 联合L²平均与共同carrier集合

Minkowski是在L²(dσ/s;outside matrix entries)中使用。对每个
k、ξ，scalar区间仅整体平移，(6)的sup可在求和前代入。
准确outside count随后给W_ell；有可积majorant，也可先截断再
单调极限。因此

\[
 \langle\lambda_R^2\rangle\ll\ell+X/s
\tag{1}
\]

无不同prime正交假设，没有从signed average推出absolute average。
取s=T/√ell，两个channels的sum平均O(ell)。Markov给同一
relative measure≥1/2集合，λ_H²+λ_L²≤C ell；不是分别选两点。

## 4. 全closed fourth与16个词

按P⊕Q块写B，B²的左上为A²+K、左下为CA+DC。于是

\[
 \operatorname{Tr}(E^*B^4E)-\operatorname{Tr}A^4
 =2\operatorname{Tr}A^2K+\operatorname{Tr}K^2
                 +\|CA+DC\|_{\rm HS}^2\ge0.
\tag{2}
\]

K=C*C≥0，所以各项upper为2y²λ²、y²λ²、4y²λ²，总7y²λ²。
Q可无限维，C从finite P出发为HS，故所有写下的finite trace合法。
这不是x⁴ operator convexity的错误使用。

raw y_H²≪X/ell²、d∼Xell结合(1)给(16)的
O(ell^−2+X/(s ell³))；所选共同集合则给pointwise O(ell^−2)。
这不以actual/physical fourth有界为前件，也不要求其uniform integrability。
全prime合并B_H+B_L依triangle leakage同样成立。

三次内部P删除，每个closed trace的缺项至少两次crossing；product
commutator将cross拆成六个λ_iλ_j Πy。平均时Cauchy配同一σ的
两个leakage，给(19) mean absolute。16个有序words在同一集合
都O(ell^−2)，不按tuple删除P、不对physical words自由循环。
这是本轮真实新付款；旧Jensen恒等式本身早已存在。

## 5. q_actual、q_sq与Φ的不同及growth-safe夹界

K_σ=E_σ*B_HQ_σB_HE_σ≥0准确给two-step compression=A²+K。
qsq−q为2τA²K−2τWK+τK²；前后两项非负且为(2)正gap的
一部分，−2τWK介于−2MτK与0。因此(22)的双边夹住成立，
不需要未知Γ norm乘小误差，也不需要q bounded。
共同carrier上|qsq−q|≪ell^−2+X^−1。

qsq仍是finite two-step compression再平方，不等于Φ，亦不等于
整个实线residual ||(B_H²−M_w)E_σ||²/d。作者最终明确未支付
后一比较的M_w crossing，未将原center W任意改写。

## 6. 移动零块、restricted nearcore与最终作用域

s=o(T)，grid长度d(2π/ell)=T+O(1/ell)。单位高度零点计数给
N(J_σ symmetric difference [T,2T])≪(s+1)logT=o(N)，padded
collar为O(√T logT)。228的同配置trace/inertia、Archimedean和
second均需uniform moving-grid版本；作者没有用旧fourth算术结果。

仅有P-good point不保证另一个独立arithmetic good point也在其集合。
若要joint选择必须先合并nonnegative defects或证明交集；第8节
保留此缺口。原σ=T也没有被平均结论免费变成pointwise good。

正nearcore的kernel实部在所有σ∼T的相同小determinant域统一正，
但只是restricted sum。小positive compression gap不能吞掉它的
leading质量；要完整upper仍需physical补集净相消。作者没有将
nearcore当成whole norm lower，也没有将P桥当成four-prime upper。

审查未发现数学阻断。限定PASS认证same scalar/coefficients/φ/d、
短anchored carrier、全height的上述mean absolute桥与合法共同选点。
未认证原固定起点T的o(1) gap、未知physical four-prime signed upper、
新数值q、零点比例或无零区域。
