# 456：高素数 opposite 四词及重复主项的独立全文审查

2026-10-07。审查人：`twisted_research`。逐段核对456全文、冻结high报告和
mixed报告的实际定义/二矩/P删除接口，并与另行完成的Topp推导比较。
没有修改456、冻结稿、math、脚本、输出、Goal或Git。

结论：**限定 PASS**。456证明原finite matrix的Topp=O(d/L)=o(N)，
因此高素数整个signed repeated union/N趋于2S_psi，flat为19/240。
未支付四distinct或完整响应预算，不产生新比例或无零边界。

## 1. 全文绑定与审查范围

文本SHA按UTF-8解码、CRLF→LF、lone CR→LF；不trim或删末尾换行。
下列bytes为当前raw bytes；这些文本与canonical UTF-8 bytes相同。

| 文件 | canonical LF SHA256 | bytes / 行数 |
|---|---|---|
| [456正文](../../notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md) | `7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96` | 8936 / 270 |
| [独立Topp推导](hybrid-high-opposite-prime-research-twisted.md) | `696ed3456eeb9623da6c19a21985aabcffcbf2038c91a59395e805b573e55da6` | 9555 / 277 |
| [冻结high输入](hybrid-high-prime-four-word-response-research.md) | `988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666` | 19170 / 572 |
| [冻结mixed输入](hybrid-low-high-mixed-four-word-research.md) | `71f62b2dd931cfda012e7dad9c4efcfece63f5cf1bb8ff5b466d3e2ac1ae89f9` | 22126 / 589 |

最终456相对已审版本仅更新状态、修复substack换行分隔，并新增有限
证据范围，均已只读核对；数学证明不变。正文全部本地Markdown证据
链接存在。下列连续/整数估计逐项由公式核验，不把有限模型当作渐近
分析的证明。

## 2. 原定义、有限维数与已付输入

