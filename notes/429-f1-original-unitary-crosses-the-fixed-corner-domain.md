# 429. 原源酉元跨出固定角点域的实际非紧边障碍

2026-10-04。继续[427](427-f1-corner-product-algebra-and-unavoidable-trace-cocycle.md)、
[428](428-f1-corner-essential-symbol-and-complete-readout-freedom.md)。
此前源T在符号商上仅为单位。本稿在完整原物理表示中证明真正酉元u不保持该域，
并给它移出的具体负p、q=1边。即使作算子范数完成，障碍仍在；不能用迹类补偿支付这项准入。
没有据此否定扩大后的几何或相对Chern构造。

## 1. 保留完整物理表示及原源

固定不同素数p、q，\(L=\log p,M=\log q\)。在原
\(\mathcal H=\ell^2(\mathbb Z^2)\otimes L^2(\mathbb R)\) 上，
\[
 P_{(a,b)}=\lambda_{a,p}\otimes\lambda_{b,q}\otimes\mathsf T_{aL+bM},
 \qquad\mathsf T_s\psi(t)=\psi(t-s).
\]
414的原非负平滑平方分割c满足 \(\sum_a c(t-aL)^2=1\)，\(\int c^2=L\)。
沿用原规定 \(d_p=c\)，\(d_q\) 是另一个M周期平方分割。
令
\[
 e=\sum_a M_{c(t)c(t-aL)}P_{(a,0)},\qquad
 v=\sum_a M_{c(t)c(t-aL-M)}P_{(a,1)},\qquad u=1-e+v.         \tag{1}
\]
两和的非零系数有限。原Green计算给 \(e=e^*=e^2\)、\(v^*v=vv^*=e\)，所以u酉。
T是另一个对象 \(T=1-Q+QuQ\)，不能把两者的域条件混同。
以下仅作425的波形酉基变换，不对角点或环面取字符评价，时间作用不变。

## 2. 深负边的准确矩阵元

令固定角点的支撑投影
\[
 E=(R_p^-\otimes W_q+W_p\otimes R_q^-)\otimes1_t,
 \qquad A(h)=EA(h)E.
\]
定义等距时间嵌入
\[
 I_n^j\psi=w_{-n,p}\otimes w_{j,q}\otimes\psi,
                        \qquad n\ge1,\ j\in\mathbb Z.       \tag{2}
\]
\(I_n^0\) 属于E，\(I_n^{\pm1}\) 属于 \(1-E\)，不同n互相正交。
425的采样矩阵元给
\[
 I_i^{0*}A(h)I_j^0=M_c\mathsf T_{(j-i)L}U(h)M_c,
                              \qquad i,j\ge1.               \tag{3}
\]
它保留原全部算子，只通过所选行列把其他通道排除。
取N大于(1)全部可能非零p次数的绝对值。\(n>N\) 时源的有限平移仍在严格负p边，
下面等式均精确成立，而非只在n极限中成立。

