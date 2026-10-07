# κ反馈三次边界正式论文：独立全文审查

2026-10-07。审查人 `/root/twisted_research`。
结论：**限定 PASS [T/R]**。全文新读正式论文，并从物理身份、实际计数
前件、连续证书和量词闭合逆核结论；不是把451研究稿的PASS直接移作
论文认证。审查发现的plain statement缺少显式slot mesh前件已由作者修复，
冻结版本无未解决的阻断问题。

## 1. 最终源绑定及准确结论范围

审查对象：[正式论文源](../../papers/kappa-feedback-cubic-boundary-paper.tex)。
实际最终文件为990行、39181个canonical UTF-8字节，canonical LF
SHA-256：

`16c0ba50a2917f2ead56843eabf55b62fbbe214e162cff373b4d8554f84315ee`。

初读版本为978行、38674字节、SHA
`89614f1ff57d97ddc3fdae7232e3f724699d01107fcc80db4f5ac6ca9cb60e47`。
我随后重新全文读取最终990行，确认前件修复、审计计数说明及版面改变。
本报告绑定最终实际文件，不继续绑定初稿。

原引用源为
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，
固定commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，实际canonical
LF SHA-256为
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。

本次以该源的具体前件为基础审核新论文；仍把如下底层输入作为
论文Definition 1的准确条件包 `R`：finite Gauss/full correlations、
reciprocity、完整support及自然零延拓；coefficientwise probe/Poisson和
finite compensation；原local表与ray校准；smooth/Gaussian/reflection
sectors、通用reflected energy、完整additive Gram；global及buffered
reciprocal、growth/functional equation和外尾；actual witnesses、marked/
recursive inverse moments、sixth-power amplification；fixed-field计数、
fixed-ray prime asymptotic；**全primitive finite-order Hecke族的7/8输入**；
有限Euler删除及quadratic transfer。

extended positive-slot plain lemma由论文§2重证，不作为超范围原statement
引用。其底层local correlation、kernel及support等仍是R依赖。
论文主定理准确为：在同一R下，`F=Q(sqrt(-3))`全部finite-order Hecke
L及经transfer的全部Dirichlet L在 `Re s>sigma_*`无零；principal pole
允许，边界线不包括。唯一bootstrap是 `beta_*<=7/8`，旧自由b边界仅
作精确比较。没有新增RH、外部kernel认证或简单临界线比例结论。

本次直接回核原源12492–12585、12910–13030、6705–6780和已读完整
plain proof12532–15015、actual selection15105–15475；物理、low、local、
principal、outer与continuation源375–505、4010–4180、6810–6940、
7663–7804、8340–8364、8654–8835、15520–15920、16375–16463
与新论文逐项对照。此前完整源读的证据另存
[450独审](450-plain-kappa-extension-review-twisted.md)；本报告独立检验
最终论文的完整新表述和应用。

## 2. Extended plain proof及修复的statement前件

最终论文189–218明确：对每个epsilon和固定bounded length range，先选
`eta_mesh`，positive data同时满足
`max_i z_i<=eta_mesh`、`n1+n2+6kappa z<=M`以及必要的
`beta_*<=(1+kappa)/2`。mesh先于slot count且uniform于
`kappa in[37/50,1]`；这与原源12547–12578的正确量词相符。
原零slot情况保留其bounded非负plain lengths、nonprincipal family及
原no-conductor-lower-bound范围。

我最初指出初稿只说“mesh can be chosen”却未将 `z_i<=mesh` 写成
命题前件，会字面扩大准入。作者已补成显式条件；证明和应用的K选择
原已遵守该条件。此问题在最终版本中关闭。

原lower endpoint的每个数值使用点在最终225–307逐项支付：

