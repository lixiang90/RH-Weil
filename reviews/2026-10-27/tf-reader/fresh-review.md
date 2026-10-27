# 五源 actual t_F 建设性预检：独立 fresh 审查

2026-10-27；审查者 `/root/tf_reader_fresh`。只写本稿，不改STATE／cadence／库，不运行T／Weil数值矩阵，不建合同。已恢复README／STATE、check→show、G20261027、C046已停止状态、D20261027E、宏观前沿及冻结五源准入。

**最终结论：限定 PASS。** 三原稿、实际谱隙证书、root总稿／前件消费记录及固定执行交接均已核；支持建设性预检0轮结算。此结论不是T/E矩阵或Hfin符号的验收，不验收长期Goal完成。

## 1. 实际证书：有限算术确实支付原cosine算子误差

全文核读 `scripts/tf_reader_arch_gap_certificate.py` 与 `arch-gap-certificate.json`，并用脚本的 `certificate(20,160,100)` 作一次独立in-memory重放；生成对象与保存JSON相同。未写第二份证书，未运行T／E或Hfin实验。

原对象是L²(0,1)上核2cos(2πxy)的自伴compression C0。Taylor有限核C_N=EDE*，H=E*E，H_ij=1/(2i+2j+1)。脚本给Cauchy inverse闭式，并逐entry以exact Fraction验证实际21×21的Hinv·H=I；该核对不是浮点逆残差。

Machin π区间由两条交错arctan级数及下一项得到，后续fixed-decimal rounding均向外。系数的奇偶符号与π上下端同步；base aHinv及diag(c_j)逐entry保包含关系。integer interval的乘法／除法下端floor、上端ceil，LDL每步除数区间不含0且所有pivot下端严格正。这给两个实际对称矩阵aHinv±D正定；通过H的congruence，等价于有限核的operator norm<a=999999/1000000。

real-variable cosine Taylor余项给全单位低方形uniform kernel bound δ=2(2π_hi)^42/42!，面积为1，故同时是HS及operator误差。脚本再向外取上界、向下取gap；这将有限核结果运输到真实C0，而非把有限section的残余当全Hilbert结论。实际JSON给

\[
 1-\|C_0\|^2>10^{-6},\qquad
 \|(I-C_0^2)^{-1}\|<10^6.
\]

这是固定physical cutoff1的投影输入，非新经典Weil数值结果。独立重放时脚本LF SHA256为 `c19e04e3e4ad3784add8d4473c98163f7403ed3d7ed16e0da773ac3bc33c174a`，JSON字节SHA256为 `4c3b71637203ff10b38b91ec1b80cff4302371b0d4baceabb1b69e2429264d91`。哈希仅固定所核版本，不替代上述证明。

## 2. 真实P／压缩逆 reader的范围

全文核读 `physical-projection-and-reader.md`。unitary log map、dilation U_t、source A_r的r(log(x/y))/sqrt(xy)核及实际cosine normalization相容；没有额外给physical源乘指数，亦未将cosine Gamma phase抹成裸reflection。

P=H−HFLR0LFH是原532／533对象。C_N的全kernel余项、真实resolvent identity给R0−R_N以及P−P_N的global operator界；R_N在有限polynomial span正交补上为I，其有限rank correction公式正确。P_N本身一般不是projection，原稿对此明确。

fixed八素数的W=B*B、dI≤W≤uI与full compressed inverse全保。Q=P(I−W/c)P及Q_N的误差、power telescoping与完整Neumann谱尾可直接核对；ρ≤β时jβ^(j−1)是有效的上界。先选J、后令e_P足够小，可以让各项趋0；该数学收敛不承诺工程可负担。B P B*、receiver或finite-word对象没有冒充Π。

对有限Hilbert向量的实际action也有可认证closure：有限physical steps的cosine transform有explicit sine kernel，外部1/x尾和近0界可积；logcell先在正compact physical区间按带导数界的L²误差逼近，unitarity将误差运到整个输出半线。cutoff／dilation和finite-rank R_N保持有效L²计算，有限词的误差按已付norm逐步传播。这比仅写抽象逆或报告finite basis残差更强，但尚未替某个实际T表选取mesh／容差／成本。

