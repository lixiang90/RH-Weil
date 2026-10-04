# 固定正角的本质范数与受限连续读出完整分类

2026-10-04。独立推导，沿用[425](../../notes/425-f1-recentered-geometric-corner-and-source-period-finite-part.md)的实际固定算子与[426](../../notes/426-f1-fixed-corner-source-commutators-and-relative-readout-module.md)的明确线性双模。这里不更改旧稿。结论是：非零测试给非紧算子；在指定测试函数拓扑中，匹配普通迹且对正象限乘子循环的读出由任意时间分布参数化。这比426的两个不同候选更强，但仍不是全循环代数、相对Chern类、算术主关系或RH证明。

## 1. 原采样算子在完整波形基中的共同因子

记 \(\mathscr T=C_c^\infty(\mathbb R)\)，\(\widehat h(\xi)=\int h(s)e^{-is\xi}\,ds\)，\(U(h)=\int h(s)\mathsf T_s\,ds\)。令 \(A(h)=K_\infty U(h)K_\infty^*\)，对象和时间方向与425相同。径向投影
\[
 E_\infty=R_p^-\otimes W_q+W_p\otimes R_q^-
\]
的两通道在完整 \(w\) 基中正交。

425(29)给p通道第 \(n<0\) 行与q通道第 \(k<0\) 行分别为
\[
 d_p(t)(B\phi)(t-nL),\qquad d_q(t)(B\phi)(t-kM),\qquad
 B=\mathcal W_p\mathcal W_q .                                      \tag{1}
\]
\(B\) 是原几何参数构造的酉元，且与所有时间平移及 \(U(h)\) 交换。径向换基也是酉的。因此在这个实际坐标系中可写
\[
 A(h)=V U(h)V^*,\qquad
 (V\phi)_{p,n}(t)=d_p(t)\phi(t-nL),\quad
 (V\phi)_{q,k}(t)=d_q(t)\phi(t-kM),\quad n,k<0.                  \tag{2}
\]
在 \(E_\infty^\perp\) 上补零。这里是在原 \(K_\infty\) 内抵消共同酉因子，未替换原源或删除混合块。

对任意 \(\phi\in L^2(\mathbb R)\)，换元 \(x=t-nL\) 后有
\[
 V^*V=M_m,\qquad
 m(x)=\sum_{n<0}d_p(x+nL)^2+\sum_{k<0}d_q(x+kM)^2.             \tag{3}
\]
原平方分割和紧支性直接给
\[
 0\le m\le2,\qquad m(x)=0\ (x\ll0),\qquad m(x)=2\ (x\gg0).    \tag{4}
\]
每个有界区间内求和局部有限，故 \(m\in C^\infty\)。右端等于2的原因是：当 \(x\) 大于两分割的支集上端时，全整数分割中的 \(n\ge0\)、\(k\ge0\) 项全为零，负项各自恰和为1。于是 \(\|V\|^2=2\)，且
\[
 \|A(h)\|\le2\|U(h)\|=2\|\widehat h\|_\infty .               \tag{5}
\]
这改进425用于准入的粗常数，但不改其算子或截止。

## 2. 精确本质范数：每个非零测试均非紧

**命题。** 对每个 \(h\in\mathscr T\)，
\[
 \boxed{\ \|A(h)\|_{\rm ess}=\|A(h)\|=2\|\widehat h\|_\infty\ }. \tag{6}
\]

