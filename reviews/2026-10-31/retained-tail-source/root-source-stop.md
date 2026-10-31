# Retained-tail 源门：生产完成，独立核验失败，未消费

2026-10-31；同 G20261027 / runtime1793085111、原冻结0c4f。Root全文读 representation10736、design10986、fresh12636、producer34788、checker35948、checker-review8555、conditional-exit12051，以及旧595全局解析运输的对应误差和域记录。冻结见 preregistration.md 与两个独立 freeze；没有使用旧C058/C066预算，没有C067/604。

## 实际完成和止点

一次生产进程32245正常退出，140.544秒：生成2047个完整旧h多项式系数、458528个新V有限系数及448列范数记录。原E448 / eta1 / L9/8 / Omega256不变；多项式到2046阶，端点对数的无限尾按精确公式保留。74MB左右的源数据保存在ignored本地库；公开代码、公式、哈希和审查。

一次独立重放69254在383.651秒后退出1，准确原因为 `INDEPENDENT_CONTAINMENT: h:0:1660`。重放使用闭式阶乘积分而非生产器的边界权递推。它在完整sinc seeds后、h0的第1660阶处停止，尚未核完h1或新V/G矩阵。不得把生产器成功、若干先前坐标或预先的代码审查当作完整源证书。

失败坐标的存储区间为[0,1]/2^640。失败日志没有保存独立区间的具体端点。只读公式范围估计条件性地把失败定位到零下端，但不证明实际系数符号或生产源正确。限定只读诊断另见 failure-analysis.md；禁止重新生成seed/列、重跑检查器、改精度、扩区间、换参数或将新数据标PASS。literal区间不包含另一包围区间本身不等于真实系数错误，也不等于候选Weil型负；实际验收失败是真实停止事实。

## 前件闭合与冻结范围

对象始终是原 H=L²((-9/8,9/8),du;C)、Fourier receiver dt/(2π)，物理 r=e^(u/2)bare；native E:C448→H。R=T_tail−tau I−U_old，V=RE，G_R=E*V；不是V*V或旧inverse-M Gram。R正性、operator domain、tinyfloor及标准shorting早付，不是本轮结果。

新的Gamma实空间表示、完整contact、端点log项和q degree576的全空间误差推导经两组织核过；旧全局band/sinc身份及原norm费用仍是输入。失败没有改变这些解析身份，也没有回滚旧595已验收的448维source、全Dlog桥、所有pp/双pole、无限秩正尾及cross/complement设施。第1660阶的新扩展核验不在旧448坐标验收范围内。

本次新源的条件性目标 ||V−Vhat||op<2^-203、HS<2^-198、||G_R−Ghat||op<2^-203，依赖完整实际重放及root消费。该前件失败，故三个目标及新补空间范数均仍不可消费。生产器显示的补空间HS约1.77仅是未验收观测，不能当旧tiny projection费，也不能当负谱证据。

signed head、(G_R+I)逆、retained shorting的数值误差和whole Schur完全未执行。conditional-exit中的精确正相关Schur身份仅标准条件设计：whole责任还需要新 mixed E*M V、完整V*V/补空间Gram或实际whole inverse。旧B−A_M²不能省；旧针对多项式的shift费用不自动适用于有端点log的MV。有限head PSD不闭合wholeQ，失败的充分lower也不排Q本身。

## 净后果和下一门

本次取得了可复核的生产记录及一次具体核验失败，尚无可用新V/G源证书、whole9/8正性、关键core/coupling改善或数学定理。统一0数学；原cadence1/history67/latest603/formal21、Goal9679和库143/manifest223850保持。新局部执行瓶颈是验收关系；长期principal/sections/mixed、signed core/cross、成长Xi与whole leading4/5负惯性UPPER不变，三个Goal门open，同运行Goal active。

当前冻结的生产/重放预算已耗尽。允许的后继须先以本次具体失败和原norm目标写出新的可判准入：只做一次proof-only比较，判断“独立包围区间嵌套”与“到既有存储中心的全列norm误差”之间是否存在严格可验证的信息差。它不得重算源、改参数、改旧证书或把条件设计算已开工；若不能在同一原误差目标下给完整h/V/G及无限尾的责任和止点，就停止，不续验证器/来源队列。新的数值核验仍须另行具体准入，不能借本轮失败预算自动重跑。

Goal没有因源门停止、保存或发布而完成。公开同步回执只验收本轮准确范围及Git版本。
