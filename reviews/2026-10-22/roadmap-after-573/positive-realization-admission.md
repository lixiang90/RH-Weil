# 独立准入：Rosati 的混合系数、determinant 的盲区与 tensor 极点预算

2026-10-22；独占审查稿。输入为563、565、567、290与573结算，不改STATE／cadence。
这是已付模型的精确再检验和路线选择证据，**不另立574，不申报经典ζ新正性**。

## 1. 函数域最值得保留的较短箭头

曲线 C 的 Jacobian J 连同一个实际 ample line bundle L，先给
λ_L:J→J∨、Rosati 对合 α†=λ_L⁻¹α∨λ_L。这里“对合存在”与“对合为正”是两件事。
后者来自同一个 L 的混合交数：

\[
 \operatorname{Tr}(\alpha\alpha^\dagger)
 =\frac{2g}{(D^g)}(D^{g-1}\cdot\alpha^*D)>0
 \qquad(\alpha\ne0).                                      \tag{1}
\]

这不是从 Frobenius 根定义正内积。实际几何的 ample/effective 相交支付符号；
Frobenius 的 π†π=q 与完整点数／迹公式再把它接到纯性和全混合 Weil 型。
原件核 [Milne《Abelian Varieties》Thm17.3及证明，pp35–36](https://www.jmilne.org/math/xnotes/AVs.pdf)。
该篇是作者1986年原书章节的校订稿；这里只归属其公式和几何来源，下面反测为本稿直接运算。

与567的 C×C/RR 路线相比，这条路可以不先复制全部 surface RR；
但它仍要求实际极化、pullback 和 mixed intersection，不能只给一个 determinant line。
π†π=q 是局部动力对偶，(1)才是独立正号。二者必须在同一对象／同一迹上相遇。

“Rosati trace”不能随便换成某个正重数的 regular representation trace。
这里 Tr 是给定 cohomological/Tate realization 的 trace，且必须证明它与点数中的 trace 相同。
相邻次数的超迹消去、任意添加副本和 quotient 丢重数都须另核；565已经给非识别模型。

## 2. 一个已执行的明确反测：所有 polynomial determinant 非负仍不足

使用563／567已经支付正 primitive、全部 Π 和 Mellin 自对偶的连续族

\[
 Z_c(s)=1+\frac{c}{s(s-1)},\qquad 0<c\le\tfrac12,
 \quad d=c-\tfrac14,
 \quad C_d=\begin{pmatrix}0&1\\-d&0\end{pmatrix}.           \tag{2}
\]

其完整源 W_c(u)=Tr(exp(uC_d))，由原始源／ODE唯一性取得，不用零点选择。
在 \(\mathcal E_d=\mathbb R[C_d]\) 上取 †:C_d↦−C_d，标量不变。
因为 C_d²=−dI，这是一个明确的代数对合，且 exp(uC_d)†exp(uC_d)=I。
它也等于二维标准非退化交替配对的 adjoint。

现在用**同一个真实 g-distribution 的二次幂** \(\widetilde Z_c=Z_c^2\)：
primitive 与 Π 各变两倍，M 是两个正计数测度的乘法卷积，故正性保持；
完成化仍为已指定的 Γ=0、极点0与1各二重，完整源是 \(\widetilde W_c=2W_c\)。
实际四维生成元为 \(\widetilde C_d=C_d\oplus C_d\)，对合分块作用。
每个实多项式 p 都有 p(C_d)=aI+bC_d，故**全多项式**身份为

\[
 \det p(\widetilde C_d)=(a^2+db^2)^2\ge0,                \tag{3}
\]
\[
 \operatorname{Tr}\bigl(p(\widetilde C_d)
                 p(\widetilde C_d)^\dagger\bigr)
       =4(a^2+db^2).                                    \tag{4}
\]

取 c=3/16，即 d=−1/16；令 p(X)=X，(4)精确为 **−1/4**。
取正控制 c=5/16，即 d=1/16，同一值为 **+1/4**，而所有 a,b 的(4)均非负。
两段都通过(3)和非退化双对偶。故“真实正 g-distribution＋对偶＋全部 polynomial
determinant/degree 非负”仍不能代替 mixed Rosati 正性。

(3)只是一个 degree-like 代数函数，不宣称已构造 abelian variety、实际 isogeny degree
或某个 scheme 的有效截面。反例反驳的是仅凭该数值包的推理；真实几何还有(1)。
它也不排 determinant **所有混合系数**具有独立几何来源的更强构造。

实际执行用 Python Fraction 验证 C_d²、分块 trace 和下节 F5 恒等式，输出为：

```text
d=-1/16: C^2=I/16, doubled Tr(C†C)=-1/4
d= 1/16: C^2=-I/16, doubled Tr(C†C)=1/4
F5: A†=[[-3,5],[-1,0]]=5 A^{-1}
F5: Tr((aI+bA)†(aI+bA))=2a^2-6ab+10b^2
F5: Rosati Gram determinant=11
```

这些是有理恒等式，脚本只是逐式核算，不靠有限采样推出全多项式量词。
全量词由 p(C)=aI+bC 和(3)–(4)的代数归约支付。

### 为什么 determinant line 的末项与所需容量不是一回事

有限维中

\[
 \det(I+tB B^\dagger)=1+t\operatorname{Tr}(B B^\dagger)+O(t^2).
                                                               \tag{5}
\]

(3)控制的是另一个多项式的最高／常数项符号；(1)要支付(5)的混合一次系数。
即使 determinant 作为函数在某一区间为正，也没有自动推出这个导数为正。
上述负例 B=\(\widetilde C_{-1/16}\) 给
\(\det(I+tBB^\dagger)=(1-t/16)^4\ge0\)，而在0的导数仍为−1/4。
因此一个正的行列式标量或末项不能替代极化的 first variation。
这与568后“非零行列式＋有限位整除＋无穷位上界”的必要区分一致：
那组量可以付非消失／容量约束，不自动给所有 signed source 的 primitive 二次型。

## 3. 函数域正控制：同一 trace 的全混合二次式

563已经从 E/F5:y²=x³+x+1 的点数、有理性和精确递推支付

\[
 A=\begin{pmatrix}0&-5\\1&-3\end{pmatrix},\quad
 H=\begin{pmatrix}1&-3/2\\-3/2&5\end{pmatrix}>0,
 \quad A^THA=5H.                                       \tag{6}
\]

本次不重报该证书为新证明，只核它与(3)–(5)的具体区分力。
在 \(\mathbb R[A]\) 上，†=H⁻¹(·)ᵀH，因 A²+3A+5I=0，
A†=5A⁻¹=−3I−A。于是

\[
 \operatorname{Tr}\bigl((aI+bA)(aI+bA)^\dagger\bigr)
 =2a^2-6ab+10b^2,
 \qquad\det\begin{pmatrix}2&-3\\-3&10\end{pmatrix}=11>0.  \tag{7}
\]

这是全部 signed polynomial combinations 的二次式，不是只核 A 或几个有效对应。
该二维商中的 polynomial 正性通过(6)／(7)付清；全周期和全部复杂 compact 源仍消费
563的完整 trace recurrence 与 periodization 身份，不能只由有限次数采样外推。
一般曲线则由(1)及完整 Frobenius trace 把同一责任付清。

## 4. 对 root 建议的 tensor 首测：可执行，但独立性必须定位

这条路线值得在新路线图上排到高于“继续制造相对设施”的位置，理由是它直接检查
函数域证明中另一种独立容量来源：全 tensor 阶对象的 global pole budget。
但567§6已经恢复机制，下面只做可推翻候选的 source0 测试，不把机制重述当新输入。

对连续族，令 k≥1，r=1/4，负段 W(u)=2cosh(ru)。在 Re z>2kr，直接展开为

\[
 T_k(z):=\int_0^\infty e^{-zu}W(u)^{2k}\,du
 =\sum_{j=0}^{2k}\binom{2k}{j}\frac1{z-(2k-2j)r}.          \tag{8}
\]

所有 residues 为正，最右极点是2kr，不能被余项抵消；直接换元与有限展开即可证明。
正段 W(u)=2cos(τu) 的同一式把 r 换成 iτ，所以所有极点的实部为0。
两段的 W(u)^(2k) 都逐点非负；“全 even tensor 系数正”没有区分力。
若能从**独立对象**给 \(\sup\Re\operatorname{Pole}(T_k)\le B\)，B不依赖k，
则(8)确实排除负段。若这条 B 只是从未知纯性读出，它仍是等价责任。

在这个二模有限指数类，直接 T_k 的统一极点上界实质上就是指数增长率≤0；
它没有生成新的算术输入。c=1/4的非平凡 nilpotent companion 与零生成元具有相同
W=2以及全部 T_k，故这类 trace/tensor 测试仍不证明原实现半单或正定可酉化。

函数域 \(W_C=L\sum a_n\delta_{nL}\) 作为分布一般**不能直接取点wise幂**。
应先用已付全递推／同源对象识别 a_n=Tr(U^n)，再用

\[
 a_n^{2k}=\operatorname{Tr}((U^{\otimes 2k})^n),\qquad
 \exp\sum_{n\ge1}\frac{a_n^{2k}z^n}{n}
   =\det(I-zU^{\otimes2k})^{-1}.                           \tag{9}
\]

(9)是**全局 H1 realization 的张量**；它不等同于 Deligne 原证明在基底各闭点
对 lisse sheaf 构造的 local tensor Euler product。两者的几何次数、global poles
和误差责任必须分别注明。290的 fake positive integer Euler 系统也有形式外代数和
Poincaré 配对，不能因能写(9)就把 Deligne 的 global pole 定理转给它。

## 5. 实际准入表与停止条件

| 候选新输入 | 本次可立即核的门 | 已有测试的结论 | 允许继续的独立证据 |
|---|---|---|---|
| 只有 determinant line、非零 minor、正 degree scalar | 要求给 signed p 的 mixed first variation (5) | 连续平方反例通过所有det符号但失败trace；停止仅末项推理 | 同一几何 metric/ample pullback 实际产生(1)式的混合系数 |
| Rosati-like 对合＋π†π=q | 必须从源给实际 Tr(αα†) 的符号来源，覆盖所有 signed α | 连续正反例均有双对偶，负例(4)失败 | 独立有效交数／实际正闭形式及完整同源 trace身份 |
| 全 even tensor coefficient 正 | 执行(8)，核是否真的有k-independent pole budget | 正反两段全部even powers≥0；负段极点线性漂移 | 实际 tensor family 的 cohomological pole theorem／monodromy bounds |
| 给未知H、未知混合capacity或未知pole budget命名 | 对照563／565／567的等价接口 | 不构成新输入，source0立即停 | 明确原域对象、来源定理及可执行正反测试，不能只换记号 |

建议根路线排序：

1. 先审 **独立全tensor global pole budget** 的对象来源；一次章节定位门足够，若没有同源
   tensor object 或所用 pole bound 已等价于目标纯性，立即停，不换几篇paper串联。
2. 并列保留 **Rosati mixed first variation／实际 ample pullback** 路线；优先寻找能实际作用于
   physical sources、消405全principal并保537非根的对象。不能把未知positive Hilbert标签当对象。
3. 573的相对pair保电荷只作为准确设施：它未给(1)、(5)的符号，也未给tensor family；
   不用“有异常／有regulator”替代正容量来源。

两条路若都只剩未知正性／未知pole budget，应把当前实际结论写成准入失败，回到宏观选择；
不增加toy参数，不把本source0审查升级为全ζ数学进展。

## 6. 根消费所需范围

本稿全部精确模型身份定义在有限矩阵代数或连续完整源的 Cc∞ 测试上；
没有构造 physical r=e^(u/2)f 到 Jacobian／全局截面／tensor sheaf 的映射。
没有付成长窗 du/Dlog 到几何范数的运输，也没有经典 Γ/contact、素数幂、双pole 的新比较身份。
连续平方操作已经保留该模型自己的完整二重pole；它不是经典ζ的Γ模型。
实际ζ最强旧542+555→557 whole leading4/5的负惯性上预算、core/coupling/Ξ均不变。
这份检验改变的是：单 determinant/duality 的入口有明确反测，tensor入口应在**独立对象与pole定理**
处验收；没有移除经典正性瓶颈，不完成G20261014。
