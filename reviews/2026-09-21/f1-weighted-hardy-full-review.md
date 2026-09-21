# 第421稿全文独立逆审

2026-09-21。完整[raw](f1-weighted-hardy-full-review.raw.json)；原十一节及(1)–(21)通过，建议补明§10的半迹归一化。

**421 全文独立逆审通过。**已覆盖十一节及公式 **(1)–(21)**，未发现必修数学错误或实质条件遗漏。第7–8节的 BV 正则化、真实近锐源极限及第9节的原子障碍均成立。另有一项 **P3 归一化措辞建议**，见第10项，不影响现有证明和公式。

实际读取：[421 主稿](H:/codex-build/RH/RH-Weil/notes/421-f1-weighted-hardy-trace-and-atomic-obstruction.md)，15755字节。[审稿快照](H:/codex-build/RH/archive/f1-421-save/reviewed-draft.md)同为15755字节，与主稿逐字一致。

```text
读前 SHA256：
cdc466cbb1ee8b280c742eb79ee1fe184e280e9d39761303d165e6e6dd642ee0

读后 SHA256：
cdc466cbb1ee8b280c742eb79ee1fe184e280e9d39761303d165e6e6dd642ee0

快照 SHA256：
cdc466cbb1ee8b280c742eb79ee1fe184e280e9d39761303d165e6e6dd642ee0
```

以下核验直接从实际源、算子块及核公式展开，未以其他代理的推导结论作为正确性依据。

1. **第1节，第7–36行，(1)–(3)：Banach 星代数、缺陷定义与权重界正确。**

   由
   \[
   [P,ab]=[P,a]b+a[P,b]
   \]
   得
   \[
   \|ab\|_{\mathcal A_2}
   \le \|a\|\|b\|
      +\|[P,a]\|_2\|b\|
      +\|a\|\|[P,b]\|_2
   \le\|a\|_{\mathcal A_2}\|b\|_{\mathcal A_2}.
   \]
   伴随满足 \([P,a^*]=-[P,a]^*\)，故等距；单位属于该代数。若序列在此范数下 Cauchy，算子范数极限与交换子的 HS 极限通过算子范数连续性相容，确实得到完备性。

   插入 \(1=P+Q\) 给出
   \[
   T(ab)-T(a)T(b)=PaQbP.
   \]
   两个非对角块均为 HS，故缺陷为迹类，且连续双线性。

   对权重估计，
   \[
   |\Psi_W(a,b)|
   \le\|W\|(x_a y_b+x_b y_a)
   \le\|W\|
      \sqrt{x_a^2+y_a^2}\sqrt{x_b^2+y_b^2}.
   \]
   因而(3)无需额外系数 \(2\)。反对称性和归一化
   \(\Psi_W(1,a)=0\) 也成立。

   \(U(h)\) 在正频率空间上是乘以 \(\widehat h\)，所以
   \(\|W_h\|\le\|h\|_1\)。实际 \(u_\zeta\) 的有限相位展开和420的 HS 估计保证它是光滑的 \(\mathcal A_2\) 值族。

2. **第2节，第38–56行，(4)–(5)：Hochschild 三项边界的次序和符号正确。**

   直接展开乘法缺陷得
   \[
   D(ab,c)-D(a,bc)=T(a)D(b,c)-D(a,b)T(c).
   \]
   对反对称缺陷的六项按三个循环排列分组，得到
   \[
   b\Psi_W
   =\operatorname{Tr}W\bigl(
   [T(a),D(b,c)]+[T(b),D(c,a)]+[T(c),D(a,b)]
   \bigr).
   \]
   三个交换子均为迹类，因为各 \(D\) 迹类、各 \(T\) 有界。

   此时才能合法使用
   \[
   \operatorname{Tr}\bigl(W[T,D]\bigr)
   =\operatorname{Tr}\bigl([W,T]D\bigr),
   \]
   得到(5)第二行。正文没有拆出一般不具备迹的
   \(T(ab)\) 后分别求迹。

   因而标量权重确实给循环 \(1\)-余圈；任意时间测试权重则不能直接继承闭性。

