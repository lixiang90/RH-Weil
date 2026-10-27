# Action-cone 独立逆审：实际代数边界、普通迹与强旧去重

2026-10-28；`/root/unit_fresh` 独占审稿。本次重新恢复 README/STATE、check 后 show、当前 Goal、宏观入口、已耗用 C047、D20261028D 和唯一 action-cone 准入；不续 unitary 章节，不执行下一候选，不改 STATE/cadence/Git。两稿终版实际全文核读后给出下列限定意见，出稿不代 root 消费。

**结论：两稿的实际代数证明与充分费用可通过；统一建议按标准强旧合成记 0 数学轮。** 这不是因为没有 RH 后果，而是全源 HH₀ 消失及 exact cone boundary 已由已付稳定角、实际有界提升和通用有限交换子恒等式直接蕴含。不能把“旧稿未打印此有限链”当作超越最强旧资产的证据。准确的 exact 结论仍须保存；不能退回只说 Ω=0 或 norm-closed ideal 吞源。

## 1. 版本、对象及域扩大

本审绑定实际读取的两个终稿（CRLF→LF 后 SHA-256）：

| 原件 | 实际字节 | LF SHA-256 |
|---|---:|---|
| [inner-homotopy-and-regulator.md](inner-homotopy-and-regulator.md) | 9531 | `80c027ddf11bbabb61ec746610d7af2df4693d9eed072eb3abdbfb7cbf0d5b61` |
| [actual-hh0-source-class.md](actual-hh0-source-class.md) | 14398 | `9f899d9904476f6925c96bcc5b440d41e2066092b732666d0d5ae93c7ad4e5c4` |

准确对象是

\[
 A_c=C^*(A_{\rm src})\subset B(\mathcal H),\quad
 I_c=A_c\cap\mathcal S_1,\quad Q=A_c/I_c.
\]

430 把全部 S₁ 纳入 A_src，故本域包含全部 K，且此处 I_c=S₁。Q 仍按 S₁ 取代数商；辅助的 A_c/K 只用于检出紧误差。两商不能交换，K/S₁ 的误差不能免费删去。链是未完成代数 tensor；有限交换子的实际恒等式才给 HH₀ 边界。范数极限仅用于在 C* 完成域构造合法链腿，不用于把 commutator span 偷换成 norm closure。

这份扩大域与较小 A_src、原始最小源代数、其有限传播/光滑链域均分开。全 L¹ 源 F_r=VU(r(−·))V* 入 A_c 是573已付的 operator-norm 延拓，不向小域回搬。

## 2. 高阶同伦、Connes-B 及锥边界符号

对 v=q(u)、α=Ad_v，在所有链腿同时施 α。稿中的

\[
 H_n=\sum_{j=0}^n(-1)^j
 (a_0v^{-1},\alpha a_1,\ldots,\alpha a_j,v,a_{j+1},\ldots,a_n)
\]

确有 bH+Hb=1−α。独立核了 n=0、1、2 的端项与内部相消；一般 face 的配对保留首端原链和末端负 α 链。特别末 cyclic face 的号是 −，不能改用只有 bar 内部 face 的证明。

对 d(x,y)=(bx−Dy,−by)，Φ_H(x,y)=(x−Hy,y) 的目标微分为 (b,−b)。weighted c=(v⁻¹,vf) 满足

\[
 c-H_0f=(1,f)-b_2(v^{-1},v,f).
\]

采用 signed cyclic τ、首插 unit 的 s 后，B=(1−τ)sN 给 B₀(a)=(1,a)+(a,1)，是 **plus**；(a,1)=b₂(a,1,1) 仅作为明确边界消去。bB+Bb=0，故 source 在 H 分裂下为 (B[f],[f])。

S₀(a)=(v⁻¹,v,a)+(a,1,1)、其余 S_n=0，使 K=H+B−bS+Sb 满足 bK+Kb=D，且 K₀(a)=(v⁻¹,va)。于是 K 分裂下为 (0,[f])。两者是合法 shear，不是两份独立 primitive 标签。

若有限一链 y 满足 by=f，令

