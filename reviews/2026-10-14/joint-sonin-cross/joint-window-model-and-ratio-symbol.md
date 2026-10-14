# 联合长窗完整 Gram 逆：双边界符号与 ratio3/2 消去

2026-10-14；独立模型推导。对象固定为实际 \(S=\{\infty,2,3\}\) 的同一 causal B，
不用 single-prime 正迹相加，不据 W 的单项读最终系数，不使用有限矩阵诊断。
本稿不改 STATE/cadence/Git，不建合同；实际 Sonin 高频运输由另一审查承担。

## 1. 恢复、量词与主结论

已按 AGENTS 读 README/STATE、check/show、Goal/frontier/C023/最新 AD 战略及
`joint-sonin-source/next-actual-ratio-cross-gate.md` 和 root-consumption-scope。
结构检查通过；现场 HEAD `ac4122a4f494be50143cfce1eb1214d7ea5295a2`，当时树 clean。
同 G20261014、固定基线 0c4f/≤538；C023 stopped，strongest-old whole leading4/5。
本稿的新任务是已准入的 actual ratio cross 所需模型费用，不重跑前一合法性门。

在原 \(H=L^2(\mathbb R,dy)\) norm 中置

\[
 U_t f(y)=f(y-t),\quad a=\log2,\ b=\log3,\quad q=2^{-1/2},\ r=3^{-1/2},
 \quad B=(I-qU_a)(I-rU_b),\quad W=B^*B.
\]

对 **ALL \(T>0\)、ALL \(R\in\mathbb R\)**，令

\[
 P_T=1_{(0,T)},\quad G_T=(P_TWP_T)|_{P_TH},\quad
 w_{R,T}=e^{iRy}1_{(0,T)}/\sqrt{2\pi},
 \quad b_R=(1-qe^{-iaR})(1-re^{-ibR}).
\]

这里 \(G_T^{-1}\) 是完整多位移的真实压缩逆；\(a/b\) 非有理，不作共同 lattice 简化。
设 \(\alpha=qe^{-iaR},\beta=re^{-ibR}\)。下面初等推导严格给每个固定
\(0<\gamma<1/2\) 的显式有限常数 \(C_\gamma\)，使

\[
 \boxed{
 |b_R|^2\langle w_{R,T},G_T^{-1}w_{R,T}\rangle-\frac{T}{2\pi}
 =-\frac1\pi\Re\left\{\frac{a\alpha}{1-\alpha}
                         +\frac{b\beta}{1-\beta}\right\}
       +\varepsilon_{T,R},\qquad
 |\varepsilon_{T,R}|\le C_\gamma(1+T)e^{-\gamma T}.
 } \tag{1}
\]

主项只含 2、3 的各自 primepowers。\(\log(3/2)=b-a\) 与 \(\log6=a+b\)
混合 harmonic 的系数严格为0。消去发生于 **整个联合 inverse 与双边界**；
结论没有假设 \(T_{23}\) 等于两个独立 single-prime 正迹之和。
证明不借外部 Wiener–Hopf/Szegő 定理，所有 norm、半线方程和 finite-window 误差在下文支付。

## 2. 因果逆与统一指数尾

记

\[
 m=(1-q)(1-r)>0,\quad M=(1+q)(1+r),\quad
 D=B^{-1}=\sum_{j,k\ge0}q^jr^k U_{ja+kb}.
 \tag{2}
\]

级数在 operator norm 绝对收敛；\(\|D\|\le D_0=1/m\)，
\(\|W\|\le M^2\)、\(G_T\ge m^2I\)。这里 D 是 inverse，非 source derivative。
用 \(x=ja+kb,c_x=q^jr^k=e^{-x/2}\) 记每个 delay。
这些 delay locally finite；2、3 的唯一分解保证无重名，但证明不需要有理 lattice。

令

\[
 A_\gamma=\sum_x c_xe^{\gamma x}
 =\frac1{(1-qe^{\gamma a})(1-re^{\gamma b})},
\]

\[
 J_\gamma=\sum_x x c_xe^{\gamma x}
 =A_\gamma\left\{\frac{a q e^{\gamma a}}{1-qe^{\gamma a}}
              +\frac{b r e^{\gamma b}}{1-re^{\gamma b}}\right\}.
 \tag{3}
\]

对 \(0<\gamma<1/2\)，两者有限，且

\[
 \tau(T):=\sum_{x>T}c_x\le A_\gamma e^{-\gamma T},\qquad
 \sum_{x>T}xc_x\le J_\gamma e^{-\gamma T}. \tag{4}
\]

因此跨越整个窗的 causal inverse 严格小：若 \(L=1_{(-\infty,0)}\)、
\(H_T=1_{(T,\infty)}\)，则

