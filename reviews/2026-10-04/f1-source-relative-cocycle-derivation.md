# 真源有限词、S₁相对循环数据与实际源保持截止

2026-10-04。继续[427](../../notes/427-f1-corner-product-algebra-and-unavoidable-trace-cocycle.md)、[428](../../notes/428-f1-corner-essential-symbol-and-complete-readout-freedom.md)、[429](../../notes/429-f1-original-unitary-crosses-the-fixed-corner-domain.md)。使用414原规定 \(d_p=c\)，保留原非负光滑平方分割、全部物理表示及时间作用。只保存本报告，不改主稿或索引。

本次得到两类严格进展：

1. 原u的任意有限共轭轨道在本质层线性独立；有限加权轨道差不能彼此修复为紧算子或S₁。
2. 存在实际有限词源保持域、明确的S₁相对迹/商1循环配对，以及源保持的invariant-x截止。但该截止在原测试上仅读h(0)，不选出原周期Λ。

这些结果不构成算术主关系或规范相对Chern比较。尤其不以自由线性扩张、Hahn–Banach或未经核验的抽象闭包赋值。

## 1. 实际有限词代数与普通迹理想

令
\[
\mathfrak B=\operatorname{alg}^{*}(1,u,u^*,\mathcal D)
\subset\mathcal B(\mathcal H),\qquad
\mathcal I=\mathcal S_1(\mathcal H).
\]
这里每个元素是上述实际有界算子的有限和、有限乘积；不是抽象普遍代数，也没有完成步骤。
\(\mathcal I\subset\mathfrak B\)且为双侧理想，因为全部因子有界。
同一相对迹与第5节HH₁配对也适用于[430](../../notes/430-f1-source-stable-periodic-smoothing-algebra.md)的更大实际域，取
\(\mathfrak A_{\rm src}=\operatorname{alg}^{*}(1,u,u^*,D_{\rm src})\)即可；430已支付其有界乘法及源稳定性。
本报告第6节的有限词理想是由原D实际生成的较小候选，没有把它误等同于允许全部周期核的解析扩大。
普通迹
\[
\tau_{\mathcal I}(S)=\operatorname{Tr}S
\]
满足 \(\tau_{\mathcal I}([B,S])=0\)对任意 \(B\in\mathfrak B,S\in\mathcal I\)，所以此数据在扩大源域里仍完全合法。
与此不同，427已排除匹配该迹的全 \(\mathfrak B\)标量迹：它的子代数D内已有非零S₁交换子。

## 2. 原u的所有整数次有限Green公式

在同一物理表示置
\[
v_m=\sum_{a\in\mathbb Z}
 M_{c(t)c(t-aL-mM)}P_{(a,m)},\qquad m\in\mathbb Z.       \tag{1}
\]
固定m时c紧支使和的非零p次数有限；\(v_0=e,v_1=v\)。
直接乘两个有限和，固定总p次数r，系数为
\[
c(t)c(t-rL-(m+n)M)\sum_a c(t-aL-mM)^2
=c(t)c(t-rL-(m+n)M).
\]
因此
\[
v_m v_n=v_{m+n},\quad v_m^*=v_{-m},\quad
ev_m=v_me=v_m,\quad u^m=1-e+v_m.                         \tag{2}
\]
全部使用原平方和；没有令原有限源平移变成未经定义的无限算子。
第二式可直接由实际伴随平移换元证明，最后式对正、负、零m都成立。

