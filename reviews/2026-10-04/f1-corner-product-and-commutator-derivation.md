# F1 固定角点的实际乘积、卷积符号与非零普通迹类交换子

2026-10-04。由[425](../../notes/425-f1-recentered-geometric-corner-and-source-period-finite-part.md)的同一个原平滑平方分割及实际采样算子出发；不改425、426，不用sharp分割替换原源。本轮首次GitHub推送完成后保存。

来源冻结：

- 425：SHA256 fe933bbb822bcc47df25511a700744ee222576012e4dc46a1f10d229d9b6afdd。
- 426：SHA256 e90e74e394c0f8a400cf678d81695e63e63eb5e6712af021ecb9bf8355ddb3bd。

结论是：426的线性空间实际上对乘法闭合，但两个测试算子间存在可明确计算、一般非零的普通迹类交换子。受限源乘子循环性不能扩展成匹配普通迹的全代数标量迹。这是本源的实际障碍，不是RH、主关系或算术正性结论。

## 1. 去掉共同酉后，frame的符号与方向

沿用425的 \(L=\log p>0,M=\log q>0\)、实值 \(d_p,d_q\in C_c^\infty(\mathbb R)\)，以及
\[
\sum_{n\in\mathbb Z}d_p(t-nL)^2
=\sum_{k\in\mathbb Z}d_q(t-kM)^2=1.
\]
令 \(\mathsf T_s\phi(x)=\phi(x-s)\)、\(U(h)=\int h(s)\mathsf T_s\,ds\)。
在完整波形基中记两个正交径向方向
\[
f_{p,n}=w_{n,p}\otimes w_{0,q},\quad n<0,\qquad
f_{q,k}=w_{0,p}\otimes w_{k,q},\quad k<0.
\]
直接定义
\[
(V\phi)(t)=
\sum_{n<0}f_{p,n}d_p(t)\phi(t-nL)
+\sum_{k<0}f_{q,k}d_q(t)\phi(t-kM).                 \tag{1}
\]
425(29)准确给
\[
K_\infty=V\mathcal W,\qquad
\mathcal W=\mathcal W_p\mathcal W_q.
\]
\(\mathcal W\)是时间卷积酉元，与所有 \(U(h)\) 交换。因此
\[
A(h)=K_\infty U(h)K_\infty^*=VU(h)V^*.             \tag{2}
\]

在(1)中作 \(x=t-nL\)，即 \(t=x+nL\)，得到
\[
\|V\phi\|^2=\int_{\mathbb R}m(x)|\phi(x)|^2\,dx,\qquad
m(x)=\sum_{n<0}d_p(x+nL)^2+
     \sum_{k<0}d_q(x+kM)^2.                       \tag{3}
\]
所以采样和的符号确为 **加号**，并且
\[
V^*V=M_m,\qquad K_\infty^*K_\infty=\mathcal W^*M_m\mathcal W. \tag{4}
\]
两级数局部有限，\(m\)光滑且 \(0\le m\le2\)。
可取实数 \(a<b\)，使
\[
m(x)=0\ (x\le a),\qquad m(x)=2\ (x\ge b),\qquad
m'\in C_c^\infty,\quad\int m'=2.                  \tag{5}
\]
例如取 \(a\) 不超过
\(\min(\inf\operatorname{supp}d_p+L,\inf\operatorname{supp}d_q+M)\)，
取 \(b\) 大于两支集上端。负端时所有负标签都取不到支集；正端时被排除的非负标签全部为零，原双侧平方分割给两份1。
尤其
\[
\|V\|=\sqrt2,\quad
V=V\,\mathbf1_{x\ge a},\quad
\|A(h)\|\le2\|h\|_1.                              \tag{6}
\]
这里的 \(\mathbf1_{x\ge a}\) 仅是证明用的时间支集投影；原 \(d_r\) 与 \(m\) 始终保持平滑。

必须区分去掉共同酉前后的乘积：
\[
\begin{split}
A(h)A(k)
 &=VU(h)M_mU(k)V^*\\
 &=K_\infty U(h)\mathcal W^*M_m\mathcal W U(k)K_\infty^*.
\end{split}                                                   \tag{7}
\]
一般不能在第二行省略两侧 \(\mathcal W\)；\(M_m\)通常不与这个时间卷积酉元交换。

## 2. 使用原平滑分割，乘积误差确为迹类

