# 424. 相对链修补的精确抵消与四分量读出的必要性

2026-10-04。接续[423](423-f1-twisted-radial-readout-and-mixed-period-obstruction.md)。本稿固定422的实际函数域；结论涉及连续读出、Hochschild链和相对锥，不把这些链自动认作循环Chern类或算术主关系。

## 1. 约定与实际链的定义域

沿用422的理想 \(\mathcal I\subset\mathcal A\subset\mathcal M\)。取非零
\(\gamma=(r,s)\)，令
\[
 W=z_{-\gamma}\otimes1,\quad \sigma=\operatorname{Ad}W,
 \quad\alpha=\sigma^{-1},\quad
 \varphi(F)=\tau(FW),\quad
 \kappa(F)=\varphi(\sigma F)-\varphi(F).                       \tag{1}
\]
\(\varphi\) 在 \(\mathcal A\) 连续，且在 \(\mathcal I\) 等于实际插入迹。
乘子张量的准入条件是至少一条腿属于 \(\mathcal A\)，其余属于 \(\mathcal M\)；各乘积仍属于 \(\mathcal A\)。
这定义一个由乘子参与、边界保持的代数链空间；本文只需其中的有限张量，不声明额外的完备张量或循环同调定理。

标准扭曲Hochschild边界采用
\[
 b_\alpha(A\otimes B)=AB-\alpha(B)A,
\]
\[
 b_\alpha(A\otimes B\otimes C)
 =AB\otimes C-A\otimes BC+\alpha(C)A\otimes B.                 \tag{2}
\]
因此 \(b_\alpha^2=0\)。记
\[
 E(A,B)=\varphi(AB-\alpha(B)A),\qquad
 D(A,B)=\varphi(AB-B\sigma(A)).                               \tag{3}
\]
423给出的准确关系是
\[
 E(A,B)=D(A,B)+\kappa(\alpha(B)A).                            \tag{4}
\]
\(E=b_\alpha\varphi\) 是Hochschild闭余链。若一条腿属于 \(\mathcal I\)，
则 \(D=0\)，且(4)最后的乘积也在 \(\mathcal I\)，故 \(E=0\)。
因此 \(E\) 降至商的准入链；记作 \(\bar E\)。
\(D\) 一般不是同一个标准复形的闭余链，不能丢掉 \(\kappa\)。

## 2. 最直接的相对锥为何把全部周期一并抵消

令 \(q\) 是向 \(\mathcal M/\mathcal I\) 的商映射，保留上述至少一条 \(\mathcal A/\mathcal I\) 腿的条件。
采用相对锥
\[
 R_n=C_n(\mathcal A;\mathcal M)\oplus C_{n+1}(q),\quad
 \partial(x,y)=(b_\alpha x,qx-b_\alpha y).                    \tag{5}
\]
在底部取 \(R_{-1}=C_0(q)\)，故度零循环的条件准确是 \(qx=b_\alpha y\)。
在度零上，候选配对为
\[
                       \mathcal P(x,y)=\varphi(x)-\bar E(y).  \tag{6}
\]
任意准入的 \(z\in C_1\) 给相对循环
\((b_\alpha z,qz)=\partial(z,0)\)，并且
\[
                  \mathcal P(b_\alpha z,qz)=0.               \tag{7}
\]
这是准确的相对边界抵消，不只针对混合群标签。

原提升的测试 \(A=T^*, B=TK_h\) 中，\(B\in\mathcal A\)，所以
\(z_E=A\otimes B\) 准入。其裸 \(E\) 读出尽管在423产生错误混合原子，
补上商链 \(qz_E\) 后由(7)得到零；同一做法也把纯p、纯q及单位测试全部抵消。

对原来的 \(D\) 也有准确链，而不需要把它误认作 \(E\)：
\[
 z_D=A\otimes B-1\otimes B\sigma(A),
 \quad b_\alpha z_D=AB-B\sigma(A).                           \tag{8}
\]
因为 \(\alpha(B\sigma(A))=\alpha(B)A\)。于是
\(\bar E(qz_D)=D(A,B)\)，再次给(7)的零。
这种修补没有选择性恢复412的纯周期权重。

若固定商链 \(y=qz\)，另取具有相同商边界的提升 \(x=b_\alpha z+i\)，
\(i\in\mathcal I\)，则
\[
                         \mathcal P(x,y)=\operatorname{Tr}(iW). \tag{9}
\]
要得到原周期分布，必须由源构造一个规范的 \(i\) 及相应比较定理；
把目标原子分布倒填成 \(i\) 不构成证明。