\[
 Z=-\sum_i\{(1,a_i,b_i)-(1,b_i,a_i)\}-(v^{-1},v,f).
\]

直接有 bZ=c−H₀f。再用 bH₁y+H₀by=Dy，核得

\[
 d_2(Z-H_1y,-y)=(c,f).
\]

两腿负号与 H₁ 的负号均正确。只给 norm-closed span 不足以使用此式；下一节确实给了有限 y，所以合并后可去掉此条件。

## 3. 稳定角和紧误差的有限交换子证书

独立核了树构造的两个容易失效处。

第一，T≥0 时根嵌入 W 只作固定有界辅助算子。√T W*、W√T 已为紧腿；树 shift 每个 level 的块带 2^{−(n+1)/2}，截断有限块紧，尾 norm 一致趋零。因而 A₀(T)、A₁(T) 在 C(X,K) 中，对 X=S¹ 还支付了一致 norm 连续性。裸 W 或未衰减 shift 没有被塞进 A_c。

第二，根的 outgoing 和为 T，每个非根的 incoming/outgoing 均为 2^{−n}T。故两 self-commutator 和确为 WTW*；加 [√T W*,W√T]=T−WTW* 得三个实际 commutator。正部四分解给任意 B 至多12项，product-norm 和≤8||B||。这不是把某个无限和称作有限 boundary。乘积不必迹类，因此不能逐项施普通迹来制造反证。

431 已付单角 B₀≅C(S¹)⊗K 和 ρ=π_Kρhat 的等距 *-同态，其中 ρhat(B)=½VBV* 是实际 contractive 线性提升。对 B=U(r(−·))，先在 B₀ 用上述12项，再经 ρhat 提升，乘法误差 E∈K。稿中没有把 E 冒称 S₁：另用单点版12项，在 K⊂A_c 内把 E 精确消去。

所以 F_r 在 A_c 内已是至多24个 commutator 的和；并非只在 Q 中、也非只在 A_c/K 中成立。其有限链 y 沿 q⊗q 给 by=f_r，进而全部 J_r 在当前未完成 action-cone 内为实际代数边界。

费用也闭合：首12项≤16||B||，||E||≤2||B||+4·8||B||=34||B||，紧误差项≤272||B||，总≤288||B||≤288||r||₁。上述锥 primitive 的代表费用≤5||y||+||F_r||，故可用粗界1442||r||₁。均是构造上界，非最优值或必要费；正部/开方的选择非线性，不声称线性有界 source contracting homotopy。

## 4. 普通迹延拓、旧 −4 与实际 physical pullback

对锥一循环 (x,y)，

\[
 \widehat\Omega(x,y)
 =\operatorname{Tr}\!\left(\sum_i[A_i,B_i]-Y+uYu^*\right)
\]

只对括号**整个迹类算子**取迹。换提升产生 bounded/S₁ commutator 或 −R+uRu*，迹为零；代数 tensor 的核也由含 S₁ 腿的有限 tensor 生成。对 d(X₂,Y₁)，以 W=b₁(Y₁) 的实际提升计算，括号严格为 −(W−uWu*)+W−uWu*=0，不需要 W 本身迹类。因此这个 regulator 确实降到 H₁(M)。

旧 ζ=q(T)⊗q(T*) 有有限秩 [T,T*]、Tr=−4，故 (ζ,0) 仍非零。它不是 J_r。对 J_r 的固定提升，括号严格为 [u*,uF_r]−F_r+uF_ru*=0。这一 physical 全零不依赖 HH₀ 计算；HH₀ 证书进一步把 J_r 判为 exact boundary。没有把旧 −4 消失误报为本轮结果，也没有加自由 HH₀ functional 补一个算术值。

## 5. 全 source、关系与原费用的消费范围

L¹ 覆盖全部 complex S_exp，故包含405全部真实 noncompact C(P_an⊗C)，不是 compact crop。回核405§2、§4–6：P=C(D²+D)h 的两个矩为零、M_p(2)=π/6，源非零；h 及两个独立 degree 方向也在相同域。它们的 f_r 作为 Q 元素均非零：431 的 essential norm 给 ||F_r||ess=2||U(r(−·))||，非零 L¹ 源由 Fourier 单射不会变成紧算子。消失的是其 HH₀／此 J 类。