456(3)准确继承[AF v2 §2](https://arxiv.org/html/2608.13637v2#S2)的
unitary Fourier常数：原(2pi/(a_L L))F* M_high F给
B_p=−b_p Mphi(R_logp+R_−logp)Mphi，b_p=logp/(a_L L sqrtp)。
正负exp的1/2与multiplier的−1/pi抵消成所列系数；四次负号抵消。
E是实际carrier tau_k=T+2pi k/L的isometry，d=floor(XL)保留到最后。
只用d/N(T,2T)→1，不使用更强且未成立的d=N+O(L)。

R_s是zero-extended物理平移。fixed chi、psi及0≤phi≤1、a_L的固定
正下界是继承前件；常数允许依赖这些固定数据。high logp>L/2使
同方向二次路径为空、两向输出支撑分离，故||Bp||≤bp确切成立。

冻结high(13)–(16)的C² Fourier crossing统一于shift，保留carrier共轭
及floor区间，给456(4)的lp和lY。后者只是triangle，不是假定prime
泄漏正交。冻结high(18)–(22)用same-direction跨度<L/2的有限几何
核及weighted Hilbert给||BP||₂=O(sqrt d)。这是已付二矩；不从未知
Tr CH⁴倒推。所有输入和新结论均不调用零自由包[R]。

## 3. 三个internal P：与独立推导的差异准确核对

置A=Bp、Y=B，原迹为Tr(PAPYPAPYP)，physical迹为Tr(PAYAYP)。
从左到右删除internal P的三个差额为

\[
 D_1=\operatorname{Tr}(PAQYPAPYP),\quad
 D_2=\operatorname{Tr}(PAYQAPYP),\quad
 D_3=\operatorname{Tr}(PAYAQYP).
 \tag{1}
\]

456对D1采用比我的独立稿不同的合法配对。循环只在这些trace-class
有限P/HS因子间进行：D1可配对QYP与PAPYP AQ，后者HS norm≤a²Y₂，
故|D1|≤a²Y₂lY。我的稿改为配对PAQ，给a yY₂lA；两者都有效。
D2配对QAP与YPAYQ，给a yY₂lA。

D3配对QYP与PAYAQ；取伴随后使用
YA P=YP A P+YQ A P，准确有||YA P||₂≤aY₂+y lA。
因此||PAYAQ||₂≤a²Y₂+a y lA，得456(6)第三项。
未遗漏右P，未令P与A或Y交换。末端P一直保留。

sum a²=O(1)、sum a lA=O(sqrt ell0)给456(7)，其除以d为
O(sqrt ell0/L^(3/2)+ell0/L³)。这里使用重复标签平方的可求和性，
不能移作四distinct词的整块ℓ¹付款。

## 4. 真实路径、carrier、alias及完整far区

456(8)的endpoint phi一次、三个内部位置phi²准确来自四个物理乘积；
finite-k平均是Kd(S)，不能以全高度时间平均替代。
五个位置同时在长L的I内，而每步>L/2，只有+−+−和−+−+可支撑。
对于前者，S=2a−b−c；若S≥L/2则S3=S+c>L，若S≤−L/2则
S1−S=a−S>L。另一pattern反射相同，故实际支撑严格|S|<L/2。

这不是先删除alias再估计：alias被五点物理支撑准确排除。原Kd的
unit carrier相位仍存在，仅在合法范围取
|Kd(S)|≤min(1,C L/(d|S|))。位置0、a给真实共同overlap≤(L−a)/L。
dummy q/r交换仅对正majorant排序，不交换非交换物理operators。

|S|≥log2的全部非空far词由1/X核界及sum bp²、sum bq控制，费用
O(L^-2)。diagonal p²=qr在prime标签下只可能all equal，费用
≤2sum bp⁴=O(L^-4)。二者均保留，未只估计near后遗漏far/diagonal。
near上qr≈p²、bp²bqbr≪p^-2及|S|≳|Delta|/p²，准确得到(15)。
即便decay上界大于1，使用它作majorant仍合法。

## 5. 整数引理、prime例外与二进制Q起点

456(13)的P可为任意实P≥1。对固定奇prime ell，q progression先单列
至多两个最近点，其余harmonic项给log(2X)/ell；中心在q区间外仍成立。
非零平方residue各至多两根，P区间内每根有O(P/ell+1)个代表。
完整residue block和残block的delta^-1和为O(log(2ell))。
由于ell≤X，(13)的统一log(2X)界成立，无需p≤X作为引理前件。

ell|p分支准确移去p²=ell q的zero denominator，剩余费用
O(log(2X)/ell)。它包括实际prime p=ell的非diagonal q项；该例外
既没有错误使用nonzero delta，也没有整个丢弃。只有作为模数的ell
必须保持prime；p与ql可放宽成整数，因为此步是正上界。

我的独立稿使用从sqrtX起点倍增的Q bins，所以有Q≥sqrtX。
456使用普通二进制[Q,2Q] bins；相关actual qs>sqrtX只推出

\[
 Q>\sqrt X/2,\quad Q\ge P^2/(4X),\quad Q\le2\sqrt2P.
 \tag{2}
\]

456写的是Q≥c max(sqrtX,P²/X)，准确容许此差异，未错误声称
Q≥sqrtX。充分大X时logQ≥L/2−log2，因此Chebyshev仍给
#prime ell∈[Q,2Q]≪Q/L。即便整数majorant纳入原sqrtX以下的
部分bin，ell仍≥Q≳sqrtX且为奇prime；原输入与常数均不受影响。
bin boundary至多固定重复次数，只用于majorant不影响渐近。

乘(13)后每(P,Q) block为O(P+Q)=O(P)。相关Q的upper/lower比为
O(min(P/sqrtX,X/P))；按P≤或≥X^(3/4)两段分别得
O(1+log(X/P))个bins。不能在min-factor前额外粗付独立L个Q段。

## 6. 总和、实际主项及量词

对P_j=X/2^(j+1)，真实log(X/p)≤(j+1)log2。
456(18)因此是有限总和上界
C L^-1 sum_(j≥0)2^-j(j+1)²=O(1/L)，uniform于每个实X充分大。
下界crossing sqrtX的最后一个bin和顶端p=X附近不要求任何prime gap。
这正是实际overlap带来的节省，不是人为添加端点weight。

加上投影费用，456(19)确为O(1/L)=o(1)，无需full CH4输入。
冻结high(36)的exact inclusion–exclusion给456(20)；既付T0/N和
T22/N都趋Spsi，Tcross、T3、T4/N都趋零。新Topp/N→0给
Srep,H/N→2Spsi。这是actual signed union，不是逐词正预算。

我另用有理积分复算flat符号d(v)=(|v|+v²)/2：
Spsi=(1/2)(1/24+1/32+1/160)=19/480，故实际极限19/240。
MT显示值只来自固定窗积分，正文保留精确2int d_MT²，并未将小数
变成严格有理新比例。对任意fixed chi、psi及epsilon>0，存在依赖
它们和epsilon的X0；不作统一数值高度或可变窗声明。

没有发现实质缺口。PASS只覆盖456的新Topp和结合既付输入的repeated
极限。四distinct、22distinct、13/31distinct及真实背景AC³尚开；
不能把这里的主项与其他子预算直接相加成full fourth常数。455的
proper-power fourth-root小量只在whole预算有界后传递total fourth差。

## 7. 最终有限审计绑定与严格范围

| 文件 | canonical LF SHA256 | canonical / raw bytes |
|---|---|---|
| [新精确脚本](../../scripts/hybrid_high_opposite_exact_audit.py) | `731d8dacae09726610b9958d04fc97d6a8b99e5e112fe21fc567026f83981574` | 3984 / 3984 |
| [最终JSON](../../output/hybrid-high-opposite-exact-audit.json) | `3bef191084595e821d3e6f892405d9a6dab6471b8bdfe02d858e5ea18e07e466` | 1801 / 1882 |

只读`runpy.run_path`导入后执行`certify()`，未执行写输出入口；结果
逐字段等于磁盘JSON，并确实读取/绑定表1的最终456正文和本节脚本。
六个1–6标签的cyclic free-word模型验证(20)的系数，允许cyclic rotation
但不施加交换关系或reflection。25个3–101内odd primes逐模验证
1134个nonzero residue的两根及harmonic majorant；225个zero-residue
progressions准确剔除零分母、核对剩余等式。Fraction积分给19/480和19/240。

这些断言仅认证列出的有限模型和有理积分；不认证无限prime计数、
dyadic求和、physical五点支撑或internal P费用。后三类分析由正文
及本独审公式核验，输出`not_certified`与456新增证据段的范围一致。
