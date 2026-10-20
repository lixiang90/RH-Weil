# 571 独立原稿：真实 receiver 的双边界 Schur 身份与 signed 机制

2026-10-20。仅写本独占原稿，不改 STATE/cadence/Git；未预设新合同、未消费研究轮。
恢复了 README/STATE、check/show、Goal、570 结算、560 及原模型/角色审计。
同 G20261014、固定 0c4f/≤538；strongest-old whole 仍为 542+555→557 leading 4/5。
本稿证明的是 560 window model 的**受限实际 receiver 身份**，不是把任意低半线
测试向量搬成 Weil 源；actual Sonin 到 window 的 fixed-F 桥与 growing-F 费用分开。

## 1. 准入三句和范围

1. 已付输入是同一 causal B、完整 D=B^{-1}、真实 window G_T 与双边界 S_T。
   它独立于未知零点位置，给合法 L² receiver 而非只有一个全空间 norm upper。
2. 可判新测试是：能否用**同一实际 receiver pair**，把 G_T^{-1}−S_T 写成
   一个保留完整 inverse/全部 returns 的双边界 Gram 差，并用 single-prime actual
   carrier 检验它是否天然取号。该身份在本稿付清；single-prime Γ-锁定检验另稿。
3. 成功只消除“具体哪个 receiver/哪些 returns 进入 signed 比较”的未知；若只给
   正 Gram、旧 fixed-F 衰减或全 H norm，不独立推出容量/Weil 正性，也不改变成长
   actual clipping/core/Ξ。本稿不给自己贴独立容量输入或宏观瓶颈已解标签。

## 2. 对象、角色和原 norm

在原酉 log 物理空间 \(\mathscr H=L^2(\mathbb R,dy)\)，
\(U_a f(y)=f(y-a)\)。先固定任意有限 prime 集 F，置

\[
 B=\prod_{p\in F}(1-q_pU_{a_p}),\quad q_p=p^{-1/2},\quad a_p=\log p,
 \qquad D=B^{-1},\quad W=B^*B,\quad Z=W^{-1}=DD^*=D^*D.
\]

\[
 m=\prod(1-q_p)>0,\quad M=\prod(1+q_p),\qquad
 m^2I\le W\le M^2I,\quad M^{-2}I\le Z\le m^{-2}I.
\]

令 \(T>0\)、\(P=1_{(0,T)}\)、\(L=1_{(-\infty,0)}\)、
\(H=1_{(T,\infty)}\)，Q=L+H。端点是零测集，无域变化。
\(G=(PWP)|_{P\mathscr H}\) 是 window compressed Gram；它不同于
560 实际 Sonin 子空间上的 \(G_F=(P_MWP_M)|_M\)。

\[
 S=P(Z-DLD^*-D^*HD)P.
\]

对任意 \(w\in P\mathscr H\)，**实际 receiver** 是

\[
 v=LD^*Pw\in L\mathscr H,\qquad u=HDPw\in H\mathscr H.                 \tag{1}
\]

二者由同一 w 产生，不可自由选择或由全空间 norm 的见证向量替换。
下文给 ALL w 的精确身份，随后才代真正 carrier

\[
 w=w_{R,T}=\frac{e^{iRy}1_{(0,T)}}{\sqrt{2\pi}},\qquad
 T=\Gamma(R)=\Re\psi(1/4+iR/2)-\log\pi=2\theta'(R)>0.                 \tag{2}
\]

R 仅取 Γ 正的足够大区域；一般身份允许任意 T/R，但实际消费不解耦 (2)。
范数均是这里的 dy norm；w、v、u 不等于 compact Weil convolution source r。

## 3. 因果半线因子与真实外域 Gram

