# C054：Jump＋killing 的三固定源定量障碍

2026-10-29；`/root/moment_fresh_audit` 当前独占数学证明腿。已恢复 README/STATE、check→show、同 Goal/runtime1793085111/原0c4f 与新 C054；旧 connected-variance 准入终态不充当本次证明。只用固定 actual Π 及项目已付原域/核，不读新 source/PDF/web、不作数值、不改 STATE/Git/cadence，不预591或Goal完成。

**本腿终态已闭合：** 原投影的常数 `2,32,8`，一般共同 `0≤R_X≤Π_X` 的真实 HS 因式/jump＋killing/尾支配，完整 Weil 平移不变性，以及合同指定 δ/ε 下三误差不能同时小。第9节已实际全文收另一腿11649-byte actual absolute-tail终稿并解除唯一接口，故全大X三源gap及第7节必要加权尾可联合消费；仍待不同fresh/root整体确认，不以旧 `o(√X/log²X)` 代替绝对尾。

## 1. 三个冻结源与完整目标值

按合同固定

\[
 \psi(u)=c\exp[-1/(1-(16u)^2)]1_{|u|<1/16},\quad
 \int\psi=1,\qquad g=\psi*\psi^\#,
\]

其中 `ψ#(u)=overline(ψ(−u))`。ψ实偶且非负，g实偶、非负、光滑紧支撑，`∫g=1`。记

\[
 G(t)=\widehat g(t)=|\widehat\psi(t)|^2,\quad
 \widehat r(t)=\int r(u)e^{-itu}du,\quad a=1/2.
\]

所以 `0≤G≤1` 全线、`G(0)=1`。|t|≤1时，ψ偶性和support给

\[
 \widehat\psi(t)=\int\psi(u)\cos(tu)du
 \ge1-1/512=511/512,
 \quad 1/2\le G(t)\le1.                                    \tag{1}
\]

三个源是 `g,τ_a g,g′`，其中 `τ_a g(u)=g(u−a)`。其支撑分别在 `[-1/8,1/8]`、`[3/8,5/8]`、`[-1/8,1/8]`，均严格包含于537窗 `I0=(−17/16,17/16)`；它们先于 X/R 固定，且属于原 du/zero-extension Dlog。这里g是本合同L¹归一化卷积，不能与587的另一du-unit bump混同。

g′非零：否则g为常数，由compact support只能g=0，与∫g=1矛盾。因此537完整固定窗正性给固定有限常数

