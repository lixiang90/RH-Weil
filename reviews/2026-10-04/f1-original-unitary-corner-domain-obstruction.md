# 原常径向源酉元在固定角域上的非紧边障碍

2026-10-04。首次GitHub保存`9d0cb1a`之后继续研究。
沿用[414](../../notes/414-f1-deep-boundary-unitary-and-time-defect.md)、
[425](../../notes/425-f1-recentered-geometric-corner-and-source-period-finite-part.md)及
[426](../../notes/426-f1-fixed-corner-source-commutators-and-relative-readout-module.md)的同一源和完整Hilbert表示。
本报告证明原源酉元u不能直接作为426线性双模的乘子；实际交换子产生非紧的新边。
这是否定现有域准入的有限结论，不是否定一切扩大后的相对Chern构造，也不证明算术主关系、Weil正性或RH。

## 1. 原源、表示和测试族

固定\(L=\log p\)、\(M=\log q\)，物理时间平移
\(\mathsf T_s\psi(t)=\psi(t-s)\)。实际协变表示为
\[
 P_{(a,b)}=\lambda_{a,p}\otimes\lambda_{b,q}\otimes\mathsf T_{aL+bM}
\]
作用在
\(\mathcal H=\ell^2(\mathbb Z^2)\otimes L^2(\mathbb R)\)。
原源\(c\in C_c^\infty(\mathbb R)\)实值非负且
\[
 \sum_{s\in\mathbb Z}c(t-sL)^2=1,\qquad \int c(t)^2\,dt=L. \tag{1}
\]
414规定425中的\(d_p=c\)，另一个\(d_q\)仍为M周期平方分割，不能把它与\(c(t-M)\)混同。

令\(M_f\)表示时间乘法。原源的实际乘子是
\[
 \begin{split}
 e&=\sum_{s\in\mathbb Z}M_{c(t)c(t-sL)}P_{(s,0)},\\
 v&=\sum_{s\in\mathbb Z}M_{c(t)c(t-sL-M)}P_{(s,1)},\\
 u&=1-e+v.
 \end{split}                                                     \tag{2}
\]
c紧支使两和只有有限个非零系数。
原Green计算给\(e^2=e=e^*\)、\(v^*v=vv^*=e\)，所以u酉。
它与\(T=1-Q+QuQ\)是不同的实际对象；T仅为一般单位化提升，u为常径向乘子酉提升。

本报告在上述完整Hilbert表示中直接计算，**不对径向环面取字符、不对角点代数评价，也不替换物理时间作用**。
波形基的变换只是425证明的Hilbert酉基变换。

## 2. 固定角支撑与准确的深负p边行

在425的完整正交波形基\(w_{n,r}=\lambda_{n,r}w_{0,r}\)中，设
\[
 E=\left(R_p^-\otimes W_q+W_p\otimes R_q^-\right)\otimes1_t,
 \quad R_r^-=\sum_{n<0}P_{w_{n,r}},\quad W_r=P_{w_{0,r}}.
\]
\(A(h)=A_\infty(h)\)满足\(A(h)=EA(h)E\)。
定义时间空间的等距嵌入
\[
 I_n^j\psi=w_{-n,p}\otimes w_{j,q}\otimes\psi,\qquad n\ge1, j\in\mathbb Z. \tag{3}
\]
\(I_n^0\)的像在E内；\(I_n^1\)、\(I_n^{-1}\)的像在\(1-E\)内。
它们的不同n像互相正交。

425(29)中的共同时间酉元与U(h)交换并抵消，因此完整p←p块的矩阵元精确为
\[
 I_i^{0*}A(h)I_j^0=M_c\mathsf T_{(j-i)L}U(h)M_c,
 \qquad i,j\ge1.                                            \tag{4}
\]
这里\(I_i^0\)的径向位置是−i，所以实际群位移为\((j-i,0)\)。
全部p←q及q←p块仍留在A中；下面的投影选择使它们不能进入所计算的行，而非从算子中删除它们。

设\(S_e,S_v\subset\mathbb Z\)分别为(2)两个有限和的可能非零p次数。
可取\(N>\max\{|s|:s\in S_e\cup S_v\}\)。以后\(n>N\)，所有源造成的有限p平移仍处于严格负边，
因此以下公式为精确等式，不是仅渐近等式。

