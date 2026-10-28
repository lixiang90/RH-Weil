# C052：零均值上界与scalar归一化的独立逆审

2026-10-28；`/root/moment_fresh_audit` 当前AJ任务，非此前C050／C051审稿续用。已恢复README／STATE、check→show、G20261027、D20261028AJ、C052、frontier及588结算；核实际工作树与两个当前terminal输出。STATE所载父运行Goal仍为1793085111／active，原冻结基线0c4f；本审不创建或终结Goal，不改共享proof／STATE／Git／cadence。

**限定PASS。** 当前两个终稿共同支付(6.7)、actual central mass／全线tail及必要localization，足以给所有先fixed compact smooth complex零均值源的actual trace little-o。root当前5043-byte稿中A／B的技术前件可以据此解除conditional；本稿只是独立审查，仍须root实际消费和统一结算。没有消费6.4 sharp lower、6.5、§7、receiver strong limit或moving translation结论。

## 1. 实际终稿绑定

下列bytes／SHA256均按UTF-8 LF现场重核；源原件raw与LF相同。两终稿已全文读，不能以此前locator或代理消息替代。

| 当前对象 | LF bytes | SHA256 |
|---|---:|---|
| 固定v2原件 `literature/local/2026-10-28-core-source-location/bramble-trace-rstation-2-v2.md` | 61862 | `541098314b2ddc5f8645babf82086e87d16c46188268cbc7ed6cfc1f98720058` |
| `goals/contracts/C052-sonin-zero-mean-upper-and-scalar-normalization.md` | 4213 | `03ad2b449f3a9022a74e3d4e6637072c17f8f2acfe9d7e7eeba442ef8e6b3bfd` |
| `next-zero-mean-upper-proof-gate.md` | 2490 | `d1ad41054ccf0843223ee552ab3dcfc9d671c90913a59d53dc0b32c8a343a069` |
| `source-upper-and-tail-proof-audit.md` | 10211 | `bab769113b4ce8c858dfd4b7a83dea6abd8808436a599d2206ea9a9bf0915fff` |
| `source-localization-proof-audit.md` | 11459 | `809bc7ffc6f1fbf4dd24af0d710af05fb7ca1bc259992430c3fd6760912ffcb1` |
| `root-zero-mean-upper-consumption-draft.md` | 5043 | `f2b9093fe3bd7486d99c69336c0c6a6a2aa6af1ef8170d85ae9cb89dfe9459e4` |

除首两行外，路径均相对本目录。上游终稿绑定的是原3776-byte C052；当前4213-byte版仅追加同lemma的fixed-pair Cauchy消费，没有更动sourceproof范围，故不存在未审的新来源接口。实际主原件阅读限667–782、784–869及必要定义／§4核；反向Q lower、无共同零点与6.9双边式不作本结论的前件。Burnol固定gap1 Th8的primary核读由上游终稿记录承担，本审核其completed/raw运输在使用处的充分性，不凭论文标签认可结论，也不新增另一paper预算。

## 2. 对象、范数和求值界逆审

physical源为先fixed的f∈Cc∞(R;C)，F(t)=∫f(u)e^(−itu)du。receiver为560同一actual Sonin投影S_X=Π_X的Mellin酉表示；D_X=∏_(p≤X)(1−p^(−1/2−it))，其range为D_XM。weighted arch norm是||h||_X=||D_Xh||_(dt/(2π))，不是原physical源norm。到actual range的等距在原arch坐标为M_D G_X^(−1/2)，G_X=P|D_X|²P|_M；有限X完整Gram逆始终保留。

上游先由固定cosine resolvent的entire Taylor界、Burnol combined E及completed kernel得到原norm下整个complex disk的unit-ball评价增长。分母s+z−1的可去性用Cauchy导数处理，除回γ(s)γ(z)用entire reciprocal gamma；不能将逐向量entire性当unit-ball界。

关键X统一性也实际支付：反射后D_X⁺在Imz≥1有ζ(3/2)^−1的统一lower，h⁺和arch conjugate C₀h⁺有同weighted boundary norm。Hardy评价及下侧解析gamma比给strip两边的h⁺/(z+2i)统一界。先对每fixed X、ε>0令矩形长度趋∞，再令ε↓0，barrier exp[−εcosh(az)]以0<a<π/2去掉内部粗norm等价的X依赖prefactor。整个盘的最终常数为exp(CRlog(R+2))，C独立有限素数集。

这一量词次序有效，不要求矩形截断对X一致；也没有把m_X^−1≈exp(2A)费用藏入o(A)。若仅有后者，本任务的Taylor指数确实不能闭。本审未发现上游这条必要桥的域、反射方向或增长障碍。

## 3. Actual质量、尾与localization逆审

设L=logX、A=√X/L、s_X=√X/L²。restriction的Taylor rank近似给s_(j+1)≤C_R√(T/π)(T/R)^j/(1−T/R)。它经真实weighted等距运输后与actual localized singular values比较，另用投影contraction界≤1。取T=L、R=√X/L⁴、n=ceil((4+ε)s_X)，logM_X=(2+o(1))A，几何尾可忽略，确得

    limsup Tr(1_[-L,L] S_X 1_[-L,L])/s_X ≤ 4。

