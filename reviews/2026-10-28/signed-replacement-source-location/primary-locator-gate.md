# Watkins v0.5 §3.4：实际 locator 的限定资格核账

2026-10-28；G20261027/runtime1793085111/原0c4f。当前任务只消费 root 已实际取得的唯一原页，不 web、不加 query、不下载或续章，不开启证明合同或计数学轮。恢复 README/STATE、check→show、Goal/C049、D20261028V、当前 summary/宏观前沿后，读取本地 HTML metadata 及§3.4，并与旧561§3–4完整范围核对。

## 1. 来源身份与实际阅读

本地原件为 `literature/local/2026-10-28/watkins-prime-evolution-v05.html`。实际复核125665 bytes，raw SHA-256 `d12ce1df08409809a44bd14275dfb46e09f7cd6ca2791fc00467762ac8d4d6a3`，与本任务给定身份一致。页面 title 是 *Prime evolution revisited: arithmetic equilibrium, Beurling flows and zeta thermodynamics*；metadata/byline 自述2026年 Watkins、Sol/ChatGPT 与 Claude Fable 合作，version0.5、August2026。这里记录的是页内自述，不把模型标签、后续邀请或合作叙述当本项目授权、证明背书或外部发表状态。

本门实际消费 raw329–368的§3.4(a) staged chain、M_a反测及(b)问题状态；metadata主要为raw157、163、169–171。未审所引 Hamburger、Lev–Olevskii 等外部原文，未消费其后来源链、后章或附录。当前只判断这个已给 locator 是否提供所需 signed 替换实物，不对整篇作真假总判。

## 2. 所给 M_a 恰是561已经支付的同一个例子

原页给出的加法测度，记 Δ_a=Σ_{n∈Z}δ_(an)，为

\[
 M_a=\frac{a}{a+1}\Delta_a+\frac1{a+1}\Delta_{1/a}.
\]

旧 [561§3](../../../notes/561-beurling-positive-measures-self-duality-and-integer-recovery.md) 已明确列出

\[
 \frac{\Delta_d+d^{-1}\Delta_{1/d}}{1+d^{-1}}.
\]

取 d=a 并乘分母就是同一测度，不是仅有相似正性或不同归一化。旧件同时记录了 Fourier 自对偶、0点质量1，以及 d≠1时单位窗内仍有非零支撑。本次新页面再次出现该例子，不带来本项目此前链外的新输入。

对任意 a≠1，min(a,1/a)<1，其相应 reciprocal lattice 在正区间(0,1)有严格正质量。它直接违反标准 Beurling integer 的最小单位空隙：单位是1，其他生成元及其乘积均>1，故加性偶对称计数 μ 应满足 μ|_(−1,1)=δ0。Fractional weights 是另一项不合计数重数的现象；**单位 gap 失败已足够**，不必先讨论 free generation 或无限重排。

因此 M_a 不是一个尚待核 Euler 正性的实际合法 Beurling 整数源，也不是同一精确 Γ 下的新 signed 替换。正的 Fourier 自对偶加法 μ，不自动是乘法对数侧正 Euler-log Π；Π≥0 更不能免费升级成 positive primitive 的全 repeats。本页本身也承认 M_a 不属于所欲的 Beurling integer 类。

## 3. 后半 analytic chain 的最强旧比较

561§3已有：偶正 tempered μ、固定 Fourier 自对偶及单位 gap，便迫 μ=Σ_Zδ_n。不要求额外 uniform discreteness、乘法闭包或整数重数作为前提；整数支撑与质量由正性、sinc²零集及周期性推出。

同节固定 Gaussian 版本也已完整支付：若全部 t>0 有固定尺度、固定质量的无缺陷 theta 身份，偶 tempered distribution 的 Gaussian 求导给全偶 Hermite span，进而给 Fourier 自对偶。原页 v0.5 的 Gaussian totality 段在本项目不是新后果。

所以，只要真正把一个标准 Beurling integer 正计数运输到上述精确 theta/Fourier 条件，原单位 gap 已由对象给出，561即完成整数识别。对这个明确域，不需要再把“finite lattice cosets 的 multiplicative rigidity”留成另一个本项目未知量。M_a的gap失败不能反测该旧定理。

