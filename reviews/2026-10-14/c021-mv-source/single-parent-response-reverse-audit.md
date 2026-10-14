# MV final response门逆审：第一母格、全部模式和全部 actual q

2026-10-14；独立逆核 root 最后 necessary gate，不改前两份 owned 原稿/hash。
已按 AGENTS 恢复 README/STATE、check/show、同Goal/frontier、C021 stopped、
D20261014Y、551当前原稿、原矩阵/G2及MV来源审。入口 HEAD
36810d109e184787027656c31fb636e880036d7f；root的STATE/来源目录有进行中改动。
子 get_goal=null 不代 root active实例；固定0c4f/≤538与唯一cadence不变。
只编辑本稿，不编辑STATE/cadence/Git/合同，不独立计轮。

**裁定：实际第一母格的 ALL N/ALL m 响应 upper 成立。**
下列 proof 保 moving cutoff、全部 proper powers、strict截尾和真实child mean。
它避免了先逐unitchild套local-gap证书的线性失费，故该证书反例不能扩张为所有MV修复失败。
但本门只给 basis diagonal；不同母格/m的完整共同Gram/G2仍open，不建C022。

## 1. exact actual接口与范围，不把 first parent 扩为所有parent

ALL整数N≥4，m∈Z\{0}，M=|m|。在新Π^a的flat坐标取

    e_m(x)=1_(1,2)(x)e^(2πim(x−1))，||e_m||²_dx=1。

每cell mean0；不是547旧weightedmean R。
actual H_N^*=Σ_(2≤q<N)Λ(q)/sqrtq C_q^*，C_q^*=R_flat U_q^*(I−P_q)。
若q|m，该模式先被(I−P_q)删除，不能再由child mean代为删除。
令a_q=Λ(q)/q·1_(q∤m,q<N)，则精确

    H_N^*e_m=R_flat F_(N,m)，
    F_(N,m)(x)=1_(1,N)(x)Σ_(q≥2)a_q e^(2πimx/q)1_(q,2q)(x)。 (1)

parent phase e^(−2πim)=1，Λ(p^a)=logp，strict q<N；包含所有properpowers。
公式(1)明确只对应**第一母格**。一般母格j的区间是(qj,q(j+1))，
不由此无声推出同样uniform-j bound。

定义本 necessary response

    R_N(m)=||H_N^*e_m||²_dx。                                (2)

回到原du单位输入ρ_(N,m)=N^(1/4)a_N e_m=sqrtx e_m，norm1；
对应原du输出也同乘N^(1/4)，故原norm响应平方恰为(2)，没有dx/du错配。
ρ是finiteBV fullzeroextension Dlog/Γoperator域源。
实际JΓ(ρ)=logM+O(1)（M→∞），精确不依N；Γ=actual2θ′，非periodiccell算子。
(2)是响应平方，不是同源signed B_C或fullWeil型。

## 2. dyadic actual支持与R_flat不扩大支持

对Q=2^k、k≥1，取q∈[Q,2Q)，令F_Q为(1)的相应块。
它的x支持在[Q,4Q)∩(1,N)。q、2q、N全整数，所有cut在unitcell端点。
所以在每一个open cell内active q集合固定，F_Q是光滑有限指数和，
R_flat仅减该cell均值，不能把支持发到原来全零的cell。
因此G_Q=R_flatF_Q仍支持[Q,4Q)∩(1,N)。

任一点最多属于三个这样dyadic支持（a.e.可更少）；于是保全部block cross有

    R_N(m)=||Σ_QG_Q||²≤3Σ_Q||G_Q||²。                       (3)

这是support Cauchy，未宣称blocks正交；strict q<N截尾只是将a_q置0。

## 3. moving cutoff的binary付款与长interval MV

在I_Q=[Q,4Q]上，active q还须x/2<q<x；它们按q排序形成连续index interval。
excluded q|m、非primepower或q≥N可直接作为零系数，interval结构仍在。
每个index interval分解为至多2(k+1)个canonical binary块。
点态Cauchy后积分，每个coefficient在每level至多出现一次，
因此总binary费用至多2(k+1)²，不把sup交换为另一个免费均值。

cycles频率λ_q=m/q全distinct（此处m是同一非零整数），并有

    |λ_q−λ_r|=M|q−r|/(qr)≥M/(4Q²)，q≠r∈[Q,2Q)。           (4)