定义 \(D_L=(LDL)|_{L\mathscr H}\)、\(D_H=(HDH)|_{H\mathscr H}\)。
因果性给 \(LD=LDL\)、\(DH=HDH\)，故二者都是有界可逆算子，逆为
\(B_L=LBL\)、\(B_H=HBH\)。例如
\(LDLB L=LDBL=L\) 与 \(LBLDL=LBDL=L\)，未将 D 当作酉。
\(D^*L\subset L\mathscr H\)、\(D H\subset H\mathscr H\) 又给

\[
 LZL=D_LD_L^*,\qquad HZH=D_H^*D_H.                                  \tag{3}
\]

交叉 block \(X=LZH\) 有两个一致的 factorization：

\[
 X=D_L(LD^*H)=(LD^*H)D_H.                                           \tag{4}
\]

第一式用 Z=DD* 与 LD=LDL；第二式用 Z=D*D 与 DH=HDH。
因此归一化的真实双外边界耦合是

\[
 \boxed{K=D_L^{-1}XD_H^{-1}=LBD^*H=LD^*BH.}                         \tag{5}
\]

这里 \(C=BD^*=B(B^*)^{-1}\) 是整线 **unitary all-pass**，因为 B 是 normal
Fourier multiplier；\(K=LCH\) 只是它的远端 block，不是 D 的全半线 norm。
令

\[
 A=D_L\oplus D_H^*,\qquad
 J=\begin{pmatrix}I&K\\K^*&I\end{pmatrix}
       \quad\hbox{on }L\mathscr H\oplus H\mathscr H.
\]

由 (3)–(5) 得到严格 operator identity

\[
 QZQ=AJA^*,\qquad QZPw=A\binom vu.                                 \tag{6}
\]

第二式的左分量是 \(LDD^*Pw=D_Lv\)，右分量是
\(HD^*DPw=D_H^*u\)。这一步将 Gram 与真实 receiver 对接，不能省去。

\(\|A\|\le m^{-1}\) 和 \(QZQ\ge M^{-2}\) 给

\[
 J\ge\frac{m^2}{M^2}I,\qquad
 \kappa:=\|K\|\le1-\frac{m^2}{M^2}<1.                              \tag{7}
\]

最后一步因 \(J-I\) 的 off-diagonal selfadjoint block 范数为 κ，谱关于零对称。
这是所有 returns 的合法完整 inverse gap，不是只验有限矩阵自伴性。

## 4. 完整逆的 exact Schur 差，不截任何 return

Z 的 P/Q Schur 补严格等于 \(G^{-1}\)：

\[
 G^{-1}=PZP-PZQ(QZQ)^{-1}QZP.                                      \tag{8}
\]

它来自 bounded strictly positive Z 的 block inverse；所有 block 都是 Hilbert
空间上的合法算子，无 infinite trace，也未对非 L² 常数使用半线 inverse。
而 S 的两个被减二次型恰是 \(\|v\|^2\)、\(\|u\|^2\)。把 (6) 代入 (8) 得

\[
 \boxed{\mathcal E(w):=\langle w,(G^{-1}-S)w\rangle
   =\|v\|^2+\|u\|^2
      -\left\langle\binom vu,J^{-1}\binom vu\right\rangle.}          \tag{9}
\]

这是与 560 exact residual 配对完全相同的 scalar：

\[
 R_T=GS-I=PWHDLD^*P+PWL D^*HDP,\qquad
 \mathcal E(w)=-\langle w,G^{-1}R_Tw\rangle.                         \tag{10}
\]

(9) 不是用某个近似 inverse 代替 (10)，而是重新组织**同一完整 inverse**。

J 的精确 block inverse 给

\[
\begin{split}
 \mathcal E(w)
  ={}&2\Re\langle v,K(I-K^*K)^{-1}u\rangle\\
    &-\langle v,KK^*(I-KK^*)^{-1}v\rangle
     -\langle u,K^*K(I-K^*K)^{-1}u\rangle.                           \tag{11}
\end{split}
\]

cross 项后跟两个非负量的负号；\((I-K^*K)^{-1}\) 和
\((I-KK^*)^{-1}\) 保留全部多次反射/returns。亦可写 exact 平方完成式

