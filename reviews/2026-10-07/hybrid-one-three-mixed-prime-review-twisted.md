# 13/31 原有限混合四词：全文重新推导核验

2026-10-07。审查人：`twisted_research`。被审旧推导亦由本审查人写成；
本次按新审查任务逐式逆核全部定义、projection、路径、算术及distinct
表示，不把它冒称另一作者认证。只新增本报告，未改旧推导、math、
冻结稿、脚本、output、Goal或Git。

结论：**限定 PASS**。13/31 actual sectors的三个同范围标签重复
union均为o(N)，因而whole sector准确约化到三个同范围标签两两不同
的实际finite sum。distinct没有O(N)或o(N)预算；本PASS不产生full
fourth常数、零点比例或无零区域。

## 1. 固定全文及输入

文本SHA按UTF-8、CRLF→LF、lone CR→LF，不trim或删除末尾换行。

| 文件 | canonical LF SHA256 | bytes / splitlines |
|---|---|---|
| [被审13/31报告](hybrid-one-three-mixed-prime-sector-research.md) | `5db2c614ab9d009a15a70f4e0639b95df2d59a6b56bd752216537fcf71e2b405` | 20215 / 524 |
| [高素数输入](hybrid-high-prime-four-word-response-research.md) | `988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666` | 19170 / 572 |
| [22混合输入](hybrid-low-high-mixed-four-word-research.md) | `71f62b2dd931cfda012e7dad9c4efcfece63f5cf1bb8ff5b466d3e2ac1ae89f9` | 22126 / 589 |
| [454](../../notes/454-original-background-and-weighted-prime-mixed-traces.md) | `8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7` | 13284 / 425 |

[AF v2 PDF](../../literature/baseline/2026-alpoge-furman-6725-v2.pdf)的
binary SHA为`6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444`，
478663 bytes。被审稿全部本地Markdown证据链接存在。此审查不扩大
已付source/经典二矩的范围，不调用零自由包[R]或未知full fourth。

## 2. 原对象和有限partition

E的实际carrier tau_k=T+2pi k/L、d=floor(XL)、真实zero-extended
R_s及C²phi均保留。b_p=logp/(a_L L sqrtp)与原unitary Fourier的
2pi/(a_L L) normalization相符。仅用d/N(T,2T)→1。
low为p≤sqrtX、high为p>sqrtX，两范围严格不交。

在Tr CR³ CS中，第一二R位置相等给A，第二三相等给bar A，第一三
相等给O；三种pair intersections及triple intersection全部为T。
所以U=2Re A+O−2T的(7)准确成立，O和T都为真实有限Hermitian
products的实迹。有限矩阵的普通循环允许把四个S放置合为4U；
不能把这个循环免费迁到带P的physical trace。

(8)要求三个R标签两两不同；S范围相反，故四标签全不同。
D+U=Tr CR³ CS为有限代数恒等式，不包含任何预算假设。

## 3. 两个不同Y/Z的三个internal P全部付款

重复A=Bp，Y=BR、Z=BS。原迹为Tr(PAPYPAPZP)，physical为
Tr(PAYAZP)。从左到右三个差额分别为
Tr(PAQYPAPZP)、Tr(PAYQAPZP)、Tr(PAYAQZP)。
第一项循环后配对QYP及PAPZPAQ，给a²Z₂lY；第二配对QAP及
ZPAYQ，给a yZ₂lA；第三配对QZP和PAYAQ，给
lZ(a²Y₂+a y lA)。其中YA P=YP A P+YQ A P，右P没有丢失。

sum a²=O(1)、sum a lA=O(sqrt ell0)准确给(13)。两种Y/Z方向的
最大费用为O(X sqrt(ell0/L)+X^(3/4)ell0/L²)=o(d)。Y≠Z无需
full Tr CR⁴；仅用已付Y₂/Z₂=O(sqrt d)和crossing。

adjacent先用positive trace泄漏替换sum Cp²，费用yz ell0。
再删D–Y及Y–Z的P，两个费用分别为z lY sqrt ell0、
lZ(lY+y sqrt ell0)，均O(X^(3/4)ell0/L²)。low的D_phy含
±2logp shifts；其每个coefficient由phi(u)phi(u±logp)²phi(u±2logp)
给出，同样在wrap处零且有统一C² variation。sum bp²=O(1)故
||QD_phyP||₂=O(sqrt ell0)。没有把low平方错当纯multiplication。

## 4. Near/far及全部signed paths

对真实四词，所有累计位置都在I；至少两个endpoint相距|S|，故
<|W|>≤(L−|S|)_+/L。乘原Kd后，log2≤|S|≤L均得O(1/X)，
在|S|=L真实积分权重零，|S|>L路径为空。这包括±L附近alias。
near才使用min(1,max(m,n)/(X|m−n|))；carrier从未先删掉。

我重新枚举low opposite的第一步p+八个符号：
++++、+++-、++-+、++--、+-++、+-+-、+--+、+---。
其displacements分别为2a+b+c、2a+b−c、b+c、b−c、
2a−b+c、2a−b−c、−b+c、−b−c，与§7.1全部行一一相符。
global反射覆盖另外八个，并保留相同绝对majorant。

