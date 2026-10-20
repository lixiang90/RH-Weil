# 567/C030 独立终逆审

2026-10-20；独立审查者review_geometric_origin_567。结论：**PASS，限下述数学范围**。
审查的主稿含§7式(13)–(14)有限cutoff预算，两原稿含最终transpose/复合段及RR-budget段。
该PASS不代root消费、合同结算、远端核验或宏观Goal完成；主稿§8的结算描述在本审查时仍待root执行。

## 1. 实质纠正与已闭合前提

初稿§2未写基域，直接使用l(D)>1⇒D·H>0。独立审查要求明确代数闭域k，
或至少另付H0(O_S)=k等相应前提；否则整而非几何连通的射影对象可有l(O)>1。
主稿及函数域来源原稿均已补“代数闭域k上的光滑射影整曲面，H0(O_S)=k”。
实际消费对象C_k×C_k满足该前提，不影响其结论。当前未发现遗留的实质数学错误。

## 2. 独立逐式复核

- **RR负号。** 对D·H=0，l(±nD)≤1；假设D²>0，surface RR使l(K±nD)同时二次增长。
  非零截面乘法将一侧注入同一固定H0(2K)，产生矛盾。此处须真实截面、乘法单射、
  有效性与RR系数，形式Euler记号不能支付。已对照[Milne Thm1.2](https://jmilne.org/math/xnotes/pRH.pdf)。
- **有限cutoff预算。** 记x=l_j(K_j−nD_j)、y=l_j(K_j+nD_j)。若某侧为0，min(x,y)≤C_j平凡；
  若两侧非零，分别乘另一侧非零截面，得x,y≤C_j=l_j(2K_j)。式(13)给
  min(x,y)≥χ_j+n²d_j/2−n|b_j|/2−ε_j−a_j，故(14)系数和方向正确。
  |d_j+Q_W(g)|≤η_j、η_j→0、limsup R_j≤0确实推出Q_W(g)≥0。
  全部量须来自同一cutoff；每fixed测试的n_j与cutoff可依赖g，容量可增长但其总预算须支付。
  这是条件量化接口，尚未构造经典sections或RR/source误差，不是独立经典正性。
- **图与fiber。** F1=C×pt、F2=pt×C给Γ_nF1=q^n、Γ_nF2=1，故D_n=Γ_n−F1−q^nF2。
  自交(2−2g)q^n和m≠n的q^min(m,n)N_|m−n|一致；不可分交重数不能省略。
  归一化后−E_mE_n=a_(n−m)，包括n=m的a0=2g。对有限指标整体平移以及实／复化合法。
- **全周期source。** W_C=LΣa_nδ_(nL)，L=logq。分段u=y+jL得到式(4)的L系数，
  compact支撑只需统一有限和。全部扩域点数、proper powers、周期pole与contact保留，
  没有从有限点数拟合外推。cyclic Gram核商rank不被误当普通trace重数。
- **连续全Π反测试。** n_c=u·dΠ_c/du，既非累计N亦非primitive P；完整powers继承562的支付。
  正反两段均n_c(u)>0，而式(7)精确给primitive pairing。负段2点det为−4sinh²(rh)，
  非负偶φ的奇compact差分测试给式(9)的−8sinh²(rh/2)系数，严格为负。
  形式transpose、scaled shift以及C[R]上的乘法、*、σ身份在t<s时也成立。
  该代数不是已构造的scheme/effective category，负段σ不是正泛函；没有由形式trace制造正性。
- **整数负例与真曲线。** 两个未归一化Gram的det分别11和−5；v=(2,−1)在290模型给energy−2，
  即D²=2，在真F5例给energy30，即D²=−30。全次数Euler正性和实际曲线责任明确继承290/563，
  没有将这次有限矩阵运算升级为全n证明。
- **经典Γ对角。** 式(11)正半轴arch系数为w(u)/2=e^(−u/2)/(1−e^(−2u))，与563的全R偶延拓一致。
  raw coincidence测度(12)非负且在[ε,R]局部有限，原点约1/(2u)不可积。
  因而不能原样沿用连续point-graph自交；主稿保留finite-part/contact、全部Λ(n)与双pole，
  也未把off-diagonal正号当成renormalized自交符号。

## 3. 高维来源、旧资产与真实增量

另核[Deligne Weil I §3.2–3.7](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)：
交替配对、open symplectic geometric monodromy和有理local charpoly支撑even tensor非负系数，
coinvariant/cohomological公式控制全局pole，得到主稿所列q_x^(β/2+1/(2k))界。
主稿没有将局部sheaf纯性偷换为经典全球ζ零点纯性，也未声称一般标准Hodge正性或原Frobenius半单性已证。
073§7范围纠正与[Milne §3 Thm3.15、Aside3.18](https://jmilne.org/math/xnotes/pRH.pdf)相符；
其抽象条件定理未被撤销，562–566的既有消费不需撤回。

强旧扣除充分：001/002的极化充分定理、073的双向增长、307的实际degree来源、
363§5的RR/effectivity/完整source策略、563全周期证书及566 heat lift均不计本轮新实际ζ输入。
本轮可登记为全Π formal graph/复合/source联合反测试，以及允许增长容量的单尺度RR条件预算。
后者来自旧机制的明确量化，既非新的外部几何定理，也未支付经典的sections、误差或同源识别。
actual whole leading4/5、560成长K/core/coupling与Ξ未改，宏观完成门仍open。
下一章节准入门只在出现实际新同源身份/误差时晋级，不能凭来源名称延长C030。

## 4. 绑定版本

以下SHA256对UTF-8文件作CRLF→LF后计算，只绑定审查版本，不认证数学。

| 文件 | LF SHA256 |
|---|---|
| notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md | 96c0c5a62e4175705696a29ed28d890eb11cec6f7351dc763641b65f3fcaec8a |
| reviews/2026-10-20/grh-geometric-origin/function-field-source-audit.md | c2bac9824d324f45bce952b67c42495600118ffb9fef37456c22cbb755fe06fb |
| reviews/2026-10-20/grh-geometric-origin/generalization-admission-audit.md | cfffb22f2fefefa735d78733492589de83d4ace73308d611558a2156fad8ee22 |
| notes/073-tempered-polarization-tensor-category.md | 3a0a9ab86a5080c4f8af0e18895ef62f31c0e5be52dfbb6ce4580b51a4a76b93 |
| goals/contracts/C030-function-field-positivity-and-source-graph-tests.md | bd2e0d2c3d059e2b658c8b264b1e4b4d834bd7cc7b0b75f5fbd3a4df730023cf |

审查采取代数推导、源归一化和primary-source前提核对；没有机械增跑与上述证明同义的测试。
