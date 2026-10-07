# 有效 κ 与原物理 detector capacity：独立条件准入报告

日期：2026-10-07。状态：**相对于明确的通用 [R] 前件，原 nominal detector-count 与 adaptive crossing 的实际准入通过**。本报告核查长度、系数类、原零延拓、严格 width、实际选槽、群例外及高度顺序；不是重证外部 recursive moments，也不宣称新的无零半平面、完整 high estimate、RH 或 Weil/RR 算术桥。

## 1. 固定来源、当前参数与真实范围缺口

只读来源为 E:\codex-build\math\preprints\The-Quasi-Riemann-Hypothesis-September-30-2026\build\paper.tex。
固定提交为 adc7f1241b42e322a6451854ab7e4b4c146bf78a；canonical LF SHA256：
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
（766316 字节）。以下行号均绑定这一版本。

当前新几何取
\[
 \sigma_1=\frac{69999}{80000}=\frac78-\frac1{80000},\qquad
 \ell_1=\frac{10003}{60000}=\frac16+\frac1{20000},\qquad
 h_1=\frac{32503}{40000},\qquad b=\frac18.                         \tag{1}
\]
保留同一个 physical finite compensated probe、实际 sixth-power-free rows、原 fixed ray data、slot profiles、disjoint prime windows 和全部 zero-on-nonunit extensions。

设 \(\beta_*\) 是原全集有限阶 primitive Hecke characters 的共同零实部上确界，当前反证条件为 \(\beta_*>\sigma_1\)。源 Part I 的共同 \(11/12\) 输入给 \(\beta_*\le11/12\)（6812–6814 行）。若另外接受已提交分析所引用的原 \(7/8\) 结论，则有更强 bootstrap
\[
 \sigma_1<\beta_*\le\frac78.                                     \tag{2}
\]
这些均是明确的 [R] 输入；本报告没有从正在证明的 \(\sigma_1\) 半平面获得零自由性。

**实质性范围问题。** 源 lem:plain 明定 \(3/4\le\kappa\le1\)（12532 行），在 \(\kappa<1\) 时另要求 \(\beta_*\le(1+\kappa)/2\)（12564–12566 行）。因此当 \(\sigma_1<\beta_*<7/8\) 时，不能静默取
\(2\beta_*-1\in(29999/40000,3/4)\) 并调用原 lemma；它没有覆盖这段参数。

无需扩大原 recursive theorem 的范围。采用
\[
 \boxed{\kappa_{\rm eff}:=\max\{3/4,\,2\beta_*-1\},\qquad
 \Delta_{\rm eff}:=\max\{\beta_*-7/8,\,0\},}
\]
\[
 \kappa_{\rm eff}=\frac34+2\Delta_{\rm eff},\quad
 \kappa_{\rm eff}\in[3/4,5/6],\quad
 \beta_*\le\frac{1+\kappa_{\rm eff}}2.                             \tag{3}
\]
这样同时落在原 theorem 和原 uniform mesh 的实际范围。
在 bootstrap (2) 下，\(\kappa_{\rm eff}=3/4\)、\(\Delta_{\rm eff}=0\) **精确成立**；不是把负的 \(\beta_*-7/8\) 填进原非负容量损失公式。

若记 \(\Delta_1=\beta_*-\sigma_1>0\)，则一般仍有
\[
 0\le\Delta_{\rm eff}\le\Delta_1.                                \tag{4}
\]

## 2. 确切 [R] 前件及不依赖固定 geometry 的部分

| 外部输入 | 源行号 | 准入性质 |
|---|---:|---|
| shared bins、actual zero ceiling | 4281–4321；6821–6829 | floor 为 \(51/100\)；非 floor bin 的 \(a\le\beta_*\)，不要求 \(\ell=1/6,h=13/16\) |
| prop:detector-witness | 4510–4547 | 任意 \(t\in[1,3/2]\)，同 presentation、同 twist height 的 actual inverse/plain witnesses；须保留其 loss/height 条件 |
| lem:marked | 9220–9269 | either common sign、原 masks、row-independent prime coefficients；严格 \(r+2z\le m-c_1,\ 2r+8z\le3m-c_2\) |
| lem:inverse-amplification | 12362–12389 | 原 sixth-power-free rows 与 no-slot inverse；统一 bounded actual lengths、rowwise smooth tests |
| lem:plain | 12492–12578 | \(\kappa\in[3/4,1]\)，fixed \(\Theta\) coefficient class、moving-radical ledger、inducing-family 排除、统一 short-slot mesh |
| physical prime bin bound | 15015–15061 | 保留 fixed-ray expansion、原 prime window/mask 和 cumulative height allowance |
| actual amplitude subdivision、greedy spike | 15064–15134 | 任意固定正 slot 系统；gain 用实际 whole slots，rounding 可付 |
| moment coefficient identification | 15136–15170 | 原 physical prime factors对应固定 \(\Theta\) 组合；whole-product conjugation 保留零与支持 |
| common-density smooth calculus | 1123–1209；15163–15167 | 允许 rowwise witness parameters 的固定 Sobolev/height cost；不允许 row-dependent prime coefficients |

