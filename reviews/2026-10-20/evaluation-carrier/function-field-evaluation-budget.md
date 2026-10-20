# 函数域评价载体检验：真实局部 jets 仍不是全局 Weil 容量

2026-10-20；评价行列式路线独立原稿。用户本轮明确优先本路线。
范围：从闭点分布独立构造实际有限评价载体，检验它与完整 Weil 源之间的映射责任。
本稿不改 STATE，不另计研究轮，不把 567 的 Gram、563 的证书或经典 RR 恢复计为新增定理。

## 1. 本轮可判对象与净后果

对每个整数截断 B，全部闭点数 b_d 确实足够构造一个有限 étale F_q 代数、
非退化的局部 trace 配对及一个正 Hilbert 点集载体。它们不依赖任何未知零点位置。
进一步可以构造形式局部 jets 和非退化 residue 配对。

新的具体反测是：这些真实局部设施在 567 的真曲线及 290 的正整数 Euler 反模型上均成立，
而两者的完整 primitive Weil 型符号不同。因而“能造非退化实际评价载体”与
“这个载体具有同源全局容量及完整 Weil 身份”是两个不同责任。
这里排除的是下面这个明确的闭点/局部-jet 直接构造，不是一般分析构造的不可行性。

## 2. 从分布无零点构造实际有限载体

给定 q 为素数幂，b_d∈Z_{≥0}，每个有限 d 的 b_d 有限。定义

\[
 R_B=\prod_{d=1}^{B}(\mathbb F_{q^d})^{b_d},\qquad
 M_B=\dim_{\mathbb F_q}R_B=\sum_{d\le B}d b_d. \tag{1}
\]

空因子略去；这是到同构为止确定的有限 étale 代数，不需要假设有全局曲线。
每个有限域是可分扩张，故

\[
 (x,y)\longmapsto\operatorname{Tr}_{R_B/\mathbb F_q}(xy) \tag{2}
\]