\[
 \mathcal E(w)=\|u\|^2
  -\|(I-K^*K)^{-1/2}(u-K^*v)\|^2                                  \tag{12}
\]

以及左右互换的式子。故

\[
 \mathcal E(w)\le\min(\|v\|^2,\|u\|^2),\qquad
 |\mathcal E(w)|\le\frac{\kappa}{1-\kappa}(\|v\|^2+\|u\|^2).        \tag{13}
\]

更准确的双侧 signed 谱界是

\[
 -\frac{\kappa}{1-\kappa}(\|v\|^2+\|u\|^2)
 \le\mathcal E(w)\le
 \frac{\kappa}{1+\kappa}(\|v\|^2+\|u\|^2).                          \tag{13a}
\]

因为 \((1-\kappa)I\le J\le(1+\kappa)I\)。正向 upper 没有坏 gap 分母；
这不消除 v/u 自身原 norm 的成长费用，也不是正下界。

从 (11) 分离**首个 cross**，剩余不是删除，而是以下严格费用：

\[
 \left|\mathcal E(w)-2\Re\langle v,Ku\rangle\right|
 \le\frac{\kappa^2}{1-\kappa}(\|v\|^2+\|u\|^2).                    \tag{14}
\]

证明：cross 多余部分范数不超过 \(\kappa^3/(1-\kappa^2)\)，两个 self
部分不超过 \(\kappa^2/(1-\kappa^2)\)；用 \(2ab\le a^2+b^2\) 合并。
因此出现符号的首个位置已明确，不能凭两个边界范数相等就宣称 cross 抵消。
也不能从正 J 或正 Z 宣称 \(\mathcal E\) 取号：正性属于被减的整个 Gram。

## 5. 真 carrier 的反射关系、原范数与固定 F 后果

全部 causal 系数是实的。定义 antiunitary 反射
\((\mathcal R_T f)(y)=\overline{f(T-y)}\)，它交换 L 与 H、D 与 D*，并且
\(\mathcal R_Tw_{R,T}=e^{-iRT}w_{R,T}\)。所以 (1) 在实际 carrier 上严格满足

\[
 u=e^{iRT}\mathcal R_Tv,\qquad \|u\|=\|v\|,\qquad
 \mathcal R_TK\mathcal R_T=K^*.                                    \tag{15}
\]

(11) 的两个 self-return 值相等，于是

\[
 \mathcal E(w_{R,T})
  =2\Re\langle v,K(I-K^*K)^{-1}u\rangle
     -2\langle v,KK^*(I-KK^*)^{-1}v\rangle.                          \tag{16}
\]

其中 \(e^{iRT}\) 与 v 里的全部 phase 同由 R 和 T=Γ(R) 决定；不允许为了
把 cross 调成某个号而自由指定它们。

写 \(x=\log n\)、\(c_x=n^{-1/2}\)，n 遍历 F-smooth integers，包括 n=1。
原 receiver 有 exact formula

\[
 v(-t)=\frac{e^{-iRt}}{\sqrt{2\pi}}
       \sum_{t<x<t+T}c_xe^{iRx},\qquad t>0,                         \tag{17}
\]

\[
 u(T+t)=\frac{e^{iR(T+t)}}{\sqrt{2\pi}}
       \sum_{t<x<t+T}c_xe^{-iRx}.                                  \tag{18}
\]

每个 fixed F 的和在 operator norm/绝对质量中收敛。式 (17) 给的是受限像，
没有理由包含旧 560(6) 在低半线任意选择的宽 bump。特别是 receiver 对数宽度、
相位和 norm 不能由那个 bump 的费用替代。

令 \(D_0=\sum c_x=m^{-1}\)、\(J_0=\sum xc_x<\infty\)。对 ALL R,T>0，