\[
 q_0=Q_W[g]>0,\qquad q_1=Q_W[g']>0.                         \tag{2}
\]

这些值包含 actual Γ/contact、全部 Λ(p^k)=logp 与indefinite双pole，未借未知零点位置。

### 完整平移，而非删 pole 后的平移

设 `μ±(r)=∫e^(±u/2)r(u)du`，完整pole为

\[
 P[r]=2\operatorname{Re}(\mu_+(r)\overline{\mu_-(r)})
 =2|\ell_c(r)|^2-2|\ell_s(r)|^2,
\]

其中 `ℓc=∫r cosh(u/2)`、`ℓs=∫r sinh(u/2)`。平移使μ±分别乘 `e^(±a/2)`，故P精确不变；等价地 `(ℓc,ℓs)` 经实Lorentz boost，保 `|ℓc|²−|ℓs|²`。这对complex源成立，不将负sinh槽丢掉。

Γ/contact源型由 `|rhat|²` 给出；全部prime powers由autocorrelation `∫r(u+v)overline(r(u))du` 给出。二者在共同平移下均不变。因此

\[
                         Q_W[\tau_a g]=Q_W[g]=q_0.           \tag{3}
\]

g′的mean为0不等于polefree；本证明没有对三个最终源施双pole-zero条件。

## 2. 实际共同正占据的域、核和非负 killing

固定有限X，receiver为 `H=L²(R,dμ)`、`dμ=dt/(2π)`，Π=Π_X为原全逆 Sonin 正交投影。所有 B_X/G_X^−1/returns保留；不以 `B_XPB_X*` 或其它投影代替。记Π的actual连续评价代表为 `e_t∈RanΠ`，其核为

\[
 k_\Pi(t,s)=\langle e_s,e_t\rangle,\qquad
 k_\Pi(t,t)=2\pi\rho_X(t).
\]

内积第一槽线性。取任意共同正contraction `0≤R≤Π`，可依X及全部测试组选择，但同层三个测试必须使用同一R。由 `kerΠ⊂kerR`，有 `R=ΠRΠ`。因此定义

\[
 k_R(t,s)=\langle Re_s,e_t\rangle,\quad
 k_{R^2}(t,t)=\|Re_t\|^2,
 \quad 0\le k_R(t,t)\le k_\Pi(t,t).                          \tag{4}
\]

这些是同一原H中的核；R不必finite-rank、trace-class或projection。实际评价代表的norm连续性保证核可测/连续，且

\[
 k_R(s,t)=\overline{k_R(t,s)},\qquad
 \int|k_R(t,s)|^2d\mu(s)=k_{R^2}(t,t).                       \tag{5}
\]

定义

\[
 \ell_R(t)=k_R(t,t)-k_{R^2}(t,t)
          =\langle(R-R^2)e_t,e_t\rangle\ge0,\qquad
 \rho_R(t)=k_R(t,t)/(2\pi)\le\rho_X(t).                      \tag{6}
\]

R=Π时 `ℓ_R=0`，但一般R必须保留它。

对本组三个源及其有限线性组合，560的夹源HS准入和R≤Π给

\[
 \|M_fR^{1/2}\|_{HS}^2
   =\int |f(t)|^2k_R(t,t)d\mu(t)
   \le\int |f(t)|^2\rho_X(t)dt<\infty.                     \tag{7}
\]

可用任一ONB、Parseval及Tonelli直接证明等式。故严格ordinary trace写法为

\[
 T_R(r,s)=\operatorname{Tr}(M_{f_r}R M_{f_s}^*),\qquad
 C_R(r,s)=\operatorname{Tr}(R M_{f_r}R M_{f_s}^*),
\]
\[
 V_R(r,s)=T_R(r,s)-C_R(r,s)
 =\langle(1-R)^{1/2}M_{f_r}R^{1/2},
         (1-R)^{1/2}M_{f_s}R^{1/2}\rangle_{HS}.               \tag{8}
\]

初始dispatch首项 `Tr(R MfMg*)` 只能按positive weighted trace/sandwich后polarization解释为此T_R；当前合同与root域澄清已改为上述严格写法。未夹源operator的字面S1消费冻结，不用于本证明。第二项可由HS×HS合法定义，且 `C_R[r]=||R^(1/2)MfR^(1/2)||HS²≥0`。所以 `0≤V_R≤T_R≤T_Π`。k_(R²)是operator square的核，不是对角k_R(t,t)的数值平方。

利用(5)展开压缩核，得到精确jump＋killing形式

\[
 \begin{split}
 V_R(r,s)={}&\frac12\iint(f_r(t)-f_r(v))
       \overline{(f_s(t)-f_s(v))}|k_R(t,v)|^2d\mu(t)d\mu(v)\\
 &+\int f_r(t)\overline{f_s(t)}\ell_R(t)d\mu(t).             \tag{9}
 \end{split}
\]

其绝对性不是形式消无穷：

\[
 \iint|f(t)g(v)||k_R(t,v)|^2d\mu(t)d\mu(v)
 \le\Big(\int|f|^2k_{R^2}(t,t)d\mu\Big)^{1/2}
      \Big(\int|g|^2k_{R^2}(t,t)d\mu\Big)^{1/2}<\infty.
\]

两条对角项、killing亦由(7)控制。先作bounded frequency cutoff的HS核乘积，再按(7)去cutoff，合法获得(9)；不拆未乘源的无限trace。Γ/全Euler信息在actualΠ中，未被模型Cauchy核替代。

## 3. 平移异常 A_R 的非负性和精确常数

因为 `f_(τa g)(t)=e^(−iat)G(t)`，而G实非负，

\[
 |e^{-iat}G(t)-e^{-iav}G(v)|^2-|G(t)-G(v)|^2
       =2G(t)G(v)[1-\cos(a(t-v))].
\]

(9)中killing部分平移前后完全相同。因此

\[
 A_R:=V_R[\tau_a g]-V_R[g]
 =\iint G(t)G(v)[1-\cos(a(t-v))]|k_R(t,v)|^2d\mu(t)d\mu(v)
 \ge0.                                                       \tag{10}
\]

不要求R real/even、与conjugation交换或每层stationary。积分绝对可控：`G(t)G(v)≤(G(t)²+G(v)²)/2`，再用(5)–(7)。这是同一R的两个actual测试之差。

## 4. 全 near/far 分区：2、32、8

固定 `0<δ≤1`，令N=`{|t|≤δ}`、F=`{|t|>δ}`，

\[
 d\omega(t,v)=|k_R(t,v)|^2d\mu(t)d\mu(v),\qquad
 B_R(\delta)=\int_Ft^2G(t)^2k_R(t,t)d\mu(t)
             =\int_Ft^2G(t)^2\rho_R(t)dt.                    \tag{11}
\]

ω非负且对称。由源导数的Fourier `widehat(g′)(t)=itG(t)`，V_R[g′]的jump被积式是 `|tG(t)−vG(v)|²/2`，无额外2π。

### N×N

写Δ=t−v。由(1)，`G(v)²≤2G(t)G(v)`。而 `|aΔ|≤δ≤1`，elementary余项给 `1−cos x≥x²/4` 于|x|≤1，所以

\[
 1-\cos(a\Delta)\ge\Delta^2/16.
\]

利用恒等式 `tGt−vGv=t(Gt−Gv)+ΔGv`，逐点有

\[
 \begin{split}
 |tG_t-vG_v|^2
 &\le2\delta^2|G_t-G_v|^2+2\Delta^2G_v^2\\
 &\le2\delta^2|G_t-G_v|^2
      +64G_tG_v[1-\cos(a\Delta)].                            \tag{12}
 \end{split}
\]

乘1/2积分给 `2δ² V_jump,NN[g]+32 A_NN`。常数32已包含variance的1/2。

### N×F 和 F×N

取t∈N、v∈F，则 `|Δ|≤2|v|`，故

\[
 |tG_t-vG_v|^2
 \le2\delta^2|G_t-G_v|^2+8v^2G_v^2.                         \tag{13}
\]

由ω对称，两个cross区域的1/2合成一个N×F积分。所以导数cross费用至多

\[
 2\delta^2 V_{jump,cross}[g]
 +8\int_F v^2G(v)^2\underbrace{\int_N|k_R(t,v)|^2d\mu(t)}_{m_N(v)}d\mu(v).
                                                                    \tag{14}
\]

### F×F 和 killing

用 `|tGt−vGv|²≤2t²Gt²+2v²Gv²`，其jump积分至多

\[
 2\int_Ft^2G(t)^2\underbrace{\int_F|k_R(t,v)|^2d\mu(v)}_{m_F(t)}d\mu(t).
                                                                    \tag{15}
\]

near killing满足

\[
 \int_N t^2G(t)^2\ell_R(t)d\mu(t)
 \le\delta^2\int_NG(t)^2\ell_R(t)d\mu(t)
 \le2\delta^2 V_{kill}[g].                                  \tag{16}
\]

far killing原样为 `∫_F t²G²ℓ_R dμ`。关键是**先合并row再估尾**：对t∈F，

\[
 8m_N(t)+2m_F(t)+\ell_R(t)
 \le8[m_N(t)+m_F(t)+\ell_R(t)]=8k_R(t,t),                    \tag{17}
\]

末等号是(5)–(6)。不能把cross与FF分别粗估为8B、2B后声称只有8B；(17)利用同一row的互补分区，严格支付这个常数。

合并(12)–(17)，以 `A_NN≤A_R` 及V各非负部分放宽，得到全部有限X、全部共同 `0≤R≤Π_X` 的精确比较

\[
 \boxed{V_R[g']\le2\delta^2V_R[g]+32A_R+8B_R(\delta)
          \le2\delta^2V_R[g]+32A_R+8B_\Pi(\delta).}           \tag{18}
\]

R=Π时killing为0，主投影链是其中的特例；一般R的扩展没有遗留conditional domain或符号。

## 5. 合同 δ/ε 的三 fixed-test gap

固定目标值(2)，按合同一次选择

\[
 \delta=\min\{1/2,\sqrt{q_1/[16(q_0+1)]}\}>0,
 \qquad\varepsilon=\min\{1/2,q_1/260\}>0.                    \tag{19}
\]

这些是证明常数，不改变g/a/Π的生成规则，均先于X/R。对任何满足 `B_Π(δ)≤q1/64` 的X，假设同一个R的三误差均≤ε：

\[
 |V_R[g]-q_0|\le\varepsilon,\quad
 |V_R[\tau_a g]-q_0|\le\varepsilon,\quad
 |V_R[g']-q_1|\le\varepsilon.                               \tag{20}
\]

则 `V_R[g]≤q0+1`，由(10)有 `0≤A_R≤2ε`。代(18)得

\[
 V_R[g']\le q_1/8+64\varepsilon+q_1/8
             =q_1/4+64\varepsilon.
\]

与(20)第三式合并，

\[
 3q_1/4\le65\varepsilon\le q_1/4,
\]

与q1>0矛盾。因此只要尾满足该阈值，就有**严格**

\[
 \boxed{\max\{|V_R[g]-q_0|,\ |V_R[\tau_a g]-q_0|,
                   |V_R[g']-q_1|\}>\varepsilon.}             \tag{21}
\]

不需要三个误差有共同方向；失败的索引可随X/R变化，但三个测试本身固定。不能把max gap升级成同一索引在全部大X上总失败；它已经足以排除三者同时cofinal收敛。该结论甚至允许每层R在知道这组三测试后选择，因所有估计对全 `0≤R≤Π_X` 同时有效。

## 6. 联合尾接口、结论范围与净值

本腿对任意固定δ已证(18)及“tail≤q1/64⇒(21)”，不需要universal offdiagonal Cauchy界、fullgap b比较、moving quiet源或fixed-X高频顺序互换。以下先列逻辑接口，再于第9节绑定其已收终稿：在同一g/G和actualρ_X上需要

\[
 B_\Pi(\delta)=\int_{|t|>\delta}t^2G(t)^2\rho_X(t)dt
                       \longrightarrow0,                   \tag{Tail}
\]

有此Tail即存在只依冻结数据的X0，使所有X≥X0和全部共同 `0≤R_X≤Π_X` 都满足(21)。X0独立R，因为尾支配在Π层付清。这里必须是绝对Tail，不能由 `o(√X/log²X)` 的旧headline直接替代。

该class含原Π、任意rank/合法无限维/nonlocal的positive contraction，以及按固定测试组选择的共同R_X；不要求每层stationary或每层消Pan。它不含破坏R≤Π的外部无界gain、任意scalar重加权、非occupation covariance、逐个被测源另选R或其它signed/几何修复。三源共同极限若是完整Q，本应分别趋q0/q0/q1，故(21)直接拒绝该完整fixed-pair身份；无需先制造一变量D′分布。

定义/一般PSD/旧核与Tail设施先扣旧；新的实际付款是同一G非负性带来的平移异常、derivative与absolute away0 tail的定量joint连接，及其共同occupation/killing推广。并非由V≤T、quiet moving源或旧单频filter停止门推出。是否整体C054统一结算为新轮仍由独立fresh/root按最强旧审定，本腿不自行计数。

这不是Q负源或RH反例，不给正性或whole4/5负惯性UPPER改善；长期primitive/principal/mixed、其它完整signed核心责任保持，Goal不由本腿完成。

## 7. 同一不等式对外部gain／正mixture的必要尾费

本节只是(18)的直接消费，不换源/δ或优化常数。若某共同R_X和外部positive scalar β_X仍满足

\[
 \beta_XV_{R_X}[g]\to q_0,\quad
 \beta_XV_{R_X}[\tau_a g]\to q_0,\quad
 \beta_XV_{R_X}[g']\to q_1,
\]

则 `β_X A_(R_X)→0`。将(18)乘β_X并移项，

\[
 8\beta_X B_\Pi(\delta)
 \ge\beta_XV_{R_X}[g']-2\delta^2\beta_XV_{R_X}[g]
                           -32\beta_X A_{R_X}.
\]

右边趋 `q1−2δ²q0≥7q1/8`，所以可保守交付

\[
                 \liminf_{X\to\infty}\beta_XB_\Pi(\delta)
                                \ge q_1/16>0.               \tag{22}
\]

同样，若 `\mathcal V_X=∫V_R dη_X(R)` 为已经合法定义的正mixture，`η_X≥0`、有限总weight `W_X=η_X(1)`，同层mixture对三个源相同，则其非负平移异常为 `∫A_Rdη_X`。有限正组合显然可用；正积分只需各fixed-pair可测，因 `|V_R(r,s)|≤sqrt(T_Π[r]T_Π[s])`，有限weight即给绝对性。对(18)积分后同一证明给

\[
 \mathcal V_X[g],\mathcal V_X[\tau_a g],\mathcal V_X[g']
      \to(q_0,q_0,q_1)
 \quad\Longrightarrow\quad
 \liminf_X W_XB_\Pi(\delta)\ge q_1/16.                      \tag{23}
\]

若actual-tail腿给 `B_Π(δ)≤Cδ exp(−bδ log²X)`，则(22)/(23)迫相应β_X或W_X对全部充分大X至少为 `cδ exp(bδ log²X)`（用safe乘积下界q1/32即可），故比任意fixed power of X增长更快。此rate只沿同一tail upper消费，不付sharpness、充分性或有效构造。

外部gain或mixture总weight增长正是主类R≤Π以外保留的逃逸；(22)/(23)是实际必要加权尾，不是对所有高gain的排除。它们不将βR重新称为≤Π，也不自动把positive mixture写成某个单occupation covariance。

## 8. 当前交付状态

本腿jump/constants、occupation/domain/killing、完整平移与定量三误差gap已闭；(Tail)已按第9节实际终稿解除，没有待证的occupation推广。原admission的0止保持为当时准确历史，新C054由后来形成的(18)量化第一步准入，不回改旧稿。

无新primary/PDF/章/web/数值/后台，未改STATE/Git/cadence/board；全链仍待不同fresh/root消费。

## 9. Actual-tail终稿的实际对齐与最终版本

现已实际全文读另一腿 `actual-gevery-tail-and-premise-closure.md`：11649 LF bytes/200行，SHA256 `dfe9e617fa984bdcca1c0d0aa83906092339d18a2b25bfdbd8005c8274afedee`，现场核验匹配。它没有换源、Euler对象、receiver norm或局部核：

1. 使用同一个本合同ψ、g=ψ*ψ#、G=|ψhat|²，并自含付其Gevrey2 upper；不是调用587另一bump的lower。
2. C052全线Tail采用actualΠ的可测weighted-HS接口，而非仅relative little-o；localization采用 `kΠ(t,t)=|D_X(t)|²Q_X(t)=2πρ_X(t)`，未将bare Q当actual density。
3. 每first-fixedδ取B=4、T=(logX)⁴，实际证明

\[
 B_{\Pi,X}(\delta)\le\|g'\|_{du}^2e^{-c_\delta A/2}
    +C_\psi'(\sqrt X+1)e^{-\gamma_\psi(\log X)^2}\to0,
 \quad c_\delta=4-4/\sqrt{1+4\delta^2},\quad
 \gamma_\psi=\log4/(4\sqrt{512}),\quad A=\sqrt X/\log X.    \tag{24}
\]

4. 其R-kernel row、nonnegative killing与strict sandwich与本稿(4)–(9)相同；`B_R≤BΠ`不使用未经证明的逐点 `|k_R|≤|kΠ|`。

因此固定(19)的δ后，(24)给一个统一X0，使**所有**X≥X0及**全部共同** `0≤R_X≤Π_X` 满足(21)，无残余tail条件。对于第7节rate，令 `b*=γψ/2>0`；在充分大X上吸收 `√X+1`，且 `A/(log X)²→∞` 吸收mid项，得

\[
 B_{\Pi,X}(\delta)\le C_\delta e^{-b_*(\log X)^2}.
\]

这给(22)/(23)所述safe superpolynomial必要gain/总weight下界。未主张该下界sharp或足以修复目标。

| 必要原件 | LF bytes | SHA256 |
|---|---:|---|
| 当前C054合同 | 4874 | 7e95d495b356df3dd9ff8c554ed98f6441ee03c7517d65fd226582e24d6fd7d2 |
| trace-domain-clarification.md | 1177 | a6c65587e133b145dce65487534e96eceba88d6c67764c3510eea8afb7a565a0 |
| 前准入actual-kernel-and-cofinal-test.md，仅原HS/kernel域 | 8830 | df200f68f9f533933f821b19de53c46674baf4def33eb0115967a3634eff275d |
| 537完整fixed窗正性 | 8155 | 269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8 |
| 当前actual-gevery-tail-and-premise-closure.md | 11649 | dfe9e617fa984bdcca1c0d0aa83906092339d18a2b25bfdbd8005c8274afedee |

Tail终稿另逐项绑定已付C052 upper10211／`bab769113b4ce8c858dfd4b7a83dea6abd8808436a599d2206ea9a9bf0915fff` 与localization11459／`809bc7ffc6f1fbf4dd24af0d710af05fb7ca1bc259992430c3fd6760912ffcb1`。本稿以其实际absolute消费对齐，不重新读取外部primary或扩C052章节。

**当前proof terminal：投影主链及全共同occupation推广、三fixedtestgap和必要加权tail推论均无未付局部前件；不同fresh/root的整体消费与统一计轮另行完成。**
