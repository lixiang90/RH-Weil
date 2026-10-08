# 十点三帧 sharing：完整低集阈值、共同闭包与有效切线

2026-10-08；perron_reviewer；本轮基线 609fe754，cadence 0。
保持 483 的 AM13 原核、θ=4/5、全部真实零点与重数、既有连续和组合计算信任。
本源证明新的十点覆盖与切线加强合同；**未取得十点统一正余量或新增比例**。
不把旧 70 胞称为更强目标的完整覆盖，也不修改任何冻结源、程序或 Git。

## 1. 输入及实际读取

canonical UTF-8 LF 为 CRLF/lone CR→LF，保留 EOF。

| 输入 | 行／LF 字节 | SHA-256 |
|---|---|---|
| [九点数学记录](am-affine-leaf-minorant-research-perron.md) | 167／10827 | f9616af18e61015682a3c41cebab630af72d9f107da1e9cb7424265875ad5a14 |
| [九点 verifier](../../scripts/am_nine_point_epigraph_certificate.py) | 236／11009 | af5f2e1974bed92ad515f06ff6047f3e5595ac60c6dc721abd7bfb5cfd930c32 |
| [九点证书](../../output/am-nine-point-epigraph-certificate.json) | 68844／1112534 | 0733022044f96b37c6be3d5d5c1e9fa6c269545142d7d535e643c835a7cf38f6 |
| [九点论文](../../papers/nine-point-joint-minorant-simple-critical-paper.tex) | 828／33967 | 5a7499ddcdd290a25a39f568965c00bcc833975688553f2321ebf02643e538a6 |
| 固定 Solution.lean | 19049／1675641 | 012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f |
| 已准入 NumericCore.lean | 11608／990515 | f21a0d9f141a7807a6524f426b64a0c0b7b2e81e12581d3ec528f467e9bd1be3 |

167/236 行与九点 lift 本轮全文重读；828 行论文上一轮全文审查，身份本轮重核。
原解码源位于 tmp/pc8-am-admission；本轮重读 PTF 10640–10662、
ext_tangent 10716–10768、tcheckPZ 12040–12064、TVal/tangent_valZ
12212–12270、mokTZ/mtermTZ 12431–12445 及 mcheckP 的完整数值入口。
所用 tangent_valZ 的其余延拓证明已经在前轮全文核对；本源不新增解析公理。

设 SA=10⁸、SC=32768、w=K²、c₀=805003/SA、δ₁=10⁻⁶、
c₁=c₀+δ₁=805103/SA，B=404350/SA。旧 F₈ 在全部非负七 gap 上≥c₀；
已准入 F₉ 在全部八 gap≥θ 上≥c₁。

## 2. 十点精确展开、预算及无穷尾

对九 gap \(g_0,\ldots,g_8\ge\theta\)，令 A、M、C 是从位置 0、1、2 开始的三个 F₈。
令 \(S_L=\sum_{0}^{7}g_r,\ S_R=\sum_{1}^{8}g_r,\ S=\sum_0^8g_r\)。
十点 lift 精确为
\[
F_{10}=\tfrac12(F_9^L+F_9^R)+2w(S)
       =\tfrac14A+\tfrac12M+\tfrac14C+w(S_L)+w(S_R)+2w(S). \tag{1}
\]
旧≤7跨度的权是三个完整旧帧按 (1/4,1/2,1/4) 卷积；
span8 的两项各为1，span9为2。每个 index-span 总预算仍≤2，全部权非负，总权≤18。
压力为
\[
b^{10}=\frac{(28898,115068,218968,289282,312968,
289282,218968,115068,28898)}{4SA},\quad \sum b^{10}=B. \tag{2}
\]
因此对任意候选 \(c_2=c_1+\delta_2\)，无限域中
\[
S\ge9\theta+\frac{c_2-\theta B}{b_{\min}^{10}}
\quad\Longrightarrow\quad F_{10}\ge c_2,\qquad
b_{\min}^{10}=28898/(4SA). \tag{3}
\]
坐标界 \(g_r\ge(c_2-\theta(B-b_r^{10}))/b_r^{10}\) 也直接支付。
它们是连续解析尾部付款，可用于缩小有限候选域，不能用有限搜索替代。
例如 δ₂=10⁻⁶ 时 (3) 的总跨度界为 5337394/72245。

## 3. 真正完整的三帧低集：中间帧可用更小阈值

欲证 \(F_{10}\ge c_2\)，只需处理两个 \(F_9<c_1+2\delta_2\) 的同时低集；
若任一不低，由另一 \(F_9\ge c_1\) 和 \(w(S)\ge0\) 已付目标。
又 \(F_9^L=(A+M)/2+2w(S_L)\)，其旧帧另一项≥c₀，故
\[
F_{10}<c_2\quad\Longrightarrow\quad
A,M,C<c_0+2\delta_1+4\delta_2. \tag{4}
\]
还可用 (1) 中 M 的权为1/2，且 A、C≥c₀，直接得更强
\[
F_{10}<c_2\quad\Longrightarrow\quad
M<c_0+2\delta_1+2\delta_2. \tag{5}
\]
所以两端旧帧捕获阈值与中间阈值分别可取
\[
T_E=\lceil805203+4SA\delta_2\rceil,\qquad
T_M=\lceil805203+2SA\delta_2\rceil. \tag{6}
\]
向上取整扩大低集，仍安全；向下取整可能漏真实边界。
只跑最大阈值 \(T_E\) 的原叶 capture 足够；中间列表可通过同叶 exact strong guard
在 \(T_M\) 是否成功筛除。必须复演原 Ng/YA 比较，不能按 F₈ 样值或浮点值筛。
例如 δ₂=10⁻⁶ 时两个 target 为805603、805403。