设
\[
 B_a(h)=M_c\mathsf T_aU(h)M_c,
 \quad B_a(h)(t,t')=c(t)h(t-t'-a)c(t').                      \tag{4}
\]
光滑紧支核或Fourier秩一积分给 \(B_a(h)\in\mathcal S_1\)，且
\[
                              \operatorname{Tr}B_a(h)=Lh(-a). \tag{5}
\]

## 3. 真源产生非紧的新输出边

向 \(I_n^1\) 输出只能由v作用于A的p边产生；A的输出始终在E内，
所以 \(I_n^{1*}A(h)uI_n^0=0\)。由(1)、(3)
\[
\begin{split}
 I_n^{1*}uA(h)I_n^0
 &=\sum_a M_{c(t)c(t-aL-M)}\mathsf T_{aL+M}
                    M_c\mathsf T_{-aL}U(h)M_c\\
 &=M_c\left(\sum_a c(t-aL-M)^2\right)\mathsf T_MU(h)M_c
 =B_M(h).
\end{split}                                                  \tag{6}
\]
外侧c因子使原有限非零系数以外的项本已为零，所以使用完整平方和没有改变原源。
于是
\[
                             I_n^{1*}[u,A(h)]I_n^0=B_M(h).  \tag{7}
\]
若 \(B_M(h)\ne0\)，选固定单位ψ使 \(\|B_M(h)\psi\|>0\)。
\(x_n=I_n^0\psi\) 是正交单位向量列，弱趋零；(7)给交换子在这些向量上的范数共同正下界。
因此
\[
              B_M(h)\ne0\Longrightarrow [u,A(h)]\text{非紧}. \tag{8}
\]
\(h(-M)\ne0\) 由(5)保证该条件，给明确合法测试。

## 4. 左右域准入均失败，且不能靠范数完成修复

现有 \(\mathcal D=A(C_c^\infty)+\mathcal S_1\) 中每个F满足
\[
                     (1-E)F,\ F(1-E)\in\mathcal S_1.        \tag{9}
\]
由(6)，\((1-E)uA(h)\) 非紧，故 \(uA(h)\notin\mathcal D\)。
不是仅凭uA非紧作这个结论；A本来就非紧，必要条件是(9)的支撑。

右侧独立计算：\(I_n^{-1}\) 经 \(1-e\) 仍为双负输入，A将其消去；
v把q次数−1移到0，投影到 \(I_n^0\) 时由(3)给完整时间核
\[
 (I_n^{0*}A(h)uI_n^{-1})(t,t')
 =c(t)h(t-t'-M)c(t')\sum_a c(t'+aL+M)^2
 =B_M(h)(t,t').                                             \tag{10}
\]
因此 \(A(h)u(1-E)\) 也非紧，\(A(h)u\notin\mathcal D\)。
同理 \((1-E)[u,A(h)]=(1-E)uA(h)\) 非紧，故交换子也不属于D。

对428的 \(\mathcal E=\overline{\mathcal D}^{\|\cdot\|}\)，(9)的范数极限只可能变成紧算子，
因为紧算子范数闭。因此当 \(B_M(h)\ne0\) 时
\[
                  uA(h),\ A(h)u,\ [u,A(h)]\notin\mathcal E. \tag{11}
\]
所以u也不是该新C*代数E的双侧乘子；并非只欠一个更弱的LF拓扑完成。

## 5. 加权真源式的q=1对角块

u酉，故
\[
                  [u^*,uA(h)]=A(h)-uA(h)u^*=-[u,A(h)]u^*.   \tag{12}
\]
在 \(I_n^1\) 输入上，只有右v*先回到q=0负p边；输出q=1又只能由左v产生。
必须保留原右伴随的平移：
\[
              v_a^*=M_{c(t)c(t+aL+M)}P_{(-a,-1)}.            \tag{13}
\]
左v次数r、右v*次数s之间A的p位移是 \(s-r\)。对 \(n>N\) 直接用(3)、(13)，
其有限双和核准确为
\[
 c(t)h(t-t')c(t')\sum_r c(t-rL-M)^2\sum_s c(t'-sL-M)^2
                         =c(t)h(t-t')c(t').                 \tag{14}
\]
于是
\[
 I_n^{1*}uA(h)u^*I_n^1=B_0(h),\qquad
                 I_n^{1*}[u^*,uA(h)]I_n^1=-B_0(h).          \tag{15}
\]
若 \(h(0)\ne0\)，则 \(\operatorname{Tr}B_0(h)=Lh(0)\ne0\)，用正交单位向量列证明该加权式非紧。
其 \((1-E)\) 部分也非紧，故该式及 \(uA(h)u^*\) 都不属于D或其范数完成E。
这也证明 \(\operatorname{Ad}u\) 不保持E。
另由(12)，\(h(-M)\ne0\) 时同样有非紧性及域否定。
一个合法光滑紧支h可以同时满足 \(h(0)>0,h(-M)>0\)，见证所有这些障碍。

## 6. 原T的商作用没有代表真源u

426的 \(\mathcal M_Q\) 乘子 \(R=\alpha1+QJQ\) 在
\(\mathcal D/\mathcal S_1\) 上左右作用都只是标量α；特别T作用为单位。
u却实际搬出E，并产生(6)和(10)中的非紧耦合。
不能先在这个商给u指定作用，再称它为原源导出的Chern比较。

要纳入真源，扩大域至少须包含负p、q=1输出边，以及右侧双负输入到原边的耦合。
它们非紧、非迹类，不能只添加S₁补偿。
之后还须处理u、u*继续搬移产生的边族、物理球截止及427的商余圈。
本稿没有给这些新元素预设读出，也没有把任何一个扩大域断言为不可能。

完整物理核推导见[原源域障碍报告](../reviews/2026-10-04/f1-original-unitary-corner-domain-obstruction.md)。
下一有限任务是构造真源保持的实际边域及规范相对链，检验它如何携带非零循环余圈并选出原周期读出。
完整算术主关系、Weil正性、实位／全素数比较、RR及RH仍未证明。
