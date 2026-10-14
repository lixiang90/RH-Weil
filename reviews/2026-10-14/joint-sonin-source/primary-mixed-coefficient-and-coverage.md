# 真正 joint finite-S Sonin：3/2、6 混合响应与来源准入

2026-10-14；独立来源／最强旧消费审查。只审 CCM 2310.18423v2 的真实
\(S=\{\infty,2,3\}\)，不建 C024、不消费 cadence、不修改公共执行状态。
结论：**固定 S 投影／迹域合法；实际混合算术系数与完整 Weil 比较未付，来源 0 停止。**
本稿是出稿，仍须 root 消费，不能由文件存在升级为已结算结果。

## 1. 恢复与原件定位

已读 AGENTS、README、STATE，运行 check/show，恢复同 G20261014、固定基线
`0c4f3a3eb609bb1d9564138fa4a35701f05605f2`、Goal/frontier/C023/最新战略及 AC。
现场 HEAD 为 `43d4b0af7fe57cbf672d85fc82e7b690fa45e7ed`；父线程正在完善同 Goal。
压缩后首次结构检查遇到并发 Goal 指纹变更，父线程完成重绑后重新 check/show 通过。
这是组织态观察，不是数学前件的缺失或通过。原数学轮仍以 STATE/cadence 为准。