\[
 \|H_TDL\|\le\tau(T),\qquad\|LD^*H_T\|\le\tau(T). \tag{5}
\]

因为 delay \(x\le T\) 的两端压缩为0，其余项逐项 norm≤1。
这保留了任意阶 mixed returns，未截断 N。

## 3. 两个半线的完整 inverse 与有限窗 parametrix

记 \(P_+=I-L\)、\(P_{-,T}=I-H_T\)，\(F=W^{-1}=DD^*=D^*D\)。
causal B 和 D 都保持 \(P_+H\)，并互为有界逆。因此在正半线

\[
 G_+=(P_+WP_+)|_{P_+H}=B_+^*B_+,\qquad
 G_+^{-1}=D_+D_+^*
 =P_+\{F-DLD^*\}P_+.
 \tag{6}
\]

这是有界 Hilbert 空间算子身份，不对不在 L² 的常数1应用 inverse。
右半线由反向 causal \(B^*,D^*\) 给

\[
 G_{-,T}^{-1}=P_{-,T}\{F-D^*H_TD\}P_{-,T}. \tag{7}
\]

定义 \(K_L=DLD^*\)、\(K_{R,T}=D^*H_TD\)，以及真正 two-boundary parametrix

\[
 S_T=P_T(F-K_L-K_{R,T})P_T\quad\hbox{on }P_TH. \tag{8}
\]

将 (6) 左右压缩到 P_T，将 (7) 同样压缩，再减去 \(WF=I\) 的 P_T block，
得到精确 residual

\[
 G_TS_T-I_{P_TH}
   =P_TW H_TK_LP_T+P_TW L K_{R,T}P_T. \tag{9}
\]

这一步保留了两个远端 coupling。由 (5)

\[
 \|G_TS_T-I\|\le2M^2D_0\tau(T),\qquad
 \|S_T-G_T^{-1}\|
   \le\frac{2M^2A_\gamma}{m^3}e^{-\gamma T}.
 \tag{10}
\]

用 \(\|w_{R,T}\|^2=T/(2\pi)\)，其 quadratic-form 误差至多
\(M^2A_\gamma T/(\pi m^3)e^{-\gamma T}\)，对全部 R 一致。
不用单半线来代整个窗，也不将分离的正/负 infinite trace 相加；这里只计算合法 L² 向量配对。

## 4. whole inverse 的 bulk 与两个边界的精确积分

设

\[
 d_R=\sum_x c_xe^{-iRx}=1/b_R,\qquad
 j_R=\sum_x x c_xe^{-iRx}.
\]

由 (2) 与 compact plane-wave overlap，有绝对收敛式

\[
 \langle w_{R,T},Fw_{R,T}\rangle
  =\frac1{2\pi}\sum_{x,z}c_xc_z e^{-iR(x-z)}(T-|x-z|)_+.
 \tag{11}
\]

将 \((T-h)_+=T-h+(h-T)_+\) 展开。
\(|x-z|>T\) 蕴含 \(x>T\) 或 \(z>T\)，(4) 给

\[
 \langle w,Fw\rangle
 =\frac{T}{2\pi}|d_R|^2
   -\frac1{2\pi}\sum_{x,z}c_xc_z e^{-iR(x-z)}|x-z|
   +O_\gamma(e^{-\gamma T}). \tag{12}
\]

例如该 O 的绝对常数可取
\((D_0J_\gamma+J_0A_\gamma)/\pi\)。第一矩可和，允许全部 double sums 换序。
这里只展开 F，不把它冒充 \(G_T^{-1}\)。

真实左修正有

\[
 \langle w,K_Lw\rangle=\|LD^*w\|^2
  =\frac1{2\pi}\int_0^\infty
       \left|\sum_{t<x<t+T}c_xe^{iRx}\right|^2dt. \tag{13}
\]

右修正 \(\|H_TDw\|^2\) 用 \(e^{-iRx}\) 替代 \(e^{iRx}\)。
由于 \(c_x\) 为实，它和 (13) **对每个 T,R 完全相等**；不是只在极限假设左右一样。
用 (4) 将 finite interval \((t,t+T)\) 换为 \((t,\infty)\)：
sum 差≤\(A_\gamma e^{-\gamma(t+T)}\)，各自幅度≤\(A_\gamma e^{-\gamma t}\)，
所以每个边界平方范数的误差≤
\(A_\gamma^2/(2\pi\gamma)e^{-\gamma T}\)。由 Tonelli/绝对第一矩，

\[
 \langle w,K_Lw\rangle
 =\frac1{2\pi}\sum_{x,z}c_xc_z e^{iR(x-z)}\min(x,z)
      +O_\gamma(e^{-\gamma T}). \tag{14}
\]

