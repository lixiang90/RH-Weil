# 471完整算子约化与四全异目标的全文审查

2026-10-08，审查人 twisted_research。结论：**限定 PASS**。
全文核对471的引用、完整有限词量词、D_T的定义与符号及其新增目标。
我为principal来源作者，本审查不充当该来源的第二位独立证明审查人；
471的tensor来源则已另行独立全文审查。本次只新增此审查，不改正文。

## 1. 最终正文与输入绑定

被审文件：
[471-original-principal-subtraction-and-signed-four-distinct-target.md](../../notes/471-original-principal-subtraction-and-signed-four-distinct-target.md)。

最终canonical UTF-8 LF SHA-256：
`a66dcc18606b59ac0aa1a879f64f6f7dae4a3278981e5fbc2c94190efa3a3ef6`；
8579 bytes，222行。规范化仅CRLF/lone CR→LF，无trim。

五个来源链接和SHA从磁盘重算全部相符。特别绑定：

| 来源 | 最终canonical SHA-256 |
|---|---|
| principal完整来源 | 87b98f4f1d176b72c66f07258dfb3c7499ac53844ce076c900d3d8ca9036a02f |
| tensor信息审计 | f9e3ffa1aa8c0be583b1c11fc952f8f09bd6deeee9f7bdfa31f3abda1523863e |
| 456actual repeated union | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 |
| 465实际残差 | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 |
| 470必要下界 | 729ddbed2b2d2af08e21e5f1ebabfb5663f906c702f52b13f81aac224402a93a |

初读发现连续积分下端phase应为it/2；来源及471已统一修正。
最终正文(3)是X^(1/4+it/2)，本审查不绑定修正前字节。
这一修正不改sup bounds及其余渐近付款，但准确积分必须采用最终式。

## 2. 主密度约化的完整词范围

定义是逐向量strong operator integral，不是假设平移在operator
norm连续。直接积分x^(−1/2+it)的上下端给

\[
 \frac{X^{1/2+it}-X^{1/4+it/2}}{1/2+it}.
\tag{1}
\]

good高度J上sup为O(X^−1/2/ell)，全高度sup为O(√X/ell)。
bad乘法两侧都有1_JcF，所以原packet HS²=O(T^−2)确实给
C0 op-small。t≈0主峰没有被省掉，也没有令原P与frequency guard交换。

含C0四词的Schatten指数为∞、∞、2、2；另一个op因子用原raw
O(√X/ell)，剩余两个用已付S2,d=O(1)。其O(ell^−2)误差不需要
H4或q bounded，且逐因子telescoping保持所有非交换次序。
Γ比较保留其O(√X/ell)增长与δΓ的小S2交费，不能只由δΓ→0
直接宣称q不变；471已正确写出这一乘积。

相同结论覆盖q_e/q_o和k。physical比较只覆盖每个含principal
的差词，以good two-crossing和raw/good dualheight付款；它不支付
原全四prime词的内部P余额。471的摘要准确保留了这一范围。

## 3. 原子能量、路径与真实长列

ν的prime原子仍是原log p；除以a_ell ell√p后仍为b_p。
prime×连续以及连续×连续的product pushforward绝对连续，不能消掉
离散semiprime原子。唯一分解给

\[
 \sum_n n|c_H(n)|^2
 =2\left(\sum_p p b_p^2\right)^2-\sum_p p^2b_p^4.
\tag{2}
\]

不同p、q的ordered coefficient是2b_pb_q，同p coefficient是b_p²，
故上式系数正确。冻结固定比例区间PNT及Chebyshev给X²/ell²。
该正能量与正nearcore均非完整signed fourth的下界，471已说明。

high交替路径允许两侧产品∼X²；31在two+/two−近共振时仍可有
X^(3/2)列。此处不把这一个near尺度当成actual entire31的免费截断，
也不把physical支撑限制迁移到未知finite-P crossing。
因此471没有把主密度约化表述为新的均值/间距上界。

## 4. 新增D_T目标与所有liminf/limsup量词

D_T是原actual C_p的有序四全异标签完整union；所有有限投影仍
在每个矩阵乘积中。它是实数，因为词反转共轭也在同一完整union，
亦可由τH4减完整repeated union得到。不要求单个词实。

456给repeated union=19/240+o(1)；465给τWH²、τW²均为
S=19/480+o(1)。因此

\[
 q_T=\tau H^4-2\tau WH^2+\tau W^2
     =19/480+D_T+o(1).
\tag{3}
\]

这里的o(1)完全由已经付款的repeated/weighted-second项产生，
不需要q或fourth bounded。于是即使使用extended-real liminf/limsup，
移去固定常数和o(1)仍合法；470的必要下界给

\[
 \liminf D_T\ge q_*-19/480,
 \quad q_*=(\sqrt{104899}-275)/15120.
\tag{4}
\]

独立重算显示小数为q_*=0.003232880359890941970…、
q_*−19/480=−0.036350452973442391363…，与正文相符。

任何固定Q<19/480的limsup q≤Q，严格等价于
limsup D≤Q−19/480<0。因此这个特定小残差目标需要净负四全异
相消；D=o(1)仅给q→19/480。正文没有将此目标强加给所有比例方法，
也没有提出新的未付Q，或重新启用被470排除的1/350。

主密度替换保持整个a、q，而非为原离散D_T另定义任意continuous
标签划分；这一点在471中表述准确。

## 5. Tensor摘要与最终范围

tensor来源的fixed m、σ(A²)=1、σ(A4)=m/2和I/A/(A²−I)
正交，确实保留所列lifted rowweight与low/parity数据，并新增高平方
HS成本。whole gap增量τH²UH²U≥0，故470必要下界保留。
F̃≥(m/2)(τH²)²的归一化与常数正确。

471明示W⊗I不等literal same-prime operator W⊗A²、dm并非
原单carrier、raw/tail及零侧feature未实现，所以有限模型不能充当
实际素数或比例反例。所列信息不够供应uniform fourth upper的结论
没有被扩大成实际RH或新边界断言。

未发现最终正文的数学阻断。限定PASS认证来源摘要、完整有限词
约化范围及新增四全异净符号目标；未知joint correlation、actual
q上界与新的零点比例仍未付款。
