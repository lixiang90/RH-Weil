# C007：真实首prime误差的来源、迹类修正及共振符号审查

2026-10-14；起始HEAD `bbbd54c26e1f335c4238877a7954edd02146dab8`。
恢复AGENTS/README/STATE/check/show、Goal、C007、D20261014C和534。
只写本辅助文件，不改STATE/cadence，不单独计轮；未扩数值、无实验或下载进程。

## 1. 原件的符号适用范围

Connes–Consani作者55页稿[Selecta.pdf](https://alainconnes.org/wp-content/uploads/Selecta.pdf)
的原字节、SHA和视觉核读收据沿C004；本次复核既有原件文本的§6.7及(142)–(143)。
Theorem6.11（印页45）要求multiplicative源支持在 `[2^-1/2,2^1/2]`，
`ĝ(-i/2)=0`，结论为 `W∞≥T∞−c|ĝ(0)|²`，`c=4γ/log2`、γ≈2.94355。
另加ĝ(0)=0才得到E∞≤0。Intro Theorem1及综述写+i/2，实反演交换两号；
不能把版本/编号和这个符号区别抹掉。原trace身份Theorem4.6覆盖所有紧支持源，
但误差符号定理没有覆盖所有支持。

本冻结源两patch的外跨度为 `a+2b=log√6>log2`，因此联合源超出该小窗；
逐patch矩零不能将两项局部误差不等式自由极化为联合误差符号。
更重要的是其投影是实际实位Sonin投影S∞，不是P₂。

[CCM arXiv2310.18423v2](https://arxiv.org/html/2310.18423v2)（2024-05-04）
§4.7 Theorem4.6给θS的hilbertian同构，§4.8 Proposition4.8给共同entire空间；
内积依赖S。此次重读HTML §1、§4.7–4.8及既有PDF编号收据，没有找到E₂≤0的
独立定理。Intro把真实正trace与Weil functional的比较列为策略，不能消费为已证符号。

## 2. 完整返回修正可在ambient TC域精确分离

physical H=L²((0,∞),dx)，L=1_(0,1)，H₊=I−L，F=F₂，K=LFL，
R=(I−K²)^-1，h(K)=KR。531给||K||<1；534的S_r插值对每r>2成立，
尤其K∈S₃。因此

    C=h(K)−K=K³R ∈S₁.

这保留完整逆R，不是删去高return。令

    Φ(T)=LTL F H₊ + F LTL F H₊F.

真实双cutoff overlap为

    O=P₂−H₊−F H₊F+I
      =F L F−H₊F L R L F H₊.

按L/H₊四块展开、利用F²=I，有完整bounded-operator身份

    O=Φ(h(K))=Φ(K)+Φ(C).

核对四块：LL为K²，LH为K LFH₊，HL为其adjoint，
HH为−H₊FL K²R LFH₊。Φ(C)是真正ambient TC，因为C∈S₁且其余因子有界。
故任意固定compact-source A_g都满足A_gΦ(C)A_g*∈S₁；
它的循环trace和从完整source overlap扣除的分离合法。
这里没有把C006绕K∞的非交换H₃余项当作角谱cutoff，也没有使用那个未付joint limit。

### ambient TC诱导source TC的独立引理

固定有限测度源支持U，取任意ambient D∈S₁。由

    q_D(g)=Tr(A_g D A_g*)

诱导的L²(U)源算子属于S₁，且其trace norm≤|U|||D||₁。
证明：转log物理坐标后A_g是convolution。对unit向量ψ，
Tψ:g↦A_gψ的kernel为ψ_log(y−u)，因而

    ||Tψ||HS²=∫_U∫_R|ψ_log(y−u)|²dydu=|U|.

将D作绝对S₁ rank展开；每项源算子为T_v* T_u，trace norm≤|U|。
绝对求和给结论，不需要g导数或carrier限制。特别完整返回Φ(C)的源修正是S₁，
不仅仅是compact或对每个g有限。实自伴型取Hermitian部分保持同一结论。

### fixed smooth源支付actual bare循环trace与共同cutoff

对r≥1及固定g∈Cc∞(−W₀,W₀)，严格有

    ||A_g L F_r L||₁≤C_g(1+log r)/√r.                  (3)

证明保留L的截断边界。log物理输出v、输入w<0的kernel为

    2e^(w/2)∫_0^∞ g(v+s)e^-s/2 cos(2πr e^(w−s))ds.

对v∈[−W₀,W₀]，∂v^j只落到g。s一次非驻相积分的lower端点phase为
2πr e^w，不依赖v；故j=0,1均有kernel界
C_g min(e^(w/2),r^-1e^(-w/2))，其w平方积分O_g(r^-1)。
对v<−W₀，没有source/L截断边界：kernel为r^-1/2 H_g(v+w+log r)，
H_g(u)=2e^(u/2)∫g(t)e^-t/2cos(2πe^(u−t))dt。
H_g及H_g'=H_(g')属于L²(R)：u→−∞为O(e^(u/2))，u→∞用smooth source
非驻相积分给任意阶衰减。因而输出interval
I_r=[−log r−W₀,W₀]上的L²(input)→H¹(I_r)算子HS norm
≤C_g√[(1+log r)/r]。一维H¹(I_r)→L²(I_r)嵌入HS norm≤C√(1+|I_r|)，
两HS乘积给该中段的S₁ bound C_g(1+log r)/√r。

深输出x<e^-W₀/r直接用cos Taylor，不把无限log体积粗界：

    kernel=2Σ_(j≥0)(−1)^j(2πr)^(2j)x^(2j)y^(2j)/(2j)!
                 ·∫g(t)e^(-(2j+1/2)t)dt.

每项rank-one；x∈(0,e^-W₀/r)、y∈(0,1)的L² norm给绝对S₁和
≤C_g/√r（factorial压住固定2π常数）。深段与中段相加证明(3)。
这里C_g依赖有限source derivatives，未升级为whole源L² uniform费用。

实际K₂的dyadic系数固定，Σ_m(1+m)2^-m/2<∞；有限低反向项也满足fixed-source
TC。因此A_g L K₂为S₁且按scale cutoff在trace norm收敛，
A_g L h(K₂)=A_g L K₂ R亦为S₁。对反演源g*同样成立。
配合A_g F₂=F₂ A_g*（real source）、A_g normal及Z与F₂交换，
Φ(h(K₂))的两个source项都为TC，可以合法循环并合并为

    E₂(g)=2ReTr_low[h(K₂) M₂(g)].                      (4)

固定smooth g另给L Z_g H₊为S₁：它仅连接有限physical rectangle，
其R_g(log(y/x))/√(xy)核光滑，先作smooth有限域延拓再乘端点projection。
因此M₂及h(K₂)M₂本身为S₁，循环迹两端均在合法TC域。
该smooth-source TC性质同样不升级为whole L²源的uniform S₁费用。

有限scale两端cutoff的循环trace也合法：低核为HS，M₂为有限source boundary HS。
由(3)的trace-norm convergence及F₂ scale series的operator-norm convergence，
其source夹心trace趋于同一bare Φ(K₂)迹。每个scale F_r均互换U_t与U_-t，
故real-source Z亦与有限scale组合交换。这样第3节double-Fourier source核的
共同cutoff身份可以支付，而非从C006 conditional角trace推断。
此论证只用于固定smooth源；源L²扩张由532 actual compact性和已核局部核界另完成。

## 3. bare双Fourier的首prime共振核

实际F₂的distribution kernel为

    F₂(x,y)=Σ_(n≥0)cos(2π2^nxy)−cos(πxy).

以C006已核的单scale `F_r(x,y)=2cos(2πrxy)`记，则系数
α_n=1/2（n≥0），α_-1=−1/2，r_n=2^n。
有限scale cutoff与有限source boundary积分给bare low pairing核

    I_(r1,r2)(t)=e^(t/2)∫_(e^-t)^1∫_0^1
                         4cos(2πr1xz)cos(2πr2e^t xz) dzdx,  t>0.

bare E核为Σα_nα_m I_(r_n,r_m)(t)，并作实even延伸；actual消费使用第2节(3)–(4)
的共同cutoff trace论证，不凭distribution乘积自动略过。共振pair的L¹核费用
O(2^-m)可求和，非共振pair的phase-gap费用亦可求和，故局部核极限合法。

令a=log2，t=a+δ。只有n=m+1（m≥0）的无限族共振。其difference-phase项为

    I_m^-(t)=2e^(t/2)∫_(e^-t)^1∫_0^1
                      cos(2π2^m(e^t−2)xz) dzdx.

t=a时I_m^-=√2；sum-phase项为O(2^-2m)。对|δ|小，
2^m|δ|≤1部分与√2的差为O(|δ|+2^(2m)δ²)，总差有界；
2^m|δ|>1部分利用两个同号Si端点的π/2取消给O(2^-2m δ^-2)，总和有界。
因此cross源核有严格局部结构

    e_bare(a+δ)= [√2/(4log2)] log(1/|δ|)+O(1).          (1)

系数为正，1/4来自两实际F₂系数。低反向n=−1项只贡献有限smooth块；
其他scale-ratio在这两patch范围有严格phase gap，不能改变(1)的log系数。
有界余项含dyadic log-periodic振荡，**不宣称该余项S₁或逐carrier o(1/R)**。

参考冻结线性phase函数

    Ψ_m(δ)=2√2∫_(1/2)^1∫_0^1 cos(4π2^mδxz) dzdx

在Fourier规范∫f(δ)e^-iRδdδ下具有非负密度

    ζ_m(R)=√2/(2·2^m)·log[1/max(1/2,|R|/(4π2^m))],
             |R|≤4π2^m; outside=0.

Σζ_m(R)在大|R|上有c/|R|≤Σζ_m≤C/|R|。这解释±cross符号机制，
但不把参考linearphase当实际核，也不据此给固定R的strict Rayleigh证书。

## 4. 对角source核S₁与cross非S₁的不同证明

同一patch的相关跨度d=2b<log2，没有distinct-scale共振。
same-scale块r=2^m的difference项为

    J_r(t)=e^(t/2)/(πr(e^t−1))
      [Si(2πr(e^t−1))−Si(2πr(1−e^-t))].

其H¹(0,d)范数≤C_d r^-1/4。一个足够的界是：
0<t≤r^-1/2时|J_r'|≤C；t≥r^-1/2时
|J_r'|≤C/(rt²)+C/(r²t³)。前一界在rt≤1用Taylor；rt≥1用
A−B=O(rt²)、|sinA−sinB|≤min(2,|A−B|)，且两Si端点一起保留。
积分平方后||J_r'||₂≤Cr^-1/4。sum-phase项H¹范数O(r^-1)。
different-scale pair因rmax与phase gap给H¹ norm O(rmax^-1)；
每个max-index只O(m)项，所以全部dyadic H¹费用可求和。
有限低反向块亦smooth。故bare对角源kernel的even延伸在H¹，诱导S₁算子。
这里用一维核的H¹→S₁：先在较大有限interval延拓，再分解
T=(I−D²)^-1/2 [(I−D²)^1/2 T]，两因子都HS。

cross块K_c无需将(1)的bounded remainder证明为TC，即可严格证非S₁。
取非零χ∈Cc∞(−b,b)，以periodic Fejér finite-rank convolution P_N作
Q_N=Mχ P_N Mχ，||Q_N||≤||χ||∞²。其正approximate-identity核在δ≈0采样(1)，

    Tr(Q_N K_c)= [√2/(4log2)] ||χ||₂² log N + O(1).      (2)

bounded remainder的贡献O(1)，因为Fejér核非负、L¹ mass=1；
χ(u)χ(v)的变化只改变有界误差。若K_c∈S₁，左侧绝对值应被
||χ||∞²||K_c||₁统一控制，与(2)矛盾。这个检验不是单个g的符号反例。

## 5. 可消费的谱后果与尚需对账的接口

经主/逆审核第2节(3)–(4)的共同source核极限身份后，532的actual源compact性、
上节对角S₁和第2节完整return sourceS₁给

    E₂,U = [[D₁,K_c],[K_c*,D₂]] + S,
    D₁,D₂,S∈S₁,  K_c compact且非S₁.

offdiagonal block的谱为±singular values(K_c)，两侧positive trace均∞。
S₁扰动不能把任一侧变为finite positive trace：在该block前N个正特征向量张成的
投影上，扰动trace绝对值≤||S||₁；bare正trace趋∞，负侧同理。
因此actual E₂具有无限正、负指数。逐patch两个矩约束为finite-codimension压缩，
只改变finite-rank项，此后果保持。合法smooth源在V稠密，bounded二次型连续，
故存在严格E₂(g)>0及E₂(g)<0的逐patch两矩零smooth源；无需有限实验或显式R阈值。

这是可供主/逆审消费的完整sign候选：本稿给出actual bare Φ(K)与第3节source kernel
共同cutoff身份的fixed smooth TC证明(3)–(4)，以及第4节源谱性质；
必须核该新增域证明与全部scale/H¹常数，不能仅凭先前角组织接受谱后果。
若该身份支付，此结果只否定QW≥T₂无费用桥；不否定完整QW≥0，
也不证明实际最低态、全ζ谱限制、成长S或长期Goal完成。

唯一下一动作：主代理及不同组织逆审核Φ block身份、sourceTC引理、
H¹对角费用、Fejér cross检验及actual共同source核极限。无辅助pending process。

主结算收据：新ordinaryTC域已经主/不同组织逆审核闭环，535消费actual无限±结论，
主证明用N个合法窄源而不需本稿额外H¹/Fejér前件。宏观门槛另由reverse§8及
独立总体完成审计验收，不由本辅助稿或合同完成自动决定。