## 3. 连续不变标量扩张在同一域中已经不可能

这个障碍比“扭曲迹不循环”更强：任意非零 \(\gamma\)，不存在连续线性
\(\Phi:\mathcal A\to\mathbb C\)，既在 \(\mathcal I\) 等于插入迹，
又满足 \(\Phi\circ\sigma=\Phi\)。

证明只用422的实际序列。固定时间秩一投影 \(P\)，在群标签 \(\gamma\) 上放
\[
 f_k(j,l)=H(j)\delta_k(l),\qquad F_k=f_k z_\gamma\otimes P.
\]
\(\|f_k\|_{E_2}=1\)，所以所有 \(F_k\) 在每个Fréchet半范数上有共同上界。
\(\sigma\)-不变也意味着 \(\alpha=\beta_\gamma\)-不变，而
\[
 \beta_{(r,s)}f_k=f_{k+s}+(H(j-r)-H(j))\delta_{k+s}(l).        \tag{10}
\]
余项属于开放 \(\ell^1\)，总和为 \(-r\)。于是
\[
                     \Phi(F_{k+s})-\Phi(F_k)=r.              \tag{11}
\]
若 \(r\ne0,s=0\)，立即矛盾；若 \(r\ne0,s\ne0\)，迭代(11)产生无界线性增长，
与连续性和上述有界族矛盾。若 \(r=0,s\ne0\)，交换坐标，用 \(\delta_k(j)H(l)\) 同样得到矛盾。
这排除了任意连续边界标量修正，而非只排除某一个系数选择。

同一负端消失条件还给 \(\mathcal A^\sigma=0\)：每个实际径向系数沿非零平移轨道不变时，
选择迭代方向使至少一坐标趋于负无穷，函数值必趋零，故原值为零。
Fourier系数唯一性给整个结论。乘子中的原酉元 \(u\) 可以固定；这不提供非零的代数内固定测试。
Cesàro平均也不能补救：\(\delta_{(0,0)}z_\gamma\otimes P\) 的平移平均点态、强趋于零，
但 \(p_0=\varphi=1\) 始终不变，故没有在原Fréchet拓扑内收敛。

## 4. 四分量是合法的相容读出，但不能压成不变标量

422已经实际构造
\[
 d(f)=(\lambda_{pq}(f),e_p(f),e_q(f),f_c)\in V=\mathbb C^4,
\]
\[
 S(a,b)(t,p,q,c)=(t-ap-bq+ab c,p-bc,q-ac,c).                  \tag{12}
\]
这是连续、平移相容的四分量读出；开放函数 \(r\) 被送到 \((\sum r)t_0\)，
所以它确实保留普通迹方向。这里用 \(t_0,p_0,q_0,c_0\) 表示四个基向量。
令
\[
 N_1p_0=-t_0,\ N_1c_0=-q_0,
 \quad N_2q_0=-t_0,\ N_2c_0=-p_0,
\]
其余基向量被相应 \(N_i\) 消灭，则
\[
 N_1^2=N_2^2=0,\quad N_1N_2=N_2N_1,\quad N_1N_2c_0=t_0,
 \quad S(a,b)=1+aN_1+bN_2+abN_1N_2.                          \tag{13}
\]
故平移复合律严格成立。另一方面
\[
 V_\Gamma=V/\langle(S(g)-1)V\rangle=\mathbb C[c_0];            \tag{14}
\]
普通迹及两条边在coinvariant中全部消失；不变标量泛函只能读 \(c\)。
短正合列 \(0\to\mathbb Ct_0\to V\to V/\mathbb Ct_0\to0\) 不分裂：
例如 \(p_0\) 在后一个商中固定，但其任何提升被 \(S(1,0)\) 改变 \(-t_0\)。

在这一四分量模型内，任意平移相容线性商 \(Q:V\to W\)，若 \(Q(t_0)\ne0\)，必为单射。
确实，对核向量依次施加 \(N_1N_2,N_1,N_2\)，先消去其 \(c_0,p_0,q_0\) 系数，再消去 \(t_0\) 系数。
因此保留普通迹方向至少需要四维；四维非半单模型本身可行。
更一般的连续有限维目标的四维下界，要求每个开放余项准确映为 \(Q(r)=(\sum r)t_W\) 的同一固定迹轴，其中 \(t_W\ne0\)，
并由连续性控制所用的有界轨道；其完整前提与证明见[独立推导](../reviews/2026-10-04/f1-four-component-relative-obstruction-derivation.md)。
不能将这些结论写成“任何有限维扩张都不可能”。