原 clear COV 区的额外压力≥θB，large-gap 区的额外压力≥θ(B−max b)。
故保持原 32 根与反射的充分整数阈值条件为
\[
T_E-805003\le\lfloor SA\,\theta(B-\max b)\rfloor=258713
\quad\Longleftarrow\quad
0<\delta_2\le258513/(4SA)=.0006462825. \tag{7}
\]
未取整时的上限为 .000646284；不能把该连续边界直接用于向上取整后的 target。
该范围内，强比较只改变日志筛选目标，旧返回、cursor 和 traversal 保持；
direction 恢复完整反射，empty leaves 仍只排空域，零宽/闭端点均保留。
新的 failing 列表与其记录须实际完整捕获，不能由本推导预测数量。

现有70胞仅覆盖 \(F_8<c_0+2\delta_1\)，对于 δ₂>0 不自动覆盖 (4)–(5)。
仅凭旧全域和此阈值，A=C=c₀、M=c₀+2δ₁、三个新增平方为0时，
所有已知 scalar lower bounds 相容且 (1)=c₁；这是代数输入不足的示例，
不是实际 AM 核或 ζ 的反例。旧九点内部 strict margin 也不能自行支付它的外域。

## 4. 三帧共享 LP 的完整几何和角点误差

三个旧 frame 的真实 union 有9 gaps、33 long spans，共42种区间约束。
旧26正权项的 physical union 为40对；加两条 span8和一条 span9为43个 z。
所以 joint epigraph 有9 gap+43 square=52变量，而不是三个独立优化问题。
先合并全部约束及 θ，再对10个 prefix 坐标做完整 difference closure；
空胞用负 cycle/Farkas，非空胞保留有理有限 gap boxes 和实际共享 \(z_{ij}=w(y_j-y_i)\)。

未缩减目标是 \(4SA F_{10}\)：三个旧 frame 的 integer pair weights 按 (1,2,1) 合并，
span8两项各4SA、span9项8SA，压力分子恰为 (2) 的整数向量。
全部 atom constant/line cuts必须按同一个 physical span 收到同一个 z；0≤z≤1由原概率窗。
任意有理 λ≥0 的残量 \(r=q+A^t\lambda\) 必须付完整有限盒
\[
F_{10}\ge\frac{-\lambda^tb+\sum_i r_i(\ell_i{\bf1}_{r_i\ge0}+u_i{\bf1}_{r_i<0})}{4SA}. \tag{8}
\]
因此恢复负斜率之后也不能只测试自由角点，更不能丢残量或跨度耦合。
旧 YA/sliding/双帧 dual 可作合法初始下界，但新目标或新交集必须重新消费精确 (8)。

## 5. 最先重用共同闭包，再增加真正通过校验的 PTF 切线

设旧 enabled point p 的 TVal 已在 \([l_0,u_0]\) 有效，点值下界为 v，
实际斜率 d∈[d₋,d₊]。共同闭包把该 physical span 缩到 \([l,u]\subset[l_0,u_0]\) 后，
取 \(l_*=\min(l,p),u_*=\max(u,p)\)，新合法 affine cuts 是
\[
v+d_+(l_*-p)+d_-(x-l_*),\qquad
v+d_-(u_*-p)+d_+(x-u_*). \tag{9}
\]
旧 anchored-cut 证明直接适用，因 x和p仍在 \([l_*,u_*]\) 内。
相对旧两条线，截距分别增加
\[
(d_+-d_-)(l_*-l_0),\qquad(d_+-d_-)(u_0-u_*), \tag{10}
\]
均≥0。当前236程序用各原叶端点生成 forms；这步三帧闭包重锚无需新表或新 tangent check。
若整个实际 span 在p右侧，可直接用 \(v+d_-(x-p)\)；
左侧可直接用 \(v+d_+(x-p)\)。若跨p，须真实按span=p分域才能用这两段；
不分域直接取两线最大值一般不合法。

再加未被旧FS选择的 PT点，必须保留独立连续语义：
PTF只给点值与导数包络，不自动给整段 tangent。
可以固定 expanded interval 包含实际 span 和p，运行原
tcheckPZ REG top bk 8 L U p (PT p) (treadU ... U p) (treadD ... L p)=true，
再由 tangent_valZ 使用原 LBSound、LBSoundD、PTF、rgOk 前件取得 TVal。
若 expanded interval 全在该p对应的同一已准入 REG convex 段内，延拓两侧自动不需要；
段外则须原 derivative/zsideF 校验实际成功，不能只读取 packed PS。
有理闭包端点转 Nat query 要下端向下、上端向上取整，且扩入p；
uc 的零宽扩张仅用于 lb，不替代 tangent 的真实域。新增结果要逐点保存和回放。

## 6. 全谱消费与实际状态

若新完整 cover+全部非空 joint (8) 以后证明 \(F_{10}\ge c_2<1/40\)，
十点滑窗给 \(c_2(m-9)-B\,\mathrm{span}\)，最多18权的平方平滑误差≤36dε m。
原 θ=.8 majorant/near pair、固定 normalized smoothing、pinching、
全真实零点 Hermitian/minmax 与重数计数保持；先 T→∞、再 ε→0。
条件比例仍是 \((2-C_{\rm AM}-B)/(1-c_2)\)，端项9c₂不能在有限阶段省略。

本轮独立 Fraction 算式实际退出0，核 (2)、九个span budgets、42/43规模、
(6)的示例、(7)与(3)的有理界；这些有限检查不替代连续证明或新 capture。
现阶段新增的是更小的 middle-cover 阈值和零新增公理的 closure-cut 加强。
尚没有十点新全域 certificate、统一 δ₂、正式新比例、原算术省幂或新零点条带。