取 \(h,k\in C_c^\infty(\mathbb R)\)，并取 \(H>0\)，使两支集都包含于 \([-H,H]\)。
由时间卷积的乘法，
\[
A(h)A(k)-2A(h*k)
=VU(h)M_{m-2}U(k)V^*.                            \tag{8}
\]
右侧不能仅因 \(m-2\) 有常端值就称迹类；它在负端恒为 \(-2\)。
但实际 \(V\) 的支集给精确修复。

选 \(\eta\in C_c^\infty\) 在 \([a-H,b]\) 上恒为1，令
\(f=\eta(m-2)\in C_c^\infty\)。
若左时间变量 \(x\ge a\)，且 \(h(x-y)\ne0\)，则 \(y\ge a-H\)；
而 \(m(y)-2=0\) 对 \(y\ge b\) 成立。所以
\[
VU(h)M_{m-2}U(k)V^*=VU(h)M_fU(k)V^*.              \tag{9}
\]
这是有界算子的准确相等，不是渐近替换。

\(U(h)M_f\)的核为 \(h(x-y)f(y)\in C_c^\infty(\mathbb R^2)\)，故它属于 \(\mathcal S_1\)。
一个直接证明是将核支集包含在有限区间内部，用区间Fourier基展开：
光滑核的双Fourier系数比任意多项式更快衰减，绝对系数和有限；每个矩阵单位的迹范数为1，因而给绝对迹范数展开。
再乘有界 \(U(k),V,V^*\)，(9)仍迹类。
因此真实存在
\[
\boxed{A(h)A(k)=2A(h*k)+S_{h,k},\qquad
       S_{h,k}\in\mathcal S_1.}                   \tag{10}
\]
它没有删去混合群块，也没有使用sharp模型。

由于 \(h*k\in C_c^\infty\)、\(\mathcal S_1\)是有界算子双侧理想，426的
\[
\mathcal D=\{A(h)+S:\ h\in C_c^\infty,\ S\in\mathcal S_1\}
\]
对乘法闭合。\(A(h)^*=A(h^*)\)，\(h^*(s)=\overline{h(-s)}\)，所以它也是一个实际代数的自伴线性空间。
这是**代数乘法闭合**，没有称 \(\mathcal D\) 在算子范数中闭合或已经是C*代数。
此前426未支付这个乘法条件；(10)准确支付它。

## 3. 第一种计算：乘积误差的核迹

由(9)，\(B=U(h)M_fU(k)\)为时间迹类算子。
有界因子的合法循环给
\[
\operatorname{Tr}_{\mathcal H}(VBV^*)
=\operatorname{Tr}_{L^2}(BM_m).
\]
其光滑紧支核对角积分给
\[
\begin{split}
\operatorname{Tr}S_{h,k}
 &=\iint m(x)h(x-y)(m(y)-2)k(y-x)\,dy\,dx\\
 &=\int h(s)k(-s)F_m(s)\,ds,\\
F_m(s)&=\int m(x)[m(x-s)-2]\,dx.                 \tag{11}
\end{split}
\]
第一行中将 \(f(y)\)还原为 \(m(y)-2\)合法：
\(m(x)\ne0\)要求 \(x\ge a\)，而 \(h(x-y)\ne0\)要求 \(y\ge a-H\)，正是(9)覆盖的区间。
对每个有界的 \(s\)，\(F_m(s)\)的被积函数支撑在一个共同有限区间：
左端 \(m(x)=0\)，右端 \(m(x-s)-2=0\)。所以全部积分绝对收敛。

