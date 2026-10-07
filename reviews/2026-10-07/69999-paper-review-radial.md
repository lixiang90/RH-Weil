# 69999/80000 正式论文独立审查（radial）

日期：2026-10-07。审查者：radial_review。

状态：最终冻结版本限定 PASS [T/R]。未发现尚未修复的数学阻断；此验收严格相对于正文明确假设的输入包 R。

论文 canonical LF SHA-256：92ba93da7cc568579b0b982bcd712e1382af749d05460c1fa4c8b25064df66d6。canonical UTF-8 长度：41612 bytes；1026 行。归一化为 CRLF、lone CR 转 LF，不作其他变换。数学冻结版本末次完整读取前后哈希均为 fa5a031ae40980c729aef83f272f9aa4dc77ce0295f4a5a49e21a36ad7fe772d；随后唯一排版改动为 appendix 前插入 clearpage。独立移除此一行后恢复相同旧哈希，故数学内容逐字相同。

审查对象：papers/seven-eighths-boundary-improvement-paper.tex，严格限制为 notes 441–445 的边界 69999/80000。独立逐节阅读了物理定义、variable-low、全部局部表、完整 tuple、whole-bin、principal/outer、实际 detector、joint strict errors、连续证书及全族 continuation。未采用 note 447 的 critical 参数。

## 1. 来源及验收边界

外部输入为：

- OpenAI September-30-2026 build/paper.tex。
- 固定 commit：adc7f1241b42e322a6451854ab7e4b4c146bf78a。
- canonical LF SHA-256：42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。

本审查只读该外部源，不修改或编译它。正文将其 generic smooth/reflection/Gram/moment/reciprocal/height/prime inputs 和原全 Hecke 7/8 结论组成明确的假设包 R。本报告的 PASS 是这些确切输入成立时的新参数推导，不是对原稿全部定理的独立重证、外部 Lean kernel 认证或 RH 证明。

核验方法包括直接读源、逐式代数推导及独立有理符号计算。未重跑旧审计，不用已有 JSON 的网格点代替连续证明。

## 2. 同一个物理对象与 low

物理表达式 eq:physicalsum 与原源 6885–6912 的定义逐项一致：

- J 指 rescaled slots，J^c 指 marked slots。
- 外系数为 (-1)^|J| q_(p_J)^(-3/2) eta_bar(p_(J^c))。
- 同一个 completed-index mask D | cn^3，及同一 Gaussian、ray、S、零延拓。
- completed 尺度变为 (X/q_(p_J),Y/q_(p_J),Z q_(p_(J^c)))；全部 slot windows 仍在原 P_i。
- 有限补偿是对先定义的物理探针的操作，不是用期望 high integral 重新定义探针。原源 3397–3412 的 completed sums 在初始 Mellin 线上绝对收敛，外部 m,s annular sums 有限；Gaussian 后来引入的全 annuli 必须保留或支付尾。

新参数给 M+ell=1、C(s)=s−11/16、C(sigma_1)=14999/80000。对 rescaled 子集：

d_J=sum_(i in J) ell_i，
ell'=ell−d_J，
M'=M−2d_J，
M'+ell'−1=−3d_J。

原 source 7663–7804 的 reflected-energy lemma 允许固定 bounded logarithmic lengths，没有将 ell 固定为 1/6。它要求实际 residual-row dyad、powerful/supported parts 冻结、原 zero masks、coefficient product form 与 common profile。这些前件在正文保留。原 source 固定几何 low 结论本身没有被直接替换参数。

Td 的精确式及 eq:dual 给 Td <= H−3d_J+small。保留 y=v+3ell_b+e_lambda<=Td+tau_ref，且 e_lambda 的负值只有 O(1/log Z)，因此 max(H,v+ell_b)=H+small。正文现已写出 generic E_ref、s_hyb=min(v,z_a,(v+z_a)/3) 与两分支推导：

- s_hyb=z_a 时 E_ref<=M'−Delta_H+small。
- 另一分支 s_hyb>=v/2；kernel saving 与 dual lengths 合计至少 Td/4−small。
- 显示的 frozen-part identity 正确；2A_0−N_0+B_0+4S_0>=0。
- 用 z_a<=ell' 得到 M'+(1+3ell'−2M'−2Delta_H+theta_N)/4+small，保留而未丢弃正部。

