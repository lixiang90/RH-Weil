# 实际 Weil 全复源固定窗正性：source-exact 尾补偿证书消费

2026-10-14；C009一完整轮，起始HEAD `3d9bbbf`；比较基线仍为 `3a72930`。
状态：经解析审查和完整重建验收的computer-assisted来源定理及其同对象净后果。
原定理归Vincent Liu，不声称本仓首次证明、世界优先权、外部人类复现或形式化完成。
C008保持止损，不等待其附件；原535 Goal完成收据保留，本次不新建runtime Goal。

## 1. 固定来源与实际执行

原来源是[公开冻结版本](https://github.com/luciferyu666/certified-weil-positivity/releases/tag/v1.0-mcom-submission)，
提交 `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`。
[字节收据](../reviews/2026-10-14/c009-tail/source-receipt.json)记24页原PDF、源包总SHA和292个文件逐一hash/路径核验；
原字节及新大数据保留于本地ignored `tmp/c009-liu`，不推送无整体转载许可的材料。
PDF印刷4页渲染核对。来源是submitted manuscript；不将投稿、发布或历史internal PASS作为证明。

[预注册](../reviews/2026-10-14/c009-tail/preregistration.json)冻结B的半窗17/16、448阶、全部prime powers、
原代码hash及新输出目录，代码先只读审驱动/worker/14个scientific modules，才执行一次FULL_REBUILD。
实际Windows/CPython3.12.5，区别于作者记录的3.12.10；未改原代码或关闭assertions。
运行 `-I -S -B`、jobs2，完整source/oracle/双compiler/每行残差重建约327秒，实际exit0。
没有机械再跑FAST_VERIFY，未执行A的另一路retained verification。

[实际运行收据](../reviews/2026-10-14/c009-tail/run-receipt.json)及[fresh证据目录](../reviews/2026-10-14/c009-tail/fresh-run/verification-summary.json)
绑定新primitive intervals、输入/输出hash、环境与日志。覆盖1024 moments、13 shifts、169 ordered pairs、
151200 source intervals、896 tail coordinates（含448 parity zeros）、100352 target entries、448 Gram rows及56 scalar assertions。
这些counts仅证明覆盖，数学验收另由下面的全源/误差桥与独立检查给出。
原驱动读取历史analytic-admission标签作为执行准入；本仓没有以该标签支付解析前件。

## 2. 真正消费的全源定理与证明链

令I=(−17/16,17/16)，Lebesgue norm，F(z)=∫f(u)e^(−izu)du，h_f(x)=∫f(v+x)overline f(v)dv。
actual Γ=Reψ(1/4+it/2)−logπ=2θ′，完整pole为2Re[F(i/2)overline F(−i/2)]。
实际prime powers为2、3、4、5、7、8，位移log n且Λ(4)=Λ(8)=log2。
odd负pole没有删除，complex源没有预设zero ordinates为real。

本轮可消费的结论是

\[
 Q_W(f)\ge2^{-49162}\|f\|_2^2
 \qquad\text{对所有 }f\in C_c^\infty(I;\mathbb C). \tag{1}
\]

[独立对象/来源审查](../reviews/2026-10-14/c009-tail/object-source-audit.md)与
[不同组织逆审](../reviews/2026-10-14/c009-tail/signed-reverse-audit.md)给逐式依赖和原TeX位置。
主审合并消费门如下：

1. **全Hilbert源尾供给。** Ω=256，B_band为支持窗上的压缩sinc算子。
   4096个间隔节点、Lagrange余项及复源constant-phase读出独立给
   I−B_band≥δI，δ=2^-49158。外部Γ余量≥C=123/1280。
   S=I−B_band−δI≥0，parity及正型complex平方完成给
   T_tail≥δ/16·I+U，U=81|Sv₀><Sv₀|+27|Sv₁><Sv₁|≥0。
   这保留真正非有限秩tail供给；不是把整个tail替换成rank-two后声称等价。
2. **实际signed prime比较。** M=7/2 I−Σ c_n J_logn的全算子weighted-Schur界
   mI≤M≤bI，m=9617/10400、b=63183/10400，七个cell及8独立精确重算。
   K保留双pole和Γ低频，Q≥τI+M+K+U，τ=δ/16。
3. **全补空间与误差。** projection cross为O(r)，负complement及norm费用分为O(r²)，
   r=2^-95、pole费p=2^-440。M正性先支付，所以block inverse无循环。
   A=E*ME、B=E*M²E，B不是A²；全13 shifts的169三重support交集及边界项均保留。
   非交换Block–Schur通过αI+β(B−A²)支付全complement，非仅finite head PSD。
4. **source→中心→sign。** Binet余项、moments、全kernel Taylor、expanded Legendre seeds/recurrence、
   primitive shift/weight费、Γ-normalization及tail columns逐项给原(11)/(22)operator allowances。
   新trial的精确Frobenius界给||X||≤8，逆上界W≥G先于目标sign；所有congruence正且可逆。
   两条新source→整数路线整个对象相等后，所有残差行给最终sign，才经解析桥推出M+K+U≥0及(1)。

primitive费用不是仅code字段：ε=2^-2048，真实/中心shift与weight误差≤ε，Σ|w_a|<10。
最终i,j≤447有D=447·448/2=100128。共同support内product变化积分≤4Dε，
端点丢失≤2ε；full weighted-pair shift费≤40051400ε。
weight product总差<241ε、overlap<3，另费<723ε。
总raw entry费<40052123ε<2^-2022，严格小于原2^-2021 padding。
expanded895阶仅计算中心矩阵并由directed intervals支付，真实primitive误差可直接在最终448阶比较；
不能把expanded最高阶的导数费误套入这里，也不能只看矩阵小数误差。
raw row/Γ界把完整费转成原norm的εA=εB=2^-220，kernel另有2^-204、tail另有9·2^-512。

## 3. 独立精确有限门及反例审查

主代理另写[完整整数Gram检查](../scripts/c009_verify_gram.py)，只读取新target/factor数据，不导入作者模块或PASS标签。
[独立结果](../reviews/2026-10-14/c009-tail/independent-gram-result.json)重核两个224阶完整矩阵的所有残差单元/行：

\[
 K_s=2^{2329}F_sF_s^*+2^{2873}I+R_s,
 \quad\max_i\sum_j|(R_s)_{ij}|<2^{2848},
 \quad K_s\succ2^{2872}I.
\]

错误符号对角的负对照由同一全行检验拒绝。
逆审又核正congruence、清分母常数、trial norm及该新脚本；结合§2全源桥消费，
没有把两个finite PD本身当连续定理。
非finite数值的最低费用反例也已核：对文中特定tail-dropping localization，
log8两窄bump及合法高频modulation给辅助Dχ的归一化极限
1/16−log2/(2√2)<−1/8，fixed compact修复仍失败。
该负方向反的是Dχ，Q=Dχ+Sχ保留非负Sχ；不反驳(1)，不声称完整Q负值。
这是已知外部指定方法边界的核验，不重复登记本仓535宏观完成。

## 4. 同对象净后果、未付输入及下一动作

自然域D_log,I={f∈L²(I):∫log(2+|t|)|F(t)|²dt<∞}。
缩支撑f_ρ及保持严格支持的mollifier给form-norm core：先weighted dilation强连续，再multiplier dominated convergence。
Γ加常数的closed positive form与bounded prime/pole扰动故允许把(1)延到整个D_log,I；域外Q=+∞。
沿536的同norm compact-resolvent接口，实际窗算子的底≥τ；不推simple、even或第二谱隙。

Q取决于autocorrelation，平移保norm及完整pole，故(1)对任何长≤17/8的平移窗口亦成立。
源域嵌入给每个半窗0<L≤17/16同一τ下界，prime项以实际相关为零自动缩减。
原C007两patchV落在这个窗内，取得真实actualQW正下界；它不推QW≥T₂或E₂≤0，不矛盾535。
C001μ13半窗log13/2≈1.282>17/16，原12样本仍只是experiment。
Theorem A的2^-151强常数未重放，不消费；(1)不靠A数字或C008未取得的证书。

相对基线，本仓新增可消费的不同算术来源是含prime8的完整complex固定窗正性，
并有真实primitive/error/全补空间/整数门；不是新RH等价、finite诊断或外部摘要。
独立来源→同一实际对象→固定窗forcing这条箭头已改善。
成长支持、真正最低态排序及与prolate/Ξ相认仍未付，未证明RH，也不将本合同/推送当新宏观完成。
C009一轮完成B准入，不扩大N/拟合零点；C008继续止损。四轮宏观复盘按同一cadence进行，不另计数学轮。
唯一下一动作：以该已验收同norm来源为基准，先审Q−sI的全源inertia/min–max消费，
判断它能否独立分离真正odd底与第二even底；若只会重述coercivity，则另选signed来源，不扩有限样本。
无pending process。原字节、新大数据及可重放hash清单保留本地；本仓保存实际审查和收据。