\[
 \|v\|^2=\frac1{2\pi}\int_0^\infty
       \left|\sum_{t<x<t+T}c_xe^{iRx}\right|^2dt
 \le\frac{D_0}{2\pi}\sum_xc_x\min(T,x)
 \le\frac{D_0J_0}{2\pi}.                                         \tag{19}
\]

这只是 old first-moment 原 norm upper 的正确 receiver 消费；不是成长 lower。
对任意先固定 \(0<\gamma<1/2\)，\(\tau_F(T)=\sum_{x>T}c_x\le A_{F,\gamma}e^{-\gamma T}\)。
(5) 由真正 cross-halfline compression 给

\[
 \kappa\le\min\left(1-\frac{m^2}{M^2},\ M\tau_F(T)\right).          \tag{20}
\]

结合 (13),(15),(19)，当 fixed F、T 最终使 κ≤1/2 时，

\[
 |\mathcal E(w_{R,T})|
 \le\frac{\kappa D_0J_0}{\pi(1-\kappa)}
 \le\frac{2M A_{F,\gamma}D_0J_0}{\pi}e^{-\gamma T}.                 \tag{21}
\]

这是受限 receiver 费用，较粗 \(\|w\|^2=T/(2\pi)\) residual upper 消去一个
T 因子；它由旧 exact identity/first-moment 直接合成，不能单靠较优 upper
冒称新 actual whole 输入。乘真实 \(|b_F(R)|^2\le M^2\)、代完整 Γ 仍是
\(O_{F,\gamma}(R^{-\gamma})\)；actual Sonin clipping 在 560(3) 中较慢的
fixed-F 费用仍须另加，原 C₀ 桥不因此升级为 cofinal 成长结论。

## 6. 成长、完整 Weil 项及独立容量边界

上面 (5)–(18) 都是每个 finite F 的 exact 身份，可以在每个 L 取
\(F_L=\{p<e^{2L}\}\)、\(T_L=\Gamma(R_L)\)。但 (19)–(21) 的
\(m_L,M_L,J_{0,L},A_{L,\gamma},\kappa_L\) 不能吞为统一常数。
“κ<1”只支付每个 fixed L 的完整 inverse 存在；离 1 的量至少按 (7) 退化，
并不支付成长实际 receiver 或两边界 signed 相消。概率归一 full-H tail 接近 1
也不决定 (16)，因为 (17) 中 phases 及受限来源仍在。

560 fixed-F source→k_R→w_R 桥是已付输入；cofinal F_L 时仍须支付原 source、
全 Sonin compressed inverse、clipping/coupling 及 Γ(R_L) 关联下的全部误差。
因此本稿不把 window model 的 \(\mathcal E\) 直接命名 actual source error。

Weil 型的责任仍是 560(1),(2)：保完整
\(\Gamma(s)=\Re\psi(1/4+is/2)-\log\pi\)、所有 primepowers
\(\log p\,p^{-k/2}\)、以及 \(2|\langle r,\cosh(u/2)\rangle|^2
-2|\langle r,\sinh(u/2)\rangle|^2\)。
本稿只处理 model 双边界 remainder，未删去这些项，也未重证其全源正性。
J 的正性来自一般 positive W，通常 causal filters 同样拥有；它不付算术 RR
容量。若把“实际 receiver 上 cross 支配 returns / 完整 source mixed Gram PSD”
直接当假设，仍由所求正性承担，不能称新独立分析条件。

真正新增的可消费信息是 exact (9)/(11)/(16) 把两边界与全部 returns 锁定到
同一个真实 receiver pair；符号还要 actual carrier test，成长容量还要独立输入。
是否建立新数学合同由 root 将它与 single-prime Γ-锁定测试、成长原 norm 审计
合并，并扣 strongest-old 后判断；本稿本身不计轮、不完成长期 Goal。

无数值/下载/后台 producer；剩余只需独立核 (3)–(16) 的 map/domain/符号，
及与另外两份实际 carrier/growth 原稿的前提一致性。