可选k_s reader亦保持了关键域：全Mellin power不属Hilbert，不能直接代P；低forcing r_s∈L¹，经C0平滑后才用R0。齐次Fourier取消power腿后，一次分部积分给C_s/x尾；W_j常数及C_s的至多线性增长充分。z_s近似差仅经HFL作用于L²向量，未比较两个非Hilbert power。主线HS方案不需要这条pointwise密度路线，不能把两个方案的尾责任互相省略。

## 3. physical HS夹心、全尾及真Hilbert residual

全文核读 `trace-and-certified-tails.md`。BM在x<1为零；FB=B*F，B*的有限负delays把Fourier侧下端降至b=1/9699690。support r⊂[-3/2,3/2]给A_rΠ的下端a=e^(−3/2)。所以D_r=1_[a,∞) A_rF1_[b,∞)满足D_rFΠ=A_rΠ，是实际支撑恒等式。

D_r核K_r(xy)与w(v)=r(−logv)v^(−1/2)的换元、端点flat积分分部、链式法则majorant均正确。变元z=xy确给

\[
 \|D_r\|_{HS}^2=\int_{ab}^{\infty}|K_r(z)|^2\log(z/(ab))\,dz.
\]

原稿完整HS上界及行／列tail公式分别积分低z常数界与高z幂衰减，包含ab附近及全部physical无限尾。log-unitary kernel依赖xi+eta，其global导数界由z≤1和z≥1两段得到；logcell mesh／scalar enclosure误差是实际S2误差。A_r本身没有被错误称为HS。

由Π²=Π，T_ij=Tr(D_i FΠF D_j*)。有限rank的误差用positive contraction FΠF夹在HS两侧，逐entry上界成立；compression误差另乘两finite-rank S2 norm。这使global operator reader误差可以合法进入trace，避免“opnorm小乘非HS A_r便trace小”的错误。

整个Hilbert空间上的Atilde=P W P+(I−P)满足dI≤Atilde≤uI，compression为V*Atilde^−1 V。任意Hilbert trial Z的exact identity

\[
 Q^{\Pi}-J(Z)=(V-\widetilde A Z)^*\widetilde A^{-1}
                    (V-\widetilde A Z)
\]

给PSD余项及d^−1 residual Gram upper。原稿要求真实H残差；有限step逼近、F的近0／远端尾、P与full inverse的global谱尾足以使它有效计算。finite matrix求解残差没有被冒充真H残差。所有Euler returns在真实逆或该residual证书中保留，未用平方自由核替代。

正迹主线不截source Fourier频率：完整source频率都已在compact v积分K_r内。此处“无另一个频尾”只限该physical HS方案；若改走point-density bandreader，就必须另付频尾。

## 4. 五源、完整Q与原norm／坐标

全文核读 `source-norm-and-full-weil-quadrature.md`。χ的complex Cauchy圈及Re reciprocal lower给Gevrey型全导数常数，常系数ODE与指数独立给五源Gram正定，endpoint flat使全部Fourier分部积分无端点项。源support闭区间贴I端点，消费的是560已付zero-extension Dlog域，并未误称严格Cc∞(I)。

actual Γ定义保digamma及contact常数。partial-fraction／trigamma可给所列粗log、一次／二次导数上界；nested Fourier与digamma节点误差、两半frequency中点规则和全频tail均单列。Dlog在0的一阶折点已分区，未误用global C²中点常数。这里的粗常数给明确有限收敛，不承诺现实计算成本。

q<e³的12个primepowers全部列全，proper powers保持Λ(q)=log base prime；双pole先保在定义，再由本五源解析取零，非从目标删除。shift/source/weight节点及rounding误差均进入Q总账，未把完整power预算与Π的Euler returns尾混同。

所有原表采用linear-first：r=Σc_jr_j时值为c^T M barc；若用常规column c*mathsfM c，N／Q／T／E须一并转置。trace稿内部compression的conjugate-first记号与row source coefficients收缩相容。该冻结族的rhat_j实数确使最终四表可实对称认证，但这是精确源对称性，不能作为一般complex表删相位的借口。