high opposite的前三步均>L/2；相邻同号必为空。只剩+-++、+-+-
及两者反射，确切覆盖全部16模式。前一ratio p²r/q>2只用far；
后一near需要平方/高低乘积计数。adjacent low的两个非local同向
p步骤也有四个后续模式及反射；local部分是一high/一low差频或
sum频。所有远区均归入同一个positive mass付款：
X^-1 sum bp² (sum_H b)(sum_L b)=O(X^-1/4/L²)。
未省略m>2X、sum frequencies或端点alias。

## 5. 三个near估计及prime zero-residue例外

high/low单素数near差频强制low q≥sqrtX/2、high r≤2sqrtX。
原系数乘Kd≤C/(X|r−q|)，整数harmonic总和O(sqrtX L)，
给O(X^-1/2 L)。乘repeated平方或bounded local symbol均合法。

low p²q/high r的near原系数同样为C/(X|p²q−r|)。p²q为复合数，
不等于prime r。near强制p²q≤2X；在p≈X^(1/4)分开，整数
hyperbola总数O(X^(3/4))。每个integer center对全部r≤X求非零
harmonic和O(L)，故O(X^-1/4 L)。此正majorant不需moving-feature
Hilbert或prime independence；far另外已付。

平方/高低乘积near系数≤C/(X|p²−qr|)，prime ranges不交保证
exact equality不可能。low重复p最多Y=sqrtX；high重复near则
p²≤2X sqrtX，所以Y=sqrt2 X^(3/4)。固定low prime r，非零
residue的平方最多两个根（r=2也适用）。每个完整block及残block
的delta^-1和O(log(2r))，不是O(r log r)。加q progression的L/r项，
给被审(23)–(24)。

实际p也为prime，r|p只能p=r，此仅在low repeated发生。删除q=r
的zero denominator后，sum_q 1/|r²−qr|≤C L/r。将q扩大到所有
integers仍保留这个剔除；没有混入所有integer p的零剩余倍数。
按prime r求和最多O(L²)。其它p用整数blocks上界及Chebyshev，
得到(YL²+sqrtX+L²)/X，分别O(X^-1/2 L²)、O(X^-1/4 L²)。
zero residue/prime exception准确保留，(25)没有被用于far alias。

## 6. Rate和actual重复union

上述adjacent及opposite都是o(d)，并覆盖各自全部physical signs。
sum ||Cp||³≤C L^-3，因为sum_(prime p)(logp)³/p^(3/2)收敛；
已付finite二矩给Tr|CS|=O(d)，故T=O(d/L³)。
合并三P费用、near/far和triple，确得(9)所列
sqrt(log(2+L))/L^(3/2)+X^-1/4 L²+L^-3的统一上界。
chi/psi固定后对任意epsilon>0存在X0，所有X≥X0都成立。
于是M13=4D13+o(d)、M31=4D31+o(d)关于actual有限sector成立；
没有把signed union改为逐词正和，也没有重用22主常数。

## 7. Distinct finite walk、当前费用及有限代数核验

我从matrix entry e^(i tau_k s) a_hat_s(j−k)重新展开。令第一index为k，
n_i=k_(i−1)−k_i，便有k_i=k−r_i。四个indices落在[0,d−1]等价于
rmax≤k≤d−1+rmin，length=d−span。phase准确是
e^(i tau_k S) exp(−2pi i(r1s1+r2s2+r3s3)/L)，故(29)–(30)
完整保留所有P、floor、carrier与crossing。Gamma换Kd是无限中间
Fourier indices的一个顺序physical trace；不能直接认为差额小。

C² coefficients的l1为O(ell0)，weighted crossing为O(L²/d)。
|Gamma−Kd|≤min(1,span/d)，span≤sum|n_i|，故四个independent
majorant sums恰给O((L²/d)ell0³)。原13与31的prime l1质量分别
X^(5/4)/L⁴、X^(7/4)/L⁴，归一后为(32)的
X^(1/4)ell0³/L³、X^(3/4)ell0³/L³。两者增长，不能支付distinct P。

另在内存重新执行9个R/S各1–3标签的cyclic inclusion–exclusion和
4个d=2,3,4,5有限Fourier-feature模型，全部精确通过。walk模型用
Fraction及整数奇偶phase，允许一般有限rational features；它们只
认证有限代数，不认证AF profile、prime asymptotics或projection saving。
未写新script/output，不把首次临时测试的浮点混入算为数学反例。

§10提出的两个闭合条件确实保持相同distinct标签、signs及internal-P
余额；没有以假设条件代替新证明。scalar spectral Jensen的whole
physical B⁴ upper合法，但one-high系数必须保留四个placements，
不等于可以免费循环为4Tr(E*BH BL³E)。

没有发现被审稿在所声明范围内的实质缺口。本PASS只支付完整13/31
重复union的o(N)及准确distinct表示；high/low/mixed distinct、全
Hermitian响应及实际背景AC³仍需要新的signed预算。