本报告以下重做的是源 prop:detector-counts（15185–15446）和 cutoff crossing（15949–15992）的实际准入，不把其中 current Part II 的 \(\Delta>0\)、固定几何或容量供给数值直接移植。

源 \(a\le\beta_*\) 只用实际零的 supremum 定义，不用 supremum 的 attainment。故每个非 floor retained bin
\[
 \delta:=2a-1>1/50,\qquad
 \delta\le2\beta_*-1\le\kappa_{\rm eff}\le\alpha:=5/6.              \tag{5}
\]
floor 本身未必有 actual witness，应继续用源单独的 floor/absolute count；不能用本报告的 actual witness count 覆盖它。

## 3. \(\alpha,D_x,P_x\) 的来源

### 3.1 \(\alpha=5/6\) 是 sixth-power amplification 的 slope

源 amplified moment（12372–12384）给
\[
 \sum_u|M_u(U^r)|^2\ll U^{e(r)+\epsilon},\qquad
 e(r)=\max\{1,(1+5r)/6\}.                                       \tag{6}
\]
它来自 injective map \((u,a)\mapsto ua^6\)、\(P=(H/U)^{1/6}\) 和 \(H/P=U^{1/6}H^{5/6}\)（12437–12455 行）。这里不出现物理 \(\ell_1,h_1\)。

除以 actual inverse spike \(U^{\delta r-\epsilon}\)，得
\[
 e(r)-\delta r=
 \begin{cases}
  1-\delta r,&r\le1,\\
  1-\alpha+(\alpha-\delta)r,&r\ge1,
 \end{cases}
 \qquad \alpha=5/6.                                             \tag{7}
\]
长 witness 的 \(r\le t+o(1)\)，加上 (5) 的 \(\alpha-\delta\ge0\)，给
\[
 L(t)=1-\delta+(\alpha-\delta)(t-1).                             \tag{8}
\]
这是 15268–15311 行的来源，不是由槽供给总长度定义 \(\alpha\)。

### 3.2 \(D_x,P_x\) 来自基准 \(\kappa_0=3/4\) 的 affine crossing

在固定 dynamic/amplitude bin 中，\(q\in[0,\delta/2]\) 是原 length-weighted amplitude mean；它不是 moment 的 moving-conductor 参数。记 \(x=q/\delta\in[0,1/2]\)。

有效 row width 是一：在基数 \(U\) 下 rows 为 \(q_u\ll U\)，presentation 的 \(\nu\) 在当前 row sum 内固定且没有额外 moving-conductor radical（15242–15245 行）。
正容量为
\[
 z_M(r)=\frac{1-r}{2},\qquad
 z_P(m)=\frac{1-2m}{6\kappa_{\rm eff}}.                           \tag{9}
\]
plain 使用两份同一 actual \(S_m\)，因此是 \(|S_m|^4\) 的 spike 和 \(2m+6\kappa_{\rm eff}z\le1\)，不能改用 \(|S_m|^2\)（15242–15243 行）。

先以基准 \(\kappa_0=3/4\)、\(z_{P,0}=2(1-2m)/9\) 比较短 witness，利用 \(m\ge t-r-O(\epsilon)\) 得
\[
\begin{split}
 A_I(r)&=1-\delta\{x+(1-x)r\},\\
 S_t(r)&=1-\delta\left\{\frac{4x}{9}
                  +\left(2-\frac{8x}{9}\right)(t-r)\right\}.
                                                                    \tag{10}
\end{split}
\]
两个 affine expressions 的 crossing 给
\[
 D_x=3-\frac{17x}{9},\qquad
 P_x=\left(2-\frac{8x}{9}\right)(1-x),\qquad
 r_*(t)=\frac{(2-8x/9)t-5x/9}{D_x},                              \tag{11}
\]
\[
 R_{\rm short}(t)
 =1-\delta+\frac{\delta P_x}{D_x}(3/2-t).                        \tag{12}
\]
这些式子只用基准 \(3/4\)、actual saturated witness lengths、amplitude spikes 和两种 moments。没有使用旧 \(\ell=1/6,h=13/16\)。

