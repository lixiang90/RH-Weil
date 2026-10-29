# Fresh audit：固定可数 Mellin 数据的完整 Pan 像

2026-10-29；`/root/moment_fullimage_fresh` 独立逆审。结论为**限定 PASS，无必须修正的数学缺口**。本稿只消费所列原件以给 root 审查意见，不更新 STATE、计轮器、合同、Goal 或 Git；出稿不代 root 消费。未访问网页、下载来源、运行数值或导入抽象矩问题定理，不声称文献首创。

## 1. 恢复与所读版本

已读 AGENTS、README、STATE，实际执行 `research_state.py check` 后 `show`；结构验证通过，不将其当数学证明。读原 Goal 的完成门与工作规则、停止的 C060、D20261029AC、宏观前沿当前段及唯一后继准入。工作树当时为 root 正在更新的 STATE 与本轮新原件，没有把旧 C060 预算重新启动。

STATE 与 parent 已核运行实例为 G20261027/1793085111、冻结基线 0c4f3a3eb609bb1d9564138fa4a35701f05605f2。子 agent 的 `get_goal` 实际返回 `goal:null`，因此本稿不声称自己独立读到了 runtime active；运行 Goal 的 live 核验由 root 负责。未创建或更新任何 Goal。

以下两原件实际全文读完，再按 raw bytes 重 hash；均 UTF-8 LF、无 CR：

| 原件 | bytes | SHA256 |
| --- | ---: | --- |
| `triangular-interpolation-and-pan-ideal.md` | 12702 | `8437005a7b3818ca6946f51a3e5d32d68f372cf2b23f1be4a465ab993fae0ff3` |
| `strongest-old-and-net-scope.md` | 13068 | `6b6f968b114fe664cd1a9fc8f8fb99b5a7335ad369020972209b284b0f149a29` |

必要依赖另实读：405 的明确 S_exp/实际 E 像/卷积 ideal 与真实 p，597 的 physical 公式、关系角色及精确/渐近范围，519/520 的对象和零点 jets/谱范围，finite-cover-trace 原稿 §§3–4 的有限像和 product-density。没有把旧去重稿声称读过的其它全文全部冒称为本 fresh 的直接阅读。

| 冻结依赖 | bytes | SHA256 |
| --- | ---: | --- |
| `goals/GOAL.20261027.md` | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| `formal-mellin-admission/next-full-image-moment-admission.md` | 2559 | `51c90b825f563424db54e8ab8d946fc5baa0855c1aa65cfcb069c8199a3357f0` |
| `notes/405-f1-adelic-restriction-moments-and-radical.md` | 14633 | `fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d` |
| `notes/597-formal-mellin-source-boundary-rank-obstruction.md` | 7886 | `51f2e19bb06515d248a310430f0b612ba844c4f7bf9fddf784c0d0dab6251c75` |
| `reviews/2026-10-27/finite-cover-trace/old-consequence-and-repairs.md` | 18129 | `1cdfcd77f6d194c2d4ef1188b561cb57e23939562072d332525c2a79ad64b0cc` |

本目录相对路径的两个新原件均位于 `reviews/2026-10-29/full-image-moment/`；表中 `formal-mellin-admission/` 相对同日 reviews 目录。哈希只绑定版本，不替代以下推导。

## 2. 审查对象与须付结论

固定 physical 实源 F=S_exp，全部 p_(N,k)(r)=sup e^(N|u|)|D^k r(u)| 有限。原始源是 U^(-1)r=e^(-u/2)r。固定 α_n=n+3/2、ℓ_n(r)=∫r(u)e^(α_n u)du=M_r(n+2)，数据为整个 B(r)=(ℓ_n(r))_(n≥0)，目标为无增长约束的 R^(N_0)。这个 B 不表示 Weil 配对。

405 给 raw 实际像 J=E(S_even,0)、闭像 I、P_an=I∩ker c∩ker d；physical P_phys=U(P_an)。待审的强结论是

    B(F)=B(U(J∩ker c∩ker d))=R^(N_0).                 (A)

实际 J 子类比仅用 I 更强；它仍是解析/adelic 关系，不自动成为几何主除子。无须也没有断言 ker B=P_phys。

## 3. 独立重导三角构造

固定非零非负 ψ∈C_c∞((0,1))。紧支分部积分给 ℓ_j(Df)=−α_jℓ_j(f)，故对 L_n=∏_(k<n)(D+α_k)ψ，

    ℓ_j(L_n)=∏_(k<n)(α_k−α_j)ℓ_j(ψ).

j<n 时恰有一个零因子；j=n 时 A_n=ℓ_n(L_n)=(−1)^n n!ℓ_n(ψ)≠0。非负 ψ 确保 ℓ_n(ψ)>0；这里的 D+α_k、(−1)^n 与正向平移 τ_a f(u)=f(u−a) 三个符号相容，ℓ_j(τ_a f)=e^(α_j a)ℓ_j(f)。

