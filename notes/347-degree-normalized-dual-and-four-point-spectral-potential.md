# 347. 度归一化对偶与四点非线性谱势

2026-09-08。周期10第1–2动作的自含有限结论。[T]。
Gibbs只读[独立复核通过](../reviews/2026-09-08/347-independent-review.md)。
这是有限谱传递准备；尚无新的实际零点比例。
不宣称经典凸对偶或归一化邻接矩阵首次出现；本篇固定其在当前截断谱余项中的准确组合。

## 1. 准确的谱对偶

沿用304、305及Devine式(5)的同一个函数
\[
 \Psi(x)=\begin{cases}(x-1)^2,&0\le x\le2,\\2x-3,&x\ge2.\end{cases}
\]
对任意n阶Hermitian G>=0，
\[
 \boxed{\operatorname{tr}\Psi(G)=
 \max_{\substack{C=C^*\\-I\preceq C\preceq I}}
 \{2\operatorname{tr}C(G-I)-\operatorname{tr}C^2\}.}              \tag{1}
\]
证明：在G的特征基上，C_ii∈[-1,1]且tr C²>=sum_i C_ii²，
目标至多sum_i max_(|c|<=1){2c(lambda_i-1)-c²}=sum_i Psi(lambda_i)。
取同一特征基上的C_ii=min(1,max(-1,lambda_i-1))即达等号。
这不要求Psi算子凸，也没有将不交换矩阵逐元素代入标量不等式。

## 2. 一个始终可用且给非负局部势的试探矩阵

现在设G为相关矩阵：G>=0、G_ii=1。任选无自环的无向有限图E，
置A_ij=G_ij当{i,j}∈E，否则为0，特别A_ii=0。定义
\[
 d_i=\max\left(1,\sum_j|A_{ij}|\right),\quad
 D=\operatorname{diag}(d_i),\quad C=D^{-1/2}AD^{-1/2}.
\]
对任意z，由2uv<=u²+v²，
\[
 |z^*Cz|\le\sum_{i,j}|A_{ij}|
 {|z_i|\over\sqrt{d_i}}{|z_j|\over\sqrt{d_j}}
 \le\sum_i{\sum_j|A_{ij}|\over d_i}|z_i|^2\le\|z\|^2.
\]
因此-I<=C<=I，这是一个已验证的算子界，没有新未证行和条件。
把C代入(1)，得到
\[
 \boxed{\operatorname{tr}\Psi(G)\ge
 \sum_{\substack{i,j\\\{i,j\}\in E}}
 |G_{ij}|^2\left({2\over\sqrt{d_i d_j}}-{1\over d_i d_j}\right).} \tag{2}
\]
右侧按有序(i,j)求和。di>=1使每个系数非负且至多1。
即使G有特征值超过2，(2)也成立；没有把tr Psi直接换成Frobenius能量。
图只含孤立配对时di=1，恢复2×2块的准确二次能量。

对多个相关矩阵G_j和theta_j>=0、sum theta_j=1，
逐个构造C_j并加权(2)即可。各矩阵可不交换；
先平均G再取Psi一般是另一较弱量，不与本式相等。

## 3. 相邻边图产生明确的四点势

令x_1<=...<=x_n为实节点，允许重合以覆盖闭合几何；
取归一化正定核k_j(x)=integral p_j(t)exp(ixt)dt，
p_j>=0、integral p_j=1，并令(G_j)_ab=k_j(x_a-x_b)。
每个G_j均为相关矩阵，|k_j|<=1。
图只保留相邻边{a,a+1}。