实际 \(\kappa_{\rm eff}\) 比基准减少 plain capacity 的 count cost 为
\[
\begin{split}
 &2q(1-2m)\left(\frac29-\frac1{6\kappa_{\rm eff}}\right)\\
 &\qquad=\frac{24q(1-2m)\Delta_{\rm eff}}
 {(9/2)(9/2+12\Delta_{\rm eff})}
 \le\Delta_{\rm eff}/4+O(\epsilon).                            \tag{13}
\end{split}
\]
这里用下节的 \(m\ge1/3-O(\epsilon)\)、\(2q\le1\) 以及两个分母均大于四。这重放源 15392–15406 的比较，始终以 \(\Delta_{\rm eff}\ge0\) 使用。

在 (2) 的当前 bootstrap 下，(13) 左端严格为零；除 requested moment/rounding losses 外，不需再加一个新 \(\Delta_1/4\) capacity cost。只有采用更弱 \(11/12\) bootstrap 时，才需保留 \(\Delta_{\rm eff}/4\le\Delta_1/4\)。

## 4. Actual witnesses 与两种 strict widths

源 actual witness proposition 给同一 presentation 下
\[
 r+m\ge t-o(1),\quad r\le t+o(1),\quad
 t-\tfrac12-O(\epsilon)\le r,\quad 0\le m\le\tfrac12+O(\epsilon),
\]
\[
 |M_r|^2\gg U^{\delta r-\epsilon},\qquad
 |S_m|^2\gg U^{\delta m-\epsilon}.                               \tag{14}
\]
实际 dyadic pair 和有限 presentation 可逐 row 不同，先 subdivision 后用共同 smooth/Sobolev 参数控制；不得在当前 row sum 内让 prime coefficients 随 row 改变。

源 crossing 范围的代数不变：
\[
 r_*(t)\ge23/37,\qquad
 1/3\le t-r_*(t)\le1/2,\qquad
 r_*(3/2)=1.                                                   \tag{15}
\]

在 inverse side \(r\ge r_*(t)\)、\(r<1\) 且 \(z_M(r)>\nu_0\)，请求容量先减一个固定 \(\nu_0>0\)。实际 selected whole slots 的长度不超过 \(z_M-\nu_0\)，故
\[
 1-r-2z\ge2\nu_0,
\]
\[
 3-2r-8z=4(1-r-2z)+(2r-1)
 \ge8\nu_0+\frac9{37}-O(\epsilon).                             \tag{16}
\]
选 preliminary losses 足够小后，可取固定正 \(c_1,c_2\) 满足 lem:marked。特别第二 width 不是只因第一 width 为正就自动满足；其独立下界来自 \(r\ge23/37\)。

在 plain side \(r\le r_*(t)\)，(14)(15) 给 \(m\ge1/3-O(\epsilon)\)。若 \(m<1/2\) 且 \(z_P(m)>\nu_0\)，选择总长不超过 \(z_P-\nu_0\)，则
\[
 1-2m-6\kappa_{\rm eff}z
 \ge6\kappa_{\rm eff}\nu_0\ge\frac92\nu_0>0.                    \tag{17}
\]
这满足 lem:plain 的 affine length condition；它本来允许边界等号，本次 decrement 额外给实际 annular offsets 的安全余量。capacity 的最大需求为
\[
 z_M\le7/37,\qquad
 z_P\le2/27+O(\epsilon),                                       \tag{18}
\]
因 \(\kappa_{\rm eff}\ge3/4\)。没有利用 \(\kappa<3/4\) 产生的新容量。

原 normalization、row width 和两个 strict inequalities 至此都已实际核验；单说 \(\ell_1/h_1\) 增加不能替代 (14)–(18)。

## 5. Same-source slot spike、系数类与群例外

