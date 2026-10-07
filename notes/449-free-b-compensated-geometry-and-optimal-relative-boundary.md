# 449. 自由 b 的补偿几何与原计数接口中的最优引用边界

2026-10-07。状态 [T/R]：在 445 明确列出的外部通用输入与全 Hecke 7/8 bootstrap
成立的前提下，重新证明自由 b 的同源 low、全部 high 范围及全族延拓。
结果的准确边界为
\[
 \boxed{\sigma_\circ=\frac{1507-2\sqrt{921}}{1653}
       =0.874957069799168740\ldots .}
 \tag{1}
\]
对 F=Q(sqrt(-3)) 的全部有限阶 Hecke L 及全部 Dirichlet L，
Re s>sigma_circ 无零，principal s=1 极点允许。
没有断言边界线本身无零，没有独立认证原输入整链、外部 Lean 或 RH。

这严格改进 [447](447-larger-slot-discriminant-and-critical-strip.md) 的固定 b=1/8 边界。
另有完全有理、带严格附加余量的
\[
 \sigma_r=\frac{40773}{46600}=0.874957081545064377\ldots .
 \tag{2}
\]
AF 的零点比例没有被用作本稿行数输入；简单临界线比例仍未改善。

## 1. 确切前件、物理表达式及准入范围