非退化。可分有限域 trace pairing 非退化，直积仍非退化；这不要求
Tr(1)=d 在 F_q 中非零。有限 étale 与 trace pairing 的准确关系见
[Stacks 00U3](https://stacks.math.columbia.edu/tag/00U3)、
[Stacks 0BJF](https://stacks.math.columbia.edu/tag/0BJF)。
所有点同时评价 R_B→∏k(v) 就是恒等映射，其矩阵在同一基下行列式为 1。
所以非零评价行列式确实可得，但这种自由评价不带任何全局高度/degree 约束。

令 X_B=Hom_{F_q}(R_B,\overline{F_q})。它有 M_B 个几何点，Frobenius
在每个度数 d 闭点之上是一个 d-cycle。定义另一个载体

\[
 \mathscr H_B=\mathbb C^{X_B},\quad
 \langle f,g\rangle=\sum_{x\in X_B}f(x)\overline{g(x)},\quad
 (V_Bf)(x)=f(\operatorname{Frob}^{-1}x). \tag{3}
\]

这是由有限集合的复线性化得到的正 Hilbert 空间，V_B 为置换酉算子。逐 cycle 得

\[
 \operatorname{Tr}(V_B^n)=N_{n,B}:=
 \sum_{\substack{d\mid n\\d\le B}}d b_d,
 \qquad N_{n,B}=N_n\quad(1\le n\le B). \tag{4}
\]

(2) 是有限特征双线性配对，(3) 是复点集上的计数内积；没有 F_q→C 的域嵌入，
它们不是经标量扩张得到的同一个 form。不能把两者合并成未经证明的几何极化。

### 2.1 可加 jets，但不能顺带取得全局 Frobenius/容量

对各闭点 v 指定一个形式参数 t_v 和长度 r_v≥1，令

\[
 J_{B,\boldsymbol r}=\prod_{v:\deg v\le B}k(v)[t_v]/(t_v^{r_v}),\quad
 \lambda_v(a)=\operatorname{Tr}_{k(v)/\mathbb F_q}
   [t_v^{r_v-1}]a. \tag{5}
\]

双线性配对 Σ_v λ_v(ab) 非退化：若 a 在某分量的最低非零项为 a_i t^i，
取 b=b_{r-1-i}t^{r-1-i}，再用域 trace 配对选 b 的系数，即使 λ_v(ab)≠0。
这是实际截断局部 complete-intersection 代数上的 residue 型配对。
普通 algebra trace 在有 nilpotents 时反而退化，不能代替 (5)。

局部 jets 的维数 Σ_v r_v deg(v) 精确可算，但没有自动给出一个小的全局截面空间。
参数 t_v、全局微分及不同点间的 gluing 尚不由 b_d 指定。
此外，几何 q-power Frobenius 使 t_v↦t_v^q，通常不是截断 jet 代数的自同构；
只令系数 Frobenius 而固定 t_v 是另一种 lift，不能静默冒充几何 Frobenius。

此处不使用特征零 Wronskian。特征 p 下 1,z^p 线性独立而普通 Wronskian 为零，
所以不能把 Landau–Siegel 证明的普通导数论证直接移植。

## 3. 真曲线与反模型的同一有限检验

固定 q=5。真曲线取 563 的 E:y²=x³+x+1，P_+(T)=1+3T+5T²；
反模型取 290 的 P_-(T)=1−5T+5T²。全部 b_d 正整数在真实曲线情形来自闭点，
在反模型情形由 290 的 Euler 递归及全 d 估计证明；下面的有限表不承担全 d 外推。

记 S_0=2，S_1=t，S_n=tS_{n-1}−5S_{n-2}，N_n=5^n+1−S_n，
b_n=n^{-1}Σ_{d|n}μ(n/d)N_d。纯整数计算给：

| 对象 | t | (N_1,N_2,N_3,N_4) | (b_1,b_2,b_3,b_4) | (M_1,M_2,M_3,M_4) |
|---|---:|---|---|---|
| 真实 E/F_5 | −3 | (9,27,108,675) | (9,9,33,162) | (9,27,126,774) |
| 290 反模型 | 5 | (1,11,76,451) | (1,5,25,110) | (1,11,86,526) |

两者所有 B 的 (1)–(5) 均存在；R_2 的 trace 配对非退化、自由 evaluation determinant
非零、V_2 在正空间上酉，而且 (4) 精确给 N_1,N_2。

完整 Weil 源却由预定 genus、pole 和归一化给

\[
 a_0=2,\qquad a_n=5^{-n/2}(5^n+1-N_n),\quad a_{-n}=a_n.
\]

其最小 primitive Gram 为

\[
 G=\begin{pmatrix}2&t/\sqrt5\\t/\sqrt5&2\end{pmatrix},\quad
 \det G=\begin{cases}11/5,&E,\\-1,&290.\end{cases} \tag{6}
\]

(6) 的符号和其 all-period/mixed 后果属于 567 旧资产，不能重计；
本轮新增的是用一个真实有限 étale/jet 评价构造同时通过两侧，再精确定位它未付的 map。
raw V_B 是权零点集的 Frobenius，不是 primitive 权一 H¹ 的归一化 Frobenius。
直接乘 5^{-1/2} 后，它的谱在半径 5^{-1/2}，更不是所需酉权一对象。

更准确地说，(4) 可以独立恢复每个有限 n 的原始 N_n，但还要取差

\[
 a_n=5^{n/2}+5^{-n/2}-5^{-n/2}\operatorname{Tr}(V_B^n),\quad n\le B. \tag{7}
\]

两个背景减一个正载体迹，是 signed/virtual 组合；(3) 的正性不传给 (7)。
B→∞ 时 Tr I=M_B→∞，而完整 Weil 的 a_0=2g 固定，故 contact 项也不是 raw 点集大小。
将这种无限差定义为一个 regularized trace 不会自动保正。

## 4. 从全递推得到 trace 代数：完整身份容易，正号仍是原责任

若另有源侧精确有理性证书 P(T)，m=deg P，令
χ(X)=X^m P(X^{-1})，A=Q[X]/χ。乘以 X 的 regular representation 满足

\[
 \operatorname{Tr}_A(X^n)=q^n+1-N_n\quad(n\ge1),\qquad
 \operatorname{Tr}_A(1)=m. \tag{8}
\]

这是 coefficient/recurrence 构造，不需先求根。reciprocal FE 使 X↦q/X 在 A 上定义对合 †。
复化后把系数共轭并入，候选 Hermitian form 为

\[
 H_A(f,g)=\operatorname{Tr}_A(fg^{\dagger}). \tag{9}
\]

在 genus-one 基 1,X 上，(9) 正是 [[2,t],[t,2q]]，两例行列式分别 11 与 −5。
所以把 local raw carrier 换成完整 trace 代数虽解决 (8) 的 identity，仍没有新的独立正性。
在 reduced 复分解上，† 的双点交换块是不定的；只有 † 在每点等于复共轭，
(9) 才是正的带重数平方和。这在该有限类中是纯性等价描述，而不是正性来源。

重根与 Jordan 必须单独保存。若 χ 有重复因子，regular trace pairing 的 radical
含 nilradical；nilpotent 不改变 (8) 的幂迹。将代数 reduced 后，根的 ordinary trace
重数不能按 quotient dimension 静默删除。例如 χ=(X−a)² 的 reduced 代数维数为 1，
原 trace(1)=2；若保原 trace functional，商上仍须保权 2。
因此“非退化商”不自动给 faithful 的 ordinary determinant/heat 重数。

## 5. 真正几何增加了哪一笔容量

实际光滑射影曲线给函数域 K=F_q(C) 对所有局部环的同一个 diagonal image。
对 divisor D 和不交于其 pole 支撑的有效 E，有实际限制映射

\[
 \operatorname{ev}_E:H^0(C,O(D))\to H^0(E,O(D)|_E),
 \quad\ker\operatorname{ev}_E=H^0(C,O(D-E)). \tag{10}
\]

deg E>deg D 时，kernel=0；target 维数为 deg E，而 RR 对 source 给
h⁰(D)≥deg D+1−g。这里上下界在同一个 map 上相遇。
局部自由对象 (5) 只给 target，没有 diagonal global source、pole filtration、
principal product formula 和 kernel 的 degree 判据。
这些是可实际检验的 gluing/section 责任，不能用“任选一个小子空间”代替。

曲线级 (10) 仍不足直接给完整 Weil 型；需平方 C×C 上 signed correspondences 的
有效化、截面/评价乘法和交重数，使同一容量预算识别为 primitive 自交。
Weil 的 canonical evaluation determinant 还须 generic nonvanishing、碰撞零重数、
极点次数预算及置换 descent（通常平方后）同时成立；仅 det≠0 不够。
RR 容量路线则须 567(13)–(14) 的实际 sections、有限/成长容量及同源误差。
来源分别为 [Connes–Consani–Marcolli §2.3](https://arxiv.org/pdf/math/0703392v1)
及 [Grothendieck §§1–2](https://denisevellachemla.eu/AG-Mattuck-Tate.pdf)。

## 6. 全周期、mixed 与完整源的消费门

函数域的完整源是 W_C=LΣ_{n∈Z}a_nδ_{nL}，L=log q。
同一几何的 graph 交数（含 q^{min(m,n)} 的不可分重数和 diagonal adjunction）
在 567 已给 −E_m·E_n=a_{n-m}。对每个 complex compact g，分段 periodization
才给全 mixed 的积分 Gram。不能从 n≤B 的 (4) 自动得到所有尺度正性。

本稿的 R_B 对每个 n 最终确能复原 N_n，甚至连同有理性可复原完整 signed W；
但正 carrier→signed primitive 的 identity/positivity 并未由局部非退化或单位范数解决。
这使失败位置比“没有几何”更具体：缺的是 diagonal gluing 后的 kernel/capacity
与同一 primitive signed 差的比较，且须在全部 signed/complex 方向成立。

连续非原子 g-prime 系统通常没有整数 b_d 与 F_{q^d}；故 (1) 只是一个可证伪的算术原型，
不是一般类 RH 的必要设施。允许连续评价/测度容量的修复仍合法；若只从正计数造
L²(Π) 则仍须另付 signed primitive 源身份，不能从本稿拒绝所有这种修复。

## 7. Root 消费记录及建议单一下一检验

| 责任 | 已付 | 未付/范围 |
|---|---|---|
| 对象/域/range | R_B、J_B 实际有限 F_q 代数；ev 恒等/局部 residue；C^{X_B}独立点集线性化 | 不是 curve 的 global H⁰，也不是 H¹ |
| source/growth | 每 B 全部 b_d，n≤B 的 N_n 精确；两例所有 B 可造 | 未有 B→∞ ordinary trace；M_B 发散 |
| norm/duality | finite-field perfect 双线性与 complex counting Hilbert 明确分开 | 无 F_q→C scalar extension；无 primitive positive norm transport |
| errors/direction | (1)–(9) 精确无数值误差；positive raw trace 被减入 W | 正 carrier 不保 signed 差的正性 |
| coverage/multiplicity | 所有 finite labels/jets；递推 trace 保重数 | global principal relations、mixed positivity、regularized contact 均未由本构造支付 |
| strongest-old net | 新增一个实际局部载体同时通过真/反例的明确 map failure | 567 全 Gram、563 正 H/全周期平方和、566 heat 不重计；classic 4/5/core 无改善 |

一个有信息的后续检验必须指定 global source S_B(D)→J_B：同时证明
kernel 的 pole-degree 界、全 cutoff dimension/capacity 及其 primitive signed 二次项。
若候选只是自由局部空间、A 的 trace Gram，或按 Q_W 反定义容量，就按本次测试停止，
不再扩 B、调 basis 或重命名 Hodge/RR。这里尚未生成经典 ζ 的这种 global source。