原物理 main factor 为（14997–15013 行）
\[
 Q_i(u;z_{\rm phys})=P_i^{-1/2}\!
 \sum_{p\in\mathcal P_i(Z)}
 \overline{\chi_p(u)}\,W_i(q_p/P_i)(q_p/P_i)^{z_{\rm phys}-1},
 \qquad P_i=Z^{\ell_i}.                                       \tag{19}
\]
原 zero extension 使 \(p\mid u\) 的 main 项为零。每个 physical prime window 仍在原 scale；没有在反射或 moment 选择时改窗。对 error slots 记 \(g_i=0\)，不从 error factor 要求 lower spike。

幅度分箱给 \(g_i\in[0,\delta/2]\)、\(q=(\sum_i\ell_i g_i)/\ell_1\)；\(g_i>0\) 的 main slot 满足 \(|Q_i|\ge P_i^{g_i}\)。在基数 \(U=Z^d\) 下，实际 slot 长度为 \(w_i=\ell_i/d\)，可用总量 \(\ell_1/d\)。按固定 bin 的 \(g_i\) 从大到小填 requested \(z\)，删除最多一个 fractional slot，可选**实际 whole positive slots**使
\[
 \left|\prod_{i\ {\rm selected}}Q_i\right|^2
 \ge U^{2qz-\delta\max_iw_i}.                                  \tag{20}
\]
若 positive slots 不足，保留其全部，gain 为 \(q\ell_1/d\ge qz\)；不需要虚构容量或填入不存在的素数。strict moment 时用 \(z-\nu_0\)，cost 不超过
\(2q\nu_0+\delta\max_iw_i\)，zero-capacity neighborhoods 另用 no-slot bound。

在固定 presentation \(\psi(n)=\nu(n)\overline{\chi_n(u)}\) 下，physical slot 相对于这个共同 row character 的 coefficient 精确为
\[
 \overline{\nu(p)}1_{p\in1_T}
 =\frac1{|T|}\sum_{\theta\in\widehat T}(\overline{\nu}\theta)(p).
                                                                    \tag{21}
\]
这是固定 \(\Theta\) 成员的有限组合，并且 row-independent。无需 \(\eta(p)=1\)。inverse moment 允许此 negative common orientation。
对 plain moment，把**两个 witnesses 和全部 selected prime factors 整体共轭**；row orientation 变成正号，coefficient 为 \(\nu(p)1_{p\in1_T}\)，仍在同一有限群。不能只共轭 witness 而保持 prime factors 原样。
该操作保留所有 masks、underlying disjoint prime supports 及 norm profiles。

原 plain lemma 对 \(z>0\) 排除 inducing character 属于 \(\Theta\) 的 rows（12518–12525 行）；判断的是 primitive inducing character，不是零延拓 presentation。
对实际 sixth-power-free \(u\)，若 \(S\) 外某个素数的 valuation 为 \(j=1,\ldots,5\)，其局部字符阶为 \(6/\gcd(6,j)>1\)；固定 \(\Theta\) 在该 prime unramified，不能消去这个 primitive ramification。故这种 row induces outside \(\Theta\)。

剩余 exceptional physical rows 全部 supported on 固定 \(S\)，sixth-power-freeness 和有限 unit group 使它们构成有限集（14975–14984、15168–15170 行）。在 selected range \(U\ge Z^{1/2}\) 下，增大 fixed-target 阈值后没有这些 rows；它们仍须在 outer/bounded physical rows 中按原方式处理，不能从完整 high object 删除。

## 6. 新实际 supply、固定 mesh 与 pool 隔离

只有 \(d\ge1/2\) 的 physical row ranges 用 selected prime factors；\(d_{\min}\le d\le1/2\) 使用源 no-slot count（16146–16172 行）。因此
\[
 w_i=\ell_i/d\le2\ell_i.                                       \tag{22}
\]
新几何给精确供给
\[
 \frac{\ell_1}{h_1}=\frac{20006}{97509},\qquad
 \frac{\ell_1}{h_1}-\frac7{37}
 =\frac{57659}{3607833}>0.                                    \tag{23}
\]
这是实际 requested capacities 的正余量，结合 (18) 与 (20)，而不是独立的 detector theorem。