原始输入固定于
[OpenAI September-30 paper.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
commit adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical LF SHA256
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
原输入包与 [445 §1](445-conditional-strip-improvement-and-family-continuation.md) 相同：

| 引用输入 [R] | 本稿重算的几何前件 |
|---|---|
| coefficientwise physical probe／Poisson、finite compensation、局部表及 ray 校准 | 同一 completed cn³ sums、原 masks、所有局部因子和正规化 |
| smooth calculus、Gaussian annuli、row sectors、generic reflected energy、quantitative additive Gram | §2 支付全部 rescaled subsets，不直接套 441 固定 b 的定理 |
| global／buffered reciprocal、Hecke 增长与 functional equation、完整外轮廓尾 | §6 在新局部域逐式重放；旧 sigma>=7/8 的 shared lemma 不直接代入 |
| witnesses、marked／plain／recursive moments、sixth-power amplification、uniform mesh | §5 的供给、whole slots、strict widths、系数类及零容量 |
| 全 primitive finite-order Hecke 7/8 结论 | 只用 beta_*<=7/8；不预先假定新边界 |
| fixed-ray prime asymptotic | 同一 A_T 的最终非零、subpower 逆及主留数 |

通用反射和 Gram 的源位置分别为 7663–7804、8340–8364；
source 1123–1209、1288–1315 和 2470–2506 控制 joint profile、Gaussian 和实际行 sectors。
其他接口的逐前件证明见 442–445；本稿给新实参数的范围及全部费用，
不以“参数连续”代替原算术前件。

固定
\[
 l_x=(1-\ell-b)/2,\quad l_y=(1-\ell+b)/2,\quad
 M=1-\ell,\quad h=(1+3\ell+b)/2,\quad
 C_b(s)=s-2/3-b/6.
 \tag{3}
\]
原 X=Z^(l_x)、Y=Z^(l_y)、P_i=Z^(ell_i)，sum ell_i=ell。
disjoint prime windows、Gaussian、S,T,xi、ray calibration、zero extensions、
joint errors、主双留数 w=1,z=1/6 和 Gaussian exp((s-5/6)²) 均保留。
这里 X,Y 是 compensated-probe 尺度，与 448 的 AF height X 不混用。

## 2. 自由 b 的完整 low 与真正交点

取 1/6<=ell<=1/5、0<b<=3(1-ell)/8。对 rescaled subset J，
写 d_J=sum_(i in J)ell_i、ell'=ell-d_J、M'=M-2d_J。
原 tuple norm ratio r_J 在固定正紧区间，且
\[
 X'=XZ^{-d_J}/r_J,\quad Y'=YZ^{-d_J}/r_J,\quad
 Q=q_{b_*}X'Y'\asymp Z^{M'},\quad M'+\ell'-1=-3d_J.
 \tag{4}
\]
M'>=1-3ell>0，l_x-d_J、l_y-d_J 也严格正。
P_a=Y'²/Q=q_(b_*)^(-1)Z^b>=1 最终成立；原 Gram 的固定多项式范围合法。

按 441 对 actual residual dyads 的推导，T_d<=H-3d_J+small；
共同 Gaussian profile 在提取 kernel saving、平方、正 sieve enlargement 之前固定。
原 generic reflected energy 给
\[
 \sum_{Nm\ll Q}|B_m^J|^2
 \ll Z^{M'+(5\ell-1+d_J)_+/4+\epsilon}.
 \tag{5}
\]
这一步不含 b。powerful fixed parts 的计数已包含，empty surviving slots 走同一包络；
原 S-primes、shared primes 与全部 permitted masks 保留。

本次保留 Gram 完整第三项：
\[
 \sum_{Nm\ll Q}|A_m(Y')|^2
 \ll(Q/Y')(1+P_a^{1/6}+P_a^2/Y')Z^\epsilon
 \tag{6}
\]
及固定 height seminorm。Cauchy 的 Q^(-1/2) 归一化给 fixed tuple
\[
 (X')^{1/2}Z^{\frac12\max\{0,b/6,2b-l_y+d_J\}
                  +(5\ell-1+d_J)_+/8+\epsilon}.
 \tag{7}
\]
tuple 数量 Z^(d_J+epsilon)、原外系数 q_(p_J)^(-3/2) 及 X' 缩短合计为 -d_J。
相对 l_x/2+b/12 的额外幂因此是
\[
 F(d)=-d+\tfrac12(11b/6-l_y+d)_+
                 +\tfrac18(5\ell-1+d)_+.
 \tag{8}
\]
每段斜率至多 -3/8，最大值在 d=0。ell<=1/5 给
\[
 L_{\rm low}=\max\{(1-\ell)/4-b/6,\ b/2\}.
 \tag{9}
\]
所取 b 范围使第一项占优，于是
|I_modified|<<Z^((1-ell)/4-b/6+epsilon)，保留全部原 Mellin、annular 尾与正 row loss。
更强的逐 J 单项吸收条件为 b<=3(1-3ell)/8；
本稿两个候选均在其严格内部。

由同一主留数的 C_b，low 交点准确为
\[
 C_b(\sigma)=(1-\ell)/4-b/6
 \quad\Longleftrightarrow\quad \sigma=11/12-\ell/4.
 \tag{10}
\]
超过 (9) 的第一分支范围，不能继续使用这个交点。
b<=0 的 P_a>=1 前件本稿未扩展；候选不依赖该端点。

## 3. 原实际 count 的连续自由 b 证书

仍用合法 kappa=3/4、alpha=5/6。对非 floor bins，
delta=2a-1∈[1/50,3/4]，q 是全部槽的 length-weighted mean amplitude，
error／zero slots 的 gain 为 0。令 x=q/delta∈[0,1/2]、y=1/2-x，
\[
 D=(37+34y)/18,\quad P=(7+18y+8y^2)/9,\quad
 J=(5/6-\delta)D+\delta P,
 \tag{11}
\]
\[
 R_*=1-\delta+(5/6-\delta)\delta P/(2J),\quad
 35/54\le J\le5/2,\quad1-\delta\le R_*\le1-2\delta/3.
 \tag{12}
\]
这些来自原 inverse／plain crossing，不因自由 b 增加新的 capacity。

在交点 (10)，d=h 的参考指数为
\[
 E_\sigma(h)=-1/4+5\ell/4+b/6
             +(1/2+\ell)\delta+\ell\delta x-h(1-R_*).
 \tag{13}
\]
其 b 导数为 R_*/2-1/3。令
F_(ell,b)=648(-2J E_sigma)=A(y)delta²-B(y)delta+C(y)，则
\[
 \begin{aligned}
 A&=252+756\ell-576b+(648+288\ell+720b)y\\
  &\quad +(288+1008\ell+864b)y^2+1152\ell y^3,\\
 B&=624-1440\ell-1176b+(504-420\ell-456b)y\\
  &\quad+(-48+120\ell+432b)y^2,\\
 C&=555-2775\ell-370b+(510-2550\ell-340b)y .
 \end{aligned}
 \tag{14}
\]
直接展开原 (13) 可核这个身份。
Q=4AC-B² 的常数项为
\[
 -530496b^2+1887840b\ell-184032b
 -10465200\ell^2+678240\ell+170064.
 \tag{15}
\]
对固定 ell，b 的极大点是 (2185ell-213)/1228，
极大值为 -1631700(1653ell²-66ell-35)/307。

取
\[
 e:=\ell_\circ=(33+8\sqrt{921})/1653,\qquad
 b_\circ=(2185e-213)/1228=-4/29+230\sqrt{921}/26709 .
 \tag{16}
\]
有 1653e²-66e-35=0，1/6<e<167/1000、123/1000<b_circ<124/1000。
A 的系数化为
(108036-82548e)/307、(160596+481716e)/307、
(42408+781416e)/307、1152e，均正。
在同一二次关系下，Q 的系数为
\[
 \begin{aligned}
 Q_0&=0,\\
 Q_1&=17404800(5465-31728e)/169157,\\
 Q_2&=1200(47597384-214807491e)/169157,\\
 Q_3&=4800(131691060e-18009311)/169157,\\
 Q_4&=14400(1377691e-209998)/8903.
 \end{aligned}
 \tag{17}
\]
Q_1,…,Q_4 的正性由上述有理隔离界直接给出。
所以对所有 y>=0，
\[
 F=A(\delta-B/(2A))^2+Q/(4A)\ge0,
 \tag{18}
\]
在真实 rectangle 上 J>0，故 E_sigma(h)<=0。
这证明连续域，没有从有限网格外推。
唯一等号是 y=0、delta_circ=(49-sqrt(921))/48∈(1/50,3/4)。

### 本交点及 count 包络中的最优性

固定 y=0、delta=delta_circ，有 R_*=2/3；此时 (13) 对任意 b 等于
\[
 -5/12+3\ell/4+(1/2+3\ell/2)\delta_\circ .
 \tag{19}
\]
它在 ell=e 为 0，ell 的斜率 3/4+3delta_circ/2>0。
因此 ell>e 时，无论 b 如何改变，这个 rectangle 内的点都会给正 E_sigma。
这仅排除保持 (10)、原 R_* 与完整 amplitude rectangle 的更强参数证书；
不是实际坏行达到包络、L 零点存在或所有方法的最优无零区。

## 4. 完全有理且严格的见证

取 ell_r=5831/34950=1/6+1/5825、b_r=617/5000，得
\[
 l_{x,r}=2480617/6990000,\quad l_{y,r}=3343183/6990000,\quad
 h_r=1891861/2330000,\quad \sigma_r=40773/46600.
 \tag{20}
\]
A、C、Q 系数全正，且 A_0Q(y)-Q_0A(y) 逐系数非负，
故由 J<=5/2，
\[
 -E_{\sigma_r}(h_r)\ge Q_0/(12960A_0)
 =10580567/347281513800000>10^{-8}.
 \tag{21}
\]
完整有理系数见精确审计输出。
447 已证 t_c<1/5841，而 1/5825>1/5841，故 sigma_r 严格小于 sigma_c。
另有 1653ell_r²-66ell_r-35=-9289/407167500<0，
正根在 ell_r 右侧，故 sigma_circ<sigma_r。小数不参与这两个比较。

## 5. 全物理范围、actual slots 与原 strict widths

一般 d 的同源 accounting 为
\[
 E_\sigma(d)=K_\sigma+(1/2+\ell)\delta+\ell q
 -h(1-R)+(d-h)(R+\delta/2-17/50),
 \quad K_\sigma=2/3+\ell+b/6-\sigma .
 \tag{22}
\]
它是完整 unfactored Mellin exponent 的代数重写；
444 的 strict labels 与 numerator 联合分配仍只扣一次 conductor deficit，g=qell。
q 的定义不改为只对 positive slots 平均。

selected nonfloor d∈[1/2,h] 的斜率至少 33/50-delta/2>=57/200>0，
所以由 endpoint 控制。floor 独用 delta=1/50、R=1、q<=1/100，
没有虚构 witness。d_min=1/100<=d<=1/2 的无槽上界
R=76/75-2delta/3 覆盖 floor，斜率为 101/150-delta/6>0；
最坏 q<=delta/2、delta<=3/4 给
E_middle<=-71/600+(329/400)ell-(421/1200)b。

在 (16) 的最优参数处，严格余量为
\[
 \begin{aligned}
 l_y-e-11b/6&=(1347-7133e)/1842>2/25,\\
 5e-h&=(6411e-1015)/2456>1/50,\\
 E_{\rm floor}(h)&=(290401e-49533)/184200<-1/200,\\
 E_{\rm middle}&=(292151e-84703)/1473600<-1/50 .
 \end{aligned}
 \tag{23}
\]
有理参数的 all-J Gram gap 为 148903/1747500，
ell_r/h_r-7/37=3420319/209996571，5ell_r-h_r=155417/6990000。

反证 beta_*>sigma_circ 时，Delta=beta_*-sigma_circ>0、
Delta<=(e-1/6)/4。取 zeta=Delta/32，则 zeta<1/384000，
ell/(h+zeta)>1/5>7/37、h+zeta<1。
斜率上界 2 使 h 到 h+zeta 的费用至多 Delta/16。
真实 high 比较 C_b(beta_*) 而非 C_b(sigma_circ)：
\[
 E_{\beta_*}(d)=E_{\sigma_\circ}(d)-\Delta .
 \tag{24}
\]
因此临界点的零附加余量仍留下至少 15Delta/16 的中央真实预算。

443 的 actual coefficient、whole-slot greedy spike 和 strict capacity 均依赖原 alpha、
kappa、供给与 fixed mesh，不依赖固定 b。此处重新满足这些前件：
只在 d>=1/2 选槽，w_i=ell_i/d<=2ell_i；
先固定 count loss、capacity decrement、rounding、plain mesh，再取 even K 和原 disjoint windows。
inverse 的 r_*>=23/37 保留第二 width 至少 9/37，
plain 的 m>=1/3 保留原 width；零容量仍走无槽版本。
实际槽与内部 plain pool 分离；整体共轭、固定 Theta 组合、outside-S inducing exceptions
及 finite S-supported units 均按 443 原证保留。没有供给加倍或把 arbitrary coefficients 准入。

## 6. Principal、small／large rows 与解析域

sigma_circ>5/6>401/600。局部因子不含几何 b；
442 的完整 local table 在 D2*(sigma_circ) 给 good defect
c_b=sigma_circ-3/50>81/100、ramified defect c_r=sigma_circ-1/20>82/100。
principal 四项幂仍为 -x、-6z、4-5x-6z、1-w-6z，最弱衰减 sigma_circ。
一般 good factor 的 4-6s-6z 项保留 theta=(-Re w)_+；
D1 中 epsilon_H=min(epsilon_0,1/50)，不能无条件用 epsilon_0。

完整 tuple 用 G_p 的系数表达式；一般轮廓不除 H_p。
只有已证明近 1 的 principal／dynamic 域使用 quotient。
whole-bin 先在 global 线上移动，再作 local buffered contour 和 partitions。
sigma_circ+1/2>4/3，small rows 用 D1(1/3) 的局部重证；
不直接套原只写 D1(3/8) 的 small lemma。
其相对 C_b(beta_*) 的自由幂为
\[
 E_{\rm small}=h(13/75)-l_y/2+63/5000
 =(2020475e-1127329)/9210000<-2/25.
 \tag{25}
\]
它单独覆盖 d<d_min 及 bounded nontrivial units。

large rows 的完整绝对 tuple 在 (2,2,z_infty) 给
\[
 Z^{B_0+(h+\zeta)(1+\epsilon)-\zeta z_\infty+\epsilon},
 \quad B_0=l_x/2+1+l_y=7/4-3\ell/4+b/4.
 \tag{26}
\]
先定 zeta，再在目标前选固定足够大的 z_infty，最后小 epsilon 和全部 height／tail 阶。
原 completed cn³ sums 仍靠绝对收敛；有限的是 compensation subsets 与 annular retained decomposition，
不是把全部 completed sums 错称有限。

principal 双留数保持同一个 c_S A_T 和同一 H_eta。
target-independent P0 可使 positive product majorant 给 |H_eta-1|<=1/2，
目标后扩大 S 只缩小同一 majorant。fixed-ray asymptotic 使 A_T 最终非零且逆为 subpower。
主轮廓先 global s，再 w=19/20、z=33/200，主双留数的 s 线最后仅向右移至 2。
三项真实留数余量分别为 m_w=l_y/20、m_z=h/600、mu<sigma_circ min ell_i，均正。

## 7. 统一顺序与全族 Mellin 反证

先固定精确几何、bootstrap 和共同 Delta。以 Delta 的小份额选择 count／moment losses、
strict capacity decrement、mesh 与 rounding，随后选 fixed even K、equal ell_i 和 disjoint windows。
此后选 mu=sigma_circ ell/(2K)>0、amplitude widths、prime 小幂、e；
principal 分别取小于 m_w/4、m_z/4、mu/4 的损失，中央总损失小于 Delta/4。
floor／middle／small 各保持其独立余量的一半。
zeta、z_infty 及所有 real exponents 在目标前固定，不用尚未选定的 mu 回选 K。

令
\[
 m_0=\min\{\Delta,m_w,m_z,\mu,1/200,1/50,2/25\}>0,\qquad m=m_0/4.
 \tag{27}
\]
目标 eta 确定后才固定最终 arithmetic data、同一 S、internal Sobolev／height 阶，
从而得到 finite A_eta、B_eta 和实际 detector ceiling tau_(0,eta)>0；
这些阶不依赖后选的 external tail order N。
所有 retained frequencies 共用一次 cumulative T1/2 allocation。
同一独立 physical probe J_eta=I_modified/(c_S A_T) 与 principal f_eta 都不含 cutoff T1，
满足
\[
 |J_\eta-f_\eta|\ll_{\eta,N}
 Z^{C_b(\beta_*)-m}(1+T_1)^{A_\eta}+Z^{B_\eta}T_1^{-N}.
 \tag{28}
\]
取 tau_eta<=min(d_min/100,tau_(0,eta),m/[4(A_eta+1)])，
再选 N_eta 使 B_eta-N_eta tau_eta<C_b(beta_*)-m/2，最后 threshold，
则 sigma_hi=m_0/8>0 可在全族目标前固定。
low 和 inverse A_T 的总小幂取 omega=Delta/2，得到
|J_eta|<<Z^(C_b(sigma_circ)+omega)，omega<Delta。

445 的小 Z 右移、Mellin／Fourier 识别和局部一致收敛仅使用 C 的斜率 1，
因此以 C_b 逐式重放。epsilon_*=min(Delta/2,m_0/8)>0 共同固定；
H_eta 非零排除 principal numerator 取消。
全族 supremum 无需达到，仍有目标零点 Re rho>beta_*-epsilon_*，与延拓至该线左侧矛盾。
所以 beta_*<=sigma_circ。

有限 Euler 删除在 Re s>0 不产生零；按 445 的二次因子分解，
全部 Dirichlet L 转移到同一严格半平面。principal s=1 极点保留，
L(1,chi_(-3))=pi/(3sqrt(3)) 非零。没有边界线或更高比例结论。

## 8. 证书范围与下一改进点

[独立优化推导](../reviews/2026-10-07/hybrid-free-b-geometry-optimization.md)
完整支付上述 source 前件和实参数预算。
[精确脚本](../scripts/hybrid_free_b_geometry_exact_audit.py) 用 Q 与 Q(sqrt(921))
核连续系数身份、正系数、几何余量和 189 个 direct endpoint 模型；
总 841 项检查不认证引用分析、实际素数、无穷轮廓或外部 kernel。

继续降低本接口边界，必须改进实际 count／gain 关联、moment 或已付 low 机制；
仅改变 b 无法越过 (19)。比例方向仍需 [448](448-canonical-type-i-admission-finite-gram-and-low-prime-fourth-norm.md)
所定位的原 signed response 联合算术费用。
这两个待办保留原研究目标，不以本参数族的最优性宣布整个目标完成。