| 使用点 | 新范围的实际计算 |
|---|---|
| prime estimate | `s_k=(1+k)/2>=87/100`，且不小于整族beta；保持原正contour displacement、finite Θ系数、weighted Fourier measure及所有高度 |
| terminal width | `z<=25M/111`取代旧 `2M/9`，但真正费用仍只用 `k z<=M/6` |
| same-band comparison | `6k-1>=86/25`、`z<25M/516<M/20`，保留旧 `M/15`余量 |
| clipping/mask erasure | `6k-1>=0`，原actual defect及whole-slot removal cost `k d_z<=F_act/6+eta_pool`不变 |
| numerical Lipschitz | `0<=6k-1<=5`，保留width floor、finite depth、strict drop |

comparison的更强直接数值为 `197M/258+xi`及 `40M/43+xi`，
分别小于论文仍使用的 `23M/30+xi`和 `14M/15+xi`。
`1/20-25/516=1/645`是严格有理余量。

两次complete extraction、共同characters、full local F2、p^6 pool、
actual child width、中心化equal-product、Θ exceptions和zero-mask
erasure都保持原对象；新的κ范围没有改local有限域计数。
实际child width严格下降，先全部zero-slot，再positive-slot；同带先
uncentered再centered，有限递归不形成循环。plain seminorm与height
orders沿原有限递归固定，外尾阶N后选，不反向修改内部阶。

这一项是重放原proof得到的范围扩展；有限有理audit不认证这些被引用
的底层估计。论文309–311准确保留了该依赖范围。

## 3. 实际counts、每个width和源coefficients

§3的 `q` 是全部物理槽的length-weighted actual amplitude，error及zero
槽gain为0。没有改为只对positive槽归一化。原双plain witness取两份
产生第四spike，与inverse线和long branch共同导出论文的

\[
 D=3-(1+2c)x,\quad P=(2-2cx)(1-x),\quad
 t=1+\delta P/(2J),\quad
 R=1-\delta+(5/6-\delta)\delta P/(2J).
\]

我独立核了crossing身份及bounds：`D>=455/222`、`P>=86/111`、
`35/48<=J<=5/2`、`1<t<3/2`。crossing的 `r(3/2)=1`且
`r(1)>=8/13`；`t-r(t)`由endpoint给 `[1/3,1/2]`。
所以inverse branch选出的 `r>=r_*(t)`有 `z_M<=5/26<1/5`；
plain branch的 `m>=t-r_*(t)`给 `z_P<=25/333<1/5`。
这些是相应branch的前件，不是任意witness的无条件r/m范围。

最终363–371两种request都减同一预先固定的positive `nu0`：

\[
 1-r-2z\ge2\nu_0,\qquad
 3-2r-8z=4(1-r-2z)+(2r-1)\ge8\nu_0+1/5-o(1),
\]
\[
 1-2m-6\kappa z\ge6\kappa\nu_0.
\]

positive margin使actual dyadic offsets和whole-slot rounding可在阈值
吸收。zero-capacity neighborhoods、`r>=1`、`m>=1/2`分别走原
no-slot或amplified endpoints，没有令shrinking request满足本来不成立
的moment theorem。

actual selection仍只在 `d>=1/2`，单槽长度 `w_i<=2ell_i`；
`e/(h+zeta)>1/5`严格供齐两branch。losses、capacity decrement、
mesh及rounding先于even K，amplitude widths后于K。
原finite Θ coefficient lists、共同presentation、自然零延拓、whole
conjugation、outside-S inducing判别及与内部pool分离的physical windows
全部保留。common mask不能变为row-dependent coefficients；
S-supported有限sixth-power-free rows由bounded/outer处理。
physical与witness参数不必相等，但共同Sobolev及一次cumulative
`T1/2`费用保留。

## 4. 同一physical probe、完整low与Mellin normalizer

§4展示的exact finite compensation保持
`(-1)^|J| q_(p_J)^(-3/2) bar eta(p_(Jc))`、原
`I_(eta;p_(Jc))(X/q_(p_J),Y/q_(p_J),Z q_(p_(Jc)))`。
underlying windows先于ray/S限制disjoint，操作不重选其他槽尺度。
原completed `c n^3` sums仍为无穷绝对收敛和，有限的是compensation。

