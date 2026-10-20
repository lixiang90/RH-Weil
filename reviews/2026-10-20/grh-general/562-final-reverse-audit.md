# 562 及三原稿：独立终逆审

2026-10-20。仅写本审查，不改原稿、公共状态、cadence 或 Git。恢复了 README/STATE、
check/show、同 G20261014、C025、当前战略、前沿和工作树；本审查不计独立研究轮。

**最终裁决：PASS。** 高维纯权至原算子酉化的范围问题已由 root 修正，并经本审查重新核读。
没有发现连续正例、全 compact Weil 判据、重数反测试或 Pick/det2 接口的证明缺口。
本结论不支付实际 ζ 的独立正性、成长 signed 费用或 Ξ 识别，不构成 RH 完成收据。

## 1. 已完成的唯一必要范围修正

Deligne 纯性直接约束的是每个 F_j 的**特征值**：|α|=q^{j/2}。
这给归一化除子在单位圆；它不单独排除 Jordan 块，因而不能自动把指定原 F_j
升级为正内积下的酉算子。高维原 Frobenius 的半单性不能由这项绝对值结论免费取得。
初稿 562 §1 的“归一化谱为酉”和数域/函数域原稿 §3 的“归一化 Frobenius 酉性”
现均已改为特征值模1，并明确后验对角模型与指定原作用的区别；原作用需另付半单性
与相容正内积。终版两处已经重新核读，与主稿 §4 的 nilpotent/Jordan 警示一致。

建议另在 562 §5 的 P_K=Σδ_{Np} 前注明“物理 x 轴上”，因为 §1 的 P 用 log u 轴。
这是坐标记号澄清，不影响原稿已经保留理想标签的 Euler 关系。

## 2. 连续族：逐式核对 PASS

对象是 [0,∞) 的正局部有限 Borel 测度 P、Π、M；P 为 primitive，Π 为全部 repeated
powers，M 含单位 δ0。它们不同于 zero-side σ，亦不同于 actual ζ 原 source/norm。

- 对 0<c≤1/2，离线段 0<α,β<1，正向段 β=barα、|α|²=c；m=2 时 A_2=2c，
  m≥3 时 A_m≥1−2c^{m/2}>0。统一 A_m≤3 合法，未误继承 561 的 A_m<1。
  c=1/2、A_3=3/2 确为有效反测试。
- p_c 的级数局部一致、原点 O(u)、每个 σ>1 指数权可积。推前 Jacobian 是 k^{-1}，
  Euler 权再乘 k^{-1}，总和 k^{-2}p(u/k)；系数 C_m=Σk^{-m-1} 精确消去。
  非负项 Tonelli 同时保完整 proper powers，没有将正 Π 直接冒充正 primitive。
- q=(e^u+1−e^{αu}−e^{βu})/u 的 Frullani 恒等式在 Re s>1 绝对收敛；可求导并用
  实 s→∞ 固定常数和 log 分支。正卷积指数的加权质量为 exp∫e^{-σu}dΠ，故真测度存在。
  Laplace 唯一性给 δ0+c(e^u−1)du；x=e^u 的 Jacobian 给 δ1+c(1−x^{-1})dx，
  N=1+c(x−1−log x)，误差与单位均准确。
- U f=e^{t/2}f(e^t) 是 L²(dx)→L²(dt) 酉，保持已指定 dy/y 卷积及 sharp；
  它不支付实际 ζ 不同 norm 的费用。
- 完整 pole 0、1 给 2cosh(t/2)，减 |t|e^{−|t|/2}q(|t|) 后精确得到 2cos(τt)
  或 2cosh(rt)。Gamma 为 0 是模型自己的背景，未改称经典 Gamma。
  全 complex compact 源的平方和成立；离线段取实奇 g=tφ，严格负值 −2F_g(r)²。
- 1/4≤c≤1/2 的中心线零点非空；c=1/4 有二重 0，D=0 于 C²，det 为 z²。
  标量 L²(2δ0) 只一维的反测试正确。τ>0 的 diag(τ,−τ)、常数及指数规范精确。

所以这是对 561 **已消费离线段之外**的新正向范围；它同时给非离散 arithmetic
分布和离散非空中心零谱，不能被压缩成旧整数识别或空零点真空例。

## 3. 一般 Weil 判据与 compact 分离 PASS

前件包括非零 entire E、阶≤1、全零点在有限竖带、完整反射除子与正整数重数。
反射 R(s)=2c0−bar s 保同一 imaginary coordinate，二次型配对
F_h(ρ) overline(F_h(Rρ)) 正确。

