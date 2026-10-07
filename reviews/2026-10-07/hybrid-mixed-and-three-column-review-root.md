# 原混合四词与三列反射：根节点全文审查

2026-10-07。结论：三份研究稿均在其声明范围内限定 PASS。根节点本轮
重新阅读全文并逐式重算关键代数、projection、carrier与contour归一化。
不把未付的distinct矩、weighted covariance或旧引用输入升级为新定理。

## 1. 实际版本

Canonical LF仅规范CRLF、lone CR为LF，不trim，保留EOF与其他空白。

| 被审稿 | canonical LF SHA256 |
|---|---|
| [13/31](hybrid-one-three-mixed-prime-sector-research.md) | 5db2c614ab9d009a15a70f4e0639b95df2d59a6b56bd752216537fcf71e2b405 |
| [22 distinct](hybrid-distinct-two-two-prime-sector-research.md) | daca79cd62b61b7bd82a3b4fdf5a1a956ac0f2a1f44f7e63c0ff3f3b912cfc0d |
| [三列反射](hybrid-three-column-reflection-research.md) | 30929e068a6b1610a1ea64aea4e5a0d46623b9fd2f7e41c18f77044d7b209878 |

原OpenAI source固定adc7f124，canonical LF
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
未修改或构建其math仓库。AF原窗/频率再次浏览
[v2 §2](https://arxiv.org/html/2608.13637v2)；Bessel transform交叉核对
[DLMF 10.22.43](https://dlmf.nist.gov/10.22.E43)与
[10.2.2](https://dlmf.nist.gov/10.2.E2)。矩估计及普通Hecke FE保留
报告明确引用的输入；此审查不认证外部whole kernel。

13/31附有作者重新推导的[审查](hybrid-one-three-mixed-prime-review-twisted.md)，
不能把该作者重审称为另一作者独审。22有
[radial](hybrid-distinct-two-two-prime-review-radial.md)与
[twisted](hybrid-distinct-two-two-prime-review-twisted.md)独审。
三列有[mixed独审](hybrid-three-column-reflection-review-mixed.md)。
本根节点报告提供另一次独立全文重算，严格区分各报告覆盖范围。

## 2. 13/31：实际重复union已付

在原finite compression中，三R标签的重复union准确为
2Re A+O-2T。三个pair intersections均为triple标签T，因此系数-2
正确；四个另一范围标签的位置可在有限矩阵迹中合法循环。

Opposite repeated的Y!=Z三P删除逐项费用是a_i^2 Z_2 l_Y、
a_i y Z_2 l_i、l_Z(a_i^2Y_2+a_i y l_i)。重复平方权重可求和，
仅用已付二矩，不预设未知第四矩。Adjacent先使用positive差的
trace O(log L)，再删P，费用均o(d)。没有带末端P的物理免费循环。

High/low差频near强制q,r在sqrtX附近，integer harmonic给X^(-1/2)L。
p^2q与high r的near窗强制p^2q<=2X；integer hyperbola count
O(X^(3/4))，给X^(-1/4)L。p^2与high×low的near窗，固定low
prime r时非零平方值最多两根，每残块positive harmonic O(log r)。
actual p为prime，zero-residue exception只可能p=r且仅在low范围；
exclude唯一zero denominator后费用O(L/r)。这支付了high重复p
上端sqrt(2)X^(3/4)的整个near范围。

所有far先乘原endpoint overlap，消去±L alias，再聚合重复平方
权重。Low16/high4个非空符号模式覆盖完整；同号连续high步
不可能非空。Triple项以sum ||C_p||^3=O(L^-3)付款。
因此两actual repeated unions为o(d)，整个M13/M31精确约化到distinct。

Finite Fourier-walk逐index独推相容：k_i=k-r_i，合法k区间是
[r_max,d-1+r_min]，相位是tau_k S-2pi(r_1s_1+r_2s_2+r_3s_3)/L。
原zero-extension由a_s的support保留，periodic coefficient展开
不制造wrap路径。Gamma替Kd的差保留全部有限projection。
现有absolute bounds仍增长，不能删除distinct P。

PASS仅覆盖repeated o(d)与exact distinct walk；没有distinct O(d)、
完整第四矩或新比例。内存有限模型只核代数，不认证无限分析。

## 3. 22：物理同号付款与实际有限余额

Hermitian代数M22=6||C_H C_L||_HS^2-||[C_H,C_L]||_HS^2，
并有2A<=M22<=6A。因此commutator的负号不能凭空消除大于d的
product norm。Repeated flat13/120引用原已付同对象。

物理同号二步强制pq<=X且H/L分解唯一，log跨度小于L/2。
Local-spacing Hilbert的weighted energy O(X/L)，carrier numerator
两相位分别吸进feature coefficients，给全异非对角o(d)。扣除
固定p/q repeated子族合法，非只对总非对角作错误等同。

Opposite rational frequencies的determinant为pq'-p'q，真实交叉
length XsqrtX；不能替换成X。Csc remainder的endpoint cancel
在共同feature积分后支付，不对pair-dependent cut套Hilbert。
Fixed q'的composite–prime near矩形是单侧nq'<=2X，union
frequency跨度有统一余量，bilinear weighted energies相容。
Far含±L aliases，依实际共同support付款。Shared q' feature
未被当作独立于prime-side的系数，因此该归约未夸大为O(d)。

Norm diagonal通过zero-frequency物理变量平移给D_HL，未用有限
循环替换物理placement。P crossing的精确identity(42)、directional
(46)及final(47)逐项相容。它们保留E、L、commutator和cross term；
已有粗norm均不允许声称这些是o(sqrt d)。Flat17/480只是该
decomposition的已知项，不是distinct主项。

PASS仅覆盖物理同号o(d)、actual identities与明确coarse upper；
Delta、Gamma及signed finite corrections仍待付款。

## 4. 三列：实际inverse残数归约

原primitive FE的根数在三变量quotient中是一个epsilon，六个
deleted factors均保留。Reciprocal dual scale是1/(CD)，不是C/D。
双plain natural reflection含完整d|R及h|R^infinity，并保留
primitive phases；二列共同epsilon^2只能在rowwise absolute square
中抵消，不提供跨row saving。原once slots未被反射或复制。

Bessel inverse transform的初始absolute Mellin strip为
3/4<Re z<1；其transform确为fhat(1-z)Gamma(1-z)/Gamma(z)。
Nonzero f的无穷端存在moment tail；减a_0/y后在1<Re z<2
准入，crossed residue为-a_0，符号正确。

Negative-line的natural inversion先用exact Euler identity，再展开
Re z=1+r的绝对收敛series，得到sqrt(q_R)、q_h及相应phase；
不是普通natural inverse polynomial。其tail界C^(-3/2)D^(-3/2)
q_R^(-1+epsilon)相容。Primitive与natural zeros、multiplicities、
horizontal joins全部保留。选无零boundary不被误认为uniform inverse
bound；external Mellin tail order没有免费消灭join。

Critical cross exponent独算为a-(ell-1)/12。因此先对reference ell
选择fixed a<(ell-1)/24，再缩小共同邻域，使uniform margin为正。
这澄清原§10的量词阅读，不修改被审hash。Eq24所称numerator
Vhat(i nu_+)指fhat(rho)；完整residue仍有D^(rho-1/2)/L'(rho)。
原正文完整formula保留该factor，没有缺失。

Eq33是actual weighted norm的quantitative replacement；不是χ>0。
Covariance subtraction、simple-zero difference quotient均代数相容，
没有microscopic shift或L'下界。All-mod-six table保留j=0的
Ramanujan分支与CRT phases，未误读generic cubic low的特殊
quadratic terminal为任意signed composite bound。

PASS覆盖明确completed identities、negative-line预算及actual Z
joint-reduction。Weighted去集中、strictγ<1/3及全域延拓改进未付。

## 5. 原完整Goal的状态

这些新归约真实缩小未知对象，但不能将子sector预算相加登记
67.25%以上的新比例。完整prime/centered第四矩、actual AC^3
covariance仍须同一finite object付款。无零方向仍需新的joint
strict saving及全族contour证书。既有引用输入下sigma*保持，
不触发新正式边界论文。Goal未完成，也未因此收缩其目标。