3. **第3节，第58–81行，(6)：完整 \(\mathcal A_2\) 上“闭性当且仅当标量”的量词正确。**

   取块对角的 \(a=A\oplus0\)，以及
   \[
   b=|x\rangle\langle y|,\qquad
   c=|y\rangle\langle z|,
   \quad y\in H_-,\quad \|y\|=1,
   \]
   有
   \[
   T(a)=A,\qquad
   D(b,c)=|x\rangle\langle z|,\qquad
   D(c,a)=D(a,b)=0.
   \]
   因此
   \[
   (b\Psi_W)(a,b,c)=\langle z,[W,A]x\rangle.
   \]
   若对完整代数上的全部三元组均为零，则 \(W\) 与所有
   \(A\in B(H_+)\) 交换，故为标量。反向由(5)成立。

   有限秩见证也正确：
   \[
   a=|x_0\rangle\langle x_1|,\quad
   b=|x_1\rangle\langle y|,\quad
   c=|y\rangle\langle x_0|
   \]
   给出的边界正是
   \[
   \langle x_0,Wx_0\rangle-\langle x_1,Wx_1\rangle.
   \]
   对所选实偶、非负且积分为一的 \(h\)，可在低正频区间使
   \(\widehat h\) 接近一，在高正频区间使其接近零，从而得到至少 \(3/4\) 的差。向量可选为 Fourier 变换光滑紧支的单位向量，故这些是实际 Hilbert 空间中的有限秩算子。

   对任意非零 \(h\in C_c^\infty\)，若 \(W_h\) 为标量，则连续函数
   \(\widehat h\) 在正半轴恒定；整函数唯一性和 Riemann–Lebesgue 极限迫使 \(h=0\)，矛盾。因此每个非零此类 \(h\) 都使完整 \(\mathcal A_2\) 上的余链不闭。

   这不推出其在任意较小源子代数上的限制也不闭。稿件第81行的限定必须保留，当前表述正确。

4. **第4节，第83–124行，(7)–(11)：实际有限系数、全部交叉项和 Fourier 常数正确。**

   源分解
   \[
   u_\zeta
   =1+\sum_g\zeta^gM_{f_g}T_{a_g}
   \]
   中，\(b=0\) 的系数带负号，\(b=1\) 的系数带正号，符合
   \(u=1-e+v\)。

   独立恒等项因 \(P1Q=Q1P=0\) 不进入非对角块，但
   \(f_{(0,0)}=-c^2\) 仍须保留。正文正确区分了这两者。

   酉 Fourier 表示中的核为
   \[
   K_\zeta(\xi,\eta)
   =\frac1{2\pi}
     \sum_g\zeta^g\widehat f_g(\xi-\eta)e^{-ia_g\eta}.
   \]
   对
   \[
   B_\zeta=Pu_\zeta^*Qu_\zeta P-Pu_\zeta Qu_\zeta^*P,
   \]
   第一个正项对应 \(Qu_\zeta P\) 的 HS 平方，第二个对应
   \(Qu_\zeta^*P\) 的 HS 平方。因此其乘法配对密度恰为
   \[
   d_\zeta(\xi)
   =\int_{\eta<0}
   \bigl(|K_\zeta(\eta,\xi)|^2-|K_\zeta(\xi,\eta)|^2\bigr)\,d\eta.
   \]
   两项次序与 \(\Psi_h(u_\zeta^*,u_\zeta)\) 的符号一致。

   展开平方后，相位分别为
   \[
   \zeta^{h-g}e^{i(a_g-a_h)\xi},
   \qquad
   \zeta^{h-g}e^{i(a_g-a_h)\eta},
   \]
   故(11)正确，前因子为 \(1/(4\pi^2)\)。全部 \(g,h\) 交叉项都在式中，没有提前施加平均或删除混合标签。

   (10)由 HS 平方与有界乘法的合法迹配对得到，不依赖对任意迹类核作逐点对角限制。

5. **第5节，第126–146行，(12)–(13)：时间密度及 Haar 平均逐频率为零成立。**

   当 \(\xi\ge0,\eta<0\) 时，
   \(|\xi-\eta|=\xi+|\eta|\)。因此各 Schwartz Fourier 系数给出
   \(d_\zeta(\xi)\) 在正无穷处任意阶可积矩，且这些控制对参数一致。

   于是
   \[
   k_\zeta(s)=\int_0^\infty e^{-is\xi}d_\zeta(\xi)\,d\xi
   \]
   属于 \(C^\infty\cap C_0\)，各阶时间导数由相应矩控制。Fubini 给出(12)，没有多出 Fourier 归一化常数。

   Haar 平均使用角色正交性，只留下 \(g=h\)。此时所有时间相位消失，而实系数满足
   \[
   |\widehat f_g(-\omega)|^2=|\widehat f_g(\omega)|^2.
   \]
   每个留下的标签在固定 \(\xi\) 上已经相消，故
   \[
   \int_{\mathbb T^2}d_\zeta(\xi)\,d\zeta=0.
   \]
   进而得到全部测试函数上的平均读出为零。

   这是直接的频率核结论，不是由普通指数零推出来的带权结论；它也不宣称每个固定 \(\zeta\) 的读出单独为零。