我另以符号计算重推论文434–447的frozen-parts identity。用
`H=M'-O-Delta_H`代入，等式逐项相消；
`T_d-(H-3d_J)`由actual sector inequalities而非虚构`H=M'-O`
得到。generic reflected energy保留kernel saving、实际dual dyads、
common Gaussian density、powerful parts一次计数、shared primes及
empty marked lists。全row energy为显示的
`M'+(5e-1+d_J)_+/4`。

Gram第三项 `P_a^2/Y'`没有删掉；`P_a~Z^b`最终满足前件。
tuple count、rescaling coefficient和 `X'^(1/2)`准确合计 `-d_J`。
low分段函数斜率最大 `-3/8`，all-J gap大于 `2/25`使所需branch
合法。low exponent准确等于 `C_b(sigma_*)`，没有复用原fixed-
geometry low theorem作范围外结论。

主信号的Mellin幂在论文403–409已修明：raw kernel的z系数
`1-l_x=h-e`，exact principal tuple贡献 `Z^(e/6) A_T`，所以

\[
 s+l_x/2-1+(h-e)/6+e/6=s+l_x/2-1+h/6=s-2/3-b/6.
\]

`h/6`合并后不再加 `e/6`；同一个 `A_T`最终为logarithmic大小。
low/high统一除以 `c_S A_T`，没有换成自由normalizer。

## 5. 连续三次证书与actual κ反馈

§5的reference `kappa_*`只作代数。一般 `Q0`是严格凹b二次式；
我独立验证其二阶导数、一般极大点、极大值以及代入
`k=5/6-e/2`后括号成为 `-p(e)`。三次root隔离和sigma消元一致。

论文新增的10个strict rational enclosures，我从保存输出的完整
`(1,e,e^2)`有理系数重新计算interval Horner，逐项严格包含在表2的
开区间中；未用浮点符号替代证书。附录的A、B、C逐系数公式也由
正文的 `W-h=-b/2-ey`直接展开一致。

`A_j>0,C_j>0,Q0=0,Q1..Q4>0`与square completion给任意实delta
的cleared polynomial `F>=0`；`E=-F/(2J)`仅在实际 `J>0`
rectangle使用。唯一等号在实际rectangle内部，`y=0`、
`delta=(5-9e)/(6+18e)`、`R=2/3`。连续域不是49点外推。

反证时真正调用的是 `k_act=2beta_*-1`，其positive-slot前提由
定义精确满足；referenceκ*没有被偷用。独立微分得到

\[
 \partial_kR=\frac{(5/6-\delta)^2\delta x(1-x)^2}{3k^2J^2}
 \le625/36963<1/50.
\]

`k_act-k_*=2Delta`的费用小于 `Delta/25`。完整E相对于
`C_b(beta_*)`只扣一次Delta，端点保留 `24Delta/25`；所有
selected `d in[1/2,h]`由正斜率控制，extension `zeta=Delta/32`
花至多 `Delta/16`。所列 `359Delta/400`与中央其余losses
小于Delta/4相容，不双扣旧边界偏移。

## 6. 全部physical ranges和解析域

我从原unfactored exponent另行符号重推新论文的fullE、floor和
middle端点公式，均一致。参数的exact区间严格给：floor
`<-1/200`、middle `<-1/50`、small `<-2/25`、supply gap
`>1/50`以及 `h+zeta<1`。floor独用理想count R=1；
`d<=1/2`独用no-slot count，不编造witness或selected供应。
small/bounded units不塞进generic moments。

local表不含新几何b。完整defect给new principal box的
`c_good=sigma_*-3/50>81/100`、
`c_ram=sigma_*-1/20>82/100`。general D1仍保留
`theta=(-Re w)_+`及 `epsilon_H=min(epsilon0,1/50)`。
完整selected G系数式用于whole-bin continuation，不能在一般域
除可能为零的H。正majorant允许目标前P0给principal H近1，
目标后扩大同一S只改善该majorant。