于是 row energy 的新增损失为 ((5ell−1+d_J)/4)_+。其 powerful-part count 已经计入，不可再乘一次。empty surviving slots 属于第一分支；不能通过假定活跃标记总长正值规避端点。

原 additive Gram (source 8340–8364) 的前件由 M'>=2/5、l_x−d_J>=11/80、l_y−d_J−11b/6>=1/30 支付。Pa>=1 和 Pa^2/Y'<<Pa^(1/6) 合法。固定 rescaled tuple 的 bound 是

(X')^(1/2) Pa^(1/12) Z^((5ell−1+d_J)_+/8+small)。

tuple 数、原 rescaling coefficient、缩短 X' 合计给

−d_J+(5ell−1+d_J)_+/8 <= −7d_J/8 <=0，

因为 ell<=1/5。这完成变参数 low 的新增费用。common Fourier profile、Gaussian arbitrary-saving outer tail、unit norm twists 与小量先后次序均保留了原 generic lemma 的统一性。

## 3. 局部 Euler 与完整 tuple

全部 j=0,...,5 的 P_p^* 表与 source 4086–4134 相同，包括 j=3 双项、j=5 boundary 和严格第二族。H_p defect 恒等式与 source 4139–4146 相同，消掉了 1−W 的分母，故 w_r<0 不会凭该分母产生伪极点。

D2* 最小边界的指数审计：

c_b=min(6sigma_1−401/100,sigma_1−3/50,47/50)=65199/80000，
c_r=min(sigma_1−1/20,3sigma_1−3/2)=65999/80000。

两个数都严格正，给予每点邻域正常收敛及全虚部 majorant。ramified finite product 是 q_u^epsilon 型，不被当作无限 good product。

D1 的 good/ramified 指数必须是 −1−epsilon_H、−epsilon_H，其中 epsilon_H=min(epsilon_0,1/50)。good E_p 的一般界在 w_r<0 时含 theta=(-w_r)_+；D2 中 theta=0。作者已按此澄清。

完整 tuple 直接用 G_p 替换 selected local H_p，未对一般 full tuple 使用 G_p/H_p。原 scalar quotient 由初始绝对区的 coefficientwise identity 一次提取。eq:highidentity 保持真实 sixth-free u-sum、所有 masks、原 Gaussian/Mellin tests 和完整 finite correction。选中因子及 H 的全高度 positive majorant 提供固定 B'，其与以后 external integration-by-parts order 无关。

## 4. Principal、whole-bin 与全部 outer rows

principal H_eta 的 |H_eta−1|<=1/2 来自

exp(C_0 sum_(Q>P_0) Q^(-1-c_b))−1<=1/2，

不是把无系数的 prime tail 直接当作 product 误差。P_0 在 target 前选择，后来扩大 S 只缩小该 positive majorant。

principal G_p/H_p 的四错误幂在 D2* 的最大值分别为

−sigma_1，−99/100，−21839/16000，−94/100。

最弱为 −sigma_1。实部/相位/虚部量词均正确，因此 R_(eta,Z)<<Z^(-mu) 的全高度范围合法，0<mu<sigma_1 min ell_i。相同的 actual ray prime asymptotic 给 nonzero A_T~(log Z)^(-K)，偶数 K 保正，inverse normalizer 只需 Z^epsilon。

main w,z residues 给同一个 c_S A_T 和 f_eta，Gaussian 变为 exp((s−5/6)^2)，C(s)=s−11/16。non-main integral 包括完整二维、三维尾；m_w=57497/2400000、m_z=32503/24000000 的正 saving 无误。

whole buffered bins 先在全局 s=beta_*+20e 移动；w=1−a−6e、z=17/50。移除外部 height box 以后才移动 retained bin 至 s=a+16e。buffered reciprocal 用 a+6e，D1(10e) 有 s+w>=1+10e。amplitude/error partitions 不能提前替代该 whole-bin contour；正文顺序正确。floor a=51/100 不制造 detector witness。

small rows 的 D1(1/3) 满足 sigma_1+1/2>1+1/3，D1(3/8) 在新边界则不满足。直接 G_p 无商估计给 off-row O(1)、on-row Q^(1/2)，保全部小 rows 和 units。独立 Fraction 核：

h*(13/75)−l_y/2+(63/50)/100=−172249/2000000。

large absolute rows 在 (2,2,z_infty) 以完整 tuple 控制，B_0=132497/80000，先选 zeta 再选固定 z_infty。此费用不依赖外部尾次 N，也没有删除难处理的 u。

## 5. Actual detector admission

bootstrap beta_*<=7/8 允许实际 plain input kappa=3/4；一般前件是 beta_*<=(1+kappa)/2，而不是在 beta_*>7/8 时仍强行使用 3/4。

相同 amplitude vector 上采用

0<=g_i<=delta/2，q=sum ell_i g_i/ell，

error 以及没有 positive spike 的 main slots 取 g_i=0。正 slot 只有 prescribed-bin-loss 上界和 g_i>0 的 lower bound；g_i=0 没有 lower bound。作者已删去对所有 Q_i 的虚假双向 asymp。

inverse amplification 的 actual map (u,a')->u(a')^6、conductor width one 与 slope alpha=5/6 来自原输入，未假定它依赖旧 ell=1/6。短 count 的 D_x/P_x/J_x 系数来自 marked/plain 两条支路在 kappa=3/4 的 crossing，非用 supply 增加直接宣称 theorem。

严格 inverse 宽度用于 r>=r_* 的支路：r_*>=23/37 给第二 margin 9/37；plain 支 r<=r_* 给 m>=1/3−small。saturated r>=1 用 amplification，m≈1/2 用 zero-slot plain；不能在 zero capacity 请求正槽。

实际 fixed presentation group Theta=<eta,T_hat>、nu in Theta 及

nu_bar 1_T=|T|^(-1)sum_(theta in T_hat)(nu_bar theta)

提供 original moment 所要求的固定有限系数类。plain 全共轭同时作用两 witness 与全部 primes，保 zero extension、support disjointness 及 inducing exception。source 15136–15170 的前件确已支付。outside-S local sextic ramification 阻止取消 fixed presentation；remaining S-supported units 仅有限，仍在 outer estimates 内。

whole positive slots 的 greedy gain 为 U^(2qz−delta max w_i)，不足 positive supply 时仍可支付 qz。严格 supply 为

ell/h−7/37=57659/3607833>0，
zeta<5ell−h=2521/120000 => ell/(h+zeta)>1/5>7/37。

uniform mesh 必须先于 K；physical w_i<=2ell_i<mesh。source 13456–13470、16280–16288 的 internal amplifier pool 从 U^(allowed_width/3)/2 开始，physical primes 至多 2U^mesh，mesh<allowed_width/6。因此两者 eventually DISJOINT；这里不是把 physical slots 包含在 internal pool 内。作者已纠正该方向表述。fixed K 的 annular offsets 仅在最后阈值吸收。

在这些 actual admissions 下才能得到 R_* count。J_x>=35/54 保分母正，1<t<3/2，floor 独用 trivial exponent one。

## 6. Joint full numerator 与连续 high certificate

local error expansion 仅在 dynamic line H 接近 one 时使用 quotient。global joins 不使用这个 division。每个 strict ramified prime 使用同一个 primitive conductor reduction，整套 distinct strict primes 只对 numerator 做一次 functional equation；没有每个 error subset 重复取 conductor saving。

全族各 j 的 local errors 和

Q^(z_0−w−(j−1)A*)<=Q^(z_0−1/2)，j>=2，

给 joint bound，包括 empty error subset。error g_i=0 与 main g_i 在同一个所有 slot 上平均，count 和 pointwise high 使用相同 q。full numerator 的 reflected value 及 deleted factors均在确切 buffered输入范围内。

独立 SymPy 有理计算以正文完整 E_sigma(d)、R_*、D_x/P_x/J_x 为起点，完成：

10368 v J_x(-E_0)
−(3+5y)[(4v delta−79)^2+49]
−4y{4v delta[(1+3y)(15+32y)delta+9−13y]+265+3485y}=0。

在 y in [0,1/2]、delta in [0,3/4] 每项非负；v<=17(3+5y)、J_x<=5/2 给 49/440640。又 2D_x−3P_x=4(1−2y)(3y+4)/9>=0，故 R_*<=1−2delta/3。沿同一 C(s) 的 geometry change 精确为 t(−1/4+delta+q+3R_*/2)<=5t/3，t=1/20000，得到

49/440640−1/12000=307/11016000。

这已包含 reference-exponent change，不能再减一次 1/80000。证明是全连续区间恒等式加 positivity；JSON 的 finite points 仅作代数审计。

d斜率、floor 和 intermediate 的显示界皆与同一 accounting 相容。floor 精确值 −4327/750000。独立展开 intermediate endpoint 的最坏 q=delta/2 得到

E_sigma(1/2)=(1562725 delta−1322422)/6000000，

在 delta<=3/4 为负，足以支持正文更弱的统一 −120907/36000000 界。zeta=307/352512000 的扩区费用<=m_ad/16，留 307/11750400。相对 C(beta_*) 另减 Delta_1>0；全部 nonprincipal dyads 均覆盖。

## 7. 量词、height 与全族反证

新 low、principal、high 均使用同一 physical I_mod、same S、c_S、A_T、H_eta、f_eta。低侧 real loss 先用 global Delta_1 支付；high mesh/rounding/strict capacity losses先用 target-independent m_ad 支付；之后选 K/windows，再选 mu=sigma_1 ell/(2K)。mesh 不因 K-dependent mu 变小而重选，无循环。

internal moment/Sobolev/seminorm orders 在 target arithmetic data 之后固定，A_eta、B_eta 此后不随 external N 变化。literal detector height hypothesis 的 preliminary ceiling 在这些 internal orders 后给出；再选 tau_eta，然后 external N_eta，最后 threshold。共同 T_1/2 buffer 只分配一次给物理 z、witness 和 prime frequencies。外部 N 增加只提高 test seminorm 费用。

omega=Delta_1/2 和 sigma_hi=m/2 是全 target 共同的严格正 exponent；tau_eta、N_eta、常数和阈值可依 target。这正是原 continuation lemma 需要的区分，未假设所有 arithmetic constants 全族一致。

Z→0 的 Gaussian absolute-line bound 与 Z→infinity 的共同 exponent saving 给 Mellin integral 在 Re s>beta_*−eps_* 局部一致收敛。Fourier inversion 最初在 Re s=2 成立，identity theorem 延伸，再以 |H_eta|>=1/2 得 reciprocal 的 holomorphic continuation。共同 eps_* 在选 target 前固定，故 supremum 无需 attained 即可选出矛盾 zero。imprimitive finite Euler factors 在 Re s>0 不为零，Dirichlet quadratic transfer 的唯一 principal pole pairing由 L(1,chi_-3)>0 排除。

该结论是严格 Re s>69999/80000，允许 principal pole。没有边界线、RH、simple-zero proportion 或规范 Weil arithmetic bridge 的追加结论。

## 8. 审查中已要求的修订与最终绑定

审查反馈的五项已由作者在论文中补充：

1. D1 的 epsilon_H 与 negative-w 的 theta 因子。
2. inverse/plain strict widths 的明确 branch scope。
3. amplitude bins 对 zero-gain slots 不虚构下界。
4. fixed Theta prime coefficients 及 full conjugation。
5. common-profile E_ref 的新 low branch algebra，以及 physical slots 与 internal amplifier pool 的 DISJOINTNESS。

这些修订均澄清本次新推导的真实前件；不扩展为新的 critical bound。

最终 paper canonical LF SHA-256：92ba93da7cc568579b0b982bcd712e1382af749d05460c1fa4c8b25064df66d6。
最终状态：限定 PASS [T/R]。正文各项 scope 与前件已明确；本审查不认证外部输入包、不认证外部 Lean、不产生 RH 或边界线上无零结论。

冻结版本的位置核对：物理对象与 low 为161–359行；完整局部表、Euler与principal为361–545行；whole-bin/outer为547–590行；actual counts为592–725行；joint full numerator与连续证书为727–850行；量词、height、Mellin与Dirichlet transfer为852–976行。审查全文还包括输入表、摘要及979–1026行的来源与范围说明。