## 3. 真源交换子的非紧见证

记
\[
 B_a(h)=M_c\mathsf T_aU(h)M_c,
 \quad B_a(h)(t,t')=c(t)h(t-t'-a)c(t').                       \tag{5}
\]
平滑紧支核给实际迹类算子，且
\[
 \operatorname{Tr}B_a(h)=Lh(-a).                              \tag{6}
\]
也可不使用抽象核迹定理而直接核验：Fourier约定
\(\widehat h(\xi)=\int h(s)e^{-i\xi s}\,ds\)给
\[
 B_a(h)=\frac1{2\pi}\int\widehat h(\xi)e^{-i\xi a}
     |ce^{i\xi\cdot}\rangle\langle ce^{i\xi\cdot}|\,d\xi.
\]
这是迹范数积分，范数至多\(L\|\widehat h\|_1/(2\pi)\)；
每个秩一项的迹为L，Fourier反演直接给(6)。

E的p边q次数为0，q边q次数严格负；v只把q次数增加1。
故\(I_n^{1*}uA(h)I_n^0\)只能来自v作用于A的p←p块。
另一方面A的输出总在E内，\(I_n^{1*}A(h)uI_n^0=0\)。
按(2)、(4)展开剩余块，对\(n>N\)得到
\[
 \begin{split}
 I_n^{1*}vA(h)I_n^0
 &=\sum_sM_{c(t)c(t-sL-M)}\mathsf T_{sL+M}
                   M_c\mathsf T_{-sL}U(h)M_c\\
 &=M_c\left(\sum_s c(t-sL-M)^2\right)\mathsf T_MU(h)M_c\\
 &=B_M(h).
 \end{split}                                                     \tag{7}
\]
第二行使用\(\mathsf T_aM_c=M_{c(t-a)}\mathsf T_a\)；(1)把平方和严格变为1。
原有限非零系数以外的项在外侧c因子上已为零，故用完整平方和没有改变有限源算子。
特别
\[
                   I_n^{1*}[u,A(h)]I_n^0=B_M(h).              \tag{8}
\]

只要\(B_M(h)\ne0\)，选一个固定单位向量\(\psi\)满足\(\|B_M(h)\psi\|=\delta>0\)。
\(x_n=I_n^0\psi\)是正交单位向量列，故弱趋零，但(8)给
\(\|[u,A(h)]x_n\|\ge\delta\)。
紧算子必须把这种向量列送至范数趋零，因此
\[
                   B_M(h)\ne0\Longrightarrow [u,A(h)]\notin\mathcal K(\mathcal H). \tag{9}
\]
\(h(-M)\ne0\)由(6)保证\(B_M(h)\ne0\)，是明确合法的充分条件。

## 4. uA与Au均不准入426的线性双模

426的域是\(\mathcal D=\{A(k)+S:k\in C_c^\infty,S\in\mathcal S_1\}\)。
**不能仅凭uA或Au非紧推出它们不在D**，因为A本来可能非紧。
正确必要条件由固定角支撑给出：对每个\(F\in\mathcal D\)，
\[
             (1-E)F\in\mathcal S_1,\qquad F(1-E)\in\mathcal S_1. \tag{10}
\]
(7)给\(I_n^{1*}(1-E)uA(h)I_n^0=B_M(h)\)，用同一正交向量列证明
\((1-E)uA(h)\)非紧。因此当\(B_M(h)\ne0\)时，\(uA(h)\notin\mathcal D\)。

右侧准入须独立计算。对\(I_n^{-1}\)的双负输入，\((1-e)I_n^{-1}\)经有限p平移仍不在E，
其A像为零。v把输入的q次数−1送至0，且p位置保持严格负。
投影到\(I_n^0\)只需p←p块。其时间核为
\[
 \begin{split}
 (I_n^{0*}A(h)vI_n^{-1})(t,t')
  &=c(t)h(t-t'-M)c(t')\sum_s c(t'+sL+M)^2\\
  &=c(t)h(t-t'-M)c(t').
 \end{split}                                                     \tag{11}
\]
所以
\[
                   I_n^{0*}A(h)uI_n^{-1}=B_M(h).              \tag{12}
\]
\(I_n^{-1}\)在\(1-E\)内；(12)证明\(A(h)u(1-E)\)非紧，从(10)得到\(A(h)u\notin\mathcal D\)。
这也给\(I_n^{0*}[u,A(h)]I_n^{-1}=-B_M(h)\)，与(8)的左侧新边方向相容。
故
\[
 B_M(h)\ne0\Longrightarrow
 uA(h),\ A(h)u\notin\mathcal D,\qquad [u,A(h)]\notin\mathcal D. \tag{13}
\]
最后一个结论同样由\((1-E)[u,A]=(1-E)uA\)的非紧性得出，未把D与迹类或紧算子域混同。

## 5. 加权真源式的准确q=1边块

u确为酉，所以代数恒等式是
\[
             [u^*,uA(h)]=A(h)-uA(h)u^*=-[u,A(h)]u^*.        \tag{14}
\]
无额外的u共轭因子需要插入。这不是426中T的加权交换子公式的域推广。

在\(I_n^1\)输入上，\((1-e)\)及其伴随保持q次数1，仍在E外；
只有v*把输入送至负p、q=0边。A的输出要经u后到q=1，也只能由v作用于p边产生。
故所计算的块正是\(I_n^{1*}vA_{pp}(h)v^*I_n^1\)。
源的右伴随项保留其实际平移：
\[
 v_s^*=M_{c(t)c(t+sL+M)}P_{(-s,-1)}.                         \tag{15}
\]
对左v次数r与右v*次数s，A的p位移为\(s-r\)；全部中间p位置对\(n>N\)仍严格负。
由(4)、(15)直接作时间核乘法，该有限双和的核为
\[
 c(t)h(t-t')c(t')
       \sum_r c(t-rL-M)^2\sum_s c(t'-sL-M)^2
       =c(t)h(t-t')c(t').                                  \tag{16}
\]
右平方和的\(t'-sL-M\)来自v*的输入变量变换；此处没有漏掉右平移。
两次(1)归一得到
\[
 I_n^{1*}uA(h)u^*I_n^1=B_0(h),\qquad
 I_n^{1*}[u^*,uA(h)]I_n^1=-B_0(h).                          \tag{17}
\]
若\(h(0)\ne0\)，\(\operatorname{Tr}B_0(h)=Lh(0)\ne0\)，同一正交向量列证明加权真源式非紧。
由于\(I_n^1\)在E外，其左\((1-E)\)部分也非紧，故该式不在D。

另外，(14)乘以酉u*保持紧性；只要(9)成立，加权式也非紧。
更精确地
\((1-E)[u^*,uA]=-(1-E)[u,A]u^*\)，故在\(h(-M)\ne0\)条件下它也不在D。
可以固定**一个**紧支光滑合法测试h，使\(h(0)>0\)、\(h(-M)>0\)，同时见证所有上述结论。
这只是测试实际源与算子的域，不以不同测试倒填目标周期或添加目标权重。

## 6. 标量商作用及下一构造的必须条件

对426的\(R=a1+J\in\mathcal M_Q\)，\(J=QJQ\)，该稿已证明
\(JA(h),A(h)J\in\mathcal S_1\)。因此在线性商\(\mathcal D/\mathcal S_1\)上
\[
                         R\,[A(h)]=[A(h)]\,R=a[A(h)].       \tag{18}
\]
T和T*的作用为单位。这个受限商看不见原u实际搬移的边；(13)证明u根本不保持D，
所以不能先在此商给u指定作用，再称其为源导出的相对Chern数据。
一般非零物理群乘子\(P_g\)也不属于\(\mathbb C1+Q\mathcal B(\mathcal H)Q\)：
它们在深负坐标处仍非标量地移动径向基，不能由Q支持的修正表示。

若要纳入原u的源闭包，必须至少加入(7)的实际负p、q=1输出边以及(12)所示的右双负输入耦合；
这些修正非紧、非迹类，不能只向D添加\(\mathcal S_1\)补偿。
进一步乘子封闭还须处理u、u*搬移所产生的边族及其物理截止传递。
本报告没有为这些新元素预设读出，也没有证明一种扩大域必然不存在。

因此目前得到的是严格、具体的下一任务准入障碍：426的源T循环相容性及保留\(\Lambda\)的候选不能直接升级为真源u的相对Chern比较。
扩大边域后的链定义、截止自然性和读出选择仍须实际构造，426的\(\Psi_0\)非唯一性也未由这些非紧行公式自动解除。
