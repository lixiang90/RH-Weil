# Perfectoid环域、层性与有理局部化：准确来源审计

2026-09-13。本报告为380及下一局部除子任务提供限定输入，不认证两部KL全文。
原PDF已在上一批保存，本批未重复下载或改变原字节。

## 标准环域和层性

[KL Foundations v5](../../literature/f1/kl-foundations-1301.0792v5.pdf)，
[固定来源页](https://arxiv.org/abs/1301.0792v5)，SHA256
`a6a117423db62aec072442bb15b70e3175bcc3b631bdcd6d74f740e3c6cfd942`。
主线程实际核读PDF82、89、92–94的相关定义／定理；PDF89、94渲染为PNG核对公式。

- Example3.6.6 / PDF89：在perfectoid系数上加入变量的全部相容p根，
  按加权Gauss范数完成，得到perfectoid Tate代数。
- Theorem3.6.14(c) / PDF94：有理局部化仍为perfectoid。
- Theorem3.6.15 / PDF94：stably uniform、sheafy及Tate／Kiehl性质。
  层性引用落在3.6.15，不把3.6.14单独写成全部层论结论。

给定C为379的域、X=t^(−a)U，取|t^(b−a)|≤|X|≤1。
相容逆根Y_n=t^((b−a)/p^n)X^(−1/p^n)的p^n次幂幂有界，
配合谱范数及380的双向稠密环映射，得到其中的完美化闭环域。
全体范数同时取log p次幂可转为原文通常的Q_p归一化。
与B_R的等距稠密身份、周期商和线丛仍是380自己的待审推导，不归给KL。

## KL II：McClintock独立只读来源审核

[KL Imperfect v3](../../literature/f1/kl-imperfect-1602.06899v3.pdf)，
[固定来源页](https://arxiv.org/abs/1602.06899v3)，SHA256
`97383900492daf1c6778959c37e993f67dd5ad379ac03c31049b870382e5d42c`。
代理核读§2.4全文、Theorem2.5.1、相关拓扑定义及下面的perfectoid定理，关键条件对照原页图像。
其报告明确返回上述原件SHA；未修改仓库、运行Git或启动代理。

Example3.3.12 / PDF61及Theorem3.3.18(i) / PDF64–65同样支持标准完美化环域；
Corollaries3.3.19–20给层性和结构层上同调消失。此输入包含a=b与p=2。

### 不能省略的稳定条件

Theorem2.4.15 / PDF40说明sheafy A的有理局部化A→S是2-pseudoflat。
但Definition2.4.4 / PDF36的Tor_1消失仅对**stably 2-pseudocoherent**模块成立。
非零因子f给有限自由分解0→A→A→A/fA→0，所以A/fA在代数意义上伪相干；
这还未验证Definition2.4.1要求的每个有理局部化商S/fS的完备性。
对自然Banach商拓扑，该条件等价于每个fS闭。

Example2.4.2 / PDF35–36在affinoid perfectoid情形给出fA闭、某个fS不闭的例子，
其中f在两侧仍为非零因子。因此稳定条件确实独立，不能由fA闭自动补出；
该例本身并不反驳380特定模型的Cartier正则性。

若已证明A/fA稳定伪相干，则

    Tor_1^A(A/fA,S)=ker(f:S→S)=0，

结合Theorem2.5.1可导入结构层的正则截面。另一更强的充分路线是证明fA闭且
**实际代数Banach商**A/fA uniform：由Theorem3.3.18(iii)商perfectoid，
再用Remark2.4.3得到所需稳定性。不能先分离化或uniform化商，再称原代数商已满足条件。

当前准确待证接口仍是对所有有理开集S证明ker(f:S→S)=0；
只检查径向子环域还不够。Cartier性也不会自行给DVR、有限长度或热带权的重数公式。

## 本批采用范围

标准环域的层性来源审核通过；尚未从相对Robba环的名称或有限系数定理导入
大实系数下的Proj／解析空间GAGA、一般φ模块等价、RR或通常ζ比较。
Tong原件继续保留为待深入核读来源。本报告不是完整F₁实现或优先权认证。

## 后续独立核读：非uniform商仍可给谱点

McClintock另行只读核对Foundations v5，输入SHA仍为
`a6a117423db62aec072442bb15b70e3175bcc3b631bdcd6d74f740e3c6cfd942`；
关键页检查原图。Definitions2.1.1、2.1.5 / PDF25–26及Definition2.2.1 / PDF27
给所用交换含幺、非阿基米德次乘法真正范数、完备性与有界代数结构。

Hypothesis2.3.1、Definition2.3.2 / PDF34定义谱点为α(1)=1且α≤||·||的乘法半范数。
**Theorem2.3.4 / PDF34：任何非零Banach环的谱非空**，
不要求uniform、约化、Noetherian、有限型或perfectoid。
Definition2.3.8 / 同页给H(α)=completion Frac(Q/kerα)及自然有界取值映射。
Definition2.4.6 / PDF40与Definition2.4.1 / PDF38支持相应Spa点；C中的p为拓扑幂零单位。

有界C结构自动使谱点限制为给定C范数：对c^n取n次根后令n趋∞给一侧不等式，
再对c^(−1)给另一侧。因此H(α)为C的完备赋值扩域，但未保证是C自身或有限扩张。
对A_y=C⟨V^H_p⟩，V及逆均范数1，故每个谱点|V|=1；
在U=t^yV下准确给|U|=exp(−y)。383只需把商谱点拉回已构造的环域，
无需先把非uniform商Q构造成sheafy空间。

同页Corollary2.3.7直接表述非单位等价于某谱点取零；本项目383保留闭商的显式论证，
从而同时交代Banach商的实际拓扑。代理本次只查来源，未替代383直接数学复核。