离线对 ρ0、Rρ0 的共同阶 m 全部除去，G 在这两点非零、其余零点仍为零；
一次插值 L 与 Gaussian e^{(s−c0)²} 给两点 1、−1。
阶≤1 的增长被固定竖带内 e^{−t²} 压倒；所有条固定竖带均快速衰减。
逐竖线 Fourier 反演和任意有限移线给 h 及全部导数的任意指数衰减，确属 S_exp。
零点和只有这对留下，值精确 −2m，未丢其余无限零点。

式(11)/(3.2a) 的分部积分界足以使 W 在 S_exp 连续；取 N 大于零点计数增长指数再加1
便可绝对求和。卷积连续可用 p_{a,k}(h*k)≤C_a p_{a+1,k}(h)p_{a+1,0}(k) 验证。
χ(u/R)h→h 在每个 S_exp 半范数成立，故二次型趋于 −2m，存在有限 compact 负测试。
此证明确实支付从 full-strip entire 分离到原 compact 域的转换。
分离函数使用 E，因此这里只是判据的直接证明，不是未知实际正性的来源。

## 4. 谱实现、Pick 与 C2–C5 PASS

全 compact 正型的 Bochner–Schwartz 对象是正 tempered 测度；其标量 GNS 是 cyclic
模型，原子权不能替 trace multiplicity。最大乘法域、自伴性、带重数 K=⊕C^{mγ}、
zero0 因子和 compact-resolvent/HS inverse 的 det2 接口均正确。
已知零自由 e^{a+bz} 不改变除子；精确函数身份的规范另需标定，未知额外零因子才会改谱。

real-type、阶≤1 的 genus-one 规范下，−F'/F 的虚部是 m0y/|z|² 加全部 Poisson
核正和；反向全纯先排 C+ 零点、real-type 再排 C−。e^{z²} 反例说明为何不能删规范。
没有把右收敛半平面的正 Laplace 测度免费运输到全上半平面的 Pick 性。

Weil difference kernel 与 OS sum kernel 的 2cos(τt) 反测试有效；两个 bump 可令
C=0、S≠0，前者给正、后者严格负。结论只是这两个明确 kernel/domain 的区别，
未排除另行定义的 OS 路线。C5 的 simple/even 前件属于特定构造；同一非零 F 的局部一致
real-zero 逼近才是 Hurwitz 传递的共同门。Gram 的 rank≤2 给 lowest 多重零的反例也准确。

root 终版新增的两个小命题均成立，并已重新核读：在交换 involutive 卷积代数中
Q(fsharp)=W(fsharp*f)=W(f*fsharp)=Q(f) 自动，故这项形式对称本身不给 FE；
正型锥在 D' 分布收敛下闭，对每个固定 h*hstar 取极限即证。
真正仍欠完整 Gamma/prime-power/pole 平衡对同一目标的全 compact 分布收敛。

## 5. 数域、函数域及来源范围

数域的 primitive/ideal norms 保标签与整数重数，非单位整数梳；Γ_C 的因子 2、
判别式因子和中心都正确，本文没有把数域 GRH 说成已证。
核 [Sutherland Lecture19 Remark19.13](https://math.mit.edu/classes/18.785/2019fa/LectureNotes19.pdf)。

曲线须用全部 closed places，包括相对于某个 affine 坐标的 infinity places。
全部周期零点与 s=0、1 的无限周期极点副本已保留；清除完整
(1−q^{−s})(1−q^{1−s}) 后，q^{g(s−1/2)}P(q^{−s}) 的自对偶规范正确。
有限相位 U 与实线全周期 D 区分准确；不能把 s 平面 pole 除子当 rank2。
核 [Milne §0–1](https://jmilne.org/math/xnotes/pRH.pdf)。

高维权线和奇零偶极的 signed determinant 公式正确，纯权因子不自动有 positive primitive。
Milne Theorem5.1 直接给各权特征值绝对值；指定原 Frobenius 的酉性另见 §1 修正。
CCM [Theorem1.1及§7–8](https://alainconnes.org/wp-content/uploads/zeta-spectral-triples-1.pdf)
确实保 simple/even/边界归一，并把向经典 Ξ 的归一化 determinant 收敛列为未完步骤。
本审查只在这些范围使用外部来源，不扩大为一般 Beurling 已知 RH 定理。

## 6. 根消费边界

允许消费：连续 positive primitive/nonempty RH 段、同族精确相变、全 complex compact
平方和、重数鉴别和本稿逐项条件纠错。一般判据/来源恢复不冒称新外部首创。
仍欠：实际 ζ 的独立完整 Weil 正性、原 source 自伴域和 Jordan 排除、faithful
determinant/Ξ 极限、成长 K/core/coupling。强旧 542＋555→557 whole4/5 不变。
本轮能改变用户所问的**一般对象类与实现条件**；未改变长期宏观完成门。
