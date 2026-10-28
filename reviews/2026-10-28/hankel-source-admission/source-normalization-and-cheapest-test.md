# Suzuki 类 Hankel 源的归一化与最便宜准入门

2026-10-28；unit_height 独占咨询 v1。恢复 AGENTS、README、STATE、G20261027、D20261028T、前沿顶部及已耗尽 C049；check→show 通过。formal17／cadence0／历史50／latest586 不动。只查本地库存，不外网、PDF、数值，不写 STATE／合同，不执行新证明。当前仅有 root 提议的公式；本稿不替它选择参数或原文版本。

**建议：先做一份原定义与原定理量词的定向来源门，不能直接准 Hankel 正性／临界紧致性证明。** 关键不是核能否写下，而是原定理究竟构造哪个移位目标，以及有没有独立、可消费的临界参数输入。仓库尚未支付这条桥；也没有依据宣布此构造已被旧有限通道反测排除。

## 1. 已核的 locator 与未核的原定义分开

本地按 Suzuki、1204.1827、2606.09096、Theta_omega、canonical system 及 Hankel 检索，实际命中：

| 本地记录 | 已核范围 | 本次不能承袭 |
|---|---|---|
| [174 OBS-1](../../../notes/174-nonconstructive-existence-and-branch-map.md) | 指向 Masatoshi Suzuki，A canonical system of differential equations arising from the Riemann zeta-function，arXiv:1204.1827；记录 \(\omega>1\) 无条件构造及 all \(\omega>0\) 的 RH 判据方向，并列局部质量／noncollapse 的观察门 | 这里只是旧观察记录，不是本次核过的原文版本、定理／公式 locator。不能由此认领任意小 \(\omega\)、某个精确 \(t\) 域或 Fredholm norm |
| [10-14 来源审查](../../2026-10-14/c012-variation/joint-source-entry-audit.md) | 实际读取的是**另文** arXiv:2606.09096v3 的 §1.2、§8.1、§7.9 相关段。原记录保 Theorem1.5 的 \(A_a-\lambda I\)、\(\lambda<\lambda_a\) 与 Corollary1.6 的额外 Ξ 比值局部一致极限；核空间收敛为 heuristic | 这不是1204.1827的核定义／行列式证明，不可混作本候选已付来源。移位 norm 实零函数、small-a simple-even 都不支付全成长未移位目标 |
| [本月 core 定位去重](../core-source-location/local-source-dedup.md)及 cycle10 | 已把上述线索列为观察／既有设施，未取得新的成长 signed 输入 | 不是原 Hankel construction 不存在，也不是所有参数族已止的定理 |

本次 literature 元数据按这些作者／ID／标题关键词未命中相应已登记原全文身份；不据此断言 ignored 目录绝无文件。1204.1827 当前不能报告已核原版本、原件字节或 SHA。Root 并行的新 primary 定位须另行绑定；本稿不替未读原文猜测定义。

本次实际使用的本地版本身份（字节为原文件，SHA 为 LF 规范化）：

| 文件 | bytes | LF SHA256 |
|---|---:|---|
| notes174 | 14398 | bfbd62b1b36cb6052c02211e0d47b86fdbc9c461d05dfbec81baefefc8e06644 |
| 10-14 joint-source-entry-audit | 8168 | 6f477943df6391cb34be18f8620ac2a79b581be42ec84fc16c672960b65f34a9 |
| notes568 | 17737 | f71ab11661107f5fe0d294ac671421b7aaef0f8860f87c238d8fbe1a15554a4a |
| notes578 | 11814 | d600adfc0fa857623f585af2ec809840296659b737afbcf5cb745eba740e0901 |

## 2. 当前唯一公式的类型还需哪些原定义

Root 提议
\[
 \Theta_\omega(z)=
 \frac{\xi(\tfrac12-\omega-iz)}
      {\xi(\tfrac12+\omega-iz)},\qquad
 K_\omega=\text{inverse Fourier of }\Theta_\omega,\qquad
 \mathsf K_\omega[t](x,y)=K_\omega(x+y),
 \tag{1}
\]
再由 Fredholm ratio 生成 \(\gamma_\omega\)。这足以标明一个具体原构造线索，尚不足以冻结其执行对象。原来源首门至少须逐项核：

