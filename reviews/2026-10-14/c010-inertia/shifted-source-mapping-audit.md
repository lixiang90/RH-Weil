# C010 单次 shifted target 的实际 source 映射及下向舍入审查

2026-10-14，同轮独立辅助，不另计轮。恢复 AGENTS/README/STATE/check/show、
当前Goal、C010/D20261014I，HEAD仍`35609baea2fb3a4456b5ab9250648b198a9a4130`。
只写本审查，不改 STATE/cadence/git/toolGoal；不覆盖fresh宏观审计的起始状态。
审的是自主脚本
[c010_shifted_inertia_certificate.py](../../../scripts/c010_shifted_inertia_certificate.py)，
不是原producer的PASS。原全源数学桥由537及full-inertia/shifted-congruence审查支付，
本文件只审 source→exact finite target 的映射和其舍入方向。

## 1. 核查结果与实际输入绑定

代码/公式映射通过：四个Fraction correction及非交换次序正确，
source degree、Gram、primitive midpoint规范正确，遍历两个完整224×224扇区。
下向 floor 加224I费用严格足够；普通mp proposal不作sign前件。
发现一个 **正缩放说明字段写反** 的问题，已立即报root/source；
真实整数实现未因此错算，惯性也不变。主代理同轮已修代码及预注册
的解释文字；live运行旧字符串作为历史保留，最终准确身份见§4。

本次实际记录并末次重核代码SHA为
`5dd87f78fcf2e68e0b7c1908bc8ceb056d43da628403b54bcac67ce1a2faf72e`。
这次hash读取时代码已经是修正后的metadata版；先前Get-Content看见的
旧字符串是独立的早期核读历史，不能将该hash误绑定到旧字符串版。
未执行这个producer，也没有另做224阶矩阵重建；本审查是独立公式/代码及
实际input inventory核查。root另做全Gram每entry检查，不由本文件冒称完成。

实际读取fresh frozen-manifest，与输入raw bytes长度/hash逐一相等：

| source | SHA256 |
|---|---|
| source-matrices | 4bce98228442805bc5ae16e9c26c8df88e85c35ab7ec8deffdd808adbf1217ac |
| sector0 V/congruence | 4303b0e6dacad1c181320a719f6b33d328c068341c4d8e720e057bdc673c2589 |
| sector1 V/congruence | 311df181b573940eb8e964727c9a9905107f5ff8eed16284f91d44e4021137db |
| sector0 old target | ce9f39f5e355b9bd77e0a04c0b94bab4c4a1e922024dfdd626e05f8a8c2d201d |
| sector1 old target | a4e7bdbd70b37fe82a39a8d8a718d95010094a4f439f440abb4b33ad6f3510fd |

四个V/target实际都是224×224、每个entry真正integer且完全symmetric。
两个raw A/B各50400个unique条目，实际核其keys准确等于448真实degree
全部same-parity uppertriangle，并且所有lo<=hi。parameters为N448、L17/16、
omega256、outputBits256、epsilonBits220；原B明确是whole M²的压缩、
有middle compression，原J0含L²换元。这些不是仅靠filename推定。

## 2. exact correction 与 noncommuting target

取t=s=1/10^34，保守不取tau credit；theta=2^-48、chi=1。
独立Fraction重算m_t=m−t>n，以及DeltaAlpha/DeltaBeta均positive。
原source errors保持epsD=epsB+(2b+epsA)epsA；D_t=D0=B0−A0²，
原H0/Uhat不变，原W_t=(1−t/m)^-1W0。
完整safe finite lower型的差准确是

    Pt−P0=−(t/m)W0^-1−[DeltaAlpha+DeltaBeta epsD]I
                         −DeltaBeta(B0−A0²).

原正congruence C=Qd^-1/2 V/(sqrt17 Cw)和
Lambda=dclear·289 Cw²T0由原C009独立桥支付；V正性在target sign之前。
S0=2^257、Cw=29·2^769、T0=17·29·607630911·2^1282。
q_j=8(2degree_j+1)用原degree_j=sector,sector+2,…,447，
不是local index。Gamma=17 Qd^-1。raw a,b中心为(lo+hi)/S0，
没有truncate midpoint或漏output256转midpoint257的因子2。

令原target K0=Lambda C*P0C，则同一congruence下

    Kt=K0−ci0 V−cd0 VQd^-1V−cb0 VbV+ca0 VaQdaV,
    ci0=(t/m)dclear·289 Cw T0,
    cd0=dclear·17T0(DeltaAlpha+DeltaBeta epsD),
    cb0=dclear·T0 DeltaBeta/S0,
    ca0=dclear·T0 DeltaBeta/(17S0²).

独立标量重算denominator bits分别[75,750,750,750]，其positive LCM
D的bits为824；全coeff positive，cb0=17S0 ca0精确成立。
旧dclear没有清新分母，脚本使用完整LCM而非int截断，方向正确。

