# 多点谱包络固定来源与有限重放独立审查

2026-10-08。审查者：radial_review。结论：**限定 PASS**。本审查完整核读被审 root 来源报告的全部74行、固定 Schwarz 提纲全部250行与正文谱包络/归一化段、ainta 原有限验证器和本轮重放脚本；数学及有限证书方法未发现阻断。实际 ζ 计数传递由另一份同轮审查单独核验，本文件不把阅读外部证明提纲当成全部解析链或 Lean 的完成认证。

## 1. 最终绑定与阅读范围

以下 SHA256 按 UTF-8 原字节 CRLF→LF、孤立 CR→LF 计算，不删末尾换行。

| 对象 | canonical LF SHA256 | LF 字节 |
|---|---|---:|
| [被审 root 来源报告](hybrid-multipoint-spectral-envelope-source-read-root.md) | 2c4a81a9a2d860e3d0882edb8a1a5928cda318679874c9be9b0adf18576b5dc5 | 5933 |
| [本轮重放脚本](../../scripts/hybrid_multipoint_cap_replay.py) | 8ac87f18cf928a51771556168e5af07400a3ba0333196b3e410394d8e4c37d05 | 11337 |
| [七点完整重放输出](../../output/hybrid-multipoint-seven-primary-replay.json) | aa6885489c1d0086bca32b72d27fc7a2a5f44a48f78483a057f23a59e5a828e6 | 2108 |
| [独立有理三点输出](../../output/hybrid-multipoint-three-rational-replay.json) | 4ee77471d08503c22a848e47a17713b44bd5f2afb95bfd57d994e878d9192456 | 1989 |
| [精确代数输出](../../output/hybrid-multipoint-cap-exact-algebra.json) | d84077ab71b47d1ea253cad9675fa8c25f9aa4dade775ad73ff53033167625c3 | 3367 |

本人还 FULL READ 本轮脚本调用的 [本地有理核实现](../../scripts/mt_triple_slack_audit.py) 全316行，其 canonical LF SHA 为597e950849415d979f236611a1ed623c4e2aff2e19dc73c801b5f5a244f0bf34。本轮 rational-three 只调用它的精确核及区间运算，不调用其中旧目标的搜索或模型计数。

外部 Schwarz 固定提交 e2453c1cafc1387ef553fe6bee74d1f5223ba801 的原字节清单与 MIT 许可已核；原 tex 读取370–510行，覆盖清单所称383–501的完整谱包络和真实 Gram 归一化，另 FULL READ docs/proof.md 全250行。原件 raw SHA 分别为：

- paper/riemann.tex：6b9796f4cd3b653781cf82de4dc6e22535076514ad62107312280abdbed85a01；
- docs/proof.md：594ec1cfc0ac0b4717bbe3a211eaa0a458b9ed318c3165bb4b5f5097fe8c0b9d；
- LICENSE：5b620cb5c067656c1174c376850723806951c00bf6e4bfccdcc348b86c367d90。

这些由[固定清单](artifacts/hybrid-multipoint-schwarz-e2453c1/source-manifest.json)逐项绑定。本审查未编译其 tex 或 Lean，未认证702行正文全部依赖或增强目标382623/10^8。

## 2. Cap 与多个大特征值的完整包络

被审§2的 cap 前件必须是 PSD 且 trG≤m。若 λ=2+δ>2，其余特征值平均≤(m−2−δ)/(m−1)<1；在[0,1]上 Ψ 递减，结合标量 Jensen 给
\[
 \operatorname{tr}\Psi(G)\ge1+2\delta+(1+\delta)^2/(m-1).
\]
若无特征值超过2，Ψ恰是平方差，故迹等于 Frobenius 能量。原列范数≤1的 Gram 符合迹前件；本稿没有错误地对任意 PSD 使用该 cap。

被审§3对 unit diagonal correlation matrix 的多个大特征值分支已逐式独核。令 λ_i=1+y_i、Σy_i=0，H={y_i>1}、h=|H|，并写 y_i=1+u_i、q=Σu_i≥r=(Σu_i²)^(1/2)。h<m，补集 Cauchy 给
\[
 E\ge h+2r+r^2+(h+r)^2/(m-h)
 =m(1+r)^2/(m-1)
 +(h-1)(m+r)^2/((m-h)(m-1)).
\]
又 E−J=r²。因此大特征值分支必有 E>m/(m−1)，且
\[
 J\ge E/m+2\sqrt{(m-1)E/m}-1.
\]
未将 h=1 当作全部一般情况。无大特征值时 J=E；两支连续，拼接导数≤1且非负。第二支的等号 correlation matrix 参数 a≤m−1，确实 PSD，验证了全 E∈[0,m(m−1)] 的精确包络。

由单调性及1-Lipschitz，E+x≥A、x≥0确实推出 J+x≥g_m(A)。这一步是将几何压力和谱缺陷合并一次，未将同一谱余项重复相加。归属声明准确：该更强包络已经存在于固定 Schwarz 来源；本轮不主张新的谱机制或世界纪录。

## 3. 真实 Gram 比较的限定

被审§4的两条归一化接口合法，但解析前件仍须明确付账。

固定 m 的 Gabor principal Gram 若对角为1+o(1)，置 R=DGD，Gram Cauchy 给 entries 一致有界，故 ||R−G||_F=o(1)。Ψ在非负轴全局2-Lipschitz，Hoffman–Wielandt 给谱缺陷差≤2√m||R−G||_F，非对角平方能量也仅改 o(1)。这里 m 固定，不能无说明改成 m=m(T)。