6. **第6节，第148–170行，(14)：一般迹类算子的 \(C_0\) 系数和一致预算的分布限制正确。**

   对奇异值展开
   \[
   B=\sum_j s_j|v_j\rangle\langle w_j|,
   \]
   Cauchy–Schwarz 给
   \(\|v_j\overline{w_j}\|_1\le1\)，因此
   \[
   d_B=\sum_j s_jv_j\overline{w_j}
   \]
   在 \(L^1\) 中绝对收敛，且 \(\|d_B\|_1\le\|B\|_1\)。

   对任意有界频率乘法 \(m\)，先对有限秩和求迹再取迹范数极限，得到
   \[
   \operatorname{Tr}(M_mB)=\int m\,d_B.
   \]
   因而
   \[
   k_B(s)=\operatorname{Tr}(T_sB)
   =\int_0^\infty e^{-is\xi}d_B(\xi)\,d\xi\in C_0,
   \]
   并有(14)全部界。这里使用的是本模型时间表示的绝对连续频谱。

   参数平均的 Bochner 积分满足
   \[
   \left\|\int B_\zeta\,d\mu\right\|_1
   \le\int\|B_\zeta\|_1\,d|\mu|
   \le\sup_\zeta\|B_\zeta\|_1\,\|\mu\|_{\rm TV}.
   \]
   若总预算统一有界，任何分布极限继承
   \[
   |F(h)|\le C\|h\|_1.
   \]
   事实上它延拓为 \(L^1\) 上的有界泛函，因而有 \(L^\infty\) 密度，不能含目标非零原子。

   稿件没有声称此极限仍属于 \(C_0\)，也没有误用 \(C_0\) 的分布闭性。

7. **第7节，第172–208行，(15)–(17)：BV 密度界、\(L^2\) 正则化和实际双侧加权迹全部成立。**

   对紧支 BV 系数，变差取整个实轴上的变差，包含可能的端点跳跃。测度形式的分部积分给出
   \[
   |\widehat f_g(\omega)|
   \le\min\left(\|f_g\|_1,\frac{\operatorname{Var}f_g}{|\omega|}\right)
   \le\frac{\|f_g\|_1+\operatorname{Var}f_g}{1+|\omega|}.
   \]
   因而
   \[
   |K_\zeta(\xi,\eta)|
   \le\frac{A_f}{2\pi(1+|\xi-\eta|)}.
   \]

   对固定 \(\xi\ge0\)，
   \[
   \int_{-\infty}^0
      \frac{d\eta}{(1+\xi-\eta)^2}
   =\frac1{1+\xi}.
   \]
   两个平方项分别贡献 \(A_f^2/[4\pi^2(1+\xi)]\)，故
   \[
   |d_\zeta(\xi)|
   \le\frac{A_f^2}{2\pi^2(1+\xi)},\qquad
   \|d_\zeta\|_2\le\frac{A_f^2}{2\pi^2}.
   \]
   (15)的常数正确。

   将 \(d_\zeta\) 在负半轴延为零，Plancherel 与 Cauchy–Schwarz 给出
   \[
   \left|\int_0^\infty\widehat h\,d_\zeta\right|
   \le\sqrt{2\pi}\,\|h\|_2\|d_\zeta\|_2,
   \]
   即(16)。对应时间分布有 \(L^2\) 密度；这里不需要也不能从该界推出逐点连续性或定义 \(k(0)\)。

   对实际算子解释，需要分别控制两个非对角块，不能仅凭它们密度之差的界。前面的核估计确实给出
   \[
   \|Qu_\zeta PR_h\|_2^2,\
   \|Qu_\zeta^*PR_h\|_2^2
   \le
   \frac{A_f^2}{4\pi^2}
   \int_0^\infty\frac{|\widehat h(\xi)|}{1+\xi}\,d\xi<\infty.
   \]
   所以
   \[
   R_hB_\zeta R_h
   =(Qu_\zeta PR_h)^*(Qu_\zeta PR_h)
   -(Qu_\zeta^*PR_h)^*(Qu_\zeta^*PR_h)
   \]
   是实际迹类算子。再乘有界 \(V_h\) 后仍迹类，并由 HS 平方的乘法配对得到(17)。

   \(R_h,V_h\) 各自非线性不妨碍标量读出的线性，因为其合成精确等于
   \(\int\widehat h\,d_\zeta\)。平滑情形下 \(B_\zeta\) 本身迹类，合法循环又将(17)还原为(10)。正文没有错误地宣称一般 BV 情形的 \(W_hB_\zeta\) 必为迹类。