* \(\xi\) 是否确为本项目 \(\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\)，\(\omega\) 及 \(z\) 的域和必要零点／增长前件。
* 原 Fourier 的正负号、\(1/(2\pi)\)、逆变换路径；\(K_\omega\) 作为函数、分布或其导数存在的准确范围，不能从符号直接当作普通 \(L^2\) 核。
* \(\mathsf K_\omega[t]\) 的 Hilbert 空间、截断半轴和端点：有限参数 \(t\) 不代表有限长度区间，更不代表 finite rank。必须由原定义决定是否是 \((-\infty,t)\) 等域，不能自行把它改为 \([-t,t]\)。
* 原文支付的是 compact／Hilbert–Schmidt／trace class 哪一级；det 是 ordinary 还是 regularized；ratio 的幂、正负次序及不为零的条件。HS 本身不支付普通 Fredholm det。
* \(\gamma_\omega\) 生成的 Hamiltonian 及其独立变量，是否与本项目物理源 \(u\)、源支撑 \(L\) 或热时间不同。

Hankel 算子可定义、\(1\pm\mathsf K_\omega[t]\) 可逆、Hamiltonian 正、所产 entire function 属于 HB 类、完整经典 Weil 型正性，是不同陈述。特别地，禁止把“实对称核”读作 PSD，或把某个 favorable parameter 的 contraction 写成全部参数的统一余量。

## 3. 系数恢复可能仅是旧算术编码

本项目已有 [036](../../../notes/036-max-kernel-prime-square.md)、[549](../../../notes/549-mobius-window-norm-full-cofactor-gram-and-physical-synthesis-gap.md)、[550](../../../notes/550-physical-row-mixed-source-admission-and-strong-old-aggregate.md)、[578 §3](../../../notes/578-prime-pole-signed-budget-and-selberg-control-gap.md) 对 Dirichlet 乘积、反射差频、proper powers 和 \(\mu*\log=\Lambda\) 的严格区分。