证明：先固定单位向量 \(\psi\in C_c^\infty(\mathbb R)\)。由于 \(h\) 紧支，\(U(h)\psi\) 也紧支。取 \(R_j\to+\infty\)，使 \(\psi_j=\mathsf T_{R_j}\psi\) 与 \(U(h)\psi_j\) 的支集都落在 \(m=2\) 的右端。则
\[
 \zeta_j=V\psi_j/\sqrt2,\qquad
 \|\zeta_j\|=1,\qquad V^*\zeta_j=\sqrt2\psi_j,
\]
并且
\[
 \|A(h)\zeta_j\|=\sqrt2\|VU(h)\psi_j\|
                       =2\|U(h)\psi\|.                     \tag{7}
\]
\(\psi_j\rightharpoonup0\)，因为向无穷平移的固定紧支 \(L^2\) 向量与每个紧支向量最终正交，再用稠密性推广；\(V\) 有界故 \(\zeta_j\rightharpoonup0\)。任意紧算子 \(C\) 满足 \(\|C\zeta_j\|\to0\)，所以
\[
 \|A(h)-C\|\ge2\|U(h)\psi\|.
\]
单位紧支光滑向量在单位球面稠密，取上确界得 \(\|A(h)\|_{\rm ess}\ge2\|U(h)\|\)。结合(5)得(6)。

Fourier变换的单射性给 \(h\ne0\Rightarrow\|\widehat h\|_\infty>0\)。因此
\[
 h\ne0\Longrightarrow A(h)\notin\mathcal K(\mathcal H),\qquad
 A(\mathscr T)\cap\mathcal K(\mathcal H)=\{0\},\qquad
 A(\mathscr T)\cap\mathcal S_1=\{0\}.                         \tag{8}
\]
特别 \(h\mapsto A(h)\) 单射。证明保留两通道和全部混合矩阵元；即使测试的所有纯轴读出均为零，仍适用。它是无限维显式分析结论，有限有理审计不能替代(7)的弱零序列证明。

## 3. 指定测试拓扑下的真正直和与商

沿用426的
\[
 \mathcal D=\{A(h)+S:h\in\mathscr T,\ S\in\mathcal S_1\}.       \tag{9}
\]
按426约定，从 \(\mathscr T\oplus\mathcal S_1\) 的拓扑经 \((h,S)\mapsto A(h)+S\) 赋予商拓扑：\(\mathscr T\) 用标准测试函数LF拓扑，\(\mathcal S_1\) 用迹范数。由(8)映射的核实际为零，故在这个**指定的**拓扑中
\[
 \mathcal D\simeq\mathscr T\oplus\mathcal S_1,\qquad
 \mathcal D/\mathcal S_1\simeq\mathscr T                       \tag{10}
\]
为Hausdorff局部凸空间的拓扑同构。这里不是从环境算子范数推导出该拓扑，也不声称环境范数中的分解逆映射连续。

426的乘子域为
\[
 \mathcal M_Q=\{R=c1+J:J=QJQ\in\mathcal B(\mathcal H)\}.        \tag{11}
\]
这是Hilbert有界双模乘子域；任意这样的 \(J\) 不自动属于原C*交叉积乘子代数。\(Q^\perp\ne0\)，所以 \(c\) 唯一。426(4)、(10)已严格证明
\[
 JA(h),\ A(h)J\in\mathcal S_1,\qquad
 \operatorname{Tr}[R,A(h)]=0.                                \tag{12}
\]
因此左右商作用均退化为
\[
 [R(A(h)+S)]=c[A(h)]=[(A(h)+S)R].                            \tag{13}
\]
这是受限源相容性未能选择读出的机制。

如果需要固定 \(R\) 的双模作用连续性，426(5)–(6)在每个固定紧支测试空间上亦给 \(h\mapsto QA(h)\) 的迹范数连续性：支集固定时 \(B,m_p,m_q,N_p,N_q\) 可统一选择，\(\|\widehat h\|_1\) 由有限个光滑半范数控制。右Q同理，故 \(h\mapsto JA(h),A(h)J\) LF到迹范数连续。普通迹类部分的作用由有界乘子的迹范数界控制。

## 4. 所有匹配普通迹且受限循环的连续读出

**分类定理。** 在线性域(9)和拓扑(10)上，每个连续线性泛函 \(\Phi\) 若在 \(\mathcal S_1\) 上等于普通迹，则唯一具有形式
\[
 \boxed{\ \Phi_\ell(A(h)+S)=\ell(h)+\operatorname{Tr}S,
                 \qquad \ell\in\mathscr T'=\mathcal D'(\mathbb R)\ }. \tag{14}
\]
并且每一个这样的 \(\Phi_\ell\) 自动满足
\[
 \Phi_\ell(RF)=\Phi_\ell(FR),\qquad R\in\mathcal M_Q,\ F\in\mathcal D. \tag{15}
\]

