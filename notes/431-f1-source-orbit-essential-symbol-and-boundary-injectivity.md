# 431. 源轨道的精确本质符号与加权边界单射性

2026-10-04。沿用[430](430-f1-source-stable-periodic-smoothing-algebra.md)的实际源稳定域。
本稿计算全部有限源矩阵的本质范数、迹类商与源作用，而非仅列一个抽象C*完成。
同一计算证明：域内任何非迹类元素的加权真源边界仍非紧，有限词不能把它修补成旧S₁链。

## 1. 有限源矩阵及严格正Gram

对有限J包含全部源指标，令
\[
 X_J=(u^jV)_{j\in J}:L^2(\mathbb R)\otimes\mathbb C^J\to\mathcal H,
 \qquad F_B=X_J B X_J^*,\quad B\in M_J(G_M).                \tag{1}
\]
任意430的有限和都能如此表示。X_J*X_J=M_GJ，
\[
 G_J(x)=[g_{k-j}(x)]_{j,k\in J},\qquad
 \Gamma_J(x)=[\gamma_{k-j}(x)]_{j,k\in J}.                  \tag{2}
\]
前者充分左端为零，充分右端准确等于后者；430(10)给Gamma_J>=I。
Gamma_J及其正平方根、逆平方根都是光滑M周期矩阵函数。
以下M_Gamma的乘法记号从简省略。

## 2. 半线模型的迹类比较

选R足够大，使G_J=Gamma_J于x>=R，令P=1_[R,infinity)。
X_J=X_J1_[a,infinity)。B有限传播且平滑，故
\[
 F_B-X_J P B P X_J^*\in\mathcal S_1.                       \tag{3}
\]
具体地，差项左或右含1_[a,R]；有限传播把另一变量也限制在一个紧区间。
先用光滑紧支chi覆盖这两个区间，chi B chi是光滑紧支核迹类，再乘半线的有界示性函数。
不能把裸半线乘法算子本身称为紧或迹类。

令
\[
 Y=X_J\Gamma_J^{-1/2}P,\qquad Y^*Y=P,
 \qquad H_B=\Gamma_J^{1/2}B\Gamma_J^{1/2}.                  \tag{4}
\]
H_B仍具有光滑、联合M周期、有限传播的矩阵核。(3)给
\[
                   F_B=Y P H_B P Y^*+\mathcal S_1.         \tag{5}
\]
Y是右半线上的真实等距嵌入，而非全空间上的形式逆。

## 3. 精确本质范数

由(5)有上界||F_B||ess<=||H_B||。
反向，取单位紧支光滑矩阵向量psi，使||H_B psi||逼近||H_B||；这类向量在L²稠密。
令psi_n(x)=psi(x-nM)。周期性使H_B与这些平移交换，
有限传播保证充分大n时psi_n、H_B psi_n都在P半线内。
Y psi_n是弱趋零的单位向量列，并且
\[
 \|Y P H_B P Y^*Y\psi_n\|=\|H_B\psi\|.                  \tag{6}
\]
任意紧扰动在该列上范数趋零，故
\[
 \boxed{\|F_B\|_{\rm ess}
       =\|\Gamma_J^{1/2}B\Gamma_J^{1/2}\|.}                \tag{7}
\]
这是原算子的实际本质范数，不声称任意多源F_B的全算子范数也等于右边。
Gamma_J可逆，因而
\[
 F_B\in\mathbb K\ \Longleftrightarrow\ B=0
 \ \Longleftrightarrow\ F_B\in\mathcal S_1.                \tag{8}
\]
不同表达式可先补零到共同有限J，所以(8)给每个商元素唯一的有限支持矩阵核B。
完整独立计算见[源轨道报告](../reviews/2026-10-04/f1-source-orbit-edge-derivation.md)。

## 4. 实际代数商及源作用

由430的乘积准入和(8)，D_src/S₁准确等于有限支持矩阵B_ij in G_M组成的代数，乘法为
\[
 (B\star C)_{i,l}
    =\sum_{j,k} B_{i,j} M_{\gamma_{k-j}} C_{k,l},
 \qquad (B^*)_{i,j}=(B_{j,i})^*.                            \tag{9}
\]
和为有限和；补零不改变实际商范数(7)。其结合性亦直接由有限矩阵BGammaCGammaD核准。
这里只使用每个有限Gamma_J，不能把可能无界的无限Gamma当作标准ell²矩阵。
例如1-alpha非零时，430(10)中的共同向量项可使||Gamma_J||随|J|增长。
所以尚不将完整源商冒称具有标准范数的普通无限矩阵代数。