本门重新核读原件
[CCM v2 §4.6–4.8.2，(57)–(58)、Theorem 4.6](https://arxiv.org/html/2310.18423v2)，
以及 531/532/535；补读 533/534 的 base-S 与迹域限制，511 的物理范数运输。
原文给有限 S、任意 Sonin cutoff 的有界可逆同构；整个函数空间相同，内积随 S 改变。
它不把该同构称为酉映射，也不在这些章节给完整 Weil 下界、联合投影的显式核或成长误差。
下文投影、迹响应及误差界是从该输入与旧 531 的同对象证明直接推导，不冒称原文新定理。

## 2. 对象、原范数与映射角色

令 \(H_S=L^2(X_S)^{K_S}\)，\(X_S=\mathbb A_S/\{\pm2^m3^n\}\)。
使用原件的物理 Hilbert 内积和 unitary \(\mathcal U_S=\mathbb F_\mu w_S\)，
经 \(J_S=\mathcal U_\infty^{-1}\mathcal U_S\) 识别回实位偶物理空间，
再使用 531/532 的 unitary log 坐标 \(H=L^2(\mathbb R,dy)\)。
在 H 中

\[
 U_t f(y)=f(y-t),\qquad \widehat{U_t f}(s)=e^{-its}\widehat f(s),
 \qquad A_g=\int g(t)U_t\,dt.
\]

这些是原物理 norm 的酉识别；不把 weighted Mellin 空间之间的 identity map 当酉。
也不把每个局部 Fourier 独立下降到共同 S-unit 商：使用的是同一共同 Fourier。
source 是原 compact smooth \(g\in C_c^\infty(\mathbb R)\)，\(g\mapsto A_g\) 是 scaling
积分映射。g 不是自动属于 Sonin range 的物理向量，Sonin range 也不是完整 Weil 源的覆盖。
固定 Sonin cutoff 为 1；它与源支持半窗 L／旧冻结的 \(\sqrt{13/5}\) 不同。

令 P 为该实位 Sonin cutoff1 的真实正交投影，M=RanP。
令 \(a=\log2,b=\log3,q=2^{-1/2},r=3^{-1/2}\)，原 (58) 在共同 norm 中给

\[
 B=(I-qU_a)(I-rU_b)=I-qU_a-rU_b+qrU_{a+b}.
 \tag{1}
\]

真正半局部 Sonin range 是 BM。\(\theta_S\) 对应 B，\(\eta_S\) 对应
\((B^*)^{-1}\)，旧 mixed pairing 是 \(\theta_S^*\eta_S=I\)，不是 \(\theta_S^*\theta_S=I\)。
固定 finite S 的 \(\theta_S:M\to BM\) 是满射；它不识别完整 Weil 的符号或非根商。

记

\[
 m=(1-q)(1-r)>0,\quad M_+=(1+q)(1+r),\quad
 G=(PB^*BP)|_M.
\]

严格有 \(m\|f\|\le\|Bf\|\le M_+\|f\|\)，因此
\(m^2I_M\le G\le M_+^2I_M\)。真实物理正交投影为

\[
 \boxed{\Pi_{23}=BP G^{-1}PB^*.} \tag{2}
\]

证明：\(V=B|_M G^{-1/2}\) 是 M 到 BM 的等距满射，\(VV^*=\Pi_{23}\)。
公式中的 inverse 只作用于 M，通过 P 嵌入 ambient H。
\(BPB^*\)、\(BPB^{-1}\)、单 prime 投影之积都不是本对象的替代品。

## 3. 3/2 与 6 的确切位置：先区分 W 与最终投影

令 \(C_t=U_t+U_{-t}\)。由于 ambient translations 交换，实际

\[
 W=B^*B
 =2I-\frac4{3\sqrt2}C_a-\frac3{2\sqrt3}C_b
       +\frac1{\sqrt6}C_{a+b}+\frac1{\sqrt6}C_{b-a}.
 \tag{3}
\]

| 对象 | 精确混合项 | 消费范围 |
|---|---|---|
| B | \(U_{\log6}/\sqrt6\) | 原 \(\theta_S\) multiplier 的有限项 |
| W | 各 \(U_{\pm\log6}\)、\(U_{\pm\log(3/2)}\) 的系数 \(1/\sqrt6\) | ambient Gram，非 Weil 原子 |
| G | 上述全部项经 \(P(\cdot)P\) 压缩 | 一般不与 translations 交换 |
| \(G^{-1}\) | 压缩 translations 的完整返回／交叉 | 不能由 W 的一项直接读取 |
| \(\Pi_{23}\) | (2) 保全 inverse 和两侧 B | 真正正交化后的对象 |

特别，裸 Mellin multiplier 的正权重为

\[
 |b_{23}(s)|^2
 =2-\frac8{3\sqrt2}\cos(as)-\sqrt3\cos(bs)
 +\frac2{\sqrt6}\{\cos((a+b)s)+\cos((b-a)s)\}.
 \tag{4}
\]

这里 \(b_{23}(s)=(1-qe^{-ias})(1-re^{-ibs})\)。
若 k_s 是 532 已付的真实裸 unitary Mellin 求值向量，则真正迹密度是

\[
 \boxed{\rho_{23}(s)=|b_{23}(s)|^2\langle k_s,G^{-1}k_s\rangle.} \tag{5}
\]

证明使用 BM 的求值 \(Bf\mapsto b_{23}(s)\langle f,k_s\rangle\) 和原 norm
\(\langle f,Gf\rangle\)。不是 Gamma-completed evaluator 的密度。
因此 (4) 的混合 cosine 系数也不是 (5) 最终密度的 Fourier 系数；
inverse 的 s 响应可以混合或消去它们。当前没有计算最终 \(3/2\) 或 6 的原子系数。

这不是语言上的保留。写 \(D=PG^{-1}P\)，\(b_1=1,b_2=-q,b_3=-r,b_6=qr\)，则

\[
 \Pi_{23}=\sum_{i,j\in\{1,2,3,6\}} b_i b_j U_{\log i}D U_{-\log j}. \tag{6}
\]

ratio3/2 的两项是 \(qr(U_aDU_{-b}+U_bDU_{-a})\)，product6 的两项是
\(qr(U_{a+b}D+DU_{-(a+b)})\)。D 含所有混合返回，且不是 translation-invariant
卷积核；(6) 的其他项也可能参与同一最终分布响应。
所以这两个有界算子项不能称为最终 \(+1/\sqrt6\) 的算术原子。
若有一具体 kernel \(d(y,z)\)，每项核为 \(b_i b_jd(y-\log i,z-\log j)\)，
也不能只把 i/j 当作其全部支持。这里只使用合法 operator 身份，不假设 kernel 已被原文算出。

另一个代数负对照：若某个 P 恰与全部 translations 交换，则 (2) 精确退化为 P，
尽管 W 的混合项仍非零。这只否定“W 项非零即最终原子非零”的推理；
真实 Sonin P 不满足该交换条件，不能据此声称其混合项已经消失。

## 4. 真正全 inverse 的迹响应与可付尾界

旧实位正迹给 \(A_gP\in S_2\)；因 A_g 与 B 交换，\(A_gBP=B A_gP\in S_2\)。
所以每个 complex smooth compact g 都有

\[
 T_{23}(g)=\operatorname{Tr}(A_g\Pi_{23}A_g^*)
 =\|B A_gP G^{-1/2}\|_{HS}^2\ge0,\qquad T_\infty(g)=\|A_gP\|_{HS}^2.
 \tag{7}
\]

这些量在该 smooth source 域有限。旧源极化域保持，不能推广成任意 L² 源的有限正迹。
令 \(Z=A_g^*A_g\)、\(R=I-P\)，则完整 ordinary trace 身份是

\[
 \boxed{T_{23}(g)-T_\infty(g)
   =\operatorname{Tr}_M[G^{-1}PWRZP].} \tag{8}
\]

因为 \(P W ZP\) 为 \((A_gBP)^*A_gBP\)，故 TC；
减去 \(G PZP\) 后正好得到 \(PWRZP\)，TC 循环给 (8)。
这一合法性在 fixed S 从 531 的证明直接闭合，不继承 534 未付的 finite-angle 迹极限。

本门还可以合法按 (3) 分开这有限个 source 夹心块：
\(P U_t ZP=(A_gP)^*A_gU_tP\in S_1\)，因为 \(A_gU_tP=U_tA_gP\) 为 HS；
\(P U_tPZP\) 亦 TC。因此 \(P U_tRZP\) 为 TC，trace norm 不超过 \(2T_\infty(g)\)。
这不是任意未夹源 ambient 块的 TC 声明。

定义实际共同-inverse 响应

\[
 \mathcal R_t(g)=\Re\operatorname{Tr}_M[G^{-1}PC_tRZP].
\]

完整实响应便是

\[
 T_{23}-T_\infty
 =-\frac4{3\sqrt2}\mathcal R_a-\frac3{2\sqrt3}\mathcal R_b
       +\frac1{\sqrt6}(\mathcal R_{a+b}+\mathcal R_{b-a}). \tag{9}
\]

**这是本门对 6 和 3/2 的实际 Gram-inverse 响应记录。**
四个 \(\mathcal R_t\) 都用同一个完整 G；不能将它们换成独立 single-p 响应。
取实部避免在非交换 compression 下免费假设每一半迹为实。
混合响应的符号、频率主项及 cancellation 尚未求出，(9) 的正系数不给响应正号。

可以支付整个 inverse 的 operator-norm 收敛，而不伪造 final coefficient。
置

\[
 c=(M_+^2+m^2)/2,\quad Q_0=I_M-G/c,\quad
 \rho=(M_+^2-m^2)/(M_+^2+m^2)<1,
 \quad G_N^{-1}=c^{-1}\sum_{j=0}^N Q_0^j.
\]

谱定理严格给

\[
 \|G^{-1}-G_N^{-1}\|\le m^{-2}\rho^{N+1},\qquad
 |T_{23}(g)-\operatorname{Tr}_M(G_N^{-1}PWZP)|
       \le (M_+^2/m^2)\rho^{N+1}T_\infty(g). \tag{10}
\]

每个 \(\mathcal R_t\) 的相应尾不超过
\(4m^{-2}\rho^{N+1}T_\infty(g)\)。同样 (5) 的密度尾被
\((M_+^2/m^2)\rho^{N+1}\rho_\infty(s)\) 控制。
这是固定 S、全 smooth source 的可用 relative real-Sonin/Gamma 尾，
不是 source-L² 均匀小误差、C₀ multiplier 或 signed Weil 比较。

不能照抄 single-p 的快速 Neumann 常数：将 G 写作 \(2I+H\) 时，(3) 的绝对
off-diagonal norm 上界为
\(8/(3\sqrt2)+3/\sqrt3+4/\sqrt6>2\)，不付 \(\|H/2\|<1\)。
(10) 的 balanced spectral expansion 是合法替代，但它没有独立算术信息。
不运行增加 N 的普通数值拟合，也不把有限 word/matrix 通过当定理。

## 5. 与真实完整 Weil 型的缺口和最强旧扣除

actual finite-place prime measure 只含
\(-\Lambda(p^n)p^{-n/2}U_{\pm n\log p}\)；\(\Lambda(6)=0\)，ratio3/2 不是 primepower。
因此若要同对象比较，混合响应必须在完整 inverse 中按正确方式消去，或进入已支付的真实余项。
“目标没有这两个原子”不证明 \(\Pi_{23}\) 的原子非零，更不证明 Q 有负值。
Γ 连续核、双 pole 与余项可能参与比较，必须保留原 \(\Gamma=2\theta'\)、du norm
和 zero-extension Dlog，不能只比有限 prime 字典。

原件给的 finite-S 同构与 531 的真实投影证明已经直接蕴含 (1)–(10) 的合法性。
532 已付每个固定 **single p** 的全部 primepowers 主项和 fixed-U compact error；
533/534 明确该 arch-base single-p 家族不能当一般 base-S telescopic sum。
535 已付 single-p 无费比较的无限 ± 边界，并明确未排真正 multi-prime 共同机制。
所以不得：

- 将 \(T_{23}-T_\infty\) 写成 \((T_2-T_\infty)+(T_3-T_\infty)\)；
- 从各 single-p compact error 推 joint error compact 或有某一符号；
- 从 positive trace、原文 de Branges 身份或 (10) 推完整 Q 的低端排序；
- 把此 fixed-S source identity 算成新的独立算术输入或宏观方法边界。

即使未来 fixed-S 的非紧主项付清，仍欠原 source comparison 的 error 签名/质量费。
成长窗 I_L 必须使用包含全部相关 base primes 的 S_L；固定 {2,3} 不覆盖。
\(m_S=\prod_{p\in S_f}(1-p^{-1/2})\) 的粗 inverse 界随 S 失控，不能当成长共同费用。
full source、finitecodim core、补空间/coupling、allproperpowers、双 pole 与 ζ/Ξ 识别均未由本门支付。

当前 strongest-old whole 对照是 542+555 的直接闭合推论 557：
\(\log B_{\rm old}(L)/e^L\to4/5\)，仍有指数 core。不是旧 printed leading1 或2。
本门没有更小 whole 预算、core 数量/符号净后果，也没有消除 Γ-relative 比较前件。
宏观箭头仍停在“合法独立正来源 → 同对象完整 signed 比较”；
对象和 trace 域已恢复，关键算术箭头没有改变。

## 6. 门结算、允许修复与唯一具体再准入动作

**本次门 source0 停止。** 不是“没有显式 kernel 所以对象不存在”：对象、inverse 和
ordinary source trace 已真实闭合。停止原因是 primary 未提供可直接消费的 joint signed
系数／source-L² error，本次仅从 strongest-old 输入重建接口，第三句 core 净后果为空。
不新建 C024，不续 fixed-S/paper 标签链，不再凭 positive Gram 或增加 N 延长门。
保留合法的共同 inverse、有符号 low-cycle/source-kernel、非有限秩 paid compact、
growing/source-adapted S 与真实 Γ-relative 费用修复；本稿不排这些类。

唯一具体再准入付款对象是 **真实 joint inverse 下 ratio3/2 的 compact-error 门**，
先不加第四个素数：令 \(d=\log(3/2)\)，选
\(0<\delta<\tfrac12\min(d,\log2-d)\)，两个 source patches 中心为 ±d/2、半宽 δ。
取非零 \(\chi\in C_c^\infty(-\delta,\delta)\)，

\[
 h_R=\frac{(\partial_y^2-1/4)(e^{iRy}\chi)}{\|(\partial_y^2-1/4)(e^{iRy}\chi)\|_2},\qquad
 g_R^\pm=2^{-1/2}\{h_R(\cdot+d/2)\pm h_R(\cdot-d/2)\}.
\]

每 patch 的两真实 pole 矩 \(\int e^{\pm y/2}h_R(y)dy=0\)；所有实际 primepower
相关严格0，因为整个差支持跨度 \(d+2\delta<\log2\)。这些是 smooth、norm1、
原 Dlog 合法且弱零的完整实际源，不是自由 label 或 plane wave；Γ 费随 R 约 logR，不能删。
以同一完整 (2)/(5)/(8) 定义实际
\(E_{23}=T_{23}-Q_W\)，核
\(C_R=\tfrac12\{E_{23}(g_R^+)-E_{23}(g_R^-)\}\) 是否趋0，
或给存在 R_j→∞ 的严格非零 lower，并支付全 inverse 尾和 Γ 余项。
该检验要使用真正 G，不能只测 W 的 \(qrC_d\) 项。

付出的独立高频 source-kernel 估计若给此 cross 非零，可严格否定该 **joint compact-error
桥**（fixed S、fixed physical source support）的这一必要条件；不推 Q 负、不排 paid
noncompact error 或所有 joint 方法。若该测试趋0，也只通过一个必要门，尚非 full error compact
或成长 core 准入。只有实际完整 signed response/error 与成长适用范围进一步支付、
扣 strongest-old4/5 仍有 core 净值时，才由 root 决定数学合同。

这给可推翻的下一费用／反例对象，不把待证 vanishing/domination 改名为现有 input。
本稿无待处理 shell producer、下载或数值运行；公共阶段、宏观总结、cadence 和 Git 由 root 消费后同步。