证明：由(10)，\(\ell(h)=\Phi(A(h))\) 是连续测试函数泛函，即任意分布；线性性与普通迹要求强制(14)。反之，任意分布及普通迹在直和拓扑上连续，且分解唯一，所以定义良好。最后
\[
 RF-FR=[R,A(h)]+[R,S]\in\mathcal S_1,
\]
其普通迹由(12)和迹类的有界乘子循环性为零，故(15)与 \(\ell\) 无关。分类同时证明必要性与充分性，并非只列两个例子。若删除连续性要求，任意代数线性泛函亦可用同一公式；本报告的连续分类准确为分布。

原物理截止选出的一个候选是
\[
 \ell=\Lambda=(L+M)\delta_0+
 L\sum_{a\ne0}\rho_p^{|a|}\delta_{-aL}+
 M\sum_{b\ne0}\rho_q^{|b|}\delta_{-bM}.                       \tag{16}
\]
这里符号 \(\delta_x(h)=h(x)\)。它是有限时间Radon测度，来自425的原Haar球／壳层截断；\(\ell=0\) 给426的 \(\Psi_0\)，\(\delta_0'\) 等任意分布也给不同连续循环读出。因此普通迹扩张、\(\mathcal M_Q\) 循环性及原 \(T,T^*\) 的源交换子零迹，不足以从(14)中选出(16)。保留原截止来源仍是额外选择数据。

## 5. 环境算子范数与算子商范数必须区分

首先，**没有**在整个 \(\mathcal D\) 的环境算子范数中连续、又匹配所有普通迹的线性泛函：取秩 \(n\) 的投影 \(P_n\)，则 \(\|P_n/n\|=1/n\to0\)，但 \(\operatorname{Tr}(P_n/n)=1\)。这个障碍与 \(\ell\) 的选择无关。

有意义的范数分类是两个迹匹配读出之差：它消去 \(\mathcal S_1\)，从而下降到商。因为有限秩在紧算子中算子范数稠密，(6)给
\[
 \|[A(h)]\|_{q}:=\inf_{S\in\mathcal S_1}\|A(h)+S\|
                   =\|A(h)\|_{\rm ess}=2\|\widehat h\|_\infty. \tag{17}
\]
\(\mathcal S_1\) 虽不在 \(\mathcal B(\mathcal H)\) 中范数闭，但在 \(\mathcal D\) 中相对闭：相对闭包包含于 \(\mathcal D\cap\mathcal K=\mathcal S_1\)，后一个等式由(8)得出。因此(17)为真实商范数，不是非Hausdorff半范数。

\(\widehat{\mathscr T}\) 在频率空间 \(C_0(\mathbb R_\xi)\) 中一致范数稠密。具体地，给 \(g\in C_c^\infty(\mathbb R_\xi)\)，其逆Fourier变换 \(f\) 属Schwartz空间。取时间紧支光滑 \(\chi_R\to1\)，则 \(f_R=\chi_R f\in\mathscr T\)，且
\[
 \|\widehat f_R-g\|_\infty\le\|f_R-f\|_1\to0.
\]
再用频率紧支光滑函数在 \(C_0\) 的稠密性，得到商的范数完成就是频率 \(C_0\)，范数为 \(2\|\cdot\|_\infty\)。Riesz表示于是给精确分类：
\[
 \ell\text{ 连续于(17)}\quad\Longleftrightarrow\quad
 \ell(h)=\int_{\mathbb R}\widehat h(\xi)\,d\mu(\xi),
 \quad \mu\text{ 为有限复Radon测度}.                         \tag{18}
\]
\(\mu\) 唯一，泛函的商范数为 \(\|\mu\|_{\rm TV}/2\)。这只分类下降到商的差泛函，不把(18)误称为整个 \(\mathcal D\) 的有界迹。

Fubini还给
\[
 \ell(h)=\int h(s)\kappa(s)\,ds,\qquad
 \kappa(s)=\int e^{-is\xi}\,d\mu(\xi),\qquad
 |\ell(h)|\le\|\mu\|_{\rm TV}\|h\|_1.                       \tag{19}
\]
\(\kappa\) 有界一致连续，未必在时间无穷远趋零；频率原子可给指数函数。因此这里的 \(C_0\) 属于频率完成，不能误写成时间 \(C_0\)。式(19)也表明任何非零时间点质量都不是这种商范数连续泛函。

## 6. 原周期读出不连续于算子商范数

取原两个不同素数，\(L/M\) 无理；两条轴的离散周期集合在任意紧区间局部有限，\(-L\) 与q轴周期及0不同。选择真实非负 \(\psi\in C_c^\infty((-1,1))\)，\(\psi(0)=1\)，并令
\[
 h_\varepsilon(s)=\psi((s+L)/\varepsilon).
\]
当 \(\varepsilon>0\) 足够小时，其支集只遇到(16)中的原子 \(-L\)。于是
\[
 \Lambda(h_\varepsilon)=L\rho_p\ne0,\qquad
 \|[A(h_\varepsilon)]\|_q=
 2\|\widehat h_\varepsilon\|_\infty
             =2\varepsilon\|\psi\|_1\longrightarrow0.       \tag{20}
\]
最后的等号由缩放公式与非负 \(\psi\) 的Fourier模在0处达到 \(\|\psi\|_1\) 得出。这严格排除 \(\Lambda\) 属于(18)，也排除 \(\widetilde\Lambda-\Psi_0\) 的算子商范数连续性。没有LF连续性矛盾：这些收缩函数的高阶导数增长，不在固定紧支测试Fréchet拓扑中趋零。

## 7. 独立精确审计与范围

新增[脚本](../../scripts/corner_commutator_moment_audit.py)和[JSON](f1-corner-commutator-moment-audit.json)用 \(\texttt{Fraction}\) 及分段多项式原函数，完成207项精确断言。两个有理分段框架的尾端为0、2，验证 \(\int m(x)(m(x-s)-m(x+s))\,dx=-4s\)；有理紧支测试 \(h=(1+t)(1-t^2)^3\)、\(k=(1-t^2)^3\) 在 \([-1,1]\) 上给
\[
 \int t h(t)k(-t)\,dt=\frac{2048}{45045}>0,
 \qquad -4\int t h(t)k(-t)\,dt=-\frac{8192}{45045}.
\]
另有隔离有理时间原子的缩放例子，精确证明替代模型中的 \(L^1\) 范数缩小而点读出不变。它们是 \(C^1/C^2\) 分段多项式替代模型，不是原 \(C_c^\infty\) 素数采样数据。审计不认证(6)、迹类性、无限维商拓扑、任意真实素数或RH；本报告(20)另使用实际光滑测试的解析证明。

本报告仅针对425的固定两位模型、426的明确 \(\mathcal M_Q\) 双模及指定拓扑。没有证明 \(\mathcal D\) 对 \(A(h)A(k)\) 关闭；没有把裸 \(u\)、一般径向移位或全交叉积乘子纳入(15)。分类揭示的读出选择自由度须由真正的几何／算术来源支付，不能以受限循环性本身代替。

绑定来源SHA256：425 `fe933bbb822bcc47df25511a700744ee222576012e4dc46a1f10d229d9b6afdd`；426 `e90e74e394c0f8a400cf678d81695e63e63eb5e6712af021ecb9bf8355ddb3bd`。精确审计脚本SHA256 `47a9dc3e5be1b1493a9fd836a7724b2616ff0b93e0846aa992f631213d52019c`；JSON SHA256 `2877df2da3a26d8bb46ee9af050765ca4c0ed78fb5ad8bfbbbd9179fbfae3e74`。