给任意实序列 b，已构造有限前缀后令 δ_n=b_n−Σ_(i<n)ℓ_n(g_i)。δ_n 只用有限个实际紧支项，故有限。取

    g_n=(δ_n/A_n)e^(−α_n a_n)τ_(a_n)L_n.

选择 a_n≥n+1、a_n≥a_(n−1)+2，支集分别包含于 [a_n,a_n+1]，局部有限。对 N,k≤n，

    p_(N,k)(g_n)
      ≤|δ_n/A_n|e^N||D^kL_n||∞e^(−(α_n−N)a_n).

α_n−N≥3/2，所以对每个 n 的有限批半范数可同时压到 2^(−n)。a_n 可在 δ_n 已知之后再选；其可任意大，不需 b 或 C_n 的增长界。δ_n=0 时 g_n=0，同样可选支集位置。不存在用未知未来项反向定义当前残差的循环。

对每个固定 N,k，尾部 n≥max(N,k) 有 Σp_(N,k)(g_n)<∞；有限前缀不影响。局部有限的实际函数 G=Σg_n 光滑，所有导数的加权一致尾趋零，故 G∈同一 F，且级数在全部原半范数中收敛。并未仅得到 formal coordinate limit，也未更换源的完成化。

对固定 j，取整数 N>α_j，直接有

    ∫|f|e^(α_j u)du ≤ [1/(N−α_j)+1/(N+α_j)]p_(N,0)(f).

故 Σ_n∫|g_n|e^(α_j u)<∞，moment 换序有绝对证书。n>j 的项精确为零，第 j 项补齐此前有限和，得到 ℓ_j(G)=b_j，对全部 j 同时成立。这是一个 G 实现完整序列，不是不同有限长度的不同源。第一项 B(F)=R^(N_0) 已付。

## 4. 独立核实际 Pan 原像和半密度

U、U^(-1) 为 F 的连续自同构；对导数用 Leibniz，p_(N,k)(e^(±u/2)f) 由有限个 p_(N+1,l)(f) 控制。普通加法卷积满足 p_(N,k)(f*g)≤2p_(N,k)(f)p_(N+1,0)(g)，且

    U(f*g)=(Uf)*(Ug).

405 的固定 raw p=(D²+D)h=Eη_0 属实际 J，c(p)=d(p)=0；physical P=Up。给 physical G∈F，必须以 raw g=U^(-1)G 卷积，而不是直接把 G 与 raw p 混用。实际 Schwartz 原像为

    η_g(x)=∫g(t)η_0(e^(−t)x)dt.

对每个非负整数 a,b，微分与换元分别付 e^(−bt)、e^(at)，故 q_(a,b)(η_g)≤q_(a,b)(η_0)∫|g(t)|e^((a−b)t)dt<∞。同一支配允许逐阶微分；所有 Schwartz 半范数有界。η_g 实偶、在0为零。又 ||η_0||_1∫|g|e^t<∞，所以 ∫η_g=0 的换序合法。

从 |η_0(x)|≤C(1+x)^(-2) 得 Σ_(m≥1)|η_0(mλ)|≤C/λ：可由递减函数的积分比较直接核。每个固定 u 下，E 求和换序被 C e^(−u)∫|g(t)|e^t dt 控制。因此

    g*p=Eη_g∈J,
    P*G=U(p*g)∈U(J∩ker c∩ker d).

raw c,d 的乘法来自带指数权的绝对 Fubini，二者因 p 而为零。这闭合了实际 E 像，不需要519的 J 闭性或以 I 代 J。对应 physical 的两个零矩为指数 ±1/2，不是 ordinary mean 的两个版本。

physical M 的指数是 s−1/2。对 P*G，两个加权绝对 L1 范数有限，故 M_(P*G)(s)=M_P(s)M_G(s)，与 raw Mellin 参数 s 一致。由405/597已付公式，

    μ_n=M_P(n+2)
       =s²(s−1)²π^(−s/2)Γ(s/2)ζ(s)/4 >0, s=n+2.

只用实 s≥2 的 ζ Dirichlet 级数和 Gamma 正性，不用 RH 或 π 超越性。把三角插值用于 b_n/μ_n 得 G，Q_b=P*G 为一个实际 physical Pan 关系且 B(Q_b)=b。这证明(A)全部强版本。

实部、虚部分别构造，直接得 complexified F、P_phys 的 B 像均为 C^(N_0)。这只赋源与数据复结构；597的实际 Φ仍仅按原加法商处理，不偷偷赋复标量或改 arithmetic carrier。

## 5. 最强直接消费：exact、mixed 与 pointwise indexed

