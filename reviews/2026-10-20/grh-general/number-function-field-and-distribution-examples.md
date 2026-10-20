# 不止整数梳：数域、函数域、纯权与分布侧的区别

2026-10-20，root原件核查／推导。此稿给一般框架的成员和范围，不替这些对象证明新RH。
来源定理只在所列范围消费；构造谱算子的后验解释不充当独立正性证明。

## 1. 数域的自然 g-integers 是带理想标签的范数

令K为数域。将每个非零素理想p的范数Np当作一个带标签的g-prime，
即使两个素理想范数相同，也保留两个生成元。自由乘法生成的标签是非零整理想a，
推前到实数轴的正测度为

\[
 dP_K=\sum_{\mathfrak p}\delta_{N\mathfrak p},\qquad
 dN_K=\sum_{\mathfrak a\ne0}\delta_{N\mathfrak a},\qquad
 \zeta_K(s)=\sum_{\mathfrak a}(N\mathfrak a)^{-s}
 =\prod_{\mathfrak p}(1-(N\mathfrak p)^{-s})^{-1}.
\]

它是合法离散Beurling多重系统，不是普通单位整数梳。把同范数标签忘掉就会破坏Euler关系。
例如K=Q(i)的两个范数5素理想给dN_K在5的权2；范数3没有整理想，不能把每个正整数都赋权1。

固定Γ_R(s)=π^{-s/2}Γ(s/2)、Γ_C(s)=2(2π)^{-s}Γ(s)。若签名为(r1,r2)，
判别式为D_K，则

\[
 \Lambda_K(s)=|D_K|^{s/2}\Gamma_R(s)^{r_1}\Gamma_C(s)^{r_2}\zeta_K(s),
 \qquad \Lambda_K(s)=\Lambda_K(1-s).
\]

Λ_K仅在0、1有简单极点，s(s−1)Λ_K去极点后的零点才是这里的非平凡除子。
这一族的中心线RH一般仍是猜想；FE已知不等于C3已知。
源于Minkowski／adelic Fourier对偶的Gamma和理想类配对，亦不要求一维整数梳自Fourier。

已核原作者讲义：Sutherland，MIT18.785 Lecture19，Theorem19.12及Remark19.13，PDF pp.8–9，
[原文](https://math.mit.edu/classes/18.785/2019fa/LectureNotes19.pdf)；
Kedlaya CFT §2.3的Euler/ideal解释，
[原文](https://kskedlaya.org/cft/sec_zeta.html)。未重证其解析延拓或Tate全局理论。

## 2. 全局函数域：lattice的算术分布也能满足RH

对F_q上光滑射影几何连通曲线C，取每个闭点v为带标签g-prime，范数q^{deg v}。
g-integers是有效除子D的范数q^{deg D}，故支撑于q^n而非普通整数梳。
令g为曲线亏格，则

\[
 Z_C(T)=\prod_v(1-T^{\deg v})^{-1}
 =\frac{P_C(T)}{(1-T)(1-qT)},\qquad
 P_C(T)=\prod_{j=1}^{2g}(1-\alpha_jT).
\]

Weil RH给|α_j|=√q。放T=q^{-s}，若α_j=√q e^{iθ_j}，则全部非平凡零点为

\[
 s=\frac12+i\frac{\theta_j+2\pi k}{\log q},\qquad k\in\mathbb Z.
\]

因此nonlattice不是类RH的必要条件。此处的独立来源是几何纯性／正性，非频率无有理关系。
原始结论与曲线FE、次数正性证明见Milne原作者综述
[§0–1](https://jmilne.org/math/xnotes/pRH.pdf)，尤其pp.1–3、10。
Kedlaya的[Theorem1.2.2及Remark1.2.3](https://kskedlaya.org/weil-cohom/chapter-1.html)
也明确给全局函数域RH及q^{-s}周期。

### 全极点和自伴角谱不能遗漏

Z_C(q^{-s})的极点不仅是s=0,1两个点，而是
s=2πik/logq和1+2πik/logq的全部周期副本。有限极点缺陷要么在T圆周模型中解释，
要么完整清除(1−q^{-s})(1−q^{1−s})并调整显式公式；不能在整个s平面当作rank2缺陷。
可取整个自对偶分子

\[
 \Phi_C(s)=q^{g(s-1/2)}P_C(q^{-s}),\qquad\Phi_C(1-s)=\Phi_C(s).
\]

后验地以U=diag(e^{iθ_j})写P_C(q^{-s})=det(I−q^{1/2−s}U)，U为酉矩阵。
这比要求某个有限自伴D在实轴上一次性产生全部纵标更自然；有限矩阵只记相位mod2π。
若必须得到实线自伴模型，可取H=⊕_{j,k}C、D e_{j,k}=(θ_j+2πk)e_{j,k}/logq，
域为Σ|d_{j,k}|²|a_{j,k}|²<∞。它保留所有周期零点及重数；
普通det未定义，须用与Φ_C相同规范的canonical／正则化乘积。
仅从FE造出U不够：没有|α_j|=√q时U并不酉，旧290已给精确负基准。

## 3. 更高维的正确一般RH是分次纯性，未必一条中心线

对F_q上光滑射影d维簇V，有

\[
 Z_V(q^{-s})=\prod_{j=0}^{2d}\det(I-q^{-s}F_j)^{(-1)^{j+1}},
 \qquad |\alpha(F_j)|=q^{j/2}.
\]

Deligne纯性约束的是各H^j的权：奇数j的零点在Re s=j/2，偶数j的极点在相应权线，
还要保留可能的因子相消。整个Z_V不必只有一条零点线。
只有固定纯权分量、作正确twist／单位化，才回到单线／归一化特征值模为1。
按这些特征值后验构造的对角模型可酉；原始F_j的酉化另需半单性、正内积及相容性，
不能从Deligne纯性单独推出高维原始Frobenius半单或自伴实现。
各个det因子自身未必还具有非负primitive测度；这是额外的谱分次结构，不能从正Euler数据直接推出。
该公式和权结论核Milne同稿§2及Theorem5.1（PDF p.55）；本稿不将所有高维纯性重述为单线GRH。

## 4. 连续性必须分三侧回答

1. **算术侧P、Π、N。** 可以离散、绝对连续或混合。C025的Z_c正段给P>0连续，
   N=δ1+c(1−1/x)dx且有非空中心零点的严格例；因此一般类RH绝不强迫算术侧离散。
2. **完成整个函数的零除子。** 非恒零全纯函数在域内的零点局部有限、重数为正整数，
   所以其零点计数测度是纯点。这是复分析局部定理，不取决于P/N的连续性。
3. **任意自伴实现的谱测度。** 可有连续部分。但若该部分要逐点成为一个非零整个函数的零点，
   立即违反局部离散性。连续谱模型要改谈谱密度、谱位移、共振或相对行列式；
   branch cut／自然边界也不能自动叫“离线零点”或假定有离散Hadamard积。

将函数域正Euler模型与C025的正连续模型相乘，会把primitive测度相加、integer测度作乘法卷积；
若保两者各自完整completion和除子，则中心线性质按乘积稳定，得到带连续部分且有无限周期零谱的混合例。
这不是“纯连续且经典Gamma／TlogT”的分类，亦不宣称所有一般分布均有completion。

对用户当前问题最有用的区分是：**RH可约束一份连续算术分布的离散零谱；
“正自伴谱表示”若只有连续σ，则尚不是C4所写的整个函数零点行列式。**