代码raw dictionary以原degrees索引，min/max只对称重建原uppertriangle。
`aqa=product(aQd,a)`严格是aQda；f=aqa−17S0 b。
V列整除q_j的原整数性质实际逐entry assert。Y=VQd^-1，
middle=ca Qd f Qd−cd Qd；代码乘Y·middle·transpose(Y)，其中
transpose(Y)=Qd^-1 V，不能当Y本身或把a,V交换。
展开准确为ca VaQdaV−ca·17S0 VbV−cd VQd^-1V。
再加D K0、减ci V，得到 **Kinteger=D·Kt**。
cb虽不另参与乘法，其值由assert cb=17S0 ca付清，没有漏B项。

product遍历每row和每column，内积zip的是长度224的已核矩阵；没有只
检查diagonal/triangle后假设未计算条目。两个parity均按完整N=224编译，
最后symmetric assert覆盖全部offdiagonal。无额外L²、无A²替B、
无原primitive误差缩放或更换了actual threshold。

## 3. 下向dyadic floor 的完整Loewner费用

令B=max integer-entry bitlength，Q=Kinteger/2^B。脚本每entry计算

    Lij=floor(2^512 Qij),
    T=L−224I.

Python整数//对负数亦向−infinity舍入，不是towardzero。
代码对全部224×224 entries核
`0<=Kinteger_ij 2^512−Lij 2^B<2^B`，所以精确误差
E=2^512 Q−L为real symmetric且0<=Eij<1（entrywise）。
由最大absolute row sum，||E||op<224；不要求E本身PSD。
因此

    2^512 Q−T=E+224I >=0,
    T/2^512 <= Q = D·Kt/2^B.                         (A)

这已包含所有条目误差。sign/inertia只沿正比例和下型方向运输：
若T PSD则Kt PSD；若T+positive rank-one PSD，则n_-(Kt)<=1。
不反推Kt的负方向就是actualQ负方向。

## 4. 已发现metadata尺度问题与处理

首次代码receipt写
`positive_actual_scale: common_denominator * 2^integer_bitB`，
preregistration也称“Kt scale is commonDenominator*2^B”。如果它表达
`T/2^512 <=Kt/(D·2^B)`，就是错误：实际实现是Kinteger=D·Kt，
所以唯一准确身份为(A)，positive factor是D/2^B。
可以改为明确文字 `T/2^512 <= common_denominator*Kt/2^integer_bitB`，
避免“scale”一词的分子/分母歧义。这个问题已立即送root/source。
随后实际读取修正代码字段
`common_denominator / 2^integer_bitB multiplying Kt`，
预注册现也明确写 `T/2^512 <= (commonDenominator/2^B)*Kt`。
live运行旧compile receipt仍保留旧字符串，主代理另记correct interpretation，
不得把修正后文字倒填为旧进程实际输出。
它不改变实际integer entries或inertia，因为D positive；本次mapping通过。

## 5. proposal与有限exact门的独立范围

mp 80digits只给Cholesky/方向proposal。Gram factor以floor256bit整数
存储；矩阵本身512-grid，因此factor integer product正好同grid，
没有缺额外2^512。guard=2^372对应2^-140，exact residual若每row
absolute sum<guard，则target>=guard I+residual严格positive。
代码每一个row遍历全部j及min(i,j)+1个lower-factor indices，未漏
offdiagonal项；floor factor正负均允许，因为exact residual负责验收。

even rank-one取w/2^192，target integer update=2^23 ww*，在512-grid
恰等rho|w/2^192><w/2^192|，rho=2^-105，符号positive。
证明至多一负方向只需actual w非零和codim1 kernel，不能靠80digit
提案“近似正交”代替rank；root/reverse应核实际packet及该门。

本辅助实际读到odd编译receipt：B=4177、LCM824bits、status记
EXACT_ALL_ROWS_PASS、224rows、最大residual263bits<guard372bits；
target SHA b1871211c56347b72e3e363f060dd2f516c869b7bbb23e5672c4cc88b6ac3027。
这只记录执行输出，**不以同脚本producer的PASS代替root独立全Gram检查**。
随后只读到root独立结果 `independent-shifted-gram-result.json`：两个
sector各224rows、25200个triangle Gram entries及wrong-sign control，
sector0 added-rank后PD给finite negative-index upper1，sector1无rank
PD给finite upper0；target hashes与实际packet一致。此处记录root的
独立算术，不冒称本辅助再重算Gram。实际even packet的w向量长度224、
非零、coefficient=8388608=2^23，lower matrix完整symmetric也直接读核。
最终whole-inertia消费仍由root/reverse的数学桥核验；本文件不独自
预写simple-even、合同完成或当前Goal终态。

一次s/rho/guard/N/dps门若失败保持失败，不sweep。无本辅助后台进程，
不计额外研究轮。下一动作是root对实际两packet独立全Gram，并由reverse
将正complement/原全source误差/阈值minmax及rank-one门完整接回actualQ。