537 的全 complex fixed 窗结论 Q_W(r)≥2^{−49162}||r||du²>0 已是旧输入。现在所有这些非根也被同一个 HH₀ map 和 J map 杀掉，所以本 recipe 不能只凭它们的类给 primitive 全源运输。不是只测试一个数值 sample，也不把 compact 非根叫 Pan。

保原 r(u)=e^{u/2}f(u)、Lebesgue du 及 zero-extension Dlog。固定窗的 L¹≤√(2L)du、Dlog≥√log2·du；强 p_(N,0) 给 L¹≤2p/N。故费用可依这些已付界运输，但不是全线 du/Dlog 统一界，不给 trace-norm 费或 Ω 的 operator-projective 连续性。任何粗上费都未被倒置为必要费用。完整 Γ/contact、全部 proper powers、双 pole、mixed complex 经典 Weil 身份没有由此被计算或省去。

## 6. 强旧去重与计轮意见

必须区分两个判断。573 的“闭 ideal 吞全源”和本次“全源在有限 commutator span 中”字面上不同，后者更强；不能直接拿前者替代后者的证明。另一方面，AGENTS 要扣的是**已付资产可立即蕴含的最强后果**，不只是旧原件已打印的命题列表。

这里有一条不依赖新 physical 参数、算术估计或 source-specific 消去的通用链：

1. 稳定 C(X,K) 的上述有限 commutator 恒等式适用于每个元素；单点版同样使 K 为 algebraically perfect。
2. 431 已提供实际 B₀ 稳定角、contractive section 及精确 mod-K homomorphism；430 已付 K⊂A_c。
3. 因而**任一**由 B₀ 提升的元素，先提升有限分解，再在 K 消有限误差，自动落入 [A_c,A_c]。这是一般扩张的直接有限 lift 论证，不使用 405、537 的特殊公式。
4. 573 的 L¹ 延拓正把当前所有 raw 源放入这一已有单角。全 Pan、双 degree、537 控制都立即随全 L¹ 量词成立。标准 inner-action shear 再把这一 HH₀ 零证书直接送成 J 边界。

所以准确的新显式证书应记录，但它属于**标准强旧合成0轮**；24/288/1442 是通用构造的粗常数，未给超过上述链的必要费、原 norm 严格改善或 source-specific 新定理。HH₀ 稿§6“原件未给有限链／比闭 ideal 强”的两点都正确，但不足单独证明应计1轮；应在 root 结算明确补上本段强旧比较。若将来证明小域仍有 exact 证书、必要费用或另一不由稳定角引理覆盖的 source/relative 信息，须按实际完整数学重新计，不能套本次0。

停止本 canonical A_c/S₁ inner-action recipe；不继续调树、shift、commutator 常数、ideal 或添自由 functional。此结论不排较小 A_src、不同非标量边、其它 relative pair、独立强拓扑/有费无限修复及 signed/D′ 输入。经典主瓶颈、whole leading4/5 负惯性 UPPER、actual core/coupling/Ξ 和 Goal 完成门均未改。

## 7. 实际阅读及交接

本次数学读入：430、431、432、573 全文（573§8–10另逐段重读）；405 的径向源、Gaussian／P_an／双 degree 部分；537 现有全源定理及同对象域后果；唯一准入稿全文；workflow计轮条款及现有标准直接合成结算作一致性比较。两个待审终稿全文实际读取并核终版 SHA。未下载新来源、未查下一 paper、未把代理推测当外部定理。恢复输出的历史长入口有工具截断，当前责任由 STATE/show、Goal、最新决策、唯一准入与必要原件单独定位；不据此声称历史长入口每行均已阅读。

无本代理后台进程或待运行证明。仅交回本审稿：root 可按上述终版合并实际 finite boundary 与费用，明确采用标准0的去重理由；本稿不代更新 cadence、建合同/585 或完成长期 Goal。