fixed-ray正渐近给同一
`A_T=(-1)^K Z^(-e/6) product S_i`最终非零且逆为subpower；
`c_S`保持原正测试、两次ζ留数及1/6 Jacobian。principal
留数的四错误指数和 `m_w=l_y/20,m_z=h/600,mu`均有真实余量。
new μ小于 `sigma_* min ell_i`；未沿用旧7/8衰减。

small线重新支付D1(1/3)，不直接引用旧D1(3/8)声明。full tuple
和完整numerator给精确small式。large在 `(2,2,z_infty)`用完整
绝对tuple，目标前在zeta后固定足够大z_infty，scale degree不
依赖后选外尾阶N。whole-bin先global/local move再pointwise
partition；strict labels共用一次numerator deficit。

## 7. 统一量词与整族Mellin闭合

最终§9的完整顺序合法：geometry、beta bootstrap、共同Delta和
k_act → losses/decrements/mesh/rounding → even K/windows →
μ和amplitude/prime/buffer losses → target及same final S →
internal finite orders与 `A_eta,B_eta`、actual height ceiling →
tau_eta → external N_eta → eventual Z threshold。

所有实参数及共同 `m0`在目标前固定；principal和中央各用独立
预算，不依赖尚未选定的μ反选mesh。目标可改变常数、finite orders
和threshold，却不改变共同omega和sigma_hi。
内部orders不依赖后选N；physical、witness、prime频率共用一次
cumulative `T1/2`，没有在下一估计重新分配。

论文的实际high合同含有限 `A_eta,B_eta`且 `J_eta,f_eta`本身
不含analysis cutoff。`tau<=m/[4(A_eta+1)]`支付height因子，
随后N支付外尾，给共同 `sigma_hi=m0/8`。low及逆normalizer
总loss为 `omega=Delta/2`，从而共同
`epsilon_*=min(Delta/2,m0/8)>0`。

small-Z右移只用于在全正轴定义的Gaussian principal signal，
无需延伸J或在小Z除AT。Mellin transform局部一致收敛后，
先于线2经Fourier inversion识别，再经identity theorem得到
reciprocal延拓；没有跨目标零点移线。`|H_eta|>=1/2`
防止numerator消零。全族supremum不必达到，仍提供适当目标零，
因为epsilon在目标前共同固定。

quadratic transfer的Dirichlet因子在0<Re s<1不能以pole消零；
Re s>1由Euler积处理，Re s=1除principal pole外同理；s=1的
潜在取消用原 `L(1,chi_(-3))=pi/(3sqrt3)>0`处理。有限Euler
删除在Re s>0不改变零。主定理的whole-family范围、允许pole和
不含boundary三项均匹配证明。

## 8. 审计、版本与未认证范围

脚本复跑通过149个**计数检查**，包括49个模型各两项identity，
共98项；内部算术assert没有都计入149。打印JSON与保存JSON逐项
相同。脚本的source SHA字段是固定metadata，不读取原source或451；
本报告另行读取并计算源hash，二者不能混为同一认证动作。
最终附录940–951准确说明这一范围。

绑定的脚本canonical SHA为
`e03d6536378fff4b51625ab71fa5eace9fcbf4fe1156ccb6ae048f03bf96bc68`；
保存输出canonical SHA为
`309f275701a1d96c245eb067d49b00598df4af8e380d220944de250fd2e9d7ba`。
冻结451仍为 `17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487`。

我另外核对新TeX无duplicate labels、missing refs或missing bibliography
keys。这是数学与静态源审查；PDF编译、13页逐页视觉验收和manifest
哈希属于另一验收对象，本报告不以作者报告的编译状态替代自身视觉审查。

旧69999源仍为
`92ba93da7cc568579b0b982bcd712e1382af749d05460c1fa4c8b25064df66d6`；
旧自由b源仍为
`5df2b6ad687572229e2c4d41292bee6cf81b57a13b762173d26732169f1688db`。
未编辑旧论文、notes450/451、脚本、输出或math源。

最终PASS仅确认在论文精确R下的新推导和全族closure。原输入整体的
独立认证、external kernel、RH和finite-constant whole four-prime response
均不在本次证明范围；未完成的比例支线不会被登记为已付输入。