这是带s_X尺度的actual trace mass，不是trace≤4，也不是Gaussian trial核质量。实际k_X按dt/(2π)为kernel，ρ_X=k_X/(2π)，故T_X[f]=∫|F|²k_Xdt/(2π)；没有额外2π可再扣。

全线tail方向正确：Sonin子空间reduces自伴P𝓕_XP且其平方在该子空间为I，因而S_X≤(P𝓕_XP)²。转Hardy Hankel block后，weighted commutator的非负difference-quotient核及Tonelli可用于measurable cutoff。它无需smooth-weight的signed trace-difference式(4.4)。phase导数的√X+log(2+|t|)粗界保留全部prime powers和Γ；对difference取min(2,Ca_t|v|)后，内积分为O(a_t)。固定Schwartz F与T=L使tail为o(s_X)。reflection只换F(t)为F(−t)，对称粗权保此估计。这里没有把trial-subprojection lower倒作整个Π_X upper，也没有将普通迹域扩到任意L²源。

localization独立核点如下：固定η的小区间中，Euler相位导数L+O(1)给E_X正测度下界，weighted norm于是给h在E_X的exp[−(2−9η/2)A]小值。quantile Lagrange的j!(n−j)!确实消去n^n费用，没有额外nlogn。取R=A/log³A、n=ceil((2+η)A/logA)、T=L^B，B先fixed，logC_R=o(A)、nlog(R/T)=(2+η+o(1))A，插值费用O_(η,B)(nlogL)=o(A)。这证明整个weighted unit球／目标complex disk的6.12 upper。

Q_X=||evaluation||_X²与actual k_X=|D_X|²Q_X相乘的系数方向正确。对于每fixedδ>0，Euler absolute uniform误差给4/√(1+4δ²)而Q上界给−4；可先选η小于该fixed gap的固定倍数，再令X→∞，得δ≤|t|≤L上exponential upper。fixedδ的中段及全线tail为o(s_X)，core只用上述actual质量。最终先X→∞再δ↓0，得到

    limsup T_X[f]/s_X ≤ 4|F(0)|²；特别地 ∫f=0 ⇒ T_X[f]=o(s_X)。

没有δ_X、η_X、moving-source统一速率，也没有从局部核信息跳到全线。另一终稿对上游U7／U8／UT已实际全文互绑，和本审的对象、norm、2π与量词一致，无循环依赖sharp lower。

## 4. 扣最强旧后的净后果

585给T_X[r₀]≥c₀s_X；587共同lower／moment spread和588弱源发散／fixed-anchor最优化均未支付当前相对upper。Gaussian t² upper只属辅助norm／trial，不能补出actual比值。因此本次新付款是相对浓缩信息，不是把两个旧lower相除或重验588。

题定587的du norm1偶bump r₀及r₁=r₀′均为原端点jets为0的合法固定源。r₁非零且∫r₁=0；完整537局部coercivity给q₀=Q_W[r₀]>0、q₁=Q_W[r₁]>0。故新upper与旧r₀lower给T_X[r₁]/T_X[r₀]→0，而完整目标要求q₁/q₀>0。α_X=q₀/T_X[r₀]的实际stationary正型tempered规则被此固定test严格排除。任意positive scalar β_X只要β_XT_X[r₀]→q₀∈(0,∞)，亦有同一失败。mean0不等于polefree，q₀／q₁保完整Γ／FP-contact、所有proper powers与双pole。

同lemma的更强直接后果也应消费：任意先fixed smooth compact complex r写作r=c_r r₀+z_r，c_r=(∫r)/h₀、h₀=∫r₀≠0，∫z_r=0。新上界给T_X[z_r]/T_X[r₀]→0，实际正型Cauchy–Schwarz同时控制z_r与r₀及两个zero-mean余项的cross terms。因此对全部先fixed源对r,s，

    T_X(r,s)/T_X[r₀] → c_r overline(c_s)，
    α_X T_X(r,s) → q₀ (∫r) overline(∫s)/|h₀|²。

该fixed-pair均值rank1结论无需r₀ exact leading或6.4 sharp coefficient。它与r₁未归一化迹仍可发散不冲突。当前没有支付从这些卷积配对到全部D′测试的factorization／拓扑论证，故不自动声明完整D′收敛；也不混同physical constant分布和spectral δ₀。

## 5. 消费范围与余项

PASS限于当前两终稿联合的(6.11)必要链、fixed-source零均值upper及上述scalar／fixed-pair后果。它改变这一纯scalar消失迹权规则的可行性，未排一般变化权、成长／漂移anchor、无界signed cross、独立非局部正族或primitive主线。完整signed净号／corecoupling／principal-mixed／Ξ仍欠，whole542+555→557 leading4/5负惯性UPPER不变，长期Goal数学门仍open。

未进行新web／下载／新文献／数值，不改manifest130，不续原sourceproof参数或章节。本审不授新编号、不计代理／文件／审稿轮，也不预判root已结算。当前root草稿仍写conditional属于执行阶段标记；以上版本技术链通过后，最终消费与唯一cadence更新由root完成。