写gap g_i=x_(i+1)-x_i>=0。对三个连续gap u,v,w，定义
\[
 d_j(u,v)=\max(1,|k_j(u)|+|k_j(v)|),
\]
\[
 \mathcal V(u,v,w)=
 2\sum_j\theta_j |k_j(v)|^2
 \left\{{2\over\sqrt{d_j(u,v)d_j(v,w)}}
              -{1\over d_j(u,v)d_j(v,w)}\right\}\ge0.             \tag{3}
\]
这是四点势，不是单个pair的固定权；两端度由相邻两条边共同决定。
对内部边i=2,...,n-2，(2)中对应无序边的贡献正好是
V(g_(i-1),g_i,g_(i+1))；端边贡献非负可丢弃。因此
\[
 \boxed{\sum_j\theta_j\operatorname{tr}\Psi(G_j)\ge
            \sum_{i=2}^{n-2}\mathcal V(g_{i-1},g_i,g_{i+1}).}     \tag{4}
\]
没有重复累计同一矩阵谱余项；n<=3时右侧为空和。
所有di∈[1,2]，但直接用最坏度2会损失间距几何，
后续应保留(3)的真实度，不能先丢失它再宣称使用了联合窗口结构。

## 4. 一个有明确计数方向的平稳证书接口

若能找到alpha>=0、eta>=0及有界实函数h(u,v)，使所有u,v,w>=0满足
\[
 \mathcal V(u,v,w)+{\eta\over2\pi}v
                 +h(v,w)-h(u,v)\ge\alpha,                       \tag{5}
\]
则对任意n>=1及任意节点构型，由(4)和望远镜求和，
\[
 \sum_j\theta_j\operatorname{tr}\Psi(G_j)
 \ge\alpha n-{\eta\over2\pi}(x_n-x_1)-C,\qquad
 C=3\alpha+2\|h\|_\infty.                                       \tag{6}
\]
对n>=4有n-3个内部边，内部gap和不大于全跨度；
n<=3时右侧<=0，仍被Psi>=0覆盖。
没有假定gap上界；若h无界，(6)的统一端点常数不能直接保留。

这里(5)是真正还要建立的非平凡输入，不因局部势已经写出而自动成立。
若另有同一实际对象的计数与Gram传递
\[
 s\ge P_{\rm mix}N+\sum_j\theta_j\operatorname{tr}\Psi(G_j)+o(N),
 \quad (x_s-x_1)/(2\pi)\le N+o(N),
\]
这里须为同一组n=s>=1节点及同阶s×s矩阵，窗口、权重和证书参数固定。
若(6)可合法应用于那些实际Gram或通过固定块极限传递，
那么在alpha<1时才得到候选后果
\[
 \liminf{s\over N}\ge{P_{\rm mix}-\eta\over1-\alpha}.              \tag{7}
\]
后续[351](351-fixed-radius-stability-and-actual-zero-transfer.md)已经独立复核：
对固定半径及有限组实偶L²概率密度，实际全链传递和完整重数账本成立，
逐边L¹误差避免了额外增长矩阵逼近假设；(5)的全域证书仍须证明。
超出上述窗口／固定半径条件时，不能默认同一实际传递。
若逐个固定长度b的块应用(6)，端点总损失为C ceil(s/b)，不是单个C。
只有在全体块合计的传递误差已证明时，才先得到
(1-alpha+C/b)s>=(P_mix-eta)N-C+o_b(N)。
恢复(7)须先对每个固定b令N趋于无穷，再令b趋于无穷，
或另证累计端点损失为o(N)，不能默认一个固定b已无端点成本。
单独证明(1)–(6)不满足GOAL的较远期验收。

## 5. 与现有来源的关系及下一实验

Devine v1.0.3第7–8页提醒pair平方能量通常位于tr Psi之上，
其平稳传递还调用分支保护；本篇没有复用尚未重建的保护／续接证书。
(2)通过一个始终有界的试探矩阵直接给下界，因而避免预设谱留在二次支内。
代价是得到间距依赖的四点势，而非原来固定系数的pair和。

下一步选明确可用窗口，计算(3)与基线损失，针对(5)做有界势函数的
联合寻优和反例搜索；若没有足够净值，就记下量化失败范围。
只做更多单窗三点或把(5)作为新未证预算保留而不求解，都不能算完成本周期。
