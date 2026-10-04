# 426. 固定正角算子的原源迹类交换子与受限相容读出

2026-10-04。继续[425](425-f1-recentered-geometric-corner-and-source-period-finite-part.md)的同一个固定算子、原物理截止及时间测试。
本稿证明正象限乘子与该算子的交换子具有实际普通迹且为零，并把原有限部延拓到一个明确线性双模。
原提升T属于允许乘子，因此得到局部的源交换子消失。这个线性双模不是已经构造的全循环代数或相对Chern类；不宣称主关系、Weil正性或RH。

## 1. 同一域及正象限的实际小角

沿用425的 \(A(h)=A_\infty(h)=K_\infty U(h)K_\infty^*\)，
\(h\in C_c^\infty(\mathbb R)\)。\(\mathsf P_{K_p,K_q}\) 为物理下截止，且
\[
 \operatorname{Tr}(\mathsf P A(h)\mathsf P)
             =(K_pL+K_qM)h(0)+\Lambda(h).                    \tag{1}
\]
令原源的正象限投影
\[
 Q=\mathbf1_{j\ge0,k\ge0}\otimes1.
\]
425的实际径向公式直接给
\[
 QC_\infty=C_\infty Q=QC_\infty Q
   =P_{b_{0,p}}\otimes W_q\otimes M_{d_p}
       +W_p\otimes P_{b_{0,q}}\otimes M_{d_q}.                \tag{2}
\]
这是两个正交径向秩一角，时间乘法仍非迹类；不能只由(2)就称整个算子有限秩。

对 \(n\ge1\)，球／波形系数还给
\[
 H w_{-n,r}=-c_r\rho_r^{n-1}b_{0,r},\quad
 c_r=\sqrt{1-\rho_r^2},\quad \rho_r=r^{-1/2}.                 \tag{3}
\]
它精确控制混合群块经Q压缩后出现的几何衰减。

## 2. 左右Q压缩是真正迹类

记425的两通道投影为 \(E_p=R_p^-\otimes W_q\)、\(E_q=W_p\otimes R_q^-\)。
完整群和本身一般只强星收敛；这里另证
\[
                         QA(h),\ A(h)Q\in\mathcal S_1.       \tag{4}
\]
取 \(B<\infty\)，使四类时间块
\(M_{d_r}\mathsf T_{aL+bM}U(h)M_{d_s}\) 非零时必须有
\(|aL+bM|\le B\)。其迹范数有共同上界
\[
 C_h=\frac{\|\widehat h\|_1}{2\pi}
                     \max_{r,s\in\{p,q\}}\|d_r\|_2\|d_s\|_2. \tag{5}
\]
这是原光滑核的Fourier秩一积分界。