交换 \(h,k\)，并在时间变量作 \(s\mapsto-s\)，得到
\[
\operatorname{Tr}[A(h),A(k)]
 =\int h(s)k(-s)[F_m(s)-F_m(-s)]\,ds.             \tag{12}
\]
此交换子迹类也已由(10)直接证明，因为 \(h*k=k*h\)。
在第二个 \(F\)中平移积分变量，两项各自可积，故可逐点相减：
\[
\begin{split}
F_m(s)-F_m(-s)
 &=2\int[m(x-s)-m(x)]\,dx\\
 &=-2s\int m'(x)\,dx=-4s.
\end{split}                                                   \tag{13}
\]
最后一步可由
\(m(x-s)-m(x)=-\int_0^s m'(x-r)\,dr\)
及紧支 \(m'\)的Fubini直接证明，适用于正负 \(s\)。
由此
\[
\boxed{\operatorname{Tr}[A(h),A(k)]
       =-4\int_{\mathbb R}s\,h(s)k(-s)\,ds.}       \tag{14}
\]
系数4来自实际两个通道总frame密度2的平方；负号来自425的
\(\mathsf T_s\phi(x)=\phi(x-s)\)及负波形标签的正时间端。

## 4. 第二种计算：先在时间算子上计算边跳

定义时间交换误差
\[
C_{h,k}=U(h)M_mU(k)-U(k)M_mU(h).
\]
它的核为
\[
c(x,z)=\int\left[
h(x-y)m(y)k(y-z)-k(x-y)m(y)h(y-z)\right]\,dy.     \tag{15}
\]
这个核自身属于 \(C_c^\infty(\mathbb R^2)\)：

- 若 \(x\le a-H\)，所有许可 \(y\le a\)，所以两项全为0。
- 若 \(x\ge b+H\)，所有许可 \(y\ge b\)，所以(15)等于
  \(2[(h*k)(x-z)-(k*h)(x-z)]=0\)。
- 非零项还要求 \(|x-z|\le2H\)，故 \(z\)也有共同紧支界。

因此 \(C_{h,k}\in\mathcal S_1\)，不需要借助负端未经证明的迹范数极限。
又 \([A(h),A(k)]=VC_{h,k}V^*\)，合法循环与光滑核对角给
\[
\operatorname{Tr}[A(h),A(k)]
=\int h(s)k(-s)I_m(s)\,ds,\quad
I_m(s)=\int m(x)[m(x-s)-m(x+s)]\,dx.              \tag{16}
\]
该内积分的被积函数在左右两端都为0。
因 \(m'\)紧支，可在任意有界 \(s\)区间微分：
\[
\begin{split}
I_m'(s)
 &=-\int[m(x+s)m'(x)+m(x-s)m'(x)]\,dx\\
 &=-\int\frac{d}{dx}[m(x+s)m(x)]\,dx\\
 &=-\bigl(m(+\infty)^2-m(-\infty)^2\bigr)=-4.
\end{split}                                                   \tag{17}
\]
第二行在后一积分平移变量即可得到；导数被积函数紧支，边值准确为4和0。
\(I_m(0)=0\)，故 \(I_m(s)=-4s\)，独立复核(14)的方向、系数及分割形状无关性。
这里使用的是真实光滑 \(m\) 的边值跳跃，未将 \(m\)替换为阶跃函数。

## 5. 具体非零测试与全标量循环的阻断

取 \(r>\varepsilon>0\)、实值非零
\(\phi\in C_c^\infty(-\varepsilon,\varepsilon)\)，令
\[
h(s)=\phi(s-r),\qquad k(s)=h(-s).
\]
此时 \(A(k)=A(h)^*\)，且
\[
\operatorname{Tr}[A(h),A(h)^*]
=-4\int s\,h(s)^2\,ds<0.                         \tag{18}
\]
这完全使用允许的光滑紧支测试，适用于原任意平滑平方分割。

因此不存在 \(\mathcal D\)上同时满足以下两项的线性泛函：

1. 在 \(\mathcal S_1\)上等于普通迹；
2. 对每个 \(F,G\in\mathcal D\)满足 \(\tau(FG)=\tau(GF)\)。

因为(18)中的实际交换子已属 \(\mathcal S_1\)，第一项强制其读出为非零，第二项强制其为零。
这不是使用“交换子迹类便必然零迹”，恰恰给出了同源反例。
426的 \(\widetilde\Lambda\)及 \(\Psi_0\) 都仍为表达式无关的线性泛函，也仍对指定 \(\mathcal M_Q\)循环；
但它们在(18)上都按普通迹给同一个非零值，不能升级成全 \(\mathcal D\)标量迹。
不存在只靠选择 \(\Lambda\)或 \(\Psi_0\)解除这个障碍的办法。

## 6. 实际essential符号：不是乘积不闭，而是非平凡边异常

除(10)外，还可准确计算
\[
\boxed{\|A(h)\|_{\mathrm{ess}}=2\|\widehat h\|_\infty,\quad
\widehat h(\xi)=\int h(s)e^{-i\xi s}\,ds.}          \tag{19}
\]
上界由 \(\|V\|^2=2\)、Plancherel及(2)给出。
下界的证明保留原平滑分割：任取单位紧支时间向量
\(\psi\)，平移 \(\psi_n=\mathsf T_n\psi\)到充分正的时间端。
对大 \(n\)，\(\psi_n\)和 \(U(h)\psi_n\)的支集都落在 \(m=2\)区间。
令
\[
\xi_n=2^{-1/2}V\psi_n.
\]
则 \(\|\xi_n\|=1\)、\(\xi_n\rightharpoonup0\)，且
\[
\|A(h)\xi_n\|=2\|U(h)\psi\|.
\]
紧算子作用于 \(\xi_n\)的范数趋0，故essential范数至少为右侧。
紧支向量在 \(L^2\)中稠密；对其取卷积算子范数的近似极值即给(19)。

尤其
\[
A(h)\text{ 紧}\quad\Longleftrightarrow\quad h=0,\qquad
A(C_c^\infty)\cap\mathcal S_1=\{0\}.              \tag{20}
\]
若 \(\widehat h=0\)，Fourier唯一性给 \(h=0\)；其逆显然。
这比426(19)的必要条件更强，但不影响旧证明或旧读出。

所以每个 \(\mathcal D\)元素的 \(h\)部分实际上唯一，且
\[
\sigma:\mathcal D/\mathcal S_1\longrightarrow
\{\widehat h:h\in C_c^\infty\},\qquad
\sigma(A(h)+S)=2\widehat h                       \tag{21}
\]
是忠实的自伴代数符号映射。
由(10)，乘积在符号上是普通点乘：
\(\sigma(A(h)A(k))=4\widehat h\,\widehat k\)。
该商是交换的，完整代数却有(14)的非零普通迹异常。
因此本次没有发现非零essential乘积阻碍；准确结论是
**乘积在卷积符号商内闭合，其交换子在迹类层非平凡**。

若按essential范数完成这个符号商，其像是 \(C_0(\mathbb R_\xi)\)：
Fourier像自伴、对卷积乘法闭合、分离频率且每个频率有非零值，Stone–Weierstrass给在 \(C_0\)中稠密。
这只是已经明确的算子商完成，不是把 \(\mathcal S_1\)称为C*闭理想，也没有主张 \(\mathcal D\)自身已范数闭合。

## 7. 原T及已证明源乘子的商作用

426准确证明对
\[
\mathcal M_Q=\{c1+J:J=QJQ\in\mathcal B(\mathcal H)\}
\]
有 \(JA(h),A(h)J\in\mathcal S_1\)。
因此在(21)的商上，左、右乘任一此类 \(R=c1+J\)都只是标量 \(c\)：
\[
[RA(h)]=c[A(h)],\qquad[A(h)R]=c[A(h)].            \tag{22}
\]
原提升 \(T=1+Q(u-1)Q\)和 \(T^*\)的 \(c=1\)，所以它们在该商作用恒等。
这解释了426的源受限循环性为什么不足以选定 \(\Lambda\)：该源乘子作用已经在算术周期读出发生前的商中退化为单位，剩余差别只在实际截止／迹类边层。
而(14)表明，试图要求完整测试代数的普通标量循环会直接遇到非零边迹。

裸乘子酉元 \(u=1-e+v\)不属于已证明的 \(\mathcal M_Q\)类型。
本报告没有证明它左右保持 \(\mathcal D\)，更不能据(22)声称裸 \(u\)也在商上恒等；
必须另计算它的准入或使用原 \(Q\)压缩提升。该类型限制与426一致。

## 8. 研究含义与认证范围

本次支付了三个具体缺口：原采样的精确frame密度；测试乘积的实际 \(\mathcal S_1\)误差；全测试交换子的普通迹类准入及非零值。
结果没有推翻425的原周期有限部，也没有推翻426的 \(\mathcal M_Q\)受限循环。
它确定了后续桥的形状：若要把原有限部接成完整主关系/Chern读出，需要容纳实际边异常的相对或更高循环数据，普通标量迹扩张已经被(18)排除。

本报告无数值替代、无sharp分割替代、无未证明强极限与迹交换，也没有宣称Lean认证、全素数与实位Weil比较、算术正性或RH进展闭环。
主稿可采用(3)–(18)的严格局部结论；(19)–(22)给更强的商结构与源作用界限。