扩展到 \(d\le h_1+\zeta\) 时，只须预先取
\[
 0<\zeta<5\ell_1-h_1=\frac{2521}{120000};
 \quad\Longrightarrow\quad
 \frac{\ell_1}{h_1+\zeta}>\frac15>\frac7{37},\qquad
 \frac15-\frac7{37}=\frac2{185}.                               \tag{24}
\]
旧的 \(\zeta<1/48\) 也足够；新允许量比 \(1/48\) 大 \(7/40000\)。

源 lem:plain 的 mesh 在 \(\kappa_{\rm eff}\in[3/4,5/6]\) 属于原 uniform 参数范围（12572–12578、16238–16243 行）。先为保留的 count loss 选 \(\nu_0\)、moment losses、rounding allowance；再取一个 fixed even \(K\)，等长 \(\ell_i=\ell_1/K\)，使
\[
 \frac{2\ell_1}{K}
 <\min\{\eta_{\rm mesh},b_{\rm round},1/185\}.                    \tag{25}
\]
于是 (22) 给所有 selected \(w_i<\eta_{\rm mesh}\)、\(\delta\max_iw_i<b_{\rm round}\)，并低于 (24) 的 supply gap 的一半。
可沿用 16253–16261 行的互不相交区间
\[
 I_i=\left(1+\frac{2i-1}{2K+1},\
            1+\frac{2i}{2K+1}\right)\subset(1,2)
\]
及非负非零 \(W_i\in C_c^\infty(I_i)\)；其 underlying supports 在 ray、\(S\) 及 row masks 前就已 disjoint。

actual annular norm ratios 把 nominal \(U\)-length 改动
\(O_K(1/\log U)\)，只能在 fixed \(\nu_0\) 等 strict margins 之后由阈值吸收（16276–16278 行）。不允许先取零 decrement 再把实际误差称为严格余量。

原 plain induction 的 centered amplifier pool 用
\(\ell_*=\sigma_{\rm width}/3\)，slot mesh 低于
\(\sigma_{\rm width}/6\)（16280–16287 行）。在基数 \(U\) 下，
physical slots 的 norm 至多 \(2U^{\eta_{\rm mesh}}\)，pool 从
\(U^{\ell_*}/2\) 开始；固定 exponent gap 使它们在足够大 \(U\) 后统一隔离。新 \(\ell_1,h_1\) 不改变这一内部 width 参数或分离机制。

## 7. Zero capacities、长 witnesses 与 equality endpoint

以下例外处理是保持 fixed width 的必要部分。

- \(r\ge1\)：用 sixth-power amplification (6)，不用 strict marked moment。由 \(\delta\le\alpha\) 给 long count (8)，包括 \(r=1\)。
- \(m\ge1/2\)：用原 zero-slot plain case，它不限制 bounded lengths；count 不超过 \(1-\delta+O(\epsilon)\)。
- \(r<1\) 但 \(z_M(r)\le\nu_0\)：no-slot inverse 给
  \(1-\delta r\le1-\delta+2\delta\nu_0\)。
- \(m<1/2\) 但 \(z_P(m)\le\nu_0\)：zero-slot plain 给
  \(1-2\delta m\le1-\delta+6\delta\nu_0\)，因为 \(\kappa_{\rm eff}\le1\)。

若 \(\delta=\alpha\)，adaptive cutoff 取 \(t=3/2\)。actual witness 有 \(r\ge1-O(\epsilon)\)。在 \(r\ge1\) 用 (7) 得 \(1-\delta\)；在邻近的 \(r<1\) 用其第一支得 \(1-\delta+O(\epsilon)\)。因此 count 是
\[
 \#\mathcal B\ll U^{1-\delta+\epsilon}(1+T_1)^A.                 \tag{26}
\]
此处 \(r_*(3/2)=1\)、inverse capacity 为零，绝不能把 \(r+2z=1\) 当作具有 fixed \(c_1>0\) 的 marked invocation。

在更强 bootstrap (2) 下 \(\delta\le3/4<\alpha\)，这个 equality endpoint 不会实际出现；保留它使条件命题在较弱 \(11/12\) 输入下仍完整。

## 8. 实际 count 与原 adaptive cutoff

前述条件、spikes、宽度、系数类和 supply 已支付后，源 count proof 可按实际 \(\kappa_{\rm eff}\) 重放，得到
\[
 \#\mathcal B
 \ll U^{\max\{R_{\rm short}(t),L(t)\}
           +\Delta_{\rm eff}/4+\epsilon}(1+T_1)^A,
 \qquad t\in[1,3/2].                                          \tag{27}
\]
这不是仅凭 (23) 猜测原 statement 可扩展：每个 moment 的 actual invocation 及其 family 条件已经在 §4–§7逐项验证；核心 moments/witness 的证明本身仍是 §2 指明的 [R] 输入。