## 5. Hochschild闭性仍不是完整循环准入

由(1)–(4)直接计算
\[
 E(A,B)+E(\alpha(B),A)=\kappa(\alpha(AB)).                    \tag{15}
\]
所以裸 \(E\) 的Hochschild闭性不足以给标准扭曲循环余圈。
若 \(G\) 同时对余链各腿施加 \(\sigma\)，则
\[
 (G-1)E=b_\alpha\kappa,\quad
 (G-1)\kappa(F)=2rs\operatorname{Tr}_t(F_\gamma)_c,
 \quad (G-1)^3\varphi=0.                                    \tag{16}
\]
完整异常形成边与角点的非半单链，不是一个可忽略的常数。
包含不变性缺陷的余链锥取 \(d(x,y)=(b_\alpha x,(G-1)x-b_\alpha y)\)，
则 \(d\varphi=(E,\kappa)\)，\(d(E,\kappa)=0\)。它在全域上由 \(\varphi\) 给出边界；
不能据此宣布已构造主消失的循环Chern角色。
[Ponge的para-S复形研究](https://arxiv.org/abs/1810.04835)可作为一般复形技术的背景；
本稿的实际恒等式由上式直接证明，未调用该文替本项目完成循环准入。

## 6. 原源的加权角点链并未自动闭合

角点上径向 \(\alpha\) 为恒等。原单位酉元 \(u\) 和时间测试 \(k\) 给
\[
                  b(u^*\otimes uk)=k-uku^*.                 \tag{17}
\]
这个边界一般非零，并有允许测试的秩一见证。取圆周 \(\mathbb R/L\mathbb Z\) 上实值光滑小支集函数 \(\psi\)，
使其支集与M旋转后不交，令 \(d(t)=c(t)\psi([t])\)。选择紧支光滑 \(h\)，在
\(\operatorname{supp}d-\operatorname{supp}d\) 上恒为1，则
\(k=M_dU(h)M_d=|d\rangle\langle d|\)。
在角点字符参数 \(\zeta=(1,1)\) 的时间表示中，原Green分割给 \(ed=d\)，
\(ud=c(t)\psi([t-M])\)，故 \(ud\perp d\)，且均非零。
单个实际字符评价的非零已足以证明原角点边界非零。
于是(17)非零。裸加权链并不是角点的Hochschild循环。

自然对称修补虽然闭合，却满足
\[
 z_{\rm sym}=u^*\otimes uk-ku^*\otimes u
           =1\otimes k-b(u^*\otimes u\otimes k).             \tag{18}
\]
其Hochschild类只见单位测试链，与源酉元无关。原提升亦有准确式
\[
 Z_{\rm sym}=T^*\otimes TK-\alpha(K)T^*\otimes T
            =(T^*T)\otimes K-b_\alpha(T^*\otimes T\otimes K). \tag{19}
\]
这给链恒等式，仍不宣称 \(Z_{\rm sym}\) 在全匹配边界上闭合。
事实上p边商 \(T_p=1-He+HvH\) 中 \(eH=He\)、\(HvH=vH\)，故
\[
               T_p^*T_p=1,\qquad T_pT_p^*=1-\delta_{k=0}e.   \tag{20}
\]
原酉角点的提升在两边匹配商并非酉元；真实Green端点缺陷必须进入边／角Chern数据。
这些见证及定义域的完整推导见[相对链报告](../reviews/2026-10-04/f1-relative-chain-derivation.md)。

## 7. 后续比较对象

指定标量修补及最直接的相对锥已经收束。下一步必须保留源提供的规范提升或非标量边／角数据。
[425](425-f1-recentered-geometric-corner-and-source-period-finite-part.md)研究一个不同的实际候选：
从412–414的几何壳层选出正角通道，证明固定算子及其截断有限部直接比较原纯周期分布。
它改变了径向极限域，需要单独证明；不由本稿的零相对边界或旧域的强极限自动推出。

本稿未证明全局主关系、包含实位的Weil比较、RR、正性或RH。连续标量障碍与相对抵消只是明确限定候选的结论。