原[MV1974](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
Cor2 global mean-square经angular2π转换，在任意起点、长度3Q的interval上给

    ∫_(I_Q)|Σ_(q∈B)b_q e^(2πimx/q)|²dx
       ≤(3Q+4Q²/M)Σ_(q∈B)|b_q|²。                         (5)

任意canonical subblock频率间隔不小于(4)；空/单term直接按norm。
这里无需错误的每child unitinterval inverse-gap upper。
因(k+1)=log(2Q)/log2及log2>1/2，可用安全常数

    ||Σ_(x/2<q<x)b_q e^(2πimx/q)||²_(I_Q)
       ≤32log²(2Q)(Q+Q²/M)Σ_q|b_q|²。                     (6)

(6)保持movingcutoff，两端条件若改为≤仅影响measure0。
本步骤只有有限q，原MV已核全部complex coefficients；不借新外部定理或未知ζ前件。

## 4. coefficient质量、raw与child derivative两条界联合

546已付Chebyshev ψ(X)≤4(log2)X，及Λ(q)²≤log(2Q)Λ(q)，给

    A_Q:=Σ_(Q≤q<2Q)|a_q|²≤8log(2Q)/Q。                     (7)

这是实际properpower系数，不把它换成uniform权或log q。
由(6)/(7)与mean projection contraction，

    ||G_Q||²≤||F_Q||²
       ≤256log³(2Q)(1+Q/M)。                              (8)

在open unitcell内，movingcutoff固定、没有in-cell jumps；body derivative为

    F_Q'(x)=Σ_active (2πim/q)a_q e^(2πimx/q)。

integer端点上的jump不用当作global弱导数来套Poincaré。
只对每个完整unitcell应用mean-zero Neumann Poincaré（cosine Parseval，常数1/π²），
并对同一movingcutoff的derivative coefficients用(6)，

    ||G_Q||²≤π^(-2)Σ_cell ∫|F_Q'|²
       ≤4M²/Q²·256log³(2Q)(1+Q/M)。                      (9)

N截尾仍在完整cell端点，(9)不增加boundary费。
合并(8)/(9)：令x=M/Q，min(1,4x²)(1+1/x)≤6min(1,x)，所以

    ||G_Q||²≤1536log³(2Q) min(1,M/Q)。                     (10)

x≥1用raw；1/2≤x≤1的比值≤6；0<x≤1/2用derivative，均同一source。
这是真正child mean low-M/high-Q抑制，不是先分别求worstfee后相加。

## 5. dyadic求和、显式统一常数与actual价格

由(3)/(10)，

    R_N(m)≤4608 Σ_(Q=2^k<N,k≥1)log³(2Q)min(1,M/Q)。          (11)

设B=log(2+min(N,M))。head Q≤min(N,M) 的和≤32B⁴：
用Σ_(l≤K)l³≤K⁴、log(2R)≤2log(R+2)、log2>1/2。
若N>M，tail取M<Q₀≤2M，Q=Q₀2^l，则
log(2Q)≤log(4M)+l log2≤(l+2)log(M+2)，M/Q≤2^(-l)。
Σ_(l≥0)(l+2)³2^(-l)=102，且log(M+2)>1，故tail≤102B⁴。
N≤M时没有该tail；M=1时head为空，同一tail计算合法。
因此一个独立安全总常数为

    R_N(m)≤10^7 log⁴(2+min(N,|m|))，
    ALL整数N≥4，ALL m∈Z\{0}，first parent1。                (12)

实际上述粗常数4608(32+102)<10^7，未追最佳常数。
negative m由相同M或complex conjugation覆盖。
包括m∈[N,2N]成长band，不只是某个fixedm/数值样本；最大模式无需有限上限。

(12)并不要求把JΓ的logm免费忽略：原ρ仍有前述fullΓ价，
但这里响应自身已对m饱和为O(log⁴N)。它与native逐child/local-gap证书的线性反费
不矛盾，因为(6)保长interval上的所有common-child phases和movingcutoff。

## 6. full joint量词没有从basis diagonal继承

对single m、所有q的真实cross已在(1)/(6)保留；
但对Σ_m c_m e_(1,m) 或多个parent cell，响应还有

    〈H_N^*e_(j,m),H_N^*e_(j',m')〉

的offdiagonal。逐列norm(12)不能界定全部coefficients单位球；
无限basis不能把trace、最大diagonal或triangle当fullGram operator费用。
原actualΓ对这些cross/source本身也须共同付款，不把logm逐列价替代全部Γ。
所以ALL N/ALL m不等于ALL independent profiles/ALL cells。

该 necessary门成功，仅说明本来源的这一真实响应检验没有排除cluster/长interval修复。
没有给fullG2、signedΓrelative、条件quasipoly wholecount、RH或ζ/Ξ净约束。
旧MV、Chebyshev、binary付款与Poincaré为现有工具；本次子审不独立新增研究轮。
不得因(12)重建名为‘fullresponse’的未知输入合同或C022。

本source按已定范围完成这一final gate后结束；C021 stopped/G2 open、宏观Goal active。
root负责将唯一下一选择放回当前战略和STATE。本子任务无待跑进程，未改旧原稿hash。

## 7. 对另一组织原稿的最终逐式逆核

已完整读并核
[single-parent-all-mode-actual-response-gate.md](single-parent-all-mode-actual-response-gate.md)，
raw SHA256 `95d83a8fe3b251f4bc1cfa38b01da0daebc4e23b8796b9c9581dc520bafd93e2`。
其§3的32、§4的1536与support保持均符合上面独推；q∣m须置零的actual前件明确保留。
其§5更保守的tail常数216log³(2M)也成立：
8(log2)³[(L+1)³+26]≤216log³(2M)，M≥1。
再用log(2M)≤2log(M+2)、log(M+2)>1，得tail≤1728log⁴(M+2)，
head32合成1760；4608·1760=8,110,080<10^7，原稿显式常数通过。
本稿§5的独立134求和界只作安全逆核，不据更小常数计功或改原稿。

前 owned collision稿 raw SHA256仍为
`af88f341dcbbd88679164c0b89f8ac0c1bdea45189b76fd20b583c09217c4293`；未改其certificate-only范围。
结论共同范围是first-parent basis diagonal通过，fullmixed/G2未付、来源0结束。