真源左右作用分别移动行或列，Ad u精确地同时平移两个指标：
\[
               (\sigma B)_{i+1,j+1}=B_{i,j}.               \tag{10}
\]
这是真实u导出的商作用；原T作用为单位的旧商无法代表它。
本稿给了代数商、它的明确范数及其源动作；完整C*源商可取这些实际范数的完成，
但其与原最小源理想及规范几何层的同构仍需另证。

## 5. 加权边界在有限词商上单射

定义delta(F)=F-uFu*=[u*,uF]。在(9)中，它是B-sigma B。
若B=sigma B且B有限支持，则每条对角上的矩阵核沿全部整数平移相等；
有限支持迫所有核为零。因此
\[
 1-\operatorname{Ad}u:D_{\rm src}/\mathcal S_1
                        \longrightarrow D_{\rm src}/\mathcal S_1
                         \text{是单射}.                    \tag{11}
\]
特别
\[
 F\in D_{\rm src},\ F\notin\mathcal S_1
       \Longrightarrow F-uFu^*\text{非紧}.                 \tag{12}
\]
此式不要求h(0)或h(-M)非零，扩展了429的特定测试见证。
例如任意有限族h_m in C_c∞，
\[
 \sum_m u^m A(h_m)u^{-m}\in\mathbb K
                    \Longrightarrow\text{所有 }h_m=0,      \tag{13}
\]
因为对应矩阵只有B_mm=U(h_m)，Fourier单射迫h_m=0。
同样，有限个共轭加权边界之和若紧，其有限差分h_m-h_(m-1)全零，继而所有h_m全零。
这不排除完成后的无限支持固定点、无限转移或不同相对理想；不把有限词单射外推到它们。

## 6. 可完整计算的单角周期符号

J={0}时Gamma=2，所以
\[
 \|VBV^*\|_{\rm ess}=2\|B\|,
 \qquad \rho(B)=\tfrac12 q(VBV^*)                           \tag{14}
\]
是G_M到Calkin代数的等距星同态。乘法因子来自m的右端2，而不是任意归一化。
还能算出G_M自身的范数完成：
\[
 \overline{G_M}^{\|\cdot\|}
       \cong C(S^1)\otimes\mathbb K(L^2(0,M)).              \tag{15}
\]
证明可直接在胞元做离散Fourier：L²(R)分成ell²(Z) tensor L²(0,M)，
联合周期核产生Laurent矩阵，有限传播使只有有限个对角块。
各胞元块是光滑核的Hilbert–Schmidt紧算子，故Fourier后为有限Laurent多项式
sum_n exp(in theta)K_n，得到(15)的包含方向及一致范数。
反向对f,g in C_c∞(0,M)周期化|f><g|并把胞元错开n格，得到
exp(in theta)|f><g|。它有全局光滑的有限传播核；这些秩一与Laurent多项式
在右边稠密，完成反向包含。

这是(12)域内一个真实非交换子商的完整计算，不等同于所有源指标的商完成，
也不把胞元Fourier参数theta直接叫作原源u的谱参数。
周期胞元分解的一般背景可参见[Kuchment作者综述](https://www.math.lsu.edu/~shipman/courses/17A-7384/Kuchment2016.pdf)
第4节；此处的有限传播核、紧块和双向稠密性由上述计算独立支付。

## 7. 原最小源理想的商也严格非交换

设E是428的原范数完成，C=C*(1,u,E)，J是E在C中生成的最小闭理想。
J包含全部紧算子，所以可以取真实商J/K；这里不把J认作430的扩大域。
取非零实偶h in C_c∞，F=uA(h)、G=A(h)u*均在J中。
427的乘积式给
\[
 [F,G]=uA(h)^2u^*-A(h)^2
       =2\{uA(h*h)u^*-A(h*h)\}+\mathcal S_1.               \tag{16}
\]
(h*h)(0)=integral h(s)²ds>0；429的真实q=1对角块证明右边非紧。
因此J/K严格非交换。这个结论对每个原合法分割都成立，
不依赖特殊gamma_r是否恰为常数，也不只是解析扩大G_M的非交换性。
由此排除把真实源稳定商仍当成原标量C₀(R)的候选，但尚未给J/K完整分类。

## 8. 研究边界

本稿支付有限源商的符号、范数、源动作及非紧加权边界，而非完整Chern比较。
427的循环1余圈不能因新商非交换而被默认延伸；需要实际相对余链与新的相对理想准入。
物理周期读出尚未由本符号规范选择，下一步必须比较原球截止和源保持截止的差异。
实位、全素数Weil比较、算术主关系、RR及RH仍开放。
