# 路线状态独立只读审计（2026-10-11）

发布说明：以下为独立子任务原始记录，涉及tmp路径和开始审计时的基线。当前研究状态见[504](../../notes/504-low-frame-strengthening-and-mixed-sixth-restoration.md)；旧c403形式化与新c4119数学证书分别记录，本文未执行新增Lean验证。

本稿只写入 ignored tmp；不修改工作树主文档、目标或 Git，不运行 Lean。主状态依据当前 README、RESEARCH_BRANCHES 的最新队列（35–57行）、503及实际形式化声明；旧 notes 保留其发表时状态。这里的“已证明”须进一步区分引用输入、有限数学证明与实际内核收据。

## 版本与验收边界

| 仓库 | 读取 HEAD | 当前证据 |
|---|---|---|
| RH-Weil | 2d2eb99b82f944b23437cd88797cdfd178021fb0 | 开始审计时 clean；审计后 root 新增 range-eight、论文及 review 未跟踪文件，不据此改变已发表数学状态 |
| RH-Zero-Proportion-Formalization | c705c4aad2ad33e5358ce17e906b0dc51b1a83fe | 当时 clean；最终收据18份源码 SHA 与现存源逐一相等；六个最终根普通模块证明与 fresh axioms，独立 Nano 82804 declarations；仅 propext/Classical.choice/Quot.sound |
| RH-Zero-Free-Formalization | ebf33a7da37784960c8bf758d4f901a9e16c1322 | 当时 clean；核心收据23份源码 SHA 与现存源逐一相等；224个公开根、独立 Nano 58126 declarations；核心真实 ζ 非零定理仍取 ArithmeticProbeObligation |

比例收据：verification/ninth-span-complete-formal-kernel.json SHA1ddac667b772ecc34aef3b49eda3ffb308ab7a366529cfa2d4d3bef5e3e760ce；independent receipt SHA74f23aa01c5b2e7122f009e8efba8d1364a1e2698f1a392792b4ff51600e88a8。无零区核心收据 SHA120c52b9ffbaacddc7b6f49efe5a6f3e6c22f25c6595894f23bd55a8dc9ef866；independent receipt SHA14337695daf10f31304d212fd97e0fa48c4bbe3092911ecdf05beb3fbbb430d9。这里核的是当前源码绑定与既有真实日志/收据范围，未重新执行 Lean/Nano。模块/独立内核验收没有自动满足网站 single-file/compiler/resource/comparator 门槛；收据的 whole_submission_compiled、submitted 等 false 不可改写为网站已接受。

## 五条路线

| 路线 | 已付款/实际变化 | 仍未付的关键输入与当前结论 | 下一可执行命题；优先度 |
|---|---|---|---|
| Weil / 算术 F1 几何 | source-relative sheaf/divisor/degree/intersection 条件推导、具体源 smoothing algebra/trace 类、有限 boundary 与 physical phase 障碍有独立证明；formal 存在性桥确为带前件的 implication | `formal/F1/Geometry/Existence.lean:66` 的 rh_of_existence 要 SquareModel、DegreeDescent、EffectiveRigidity、SectionExistence，还经经典 Weil bridge；`GeometricRealization.lean:112` 要实际 SourceRealization、GeometricSections、rigidity 与 GeometricRR。没有算术 square 实例和 RR 全局截面见证；blueprint 尚有10个 classical_sorry/admission。全 RH、principal radical 的实际几何来源、两次数和 RR 未闭合 | 若投入该线，直接选择 A(h)uA(k) 的真实任意传播 full-ball trace/phase 到闭 HH1 arithmetic comparison，或给实际 admissible global section；不再把 model/reference 双射或 GNS 当正性存在。长期保留，短周期减量 |
| partial-Weil 二/四阶与算术四高素数 | 有限 rank–trace–inertia 与全零点带重数计数桥；固定 centered fourth 的消费已有严格前件。原 actual scalar 子族/误差、完整低标签 mixed、高产品 shared-factor O(X^.5 log^C)、coprime tube 正付款是真的输入缩小 | 197 的 16/21、37/42 仍需同一实际配置 m0,m1→1、E0,E1=o(N)、中心 b2,b4、b2<1/正分母/σ分支。canonical whole增长 B_I(σ*)≈.714198002953028 不是中心常数。四高素数 core 全 q,s,p,r>X^.9 和真实 ν/n外twist 的 tube外 `[Cout]_+` 未付 | 直接证明同一真实系数/mask 下 `[Cout]_+≪X^(1+2B*−η)`，η>0；顶端指数需严格低于约2.428396005906056。或证明同一 actual partial configuration 的中心 B4<2765365/8469189（flat v=1/3，只是指定配置消费门槛）。保持一条主算术线，拒绝 free coefficients 大筛或 signed subset 代替完整合同 |
| AM simple-critical 比例 | 现行已发表实际下界941021/1397107≈67.3549699486%；NinthSpan.lean:44,53 的 simple dyadic/cumulative 正是 actual Zeta23.N0simple 与 Ncount；distinct 是其包含推论。完整局部几何/capture/真实点与对偶已被模块化内核证明，无 numerical/analytic 剩余前提 | 网站未接受，不把本地 four-thread Nano 702.610秒解释成官方串行资源验收。503“还未Lean”是保留原研究时刻，已由 formal repo/addendum supersede。普通7/8宽条带不提供统一离线深度，不能自动增强负谱/Schur平均 | 当前新 c4119 候选只改单帧低域：10个patch+231旧YA；明确保留旧全连续 capture/PTF/REG 与全零点计数链。独立精确检查通过但新 reward 尚未 Lean/Nano。再优化须有真正全连续强捕获/合法 high-transition 或新range，不追逐固定 relaxed H↔low 模型的循环。该线成果明确，可控比例推进优先 |
| Hecke 原7/8及改进 strict σ* | 原固定Q(√−3)有限阶 Hecke whole7/8是引用输入 [R]；445/450/451完整原对象反馈费用与指定 cubic root 推 strict σ*=.874957019420098946…，严格boundary/pole例外保留。新 formal 库实际完成代数连续证书、ordered-height/真实ζ inverse Mellin 身份；另有实际 slots/Euler/marked/FirstTail arithmetic 条件链 | 不把原整篇外部证明称项目独立形式化。`ZeroFree/ZetaSignal.lean:114–126` 的 actual nonzero theorem 明取 ArithmeticProbeObligation（实际 ProbeData 存在性）。HighData/四字段Moments/source-wide unmarked容量、改进 detector count、variable reflected low/raw high、全Hecke实例未闭合；当前 formal σ 不是无条件新 strip | 优先一个共同 presentation、同 height/slots/masks/normalizer 的 long-inverse × short-plain × selected Qi mixed moment/容量合同；若保持原low费用，σ=.87495 要 χ>3.7952664e−5 的严格真实count saving。或明确构造 whole physical ProbeData 以消除实际 theorem 唯一算术存在前提。避免重新调已在所用三仿射约束内最优的 b/κ |
| 换数域 | 457准确识别−3的 cubic/sextic反射把残余角色降quadratic；Gaussian实际目标/Euler/sign-normalized有限probe与458全actual rows（包括powerful、ramification、units）费用已付 | 换判别式/单位只改常数，不能保留−3特有cubic theta又换虚二次域。Q(i)全行界 U+(UD)^(2/3)+D U^(1/3)，仅U≥D²给近linear raw；需要的任意c>0、U≥D^(1+c)合同未付。order4收益是带ideal raw/完整reflection的条件论证，未给新σ | 仅当能给完整目标completed theta reflection/真实un-slotted raw界，或slots能把U≥D^(1+c)全部域付掉再恢复。否则降优先，不重复连续u平均/普通quartic大筛同一正幂损失 |