因此若原来源把(1)的 ζ 比值展开为 Euler／Möbius 系数，或在临界参数的一阶变分中恢复 \(\zeta'/\zeta\)，其算术系数出现 \(\Lambda(p^k)=\log p\) 本身是旧编码，不是新的 signed 消失或独立正性。作为**待与原定义核对的归一化字典**，令 \(s=\frac12-iz\)，在合法非零解析域，
\[
 \left.\partial_\omega\log
 \frac{\xi(s-\omega)}{\xi(s+\omega)}\right|_{\omega=0}
 =-2\frac{\xi'}{\xi}(s),
 \tag{2}
\]
\[
 \frac{\xi'}{\xi}(s)
 =\frac1s+\frac1{s-1}-\frac12\log\pi
    +\frac12\psi(s/2)+\frac{\zeta'}{\zeta}(s).
 \tag{3}
\]
这里只列旧函数恒等式作原文校准，不把(2)当临界算子极限或参数可微性证明。ζ 部分的 Möbius 反演须保**全部**幂；Gamma 比值、两个有理 pole 项和 contact 不能从 ζ 系数出现就推定已运输。

尤其不能把同向 \(x+y\) 的 Hankel 核直接当作物理 \(u-v\) 的 Hermitian Weil 差核。旧568§3已明确：naive 和核 PSD 甚至会错误拒绝真实正型 \(2\cos(\tau u)\)。该反测只排无桥换核，不排 Suzuki 的 canonical-system／reflection／determinant 构造；其实际桥必须从原公式读取。

## 4. 原 norm 与全源目标的最低验收

本项目目标保物理源 \(r=e^{u/2}f\)、全部 complex \(C_c^\infty\)／\(\mathcal S_{\exp}\)、du、全线零延拓 Dlog，Fourier 为
\[
 \widehat r(\nu)=\int r(u)e^{-i\nu u}\,du,\qquad
 \|r\|_{D\log}^2=
 \frac1{2\pi}\int\log(2+|\nu|)|\widehat r(\nu)|^2d\nu .
\]
未冻结 \(r,s\) 到原系统的实际读出前，不能把 \(\|\mathsf K_\omega[t]\|\)、determinant 或 \(\gamma_\omega(t)\) 的 bound 当成原源费用；Hilbert 空间中 \(x\) 的积分范数也不能自动改名 du。若只是 transfer function／entire function 的身份，应准确记录这个身份，不虚构同名 bilinear 源映射。

真正目标仍是全部 \(\Gamma(\nu)=\Re\psi(\frac14+i\nu/2)-\log\pi=2\theta'(\nu)\)、FP-contact、全部 \(p^k\) 及双 pole 的同一 \(W_\zeta\)，再作用于 \(r*s^*\)。须先核原文究竟对移位 \(s\pm\omega\) 的哪个对象给身份；固定 \(\omega\) 成功不自动给未移位通常 Ξ。

原 norm 的便宜旧校准是552的实际 fixed-window 调制源：原 du 不变，完整 \(Q_\zeta(r_R)=\log|R|\,\|r_0\|_2^2+O(1)\)，Dlog²仅同阶 log。若后续**实际冻结的 total reader**在该窗给 cofinal 参数统一 du bound，却声称完整型极限，先扣这个旧检验。它不套到尚未定义的 reader，亦不从一个组件的 bound 推 total 不可能；若原费随参数／频率发散，须支付那份实际费用而不是称已排。

405／553的全 noncompact Pan 仅在声称一个全域 exact 商／principal／mixed 读出时按原角色核。不能给每个 finite \(t\) 或 fixed \(\omega\) 自动添加“须消 Pan”条件。若后续选择独立正分布的 D′ 逼近，Goal 允许逐层不消405；但必须真的有完整 signed 缺陷趋零。反之，若最后 total 在某个 global fixed finite Sobolev 上连续且 exact 消全Pan，才按553最强旧密度扣除；不预设该前件。

## 5. 最便宜可改变选择的门与严格止损

本次建议仅一个下一动作：**在 root 定位的至多一份 primary 中，核(1)原定义及承担目标身份的那一条定理／紧邻必要公式，冻结其参数量词与独立输入。** 它必须回答：

1. 原定理无条件可用的 \(\omega,t\) 范围是什么；所产对象是 \(\xi(\frac12+\omega-iz)\)、其比值／变换，还是通常 Ξ，是否只给 favorable shift。
2. 从该已给范围到 \(\omega\downarrow0\)／all \(\omega>0\)，需要哪一个原文准确条件；该条件是已证明估计、条件定理还是 heuristic。
3. 有无一个原公式已把原参数族接到同一完整源／transfer identity，且其范数、noncollapse、极限次序有实际付款；不能以未知 critical norm／Hamiltonian 质量重新命名 input。

这首先是定义／陈述门，不证明小 \(\omega\) invertibility，不构造 Hamiltonian 极限。其信息能直接改变投入：若只恢复旧174的有利移位存在或10-14的额外 Ξ 极限条件，则来源0止，不开新 math；若真定位到尚未消费、独立支付临界非退化或同源净误差的原命题，再针对**那条具体输入**准入，而不是把整篇或整个 Hankel 设施领作新预算。

固定 favorable \(\omega\) 的费用可以依赖 \(\omega\)；这不提供 \(\omega\downarrow0\) uniform bound。即使每个 compact \(t\) 范围有 bound，也不自动得到全 \(t\)／通常 Ξ。形式上 \(\Theta_0=1\)（零处分式需取解析意义）还提示未缩放比值的平凡极限不等于 canonical system 的所需临界读出，不能跳过原归一化和 noncollapse。这里不证明交换任何极限。

当前没有 primary 定义／版本已核，没有 \(\omega\)／原域冻结、独立 critical 输入或新数学合同；本咨询0，不改唯一 cadence。未得原命题即止本次定位，不追加 toy、参数、正 Gram 或 paper 链。原 fixed Tate／互素加法／theta 谱停止范围及 whole4/5 UPPER 保持；不据有限定位或旧条件判全体 Hankel 方法失败。