记
\[
A_m(h)=u^m A(h)u^{-m},\qquad
I_n^j\psi=w_{-n,p}\otimes w_{j,q}\otimes\psi.
\]
沿用429的
\[
B_s(h)=M_c\mathsf T_sU(h)M_c,\quad
B_s(h)(t,t')=c(t)h(t-t'-s)c(t').                           \tag{3}
\]

## 3. 任意有限共轭轨道的准确深边矩阵元

对固定整数m,d,j,k，只要n足够大，有准确等式
\[
\boxed{I_n^{j*}A_m(h)I_{n+d}^{k}
 =\mathbf1_{j=m}\mathbf1_{k=m}\,B_{dL}(h).}                \tag{4}
\]
阈值只依赖固定有限源次数及d；可以为任意有限m,j,k列表共同选取。
它不是渐近公式。

证明要保留原e投影，不能把u全局当裸q移位。
在这些深负p行列里，原A仅有q=0的p通道可进入；原q通道的p坐标0不能经有限源平移到深负p。
原p块为
\[
I_i^{0*}A(h)I_l^0=M_c\mathsf T_{(l-i)L}U(h)M_c.
\]
由原平方和，e在该深p块的左右作用分别准确为单位：
左侧系数合并成 \(\sum_a c(t-aL)^2=1\)，右侧合并成
\(\sum_a c(t'+aL)^2=1\)。
因此将 \(u^m=1-e+v_m\)在左右展开时，所有含1−e的深块严格消失；不是删掉完整A的混合部分。

只剩 \(v_m A(h)v_m^*\)。
右 \(v_m^*\)要求输入q次数k=m，左 \(v_m\)要求输出j=m。
左p次数r、右p次数s使A中间索引为n+r与n+d+s，时间位移 \((d+s-r)L\)。
左、右中间时间分别 \(t-rL-mM\)、\(t'-sL-mM\)，故h核的变量为
\[
t-rL-mM-(t'-sL-mM)-(d+s-r)L=t-t'-dL.
\]
完整系数为
\[
c(t)c(t')\sum_r c(t-rL-mM)^2
                   \sum_s c(t'-sL-mM)^2=c(t)c(t'),
\]
给(4)。
当m=0，(2)仍是实际单位，(4)退回原p块，方向也一致。

### 任意非零h都可被某个p位移块检测

不需要额外要求h(0)或某个离散采样非零。
取s₀使h(s₀)非零、取t₀使c(t₀)>0。
平方分割
\(\sum_d c(t_0-s_0-dL)^2=1\)
给某整数d使 \(c(t'_0)>0\)，其中 \(t'_0=t_0-s_0-dL\)。
于是
\[
B_{dL}(h)(t_0,t'_0)=c(t_0)h(s_0)c(t'_0)\ne0.
\]
光滑核在一点非零便定义非零算子，可用该点附近小支集时间向量直接检测。
所以
\[
h\ne0\Longrightarrow\exists d\in\mathbb Z:
B_{dL}(h)\ne0.                                           \tag{5}
\]

## 4. 新的有限轨道与加权修复障碍

令有限多测试h_m非零，若
\[
F=\sum_m A_m(h_m)
\]
是紧算子，则每个h_m必须为0。
若某h_{m₀}非零，按(5)选d及单位ψ使 \(B_{dL}(h_{m_0})\psi\ne0\)。
输入 \(I_{n+d}^{m_0}\psi\)是正交单位弱零列；
(4)的输出 \(I_n^{m_0}\)块准确为 \(B_{dL}(h_{m_0})\psi\)，其他m全部为0。
完整范数有固定正下界，与紧性矛盾。因此
\[
\boxed{\sum_{m\ {\rm finite}}u^mA(h_m)u^{-m}\in\mathbb K
\Longrightarrow h_m=0\ \forall m.}                       \tag{6}
\]
这支付了任意有限整数轨道的本质线性独立，不仅是一条q=1边或h(0)见证。

特别令原加权式
\[
X(h)=A(h)-uA(h)u^*=[u^*,uA(h)].
\]
对有限测试族，精确有限差分为
\[
\sum_m u^m X(h_m)u^{-m}
=\sum_m A_m(h_m-h_{m-1}),                                \tag{7}
\]
区间外h_m=0。
若此算子紧，(6)给所有有限差分为0，有限支集迫使h_m全为0。
所以任何非平凡的这种有限加权轨道修复都仍非紧，更不可能属于S₁。
例如 \(A(h)-u^N A(h)u^{-N}\)在h非零、N非零时必非紧。

这是**有限共轭轨道差这一明确候选**的准入障碍。
没有证明所有含其他乘积的链修复都不可能；下面也保留真正可定义的相对数据。

## 5. 不需要自由扩张的实际S₁相对链数据

对代数商 \(\overline{\mathfrak B}=\mathfrak B/\mathcal I\)，取代数张量链
\[
C_n(\mathfrak B,\mathcal I)
=\ker\!\left(\mathfrak B^{\otimes(n+1)}
\to\overline{\mathfrak B}^{\otimes(n+1)}\right).
\]
在复数域，该核由至少一个槽在I中的张量张成。
Hochschild b、循环置换及单位插入均保持它，给实际相对循环链域。
度0就是I，度0普通迹在度1相对边界上为0，因为那些边界都是含S₁因子的有界交换子。
所以 \(\tau_{\mathcal I}\)是这个明确相对域上的0循环数据；未给裸非迹类元素任意赋值。

还有不需全局选择线性截面的规范连接配对。
对商中的1循环
\[
\bar z=\sum_r\bar B_r\otimes\bar C_r,\qquad
\sum_r[\bar B_r,\bar C_r]=0,
\]
任取实际有限词提升，定义
\[
\boxed{\Omega(\bar z)=
\operatorname{Tr}\left(\sum_r[B_r,C_r]\right).}             \tag{8}
\]
商循环条件恰使括号之和属于S₁，故其普通迹有定义。
提升差属于相对度1链，其b的迹为0；等价地每项差都有S₁因子，普通迹合法循环。
所以(8)与所有提升、张量表达无关，不使用Hahn–Banach。

若商循环是b\(\bar w\)边界，提升w后配对为0。对每个三槽实际张量，完整抵消为
\[
\begin{split}
b_2(B\otimes C\otimes D)&=BC\otimes D-B\otimes CD+DB\otimes C,\\
b_1b_2&=(BCD-DBC)-(BCD-CDB)+(DBC-CDB)=0.
\end{split}
\]
其他提升之差的b迹也为0，所以配对准确降至
\(HH_1(\overline{\mathfrak B})\)。
设未带符号flip将 \(B\otimes C\)变成 \(C\otimes B\)，则 \(b_1\operatorname{flip}=-b_1\)，
flip保持商1循环，且
\(\Omega(\operatorname{flip}\bar z)=-\Omega(\bar z)\)。
对称组合的配对为0，来自实际交换子的逐项抵消。
这里仅声明**代数HH₁ charge及这个flip关系**；不据此冒称完整周期循环余圈、全相对Chern配对或所有商1链的普通交换子迹都已定义。

原交换符号子代数中的每个 \(a\otimes b\)是商1循环，提升A(h),A(k)后(8)恰给
\[
\Omega(a\otimes b)=\omega(a,b)
=(2\pi i)^{-1}\int a'(\xi)b(\xi)d\xi.
\]
427的非零见证因而在扩大商内仍不可能成为边界：若成为边界，(8)应为0。
有限u共轭后的同一测试循环也有相同配对，因为普通S₁迹在有界酉共轭下不变。
这是实际保留的相对异常，没有由该异常恢复算术周期系数。

### 加权源链仍未支付商循环条件

原加权1链 \(u^*\otimes uA(h)\)的b为X(h)。
h非零时(6)使X非紧，所以其商边界非零，不能直接把该链送入(8)。
由(7)，有限轨道叠加也不能支付这个条件，除非测试族全为0。
源的未加权链 \(u^*\otimes u\)虽是循环，但实际酉提升使其b为0，其连接配对也为0。

存在平凡的更一般有限词链抵消，不能隐瞒它：
\[
b(u^*\otimes u\otimes A)
=1\otimes A-u^*\otimes uA+Au^*\otimes u.
\]
它形成确切边界，其(8)配对当然为0。
这说明(7)不否定所有链修复；但这种普遍代数恒等式没有选出Λ，也没有识别原算术主关系。

## 6. 一个实际有限词源保持边域

下面使用425完整w基标签j,k作酉坐标变换
\[
(G\psi)_{j,k}(x)=\psi_{j,k}(x+jL+kM).                     \tag{9}
\]
不能把此处j,k暗换成物理e基并仍保留同一个简单V公式。
在w基源的λ仍平移标签，因此原群位移保持x，u成为逐x的酉纤维 \(u_x\)。
原V成为向量乘法：
\[
(GV\phi)(x)=v(x)\phi(x),\quad
v(x)=\sum_{n<0}c(x+nL)e_{n,0}
       +\sum_{k<0}d_q(x+kM)e_{0,k}.                       \tag{10}
\]
这里e仅记w坐标的标准标签向量；不是把径向原e基来源改写。
\(\|v(x)\|^2=m(x)\)，v在充分负端为0；在每个紧x区间径向坐标有限，且光滑。
原u是有限源平移和，每个固定整数次u^i也如此，所以
\(v_i(x)=u_x^i v(x)\)在紧x区间仍有有限径向支集。

置
\[
g_r(x)=\langle v(x),u_x^rv(x)\rangle.
\]
所有g_r光滑、函数及各阶导数有界：v的导数范数由对应完整周期平方和的一致界控制，原有限源系数的导数算子范数一致有界。
实际有界时间算子满足
\[
V^*u^rV=M_{g_r},\qquad g_0=m.                             \tag{11}
\]

令 \(\mathfrak J\)为实际 \(\mathfrak B\)中由D生成的双侧理想。
每个含S₁槽的有限词仍在S₁；
每个其他有限词准确写成有限和
\[
F_{i,j}(B)=u^iVBV^*u^{-j},                               \tag{12}
\]
其中B从各U(h)核及(11)的中间g乘法有限次组成。
这些时间核具有有限传播、光滑且各阶导数有界；该性质由核积分中有限长度的y区间直接保持。
统一有限传播/有界核也给Schur有界性。

特别
\[
F_{i,j}(B)F_{k,l}(C)=F_{i,l}(BM_{g_{k-j}}C),\quad
F_{i,j}(B)^*=F_{j,i}(B^*).                               \tag{13}
\]
这严格构造了实际有限词源保持星域，无需范数闭包或普遍存在性接口。
u左右乘只改变i,j，故u是该边域的实际乘子。
它没有改变429的结论：旧D及其旧范数完成不准入u，此处支付的是更大的实际非紧边族。

## 7. invariant-x截止确实准入，且每个截止与真源相容

在(9)坐标取全Hilbert投影
\[
P_R=\mathbf1_{x\le R}\otimes1_{\rm rad}.
\]
它与原u交换，且R趋正无穷时强趋全单位。
对(12)，在该坐标下的核为
\[
|v_i(x)\rangle\langle v_j(x')|K_B(x,x').
\]
v_i,v_j在x≤a为0，P_R同时将x,x'限制到[a,R]；
在该紧区间径向坐标只有有限个。
选光滑紧支χ在[a,R]恒为1，先压得到有限径向矩阵的光滑紧支二维核，因而S₁；
再左右乘有界sharp P_R，仍S₁且准确等于所需压缩。
所以此sharp只是有界投影乘子，未代替原平滑分割。

明确核对角给
\[
\boxed{\operatorname{Tr}(P_RF_{i,j}(B)P_R)
=\int_a^R g_{i-j}(x)K_B(x,x)\,dx.}                       \tag{14}
\]
迹中的内积为 \(\langle v_j,v_i\rangle=\langle v,u^{i-j}v\rangle\)，i−j方向正确。
任意S₁词的压缩也S₁，所以该准入覆盖整个 \(\mathfrak J\)。
纯u或单位的P_R压缩一般仍有无限径向秩，**不在上述迹类准入内**。

源共轭同时把i,j加1，差i−j不变；更直接地P_R与u交换且有限压缩已S₁，普通迹合法循环给
\[
\operatorname{Tr}\!\left(P_R(F-uFu^*)P_R\right)=0
\quad(F\in\mathfrak J)                                  \tag{15}
\]
对每个R精确成立。
这不称非紧的 \(F-uFu^*\)本身有普通迹，也不交换其裸强极限与迹。
有限截止泛函只在压缩上给迹；对S₁部分它在R趋无穷时回到普通迹。

## 8. 实际源保持截止仍不选择原周期

对原测试A(h)，(14)准确成为
\[
\operatorname{Tr}(P_RA(h)P_R)=h(0)\int_{-\infty}^R m(x)dx. \tag{16}
\]
R充分大后该积分为 \(2R+C_m\)，所以用原x起点0扣除2R体积后的有限部只有 \(C_mh(0)\)。
可以直接算这个真实常数，而无需sharp分割：
\[
C_m=-\frac1L\int t\,c(t)^2dt
     -\frac1M\int t\,d_q(t)^2dt-\frac{L+M}{2}.             \tag{17}
\]
例如p项的准确标签计数是
\(\int c(t)^2\lfloor(R-t)/L\rfloor dt\)（R充分大时无需截正）。
其整数部分展开给R−L^{-1}∫tc²，周期小数部分的c²平均由原平方分割精确等于L/2；q同理。
这是光滑c²的积分恒等式，不是阶跃模型。
常数体现此x截止的原起点及分割形状，未调它以匹配目标。

取隔离−L的非零周期测试h，h(0)=0、h(−L)=1。
(16)对每个R都为0，而425的原物理球截止给 \(\Lambda(h)=L\rho_p\ne0\)。
因此已经给出**真正源保持且每个截止相容的明确机制，仍不选物理周期Λ**。

有限共轭轨道域
\(\sum_m A_m(h_m)+S_1\)
因(6)具有唯一测试分解。
由(15)–(17)可在此准确取共同有限部
\[
C_m\sum_m h_m(0)+\operatorname{Tr}S,
\]
它在u共轭下不变并匹配普通迹；此声明仅是该明确线性轨道域。
对整个 \(\mathfrak J\)的一般B，(14)的对角可能有周期端点振荡，未证明任意R体积扣除后均有极限。
不能把逐R源相容性自动升级为全扩大域的唯一连续有限部。

## 9. 下一桥的准确状态

已构造的规范数据是S₁普通迹及商循环的连接配对(8)；它保留ω，却不赋予非循环的加权源链数值。
有限原u轨道修复受(6)–(7)严格阻碍；更一般链和边域仍可构造，不能把此有限障碍扩大成总不可能性。

实际有限词源保持域及x截止已支付源准入、每次压缩迹类和真源相容性，但周期Λ选择仍没有完成。
它与原物理球截止的差需要真正的边界传递或几何链身份，不能由“源保持”“普通迹匹配”“受限循环”这些同级公理替代。

本报告未定义原源的规范相对Chern比较，未证明算术主消失、固定双次数、实位/全素数Weil正性、有效性/RR或RH。
后续应围绕(8)的商循环准入、实际 \(\mathfrak J\)及两个来源截止之间的相对传递继续，保留已证ω和非紧轨道层。