对 \(1/50<\delta<\alpha\)，定义原 crossing
\[
 \mathcal J=(\alpha-\delta)D_x+\delta P_x,\qquad
 t=1+\frac{\delta P_x}{2\mathcal J},\qquad R_*=L(t).              \tag{28}
\]
原代数给
\[
 37/18\le D_x\le3,\quad 7/9\le P_x\le2,\quad
 D_x-P_x>0,\quad 35/54\le\mathcal J\le5/2;
\]
\[
 1<t<3/2,\qquad R_{\rm short}(t)=L(t)=R_*.
                                                                    \tag{29}
\]
这些 bounds 只用 \(0\le x\le1/2\)、\(0<\delta\le\alpha\)，不含物理 \(\ell_1,h_1\)。共同 row exponent 所以为
\[
 \boxed{\#\mathcal B\ll
 U^{R_*(\delta,x)+\Delta_{\rm eff}/4+\epsilon}(1+T_1)^A.}         \tag{30}
\]
bootstrap (2) 下可以去掉 \(\Delta_{\rm eff}/4\)，因为它是零。
使用弱 bootstrap 时也有
\(R_*+\Delta_{\rm eff}/4\le R_*+\Delta_1/4\)。
不能把 \(2\beta_*-1<3/4\) 的额外供给当成新的更强 \(D_x,P_x\)；本报告没有获得这种未覆盖的 plain theorem。

对 no-slot \(t=1\) 范围，原 proof 同样给
\(\#\mathcal B\ll U^{1-2\delta/3+\epsilon}(1+T_1)^A\)，不需 prime-supply 条件。

## 9. 统一性顺序与未完成的 high 接口

必须沿用以下顺序：

1. 固定 global bootstrap、(1) 几何与 bounded actual \(r,m,t,\delta,x,d\) ranges；指定最终可支付的 real count loss。
2. 选 fixed capacity decrement、moment/rounding losses、plain mesh 和 (25) 的有限 slot 系统。再选 amplitude bin width 和原 prime-bound preliminary real losses，使 \(U^{\epsilon_1}\) 在每个固定 \(d/\ell_i\) 范围内被 bin allowance 吸收（15064–15070 行）。
3. 对 fixed target 选 arithmetic datum、finite \(\Theta\) 与全部 internal seminorm/height orders。保持所有 retained physical/witness Fourier variables 的**同一个** cumulative \(T_1/2\) allocation；不能每次移线更新高度预算。
4. 按原 15473–15493 行的 detector height ceiling，取 \(T_1=Z^\tau\) 且 \(\tau\) 足够小，使 \((1+T_1)^A\) 被已留的 \(U\)-小幂支付。该 \(\tau\) 可依赖目标和已固定内部阶数。
5. 最后选 external Fourier tail order、增大 \(Z\) 阈值，以吸收 annular ratios、固定 family exceptions、支持分离及 logarithmic counts。提升 external tail order 不能改变先前已固定的 arithmetic height order或 slot mesh。

本报告只完成**原 same-source detector counts 与 nominal adaptive cutoff 的条件准入**。
下列内容仍未由它支付：

- 完整 central error-slot / strict ramified-label decomposition 的 joint numerator 估计及新 contour 全部层级。
- 把 (30) 和实际 error gains \(g\) 放入新 central Mellin envelope 后，对所有 \(d,\delta,x\) 的 uniform 严格 saving。
- 从 \(d=h_1\) 到 \(h_1+\zeta\) 的完整 high envelope 控制；(24) 只支付 capacity supply。
- 新 low/high principal normalization、全部 outer/principal/central tails 共同兼容的 order-of-choices，以及 continuation criterion 的完整物理函数合同。
- 与实际 Weil 正性、几何 cohomology 或 RH/RR 的算术来源比较。

有限 Fraction 核对认证 (1)、(23)、(24) 的有理代数，不认证外部 infinite-analysis [R] 前件。本任务仅写本报告，未改已提交 notes/checkpoints、旧报告或外部 math 文件，也未构建外部项目。