8. **第8节，第210–237行，(18)：真实近锐族及加权迹范数极限成立。**

   所给正弦／余弦过渡在重叠区平方相加为一，在中间平台只有一个非零平移，故 \(c_\varepsilon\) 满足原平方分割。端点平坦保证光滑拼接。

   其幅度为一，单调上升和下降各贡献一次变差，因此
   \[
   \|c_\varepsilon\|_\infty=1,\qquad
   \operatorname{Var}c_\varepsilon=2.
   \]
   支撑重叠要求 \(|nL+bM|\le L+\varepsilon_0\)，确实给出共同有限 \(F\)。乘积变差界给
   \[
   \operatorname{Var}
   \bigl(c_\varepsilon(\cdot)c_\varepsilon(\cdot-a_g)\bigr)
   \le 1\cdot2+1\cdot2=4.
   \]
   与共同支撑长度结合，(18)成立且不依赖 \(\varepsilon\)。

   系数的 \(L^1\) 收敛给 Fourier 系数逐点收敛。对每对有限标签先在负频变量使用共同平方核包络，再在正频变量使用
   \((1+\xi)^{-2}\) 的可积控制，可得
   \[
   \sup_\zeta
   \|d_{\zeta,\varepsilon}-d_{\zeta,0}\|_2\longrightarrow0.
   \]
   因此时间密度也在 \(L^2\) 中收敛，不会产生原子。

   算子层面，有限个系数乘法及其平移伴随均有界且几乎处处收敛，故
   \[
   u_{\zeta,\varepsilon}\to u_{\zeta,0},\qquad
   u_{\zeta,\varepsilon}^*\to u_{\zeta,0}^*
   \]
   分别强收敛。正是这两个强极限一起保证极限仍酉；单有酉算子的强收敛并不足够，而稿件没有遗漏伴随方向。

   对固定 \(h\)，加权核差的平方有可积控制
   \[
   C\,\frac{|\widehat h(\xi)|}{(1+\xi-\eta)^2},
   \qquad \xi\ge0,\ \eta<0.
   \]
   因而两个加权非对角块在 HS 范数中收敛。再用
   \[
   \|X_\varepsilon^*X_\varepsilon-X_0^*X_0\|_1
   \le(\|X_\varepsilon\|_2+\|X_0\|_2)
        \|X_\varepsilon-X_0\|_2
   \]
   得到所述实际算子的迹范数收敛。

   这一结论针对固定 \(h\)。它不自动提供变化测试函数上的一致误差，也不使极限 Hardy 压缩自动 Fredholm，更不自动继承420的指数束。正文对这些界限的表述正确。Haar 平均零值则可由一致 \(L^2\) 收敛传递，也可对实 BV 系数重新逐频率验证。

9. **第9节，第239–275行，(19)–(21)：孤立原子检验、尺度界和必要速率的条件正确。**

   不同素数保证 \(L/M\) 无理。可具体取
   \[
   \delta=\frac12\min\{L,\operatorname{dist}(L,M\mathbb Z)\}>0.
   \]
   则 \(-L\) 的该邻域避开零、其他 \(p\) 周期以及全部 \(q\) 周期。对
   \[
   h_\varepsilon(s)=\psi((s+L)/\varepsilon),\qquad
   0<\varepsilon<\delta,
   \]
   确有
   \[
   \mathcal P_{p,q}(h_\varepsilon)=L\rho_p,\quad
   \|h_\varepsilon\|_1=\varepsilon\|\psi\|_1,\quad
   \|h_\varepsilon\|_2=\sqrt\varepsilon\|\psi\|_2.
   \]

   固定迹类或总迹范数预算有界的机制，其值为 \(O(\varepsilon)\)；共同 BV 预算有界的机制，其值为 \(O(\sqrt\varepsilon)\)。这些界对全部 \(\zeta\) 成立，也覆盖第8节任意近锐参数及其极限。因此可以选择足够小的测试，排除整个固定预算候选类与目标分布的恒等。

   测试只命中 \(p\) 原子，所以把 \(q\) 项改成负号不影响这个见证。排除的是完整测试类上的相等，并不排除某个单独测试上的偶然相等。

   若额外满足
   \[
   |\text{候选}(h_\varepsilon)-L\rho_p|
   \le |L\rho_p|/2,
   \]
   则候选绝对值至少为 \(|L\rho_p|/2\)。分别代入(14)、(16)，恰得到(21)两个常数：
   \[
   \|B\|_1\ge
   \frac{|L\rho_p|}{2\varepsilon\|\psi\|_1},
   \]
   \[
   A_f^2\ge
   \frac{2\pi^2}{\sqrt{2\pi}}\,
   \frac{|L\rho_p|}{2\sqrt\varepsilon\|\psi\|_2}.
   \]
   第二式是对 \(A_f^2\) 的下界，等价于对 \(A_f\) 的
   \(\varepsilon^{-1/4}\) 级必要下界。

   第273–274行的误差条件至关重要：一般分布收敛只控制每个固定测试，并不自动控制随 \(\varepsilon\) 缩窄的测试。稿件没有偷换这两个量词。参数积分时，由总迹范数预算或 \(A_f^2\|\mu\|_{\rm TV}\) 支付相应下界，也正确。