(A)给每个固定 r 一个固定实际 Q_r∈U(J∩ker c∩ker d)，全部 B(Q_r)=B(r)。因此只依 B 的任意 set postmap，若把全部 Pan 送到同一 base，也把全部源送到该 base。无需线性、连续性、局部性、有限秩、norm bound 或 Hausdorff 性。所有自适应参数若也只依 B，仍已包含在同一 map 中。

同理 J_formal=ι∘B 的 Pan 像等于全部源像；进一步 Φ 商或 set postmap 不能既消全部这些关系，又保537某个正非根。此论证仅用了必须消 Pan 的必要条件，没有要求 ker J=Pan。

若配对 H 仅依 B(r),B(s)，且对全部 Pan p、全部 s 满足 H(B(p),B(s))=0，取 Q_r 替换第一槽即得 H 在全源数据上为零。没有自动 principal map 或 positivity 前件；它不能等于有537正值的完整 Weil 配对。这是(A)同一集合后果，不另计 mixed 新轮。

更强 indexed 后果也必须一次收齐：对任意同数据族 F_κ、任意 fixed r，

    F_κ(B(r))=F_κ(B(Q_r)) 对所有 κ 同时成立。

Q_r 与 κ 无关。因此在同一目标识别/收敛判据下，若每个 fixed真实Pan都点态趋规定零/base，每个 fixed源也如此。改变目标拓扑、允许非连续/非线性/任意增长费用，均不能破坏每阶段相等；同B、全局同域、全部fixedPan责任下的 pointwise 渐近不是逃逸。混合配对同样可固定 Q_r 与 s 后传递这一点态后果。

必须精确区分：若**每个阶段**都 exact 杀全部Pan，则每个阶段都在全部源像上常值，连 joint 成长 r_κ 也不能在这项 exact 结论下逃逸；若只要求每个 fixed Pan **点态渐近**消失，则未得 uniform rate，不能自动外推所有 joint 成长源。原两稿的费用/成长保留应按这两个量词阅读，不能混合成更弱或更强边界。

597的形式尾截断真实存在，但它同时消所有 fixed源，恰与新结论相容；不是反驳(A)，也不是保 nonroot 的构造。真正未排的是携带 B外额外源/finite/arch/relative数据、不同实际源域使 Q_r 不准入、不同encoder、只测有限/较小关系类，以及没有全局同F全部Pan点态责任的独立正 D′ 比较。

## 6. 最强旧与计轮判断

405已付实际 ideal 与固定非零 p；519/520已付完整零点 jets 和谱商。这些不是当前无界正实整数采样的任意取值满射。597已付单关系无限 Q秩/有限 Q秩 exact修补边界，不能从一条非零关系直接推(A)。

finite-cover 原件已付任意有限 readers 的同像与无限reader的 product-density；其 §4 明确不付 exact infinite image 或任意非连续 postmap。584的一维同像后处理与 compact-real uniqueness，也不能免费替代完整可数构造。对本门有限 α_j 样本，虽各 reader 是 δ_(α_j) 而非 L1，finite-prefix结论仍可由405平移直接重得：若有限 Σc_j μ_j e^(α_j b) 对全部 b 为零，最大指数逐次剥离给全部 c_j=0。α_j≥3/2 不含两 pole例外。这是旧有限维机制，不是本门新增。

因此已付有限投影和 product-density必须先扣。新的责任仅是：在同一 S_exp 中实现任意完整可数序列，并把它提升到一个实际 J 中的 physical Pan；由此排不依连续性或norm的同数据完整后处理及其上述点态族。新证明没有退回只证明有限 jets，也没有靠有限维像闭性错误推出无限满射。

建议 root 在原稿/本 fresh 前件全部消费后，把(A)、complexification、actualΦ进一步商、exact/mixed/pointwise indexed 后果统一按**一个实际数学迭代**结算；不按构造引理、ideal重核、标准集合推论、审稿或文件计轮。若 root另找到同一无界全序列已付原件，应相应去重；本 fresh 不主张穷尽外部文献。

## 7. 长期完成门与停止

原 norm 与几何责任未付：未给任意序列范数到 du/zero-extension Dlog/Hilbert 的统一选择代价、连续线性截面、成长窗/Ξ集体控制、新非零 arithmetic primitive、真实 principal/section/mixed RR、或 full Weil dangerous core/cross 的独立有利净号。全源集合满射不能被这些标签替代。

故 whole542+555→557 leading4/5负惯性UPPER未改，Goal三门仍开放；本 fixed encoder 的完整同数据边界不自动通过实质核心方法类完成门。C060停止范围保持，本次证明不得倒填为597的前件或恢复其预算。后继须另有实际 input/test/net，不能因本审稿 PASS 自动转新采样、frame、degree、源权或来源章。

本 fresh 无必须修项；以上 exact与pointwise成长量词澄清须在 root最终消费中保存。最终数学计轮、宏观第4轮审视是否执行、STATE/cadence及GitHub发布均由 root按实际状态处理。本文件之外无修改，无后台进程。