304 的直接 Hilbert 接口对每个固定平滑参数 δ直接给单位向量；实轴核一致收敛使固定 m 的能量误差 O_m(||kδ−k0||∞)。顺序必须是固定 δ、T→∞、最后 δ→0。对完整复零点保留的真实自伴算子和正惯性账本是实际计数传递的必要输入；没有通过删去非实零点来上界正和。

本人重读304§2、§3和§5的有限稳定性、完整算子、计数账本与两极限，并核305的历史基线及已知优先权。本报告不直接给出不同零点比例；一般 D≥(N+s)/2 本来不成立，被审稿已经正确警示，后续必须用完整 HS 和实际 b 的关系消元。

## 4. Ainta 固定有限验证器的方法核验

[ainta 原清单](artifacts/hybrid-multipoint-ainta-040c5e8/source-manifest.json)提交040c5e899e658aed7b56a2a87f501798fe10761d的复制模块已经 FULL READ：kernel.py190行、rounding.py45行、constants.py23行、verify_seven.py339行、verify_three.py106行、report.py46行及初始化文件。脚本逐项校验复制原字节 SHA 和许可后才导入；其中关键原字节为：

| 模块 | raw SHA256 |
|---|---|
| kernel.py | e83aa966699770bc72f67d3e55079cff89c2432a05ad25abd12afc8cbf9af1dd |
| rounding.py | 2419f77bae2fb73ccb1da4e5d2bbaf3247e7d900d53871de9011296f7de5844e |
| constants.py | 8344ed3792603e51a5621a72fc04e0f5bcb115c6599a72579b7a0f4b89c0bbff |
| verify_seven.py | 66ff0b10d18125144521f110afb5c0de9f9201e04c7e6ad6ad6cc6311080c355 |
| verify_three.py | ef2b91bb3323fba459cc5e0b2be2e9408da7a39ba9c56517833c6e3c7109ab20 |

归一化 k(0)=1 与真实 K(0)=√2 sin(1/√2)正确。闭 cell 由精确 fmpq 中心和半径输入 Arb；span 个 gap cell 的整个和区间为[Σlow,Σhigh+span−1]，查询包含端点。超表范围的平方下界取0、二导数下界取−∞均保守。

七点 local pressure 是1/3000，聚合六个 gap 后是1/500；cutoff45600/grid4000/3000=19/5000 精确。因此域外任一 gap 和低索引和剪枝不用浮点等号。one-body 用向下值对向上目标比较。Hessian 对负二导下界选系数上界，对非负下界选系数下界，每项再向下舍入，保留了符号。

浮点 LDL 仅作启发，接受 tangent 前会用各 binary64 的精确有理表示重建 Arb 下界矩阵、证明所有 pivots 严格正。半正定外积项和 Hessian 下界保证整箱凸性；再由中心值及梯度区间给整箱 tangent 下界。不能由未认证浮点 LDL 直接剪枝。未解决 terminal cell 抛异常；只有栈完全清空才报告 verified=true，故该程序不是采样通过。

## 5. 本轮独立重放与证据边界

本人实际以只读 --check 执行：

~~~powershell
C:\Python312\python.exe -B scripts/hybrid_multipoint_cap_replay.py algebra --check
C:\Python312\python.exe -B scripts/hybrid_multipoint_cap_replay.py rational-three --check
~~~

两项均退出0并 PASS，与冻结 JSON 除运行时间外的全部确定字段一致，未改源或输出。

有理三点重放使用 Machin π、整数平方根、带显式余项 sinc 和精确整数量化包络。正 Fourier 概率核的 |k'|≤π 给整 cell 的区间扩张，三个平方下界保留符号过零情形。闭三角域完整覆盖；资源/terminal 失败均不会生成 PASS。输出445581节点、333733有效 leaves、453域外 leaves、深度19，目标221/10^6成立。它是独立有理方法，不伪装成执行了 Arb verify_three。

七点冻结输出记录原 verifier 完整执行：707901节点、354315剪枝、353586分裂、最大深度37、初始729箱；三种剪枝计数257493+3087+93735=354315，核表 SHA a9992300d2bf71665aa2b6bd2727e798624cd297103bb200c7f0ca2baea55a2c，二导数表 SHA 7913c5511a572c32dd573cd53123d8cf3ddf73d3ec63b1aa823faae2ae83570a。本人 FULL READ 方法、输出和绑定，但未重复七点执行；compression 的首次完整运行及其只读 --check 另行记录，root 完成代码/输出阅读与精确代数复核，均不能写成本人的七点实跑。

精确代数以有理 Taylor 余项和整数根包络重现 C0、m269、m270 cap 比较，以及 m280 已知 g 包络的明确更强结果。显示小数不是认证基础。原 trace cap 的小改善和已知 g 包络的更强数值均未被称为首次纪录。

## 6. 结论与未认证范围

被审来源稿和有限代码方法限定 PASS。本轮 root 已阅读的外部全提纲、本人独立数学证明、成功有限重放、原解析输入及真实零点传递是不同证据层；本文件保留此区别。

未在本审查认证：Schwarz 增强七点目标、其全部 Lean 闭包、全论文所有解析依赖、世界纪录或有限高度真实零点认证。有限核证书不证明 RH，也不将原 growing fourth 上界当成 O(1) 四矩预算。实际比例及不同点计数须以本轮独立计数源和对应审查的完整前件为准。