Gram conditioning、真正原norm正交core／测试补空间和source coordinate map有单独责任；raw block不自动是正交block。normalizedE扰动界及用明确rational coefficient向量作正Rayleigh反证的有限门均正确，且要求actualT总误差已纳入。

## 5. 当前限定净值／尚未验收内容

535／560的trace域、actual fixed-window Gram存在性、全Weil身份均为旧输入；本轮将冻结对象的有限计算路线及误差输入落实，并有实际精确谱隙证书。三稿尚未输出T/E表、没有Hfin符号、没有全源或成长core／coupling及primitive RR／经典正性结论。不能由文件数、operator证书或收敛公式新增数学轮，也不能把工程未实现写成矩阵已算。

本审查支持在该范围内把建设性预检视为标准／旧设施的0轮实现；最终由root消费与结算。若下一步有实际compression，必须保存所用有限输入、真正H误差及成本；不得再次把同一抽象reader公式循环当进展。Source-adapted或较好trial合法，但固定五源Hfin的有限pass不代RH／whole结果。

## 6. root实际版本及单输入实施交接的最终核验

实际全文核读 `goals/reviews/2026-10-27-five-source-actual-trace-reader-precheck.md`、`root-consumption-scope.json` 与 `execution-handoff.md`。root将固定source／原norm、actual cosine／Π、HS夹心、有限compression与无限Hilbert residual的角色逐项保留，未把局部正确前件合成未算出的T/E表或全源signed结论。

root总稿保留了actualP、global inverse及Euler returns，且明确主线不作source frequency clipping、Q／Dlog频尾另付。m／d／ρ／保守R0成本未伪装成成长uniform bound，也未将这些充分计算费用说成actual signed误差的必要下界。它按535／560已付trace/domain/Gram扣旧，以建设性0轮记录，没有C047／584或新classic／whole／primitive RR成果。

交接的h0=1_[1,2]确为原physical norm1向量，Fh0的sin差/(πx)公式正确，q0=<h0,FΠFh0>∈[0,1]。该单输入是reader实现的必要验收，不替代冻结五源表或改变Hfin／source／F。actual trial z的variational J与真H残差必须实际产生后才能报告q0；交接没有预填成功。

固定验收宽≤1/16的一组充分预算也正确：J半宽≤1/128，residual²/d≤1/32时，未交[0,1]前总宽≤2/128+1/32=3/64<1/16。该误差门须包括V／Az action和inner product的实际enclosure；finite solve residual不能代之。若成本不能支持验收，应保确切费用／日志并停止该冻结计算，不能换h0／L／j／F来躲过。

已现场核root记录的七项实际LF SHA256，全部匹配：

| 原件 | LF SHA256 |
|---|---|
| root总稿 | `2a626554685e4f3a77c5f3483a68a75b16240b207d78f80a45189b771b19ed9f` |
| projection reader | `4798315fb12bc6a04431ce24310803dbbe7d9f831c851365777e5e92dea99300` |
| trace／全尾 | `b68315f3de4f88e71c1225aacc3d9af6236b88d350bba38d116f44c4fffc3ce9` |
| source／完整Weil求积 | `95075b97594c95ee824e979cfb552b2bfe80d9d15b98fd0d41fe179602213265` |
| 精确gap脚本 | `c19e04e3e4ad3784add8d4473c98163f7403ed3d7ed16e0da773ac3bc33c174a` |
| gap JSON | `4c3b71637203ff10b38b91ec1b80cff4302371b0d4baceabb1b69e2429264d91` |
| execution handoff | `6d052677352c310a45bd25589ef10bfd37ff593d82c5981bb834564c5c42d828` |

无剩余必须阻止该精确范围结算的修正项。当前实际执行仍仅是C0证书及独立重放；q0／T／E／Hfin均未运行或认证。哈希只固定所核版本，不代证明。本稿不验收GitHub同步、不修改STATE／cadence／库或长期Goal完成状态。
