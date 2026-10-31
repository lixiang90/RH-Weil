# 直接9/8完整Weil证书：已有全head数据，未出现新整体sign输入

2026-10-31；`/root/whole_weil_matrix_input` 独占审计。Same G20261027/runtime1793085111、原冻结0c4f；父任务本轮已核6e472102发布，本稿不冒称独立核父Goal/API。恢复README/STATE、check后show、Goal完成门、C066准入快照/603结算、BC及前沿。当前只是不同的direct-Q准入，不建C067/604，不计数学轮。

## 1. 本次实际读到的现成数据

读取537、595及595 physical-root消费中的必要范围，定向核全窗/解析transport和physical-lower的strongest-old稿；实读physical-lower脚本，core脚本的固定配置、trial/inverse/compiler段及source/scalar/cosh脚本的配置与输出边界。没有运行科学driver、proposal、Gram、witness或同v重放，没有新web/primary/作者正文。

另实际读取并计算下列本地旧packet的SHA，与旧receipt一致；不是根据文件名猜测内容：

| 原packet（相对`literature/local/2026-10-29-weil-9-8/pilot/`） | bytes | SHA256 |
|---|---:|---|
| `run-01/certificates/moments.json` | 734638 | `2d166f7ae457fd61826329d31365564e25f1cfc6bc19d09aef22d2ec89c6bbd9` |
| `run-01/certificates/source-matrices.json` | 23377672 | `a5486fea38c3c8f91dcf4bb77c7677e734efe2ac9cbf59ddabc4674739fdb2f2` |
| `run-01/certificates/tail-columns.json` | 296046 | `d714fa8d717a8f39d8b3b57cc6292e3f14844041b83802cf57ee47aa03c65a0e` |
| `core-run-02/even-target.json` | 43104610 | `14dcbebe5b553d7fa30e5e0d2ded203c32d75693cc3f2e39525fc236673f6401` |
| `core-run-02/odd-target.json` | 43104681 | `847fa3a860460571de45201b977bf10ad7a2077d6f573a29c6b5f10651d3a1e3` |

Source矩阵含N448的A/B/J0各50400个同parity上三角interval，共151200项；覆盖两224-sector。固定L9/8、Omega256、完整pp字典2/3/4/5/7/8/9、15 shifts和225 ordered pairs已经重建。896尾列项也已存在，不是本次需要从零生成的小head。

两target各有50176个完整entry、双compiler equality；它们是595的congruent充分比较Kcert，**不是完整Q矩阵**。Even原Kcert已有exact负witness，odd target已编译而odd Gram未执行。这里未重跑其sign，也不把compiler equality当PSD。

Packet自身的SOURCE_ONLY/`fullQCertified=false`、tail的`fullQTransfer=NOT_ESTABLISHED`等是有限生产阶段的历史scope；595后来已另付解析/原范数误差桥。本稿不以这些flags回滚已付旧数学，也不把它们改成全Q PASS。哈希只核版本，不认证定理。

## 2. 矩阵与范数的准确角色

在I=(-9/8,9/8)的原du空间，源f即本项目physical r=e^(u/2)bare，不再加第二次半密度。以raw Legendre p_j为基，

    Γ_du,jj=2L/(2j+1)=9/[4(2j+1)].

Even sector j=2i时，Γ_du=18 diag(8(4i+1))^−1。这个Γ是有限源的**du Gram**，不是Dlog Gram，也不是archimedean Γ(t)=2θ′。有限Legendre零延拓为compact BV、Fourier O(1/t)，故在zero-extension Dlog域，但这不使两个范数相同。

JSON A/B/J0先是raw interval/center矩阵；经该正Gram congruence后，分别对应

    A=E*ME，B=E*M²E，H₀=E*Kcompact E.

B保真实三重overlap和middle compression，不能替为A²；packet的J0约定明确是`L_squared_H`。两raw tail columns给既定U=81|h₀><h₀|+27|h₁><h₁|，raw系数36及归一由旧解析桥支付，不是完整非有限秩Fourier-tail矩阵。

原全型在Dlog上是

    Q_W(f)=〈f,(M+Kcompact)f〉+T_tail(f),
    T_tail≥τ||f||²+〈f,Uf〉，τ=2^−49162.

因此这些数据能装配的canonical bounded head是Llow=M+Kcompact+U的compression；Q_W还含未用的非有限秩positive tail。完整Γ/contact、所有proper powers及even正/odd负双pole在原恒等式中，不能用这些JSON把Q写成一个有界全L²矩阵。现有packet也没有直接输出完整Q的Dlog Gram或全部tail-energy head。

## 3. 最强已付结论及真正缺失的耦合

537已付17/16窗全复Dlog coercivity与全补空间，不只是有限head。595则已付9/8新源区间、M上下界15/64和433/64、全tail供给、projection/kernel/source误差、完整inverse/congruence/两compiler；本固定充分目标P₀非PSD。改变同一目标的Gram精度不能修正exact负号。

595的physical后继又已完整消费同一source链

    v→Bc v→raw x=Vint v/(18Cw), Cw=2^769,

得到同物理norm的Llow Rayleigh在(2^−62,2^−61)，P₀在(−2^−67,−2^−68)，合并gap>2^−62。v的14个非零contract坐标不意味着physical源低阶；raw源全部224项可非零。这个强旧point已比“P₀负所以Q可能负”的弱读法强，不能重算或重新归因某条inverse腿。

即使现成raw数据装配出的全448 head C_head为PSD，也仍须控制M的head/complement coupling。理想精确finite-range情形涉及G=E*M^−1E及A−G^−1；实际情形还带已付source/projection/cross误差。现有W≥G及α/β费用给的充分比较P₀恰在这一步失败。仅有C_head≥0、M≥mI或某个向量C_head>0不能支付整体Schur margin。

特别地，一般residual inverse写法不是新输入：595的既定trial已经含

    Z+Z*−Z*AZ+8R*R，R=E−MEZ，

等价于其8I+Z+Z*+Z*(8B−A)Z−8(AZ+Z*A)结构。重新命名为residual/graph/normal equation不会产生新的whole signed比较。若改trial、μ、theta、N或precision，则是原停止配置的修复，不能从现有预算自动继续。

未出现的实际证据是：一个不同且有误差闭合的原范数Schur下界，或对完整未用tail与全部head/complement的联合signed供给，足以把同一完整Q的全源sign闭合。把它写成“需要控制G/剩余tail”只是缺口描述，本身不是新input或新test。

## 4. Pilot裁决与边界

**本次不运行pilot。** N≤64的A/B/J0/U compression已包含在旧448完整数据里；抽取后做PSD或eigenvalue检查不能改变上述whole耦合选择。另造完整Q小head虽会加入未用tail的有限数值，但在没有新全补空间/耦合机制时仍只给head现象，不能据此重开9/8窗口/精度/方向链。本任务允许的单次pilot因此没有必要条件，不以“多算了一张矩阵”制造输入。

现有driver均绑定固定source路径/配置和exclusive输出，不是可安全改N的通用whole-Q API；本稿未执行prepare/run，不改旧大数据。唯一新文件是本审计，没有新科学过程或待轮询handle。

裁决为**已有数据的strongest-old恢复／INPUT0，0数学**。它不证明9/8不正，也不排不同完整source/tail/operator证书；只说本次未取得能够越过旧head-tail缺口的新实物。Whole4/5仍是负惯性UPPER，principal/sections/mixed、危险core/cross、成长Ξ与三个Goal门保持open；不新建C067/604、来源队列或第二counter，不将困难称external blocked。