double sum 在 x,z 互换下对称，可将 phase 换为 \(e^{-iR(x-z)}\)。
将 (12) 减去 (14) 的两个真实边界，在 **全 double sum 内** 使用

\[
 |x-z|+2\min(x,z)=x+z,
\]

于是

\[
 \langle w,S_Tw\rangle
   =\frac{T}{2\pi}|d_R|^2
       -\frac1\pi\Re(j_R\overline{d_R})
       +O_\gamma(e^{-\gamma T}). \tag{15}
\]

这就是 mixed pairs 如何消去的具体机制：不能只保留 whole-F 的 \(|x-z|\) 项，
也不能删掉任何一个边界的 min 项；二者均会留下错误的 rational/composite harmonics。

## 5. 联合因果符号的对数导数：无 mixed 主项

几何 double sum 给

\[
 j_R=d_R\left\{\frac{a\alpha}{1-\alpha}
                         +\frac{b\beta}{1-\beta}\right\}.
 \tag{16}
\]

由 \(|b_R|^2|d_R|^2=1\)，将 (15)、(10) 合并便得 (1)。
可取

\[
 C_\gamma=M^2\left\{
    \frac{D_0J_\gamma+J_0A_\gamma}{\pi}
       +\frac{A_\gamma^2}{\pi\gamma}
       +\frac{M^2A_\gamma}{\pi m^3}\right\},
\]

使 (1) 对全部 T>0、全部 R 成立。
这是原 norm 的显式 fixed-S 费用，常数可大；不称其 uniform growing-S 小费。

主项可写成绝对、一致收敛的真实 Fourier series

\[
 F_{23}(R)=-\frac a\pi\sum_{n\ge1}q^n\cos(naR)
              -\frac b\pi\sum_{n\ge1}r^n\cos(nbR). \tag{17}
\]

因此在其 Bohr coefficient（长均值，允许 termwise 因绝对一致收敛）中，
频率 \(b-a\)、\(a+b\) 的系数严格0；它们不等于任何 \(na\) 或 \(nb\)。
W 的 \(+1/\sqrt6\) 混合 shift 经完整压缩 inverse 与两端边界后消去。
给出 additive 最终符号的是 (16) 的 **joint** 对数导数；
并未声称实际投影可以 split、实际 traces 可以相加、或其低频 error 也相加。

## 6. actual Gamma 载频消费范围及未付责任

在 532 的真正高载频模型，\(T=\Gamma(R)=2\theta'(R)
 =\log(R/(2\pi))+O(R^{-2})>0\)（R 足够大）。
固定 \(\gamma=1/4\)，本模型误差因此为
\(O(\log R\,R^{-1/4})\)，趋0且不残留 relative \(\Gamma\) 大尾。
常数与 R 无关，未使用未知 ζ 零点位置或拟合。

**本稿支付模型 inverse 与 boundary symbol，不支付实际 Sonin 到模型的运输。**
实际消费还须另一稿证明

\[
 |b_R|^2\langle k_R,G^{-1}k_R\rangle
   -|b_R|^2\langle w_{R,T},G_T^{-1}w_{R,T}\rangle\longrightarrow0,
\]

使用真正 \(G=PB^*BP\)、532 的 k_R/clipping 与足够 absolute error，
而不是固定 inverse 截断的 relative \(\rho_\infty(R)\) 尾。
若该前件闭合，可得 fixed-S actual density 的主项 (17) 与 C₀ 高频余项；
仍需保持 local evaluation/norm 连续性，才消费 fixed-support compact-error。
这不决定该 error 的符号；535 的 single-p infinite ± 结论也不能直接 sum 到 joint。

对冻结 ratio3/2 双patch、双 pole/allpp零、norm1 weakzero 源，模型主项没有 rational
mixed 残留。所以“用 W 的3/2项造非零 cross”的候选被全 inverse 计算否定。
若 actual 运输也成立，此 particular cross 仅必要门 pass，非 whole positivity／core 净费用。
源窗已被 537 覆盖，且目前 whole strongest-old 为 leading4/5；本稿不以 fixed-S 重验收 Goal。

本证明的因果 tail 因子逐 S 相乘；成长 S_L、全源共同 error、signed 低域、core/coupling
与 ζ/Ξ 识别仍另付。这里没有 global growing-S 常数，也不把同一个实际无限量词偷偷换成 fixed-S。
所有“新增输入／结算”标签由 root 最强旧与 actual 运输审查决定；本代理没有消费轮数。
本稿无 shell producer 或待处理计算，唯一交接动作是核 actual-to-model absolute error 的原稿，
再按本 necessary gate 的真实范围消费，不再 ordinary 增 N 或另加素数。