同通道p块仅 \(b=0\) 非零，许可a只有有限个；左Q后径向块
\(P_{b_{0,p}}\lambda_aR_p^-\otimes W_q\) 秩至多一、迹范数至多一。
q同理。交叉p←q块是
\(|w_a\otimes w_0\rangle\langle w_0\otimes w_{-b}|\)，\(a=-n<0,b>0\)。
左Q使其径向迹范数精确变为 \(c_p\rho_p^{n-1}\)。
对每个a，许可b数至多 \(N_q=1+\lfloor2B/M\rfloor\)；另一交叉方向同样由
\(c_q\rho_q^{n-1}\) 及 \(N_p=1+\lfloor2B/L\rfloor\) 控制。
因此完整左Q群和的迹范数总和有限，并可用
\[
 C_h\left[m_p+m_q+
             \frac{N_qc_p}{1-\rho_p}+\frac{N_pc_q}{1-\rho_q}\right] \tag{6}
\]
控制，其中 \(m_p=\#\{a:|aL|\le B\}\)、\(m_q=\#\{b:|bM|\le B\}\)。
该迹范数和与425的Schur强和在矩阵元上一致，故确为 \(QA(h)\)，非另定义的算子。
\(A(h)^*=A(h^*)\)，\(h^*(s)=\overline{h(-s)}\)，于是右Q压缩亦迹类。

## 3. 原源及所有正象限支持乘子的零普通迹

考虑明确乘子代数
\[
 \mathcal M_Q=\{R=c1+J:\ c\in\mathbb C,\ J=QJQ\in\mathcal B(\mathcal H)\}.
                                                                    \tag{7}
\]
这里称的是所构造线性双模的Hilbert有界乘子；没有证明任意 \(QJQ\) 都属于原C*交叉积的乘子代数。
原414提升 \(T=1-Q+QuQ=1+Q(u-1)Q\) 及 \(T^*\) 都属于此域；
这不要求T酉，也不要求它与 \(C_\infty\) 交换。
由(4)，\(JA(h)\) 和 \(A(h)J\) 均迹类，故
\[
                         [R,A(h)]\in\mathcal S_1.            \tag{8}
\]
另一方面 \(\mathsf P Q=Q\mathsf P=Q\)，所以 \([\mathsf P,R]=0\)。
令 \(B_K=\mathsf P A(h)\mathsf P\in\mathcal S_1\)，则
\[
 \mathsf P[R,A(h)]\mathsf P=[R,B_K],\qquad
                              \operatorname{Tr}[R,B_K]=0.    \tag{9}
\]
迹类算子经强趋单位的双侧压缩在迹范数中收敛（由有限秩逼近直接证明），
所以(8)–(9)推出
\[
                              \operatorname{Tr}[R,A(h)]=0.  \tag{10}
\]
这不是由“交换子迹类”单独推出的循环结论；(9)中与原截止相容的乘子条件是实际证明的关键。

特别地，原源自然的加权交换子满足
\[
 X_h=[T^*,TA(h)]\in\mathcal S_1,\qquad
                                 \operatorname{Tr}X_h=0.    \tag{11}
\]
迹类性可将 \(T=1+J\) 展开，得到
\(X_h=J^*A-AJ^*+J^*JA-JAJ^*\)，每项由(4)迹类。
又因物理截止与T、T*交换，
\[
 \mathsf P X_h\mathsf P=[T^*,TB_K],\qquad
                   \operatorname{Tr}(\mathsf P X_h\mathsf P)=0 \tag{12}
\]
对每个有限K已经精确成立。完整 \(X_h\) 的普通迹因此确为零。
这里原时间核、两条边和全部混合群块都被保留，没有先删掉错误混合周期。

## 4. 有限部与普通迹的交集一致

为避免给不在425测试族中的元素任意指定数值，取明确的线性空间
\[
 \mathcal D=\{A(h)+S:\ h\in C_c^\infty(\mathbb R),\ S\in\mathcal S_1\}.
\]
若 \(A(h)\) 本身迹类，(1)左边有界，而 \(K_pL+K_qM\to\infty\)，所以 \(h(0)=0\)。
再由迹范数压缩收敛得
\[
                  A(h)\in\mathcal S_1\Longrightarrow
                  \operatorname{Tr}A(h)=\Lambda(h).          \tag{13}
\]
因此
\[
                \widetilde\Lambda(A(h)+S)=\Lambda(h)+\operatorname{Tr}S \tag{14}
\]
与表达式选择无关；两种表达的差由(13)处理。
更直接地，(14)由实际截断定义：
\[
 \widetilde\Lambda(A(h)+S)=\lim_{K_p,K_q\to\infty}
 \left[\operatorname{Tr}(\mathsf P(A(h)+S)\mathsf P)
                       -(K_pL+K_qM)h(0)\right].             \tag{15}
\]
不同表达式的 \(h(0)\) 相同，因为其A部分之差迹类。这给完整的定义域准入与联合极限。
在测试函数加迹范数的商拓扑中，(14)连续；本稿只使用该线性空间，不另完成一个乘法代数。

## 5. 源乘子双模内的准确循环相容性

由(4)，\(\mathcal D\) 是 \(\mathcal M_Q\) 的双模：
\(RA(h)=cA(h)+JA(h)\)，\(A(h)R=cA(h)+A(h)J\)，后项均迹类；
迹类理想部分也被有界乘子保持。
式(10)和普通迹的有界乘子循环性给
\[
 \widetilde\Lambda(RF)=\widetilde\Lambda(FR),\qquad
                         R\in\mathcal M_Q,\ F\in\mathcal D. \tag{16}
\]
特别 \(TA(h)\in\mathcal D\)，所以
\[
 \widetilde\Lambda(T^*TA(h)-TA(h)T^*)=0.                      \tag{17}
\]
这既是(11)的普通迹结论，也是在保留原纯周期有限部的同一线性域中的源相容性。
因此可以同时保留425的非零纯周期读出及该自然源交换子消失。

范围必须严格：没有证明 \(A(h)A(k)\in\mathcal D\)，
一般径向群移位亦不属于 \(\mathcal M_Q\)；(16)不是全交叉积上的不变标量迹。
没有构造完整相对循环Chern类、把(17)识别为算术主关系，或证明对所有几何主除子消失。
425的其他真实强截止仍给不同的A族有限部；本稿的相容性保留了原物理截止。

## 6. 与截止自然性的具体关系

425的有限波形截止不保留球向量。若 \(K_p,K_q\ge1\)，由(3)，
其像与 \(Q\) 作用后的像之和，恰为
\[
 (R_{K_p,p}^-\otimes W_q)\mathcal H_{\rm rad}
       \oplus(W_p\otimes R_{K_q,q}^-)\mathcal H_{\rm rad}.     \tag{18}
\]
一维证明是向 \(w_{-K},\ldots,w_{-1}\) 添入 \(b_0\)，
用球／波形的三角递推恰恢复 \(e_{-K},\ldots,e_{-1},b_0\) 的张成空间。
由于 \(F+QF\) 对投影Q不变，这正是该波形截止的最小Q约化包络。
它恢复原物理截止在 \(C_\infty\) 像上的有效有限空间。

这个事实只解释指定波形截止族与正象限Q相容时为什么补回原球方向；
不证明任意截止唯一，也不把有限径向包络与整个T交换混同。
真正与T交换的是包含整个Q空间的物理下截止 \(\mathsf P\)，其作用由(9)精确说明。

## 7. 受限源相容性仍不能唯一选出周期读出

425的波形截止 \(F_K\) 满足 \(F_K\to E_\infty\) 强收敛，且
\(A(h)=E_\infty A(h)E_\infty\)。若 \(A(h)\) 迹类，由(13)先知 \(h(0)=0\)，
再用波形压缩的迹范数收敛及425(31)，得到
\[
                   A(h)\in\mathcal S_1\Longrightarrow
                   \operatorname{Tr}A(h)=\Lambda(h)=0.       \tag{19}
\]
因此同一个 \(\mathcal D\) 上还有表达式无关的线性泛函
\[
                    \Psi_0(A(h)+S)=\operatorname{Tr}S.        \tag{20}
\]
它也连续于上述商拓扑、匹配普通迹，并满足对每个 \(R\in\mathcal M_Q\) 的循环相容性：
\([R,A(h)]\) 的普通迹为零，迹类部分亦如此。
它在纯周期轴测试上与 \(\widetilde\Lambda\) 不同。
所以保留普通迹、受限源乘子循环性和自然源交换子消失，并不足以唯一选定原周期读出。
本稿成功建立的是原物理截止来源的相容候选，而不是由这些公理唯一推出规范算术迹。

下一步要证明(16)的受限线性双模如何接入原边／角相对Chern链及算术主消失，并支付(20)揭示的读出选择问题。
若这一步无法成立，应给链层面的明确障碍；已有周期比较和源交换子零迹本身仍不能推出RR或RH。