重要定位：RESEARCH_BRANCHES.md:35–57是最新队列；:71–76是 tube 未付核心；:124–136是497完整mixed/原core；:293是whole B*；:525–538是换域合同；:660–683是F1实际源几何下一输入。197:3、451:1、457:1、458:1的范围均保留引用/条件标记。goals/NEXT.20260909.md 与 PROGRESS 顶部旧日期不是503后live目标替代品。

## 复盘与预算

cadence `rounds_since_review=2`，最新数学轮为503，默认6/最早4/最晚8；前一形式化完成是真实 proof progress，但按当前协议不计数学round。尚未因本次并行子任务/脚本数自动加轮；root应在整体数学iteration交付时计一次。完整目标保持，局部 AM 新候选或任一 formal leaf PASS 都不是 RH/新σ/中心四矩完成。

## 本次范围八与新低帧复算

- `scripts/am_range_eight_periodic_ceiling_certificate.py` SHAa4699ea07356812abed1a37d0d7105572e1c0346b79b73634074739048151ce0：全文读脚本/JSON/原语及499周期证明；独立Fraction、readonly --check实际0。方法域为同AM核、固定非负pair权、span≤8、每span总容量≤2、有界telescoping storage。周期是无限实线gap链的测试输入，非circle最短距离，也不声称真实ζ周期。
- `c≤B g_i+E_i`，`u_i=1−E_i`；t=1/(1−c)>0,z=B/(1−c)。两个正λ满足 λ·u=Ahi、λ·g=1，因此 Ahi t−z≤Σλ；实际 A<Ahi 得严格输出上限331856527056851000/492670815881465791<.673586737。固定F9压力/权的period2另给668124911000/991901956623。仅是指定方法上限；不是actualζ比例上限或新lower。
- 新 `low_frame_complete_point_certificate.py` SHA42624843bf634f53e866835d9b09316e2dffab97c49190eb05ac18a46e3d5925 / JSON8ea2d95aa68c813a65bf1012c2b1ad3d53645218efdb42de5350b9914b3a32f2：没有import作者checker，独立重建全部10个33列矩阵/35新增行/287正对偶与非零residual收费；32原PTL点pack/n对原source逐个匹配，REG内含anchor及整span区间，故tcheckPZ越界分支不消费。反射是完整权与fee恒等。F8≥805021/1e8；high-low安全平均805412/1e8，c4119余量1e−9；既有完整low-low公开minimum仍严格>c4119。新比例668124910/991945881≈67.35497599188075%，没有新Lean/Nano/网站验收。
- 复算源/报告：`tmp/research-resume-20261011/audit/independent_fraction_audit.py` 与 `independent-fraction-audit.json`；本次只新写audit scratch。新最低常数来自原low-low而非浮点LP，单帧231旧YA中的label71成为最低；critical131/148新增13/18行分别全域验证。