10. **第10节，第277–287行：排除范围正确；一项 P3 归一化措辞建议。**

   原 \(A_N(h)\) 是在完整群求和与时间测试共同作用后得到的迹类算子。本文的固定 \(B\) 定理不能反过来把未经测试的群和认成有界或迹类算子。

   \(C_N^2\) 含径向非零有限秩投影张量非零时间乘法算子；在非原子 Lebesgue 空间上，该时间乘法算子非紧。因此它确实不满足固定迹类 \(B\) 的前提。这里没有用这一单项独自证明所有可能的相对机制不成立；完整排除依据仍是前面的范数界和原子测试。

   **P3 建议位置：第279行的“并有(19)”。**建议显式写出半迹归一化，避免被读成
   \(\operatorname{Tr}A_N(h)=\mathcal P_{p,q}(h)\)。最小替换为：
   \[
   \frac12\operatorname{Tr}A_N(h)
   =D_Nh(0)+\mathcal P_{p,q}(h),\qquad
   D_N=(2N_p+1)L+(2N_q+1)M.
   \]
   特别地，\(h(0)=0\) 时
   \(\mathcal P_{p,q}(h)=\tfrac12\operatorname{Tr}A_N(h)\)。

   第9节已经把(19)限定为原414的非零时间部分，因此这是一项归一化说明的编辑澄清，不是(19)–(21)的计算错误，也不改变原子障碍。

   本节保留了更奇异的相对正则化、不同全群传递及明确测试依赖的可能性，没有把本候选失败提升为 \(F_1\) 不存在性。

11. **第11节，第289–301行：来源、形式化和未完成范围准确。**

   本次只读核对了本地 Connes 固定 v1 的第16–18、22–24、28页文本。第16–18页讨论几何分布迹；第22页给带截止的局部迹公式，第23页明确称固定 \(R_\Lambda\) 为迹类；第28页也明确区分形式计算与尚需解决的算子论问题。因此稿件没有把所有外部截止一概描述成“仅经 \(h\) 平滑后才迹类”，这一来源限定有原文支持。

   已只读检查三个 Lean 定理及既有核验 JSON；源文件和审计文件的当前哈希与报告记录相符。三条内容确实仅涉及：
   - 乘法缺陷的结合律恒等式；
   - 反对称缺陷的三项代数边界；
   - 带权交换子的代数转移。

   它们没有形式化 Schatten 理想、迹的定义域、Fourier 常数、循环余圈闭性定理、BV 极限或原子比较。本次没有运行 Lean，也未将已有核验记录当作这些分析结论的认证。

   全文节号1–11完整，公式标签(1)–(21)依次各出现一次；数学交叉引用未发现错位，所有本地链接存在。第199行的“(15)的核估计”应结合其前面的 \(K_\zeta\) 上界理解，实际加权 HS 证明已在本报告第7项分别核准。

   主除子、两次数、RR、通常 \(\zeta\) 的正性及目标 \(F_1\) 结构非空仍开放。本文完成的是特定实际 Hardy 带权读出的构造、闭性障碍及其明确预算范围内的非原子限制。

**必要数学修改：无；建议补全上述一处半迹归一化措辞。**全程只读，未写文件，未运行 Git、Lean 或构建。