这只是恢复本项目已付的强范围，不声称外部文献首创，也不由此宣称一般 FE 已足以进入该域。561§4仍明确区分：整数识别与完整乘法 Weil 正型是两条箭头；即使识别出经典 ζ，RH的独立正性能量仍未支付。

## 4. 第一 FE→theta 桥仍须携原 pole／质量／增长责任

原页 first step 对 Γ(s/2)ζ_P 的 meromorphic FE、pole位置0/1和 vertical-strip finite order 作条件叙述。当前 locator 没有构造一个新的 signed Beurling 系统并逐项核实这些条件；也未把所需 pole阶、留数与 μ 的0点质量完整带入它所写的无缺陷 theta 身份。

一个精确、仅用旧件的字面反测是：取旧561允许参数 c=3/16及

\[
 F_c(s)=1+\frac{c}{s(s-1)},\qquad Z_B=\zeta F_c.
\]

旧561已付 F_c 的正 primitive／全部 repeats、正整数测度和 FE。与普通整数相乘时 primitive相加、整数测度卷积仍正；原 Γ 不改，Λ_B=π^(−s/2)Γ(s/2)Z_B 仍有同一 FE、有限strip阶，pole位置也仍**只有0和1**，但两处变成double poles。移线留数因此有 log(t) 缺陷，不能直接得到页面所写的 unit-mass 无缺陷 theta 身份。若硬用该 theta 身份，旧561结合此正计数的unit gap便迫 Z_B=ζ，与 F_c≠1冲突。

准确地，Λ_B=Λ_ζF_c在0、1均有double poles；Ξ_B=[s(s−1)/2]Λ_B=ξF_c仍有实pole，**不是entire**，minimal pole-clearing须含s²(s−1)²。这里仅保持Γ因子，未保持原经典simple双pole／minimal完成背景，不能冒充补齐578所缺的一般经典背景countermodel。F_c使用的是旧561真实**连续**正Beurling测度；该反测在本项目的连续g-integer域中有效，不另宣称存在离散free-generator子类的同型反例。它只阻止将页面那组字面条件无声推广为一般g-integer定理。

这个反测只说明 first step 字面“pole位置”不能代替 pole阶和缺陷，不泛判整页、也不反驳补齐simple poles及正确质量之后的标准桥。对于simple-pole版本，实1的留数A与 μ 的0点质量应匹配：Mellin移线先给相应A缺陷；把0点质量预置为1后，尚须核A=1或证明它由其余实际对象条件推出。Higher-order poles的log项则不能忽略。

原右半面 Mellin绝对收敛、正计数的polynomial/tempered费用、所需strip控制／合法移线及全部留数也须在实际对象上核实。有限阶若在准确假设下经标准 Phragmén–Lindelöf补足移线界，应记录那条依赖；本门没有外读原证明，不能把 ordinary整数 Dirichlet-series 的 Hamburger结论直接改写成 general g-integer 已付定理。反过来，本门也不从当前条件叙述的省略推断所有加强版本都失败。

## 5. 准入结果与停止范围

当前 §3.4 是限定为问题／分阶段研究的议程，不是本轮所需的新 actual signed Euler 替换命题。其两个实物——reciprocal comb 与 Gaussian totality——都被561旧原件覆盖；第一 FE→theta责任仍须由实际系统、完整pole与增长前件支付。没有新的Π删减／重排规则，没有同一完整Γ/contact、proper powers、双pole下的原du/zero-extension Dlog两源净费用，也没有危频core／coupling的独立signed量。

建议将本唯一locator按**来源／强旧0止**，不准C050/587，不续spacing、finite-coset、bounded-error、Hamburger证明或下一paper/query。无合格locator是本批的准确结果，不是已经排除所有经典Γ的正Beurling模型或signed/joint修复。

原Γ=0对照、有限rational(s)与单调正Euler增量的旧筛选范围保持；一般正Π允许删减原原子，仍不能被这些类拼合排除。原同一非零primitive/mixed、signed/corecross/Ξ核心瓶颈及whole4/5负惯性UPPER未改；cadence0/历史50/latest586/formal17不动，Goal active/open。本文为支持原稿，root核消费与结算仍另行执行。
