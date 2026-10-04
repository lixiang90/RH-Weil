# 实际边／角相对链：强制传递、连续性障碍与加权源链退化

2026-10-04。独立推导草稿；接续 [423](../../notes/423-f1-twisted-radial-readout-and-mixed-period-obstruction.md)
及 [下一有限任务](f1-edge-corner-relative-chain-next-proof-plan.md)。
这里只构造并核验指定域内的相对 Hochschild 链、低次数循环比较及来源障碍；
尚未构造完整的周期循环 Chern 比较，不宣称主关系消失、RR 或 RH。

## 1. 四分量的实际平移模块

沿用 422 的 \(\mathcal A\)、\(\mathcal I\)、\(\mathcal M\) 及全部实际时间迹类定义域。
对固定标签 \(\gamma\)，令
\[
 \tau_\gamma(F)=\operatorname{Tr}_t\lambda_{pq}(F_\gamma),\quad
 \eta_{p,\gamma}(F)=\operatorname{Tr}_te_p(F_\gamma),\quad
 \eta_{q,\gamma}(F)=\operatorname{Tr}_te_q(F_\gamma),\quad
 \kappa_\gamma(F)=\operatorname{Tr}_t(F_\gamma)_c.
\]
后三项在 \(\mathcal I\) 上为零，因而是实际匹配边界代数上的连续泛函。
对 \(\beta_{(a,b)}\)，其列向量变换是
\[
 \begin{pmatrix}\tau\\\eta_p\\\eta_q\\\kappa\end{pmatrix}
 \longmapsto
 \begin{pmatrix}
 1&-a&-b&ab\\0&1&0&-b\\0&0&1&-a\\0&0&0&1
 \end{pmatrix}
 \begin{pmatrix}\tau\\\eta_p\\\eta_q\\\kappa\end{pmatrix}.       \tag{1}
\]
它等于 \(\exp(aN_p+bN_q)\)，其中 \(N_p^2=N_q^2=0\)、\(N_pN_q=N_qN_p\)，
\(N_p\) 的非零项是 \((1,2)=(3,4)=-1\)，\(N_q\) 的非零项是
\((1,3)=(2,4)=-1\)。所以角点的 \(ab\) 项是两条边变换的复合结果。

也可将四分量保留为实际多项式值泛函
\[
 \nu_\gamma(F;x,y)=\tau_\gamma(F)+x\eta_{p,\gamma}(F)
                           +y\eta_{q,\gamma}(F)+xy\kappa_\gamma(F).
\]
它严格满足
\[
 \nu_\gamma(\beta_{(a,b)}F;x,y)=\nu_\gamma(F;x-a,y-b).           \tag{2}
\]
这是有限部扣除起点的协变性；固定在 \(x=y=0\) 求标量值会失去该协变性。
不能把多项式值泛函称为一个已经不变的标量循环迹。

## 2. 任意连续标量不变修复的障碍

这里的结论不限于给 \(\tau_\gamma\) 添加有限多个 \(\eta_p,\eta_q,\kappa\)。

**命题。** 对每个 \(\gamma\ne0\)，不存在连续线性泛函
\(\Phi:\mathcal A\to\mathbb C\)，同时满足
\[
 \Phi|_{\mathcal I}(F)=\operatorname{Tr}(FW_\gamma),\qquad
 \Phi(\sigma_\gamma F)=\Phi(F),
 \quad W_\gamma=z_{-\gamma}\otimes1.
\] 
即使不要求 \(\Phi\) 是扭曲迹，该连续不变扩张也不存在。

证明：写 \(\gamma=(r,s)\)，\(\alpha=\sigma_\gamma^{-1}\)，固定时间秩一投影
\(P\)，\(\operatorname{Tr}P=1\)。令
\(F_k=H(j)\mathbf1_{k'=k}z_\gamma\otimes P\)。各 \(F_k\) 在每个固定
\(p_n\) 中有同一范数 \((1+|\gamma|_1)^n\)，故连续 \(\Phi\) 在这族上必须一致有界。
实际系数乘法给
\[
 \alpha(F_k)-F_{k+s}
   =[H(j-r)-H(j)]\mathbf1_{k'=k+s}z_\gamma\otimes P\in\mathcal I,
\]
且该开放理想项插入 \(W_\gamma\) 的普通迹为 \(-r\)。不变性强制
\[
                         \Phi(F_{k+s})-\Phi(F_k)=r.            \tag{3}
\]
当 \(r\ne0,s\ne0\) 时沿 \(k+Ns\) 迭代产生 \(Nr\) 的增长，违背一致有界。
当 \(r\ne0,s=0\) 时，(3) 直接矛盾。若 \(r=0,s\ne0\)，
用 \(\mathbf1_{j=j_0}H(k')z_\gamma\otimes P\) 交换两坐标，同样直接矛盾。
证明覆盖所有非零标签及任意连续边界补正，而不是仅覆盖格点起点调整。

另一个域内事实是
\[
                         \mathcal A^{\sigma_\gamma}=0
                         \quad(\gamma\ne0).                  \tag{4}
\]
对每个 \(E_2(\mathcal S_1)\) 系数，在任一有限坐标趋负无穷时，函数一致地趋零；
这直接由 422 的四分量展开及 \(\ell^1\) 余项得出。
沿非零平移轨道选一方向使某坐标趋负无穷，固定系数只能为零。
有限格点处全为零再强制两条边及角点极限为零，最后用群系数唯一性得到 (4)。

因此不能在当前域内通过平移平均生成非零固定时间测试。
例如 \(F=\mathbf1_{(j,k)=(0,0)}z_\gamma\otimes P\in\mathcal I\)，
其 \(2N+1\) 个平移的 Cesàro 平均点态趋零，但始终有
\(p_0=\tau_\gamma=1\)。它不在 \(\mathcal A\) 中收敛。
这不排除真正相对数据，也不否定带新拓扑或新几何输入的对象。

## 3. 使用实际匹配边界的乘子链复形

令 \(\mathcal B=\mathcal A/\mathcal I\)，按 422 将其识别为两条实际限制
\(F_p,F_q\) 在双无穷角点匹配的代数。
对 \(\mathcal M\) 也取同样两条正无穷限制，其像记为 \(\mathcal M_\partial\)。
边上的径向系数属于 \(D_1\)，角点相同；\(\mathcal B\) 是该边界乘子像的理想。
限制乘法是实际系数乘法，不将负尾乘子核误认为只有开放 \(\ell^1\) 理想。

在本节只使用有限个代数张量，每个张量因子都是已经准入的实际算子。
定义 \(X_n\subset\mathcal M^{\otimes(n+1)}\) 为至少一个腿在 \(\mathcal A\) 的张量和，
\(Y_n\subset\mathcal M_\partial^{\otimes(n+1)}\) 为至少一个腿在 \(\mathcal B\) 的张量和。
限制给满射 \(q_n:X_n\to Y_n\)，其中 \(X_0=\mathcal A,Y_0=\mathcal B\)。
令 \(\alpha=\sigma_\gamma^{-1}\)，并采用
\[
 b_\alpha(a_0\otimes\cdots\otimes a_n)
 =\sum_{i=0}^{n-1}(-1)^i
 a_0\otimes\cdots\otimes a_i a_{i+1}\otimes\cdots\otimes a_n
 +(-1)^n\alpha(a_n)a_0\otimes a_1\otimes\cdots\otimes a_{n-1}.
                                                                  \tag{5}
\]
\(b_\alpha\) 保持至少一个迹类腿，因 \(\mathcal A\) 是 \(\mathcal M\) 的理想。
结合律及 \(\alpha\) 的乘法性直接给 \(b_\alpha^2=0\)，限制与它交换。
特别地，本稿使用的三腿边界符号严格是
\[
 b_\alpha(A\otimes B\otimes K)
 =AB\otimes K-A\otimes BK+\alpha(K)A\otimes B.                 \tag{5a}
\]
再用 \(b_\alpha(A\otimes B)=AB-\alpha(B)A\) 展开，
\(ABK\)、\(\alpha(K)AB\)、\(\alpha(B)\alpha(K)A\) 各自两两抵消。
每个需要求 \(\tau_\gamma\) 的乘积仍在 \(\mathcal A\)；这正是允许
\(T^*\) 作为乘子腿、\(TK_h\) 作为迹类腿的准入。
这里没有声称这些乘子本身时间迹类。

标准 \(E_\gamma=b_\alpha\tau_\gamma\) 在 \(X_1\) 上有定义，并下降为
\(\overline E_\gamma:Y_1\to\mathbb C\)。理由是 423 的
\(E=D+\Delta_\gamma\tau_\gamma(\alpha(B)A)\) 中两项都只依赖乘积的实际两条边及角点。
若一个乘子腿的两边限制为零，所有相应边／角乘积为零；若迹类腿在
\(\mathcal I\)，则普通插入迹循环直接给零。
因此下降不只依赖某个有限维形式模型，而来自实际限制映射。

扭曲方向同 423 及
[Rennie–Sitarz–Yamashita 的 Definition 2.1](https://rennieillawarramath.com/website-pdfs/JournalArticles/2013RSY-Prepub.pdf)
中的“末因子移到首位”约定一致。本稿的映射锥公式在下面逐项证明；
不以一般循环理论自动宣布它是完整循环 Chern 配对。

## 4. 实际相对映射锥与强制配对

取链映射 \(q:X_\bullet\to Y_\bullet\) 的锥，约定
\[
 \operatorname{Cone}_n(q)=X_n\oplus Y_{n+1},\qquad
 \partial(x,y)=(b_\alpha x,qx-b_\alpha y).                       \tag{6}
\]
由 \(qb=bq\) 直接得到 \(\partial^2=0\)。
一个相对零循环满足
\[
                 x\in\mathcal A,\quad y\in Y_1,\quad
                 qx=b_\alpha y.
\]
实际配对是
\[
                 \Omega_\gamma(x,y)
                 =\tau_\gamma(x)-\overline E_\gamma(y).        \tag{7}
\]
它在每个锥边界上为零：若边界为
\((b_\alpha z,qz-b_\alpha w)\)，则
\(\tau(bz)=\overline E(qz)\)、\(\overline E(bw)=0\)，后者来自 \(b^2=0\)。
故这是合法的相对 Hochschild 配对。它保留真实开放理想迹。

对任意已准入 \(A\in\mathcal M,B\in\mathcal A\)，
\[
 z_E=A\otimes B,\quad x_E=AB-\alpha(B)A,
 \quad (x_E,qz_E)=\partial(z_E,0).
\]
于是
\[
                         \Omega_\gamma(x_E,qz_E)=0.             \tag{8}
\]
这项边界修正来自同一提升的边界方程，消掉所有原始 \(E\) 数值；
不能只取其中抵消混合周期的一部分。

还有精确的自由度分类。若 \(y=qz\) 固定，而 \((x,y)\) 是任意相对循环，
则
\[
 i=x-b_\alpha z\in\mathcal I,\qquad
 \Omega_\gamma(x,y)=\operatorname{Tr}(iW_\gamma).                \tag{9}
\]
这只使用 \(\ker q_0=\mathcal I\)，不需要假设高次限制核等于某个粗略的张量理想。
其余相对循环也可先选 \(y\) 的实际提升得到同一表达。
因此本稿没有否定非平凡相对类；它指出非零值必须由一个独立来源确定的开放理想类支付。
将 \(i\) 自由取为所需 \(A_N(h)\) 并不是主关系的同源比较。

## 5. 包含 \(\Delta\) 的显式单位链传递

不仅标准 \(E\) 有 (8)，原始 \(D\) 也能给出正确方向的强制传递。
对同一 \(A,B\)，令
\[
 z_D=A\otimes B-1\otimes B\sigma_\gamma(A),\qquad
 x_D=AB-B\sigma_\gamma(A).
\]
第二项的第二腿仍在 \(\mathcal A\)，第一腿是合法乘子单位。
按实际群乘法计算，不把右侧系数保持在未平移位置：
\[
 b_\alpha z_D
 =AB-\alpha(B)A-B\sigma(A)+\alpha(B\sigma(A))
 =AB-B\sigma(A)=x_D.                                         \tag{10}
\]
于是 \((x_D,qz_D)\) 也是锥边界，且
\[
 \overline E_\gamma(qz_D)
 =E_\gamma(A,B)-E_\gamma(1,B\sigma(A))
 =D_\gamma(A,B),\qquad
 \Omega_\gamma(x_D,qz_D)=0.                                   \tag{11}
\]
其中
\(E_\gamma(1,B\sigma A)=\Delta_\gamma\tau_\gamma(\alpha(B)A)\)，
正是 423 的不变性异常，不是按目标原子选择的补偿。

取 \(A=T^*,B=TK_h\)，上述全部链属于实际乘子／迹类腿域。
对 423 的下过渡见证，原始 \(D>0,E=2D>0\)，但 (8)、(11) 的完整相对值均为零。
平台测试原本就是 \(D=E=0\)，修正仍为零。
纯 \(p\)、纯 \(q\)、单位及其他混合标签都由同一恒等式归零。
所以这给出合法且自然的一个直接版本，但它没有选择性恢复正确周期分布。

实际条带也被保留。写 \(R=\sigma(T)-T\)，则
\[
 \sigma(T^*)-T^*=R^*,\qquad
 B\sigma(T^*)=BT^*+BR^*.
\]
\(BR^*\in\mathcal A\)，其双无穷角点为零，通常仍有两边分量。
因此 (10) 的单位链中确实包含该原提升条带；没有把 \(R\) 宣布为开放理想零项。
同样 \(\sigma(K_h)-K_h=(\beta_{-\gamma}Q-Q)\otimes M_dU(h)M_d\) 是实际测试条带。

## 6. 原点、平移及低次数循环比较均由边界方程控制

令 \(\delta_\gamma\) 为 \(\mathcal B\) 上的实际泛函
\[
 \delta_\gamma=\gamma_1\eta_{p,\gamma}
              +\gamma_2\eta_{q,\gamma}
              +\gamma_1\gamma_2\kappa_\gamma.
\]
则
\[
 \sigma^*\tau_\gamma-\tau_\gamma=q^*\delta_\gamma,
 \qquad \sigma^*\overline E_\gamma-\overline E_\gamma
                      =b_\alpha\delta_\gamma.                 \tag{12}
\]
对相对循环 \(qx=by\)，两式强制
\[
 \Omega_\gamma(\sigma x,\sigma y)-\Omega_\gamma(x,y)
 =\delta_\gamma(qx)-\delta_\gamma(by)=0.                       \tag{13}
\]
所以相对配对的不变性无需一个不存在的连续标量不变扩张。
它由明确边界链同伦支付；这仍不等于一个完整的 \((b,B)\) 周期循环构造。

改变格点扣除起点 \((u,v)\) 时，令
\(\theta_{u,v}=u\eta_p+v\eta_q+uv\kappa\)。按 422 的真实有限部公式，
\(\tau^{u,v}-\tau=q^*\theta_{u,v}\)，
\(E^{u,v}-E=b_\alpha\theta_{u,v}\)。故 (7) 在每个合法相对循环上不变。
混合角点项不能省掉，否则这项自然性不成立。
若改变允许的 \(c,d\)，上述直接源链仍始终是由 (8) 或 (10) 给出的锥边界，
其零值也由同一链方程控制，未通过调节 \(c,d\) 选定目标权重。

还能逐项核验一次扭曲循环移位的比较。令
\(t_\alpha(A\otimes B)=-\alpha(B)\otimes A\)。直接计算
\[
 b_\alpha z-b_\alpha t_\alpha z=(1-\alpha)(AB),\qquad
 E_\gamma(z)-E_\gamma(t_\alpha z)
                             =\tau_\gamma((1-\alpha)(AB)).     \tag{14}
\]
若相对循环写为 \((x,qz)\)，则
\[
 (x-(1-\alpha)(AB),qt_\alpha z)
\]
仍是相对循环，且 (7) 的值相同。
当换用另一提升时，其额外乘积在 \(\mathcal I\) 中，\(\tau_\gamma\) 在该理想上
的 \(\alpha\) 不变性保证这次比较的数值不受影响。
这是一项实际低次数循环传递，不能据它省去高次链方程。

## 7. 实际时间测试破坏角点源循环；自然对称修复丢失源类

双无穷角点上的 \(\alpha\) 是恒等作用。原源 \(u\) 是真实单位酉，
所以未加权链 \(u^*\otimes u\) 的 Hochschild 边界为零；
但它没有迹类腿，不在本稿的测试求迹域中。
插入允许的时间算子 \(k=M_dU(h)M_d\) 后，
\[
             b(u^*\otimes uk)=k-uku^*.                        \tag{15}
\]
该算子一般非零。只有普通时间迹为零并不能使它成为一个链循环。
角点为零的纯边／条带链修正也不能消去这个非零角点边界。

这里有完全绑定原测试的见证。在角点参数 \(\zeta=(1,1)\) 处，
选圆周 \(\mathbb R/L\mathbb Z\) 上非零实非负光滑 \(\varphi\)，
其很小支集与向 \(M\) 的旋转支集不交。这可行，因为 \(M/L\) 非整数。
置 \(d(t)=c(t)\varphi([t])\)，并选 \(h\in C_c^\infty\) 在
\(\operatorname{supp}d-\operatorname{supp}d\) 上恒为 1。
则实际核恒等式给
\[
 k=M_dU(h)M_d=|d\rangle\langle d|.
\]
平方分割逐项给 \(ed=d\) 及
\[
 ud=vd=c(t)\varphi([t-M]).
\]
两个向量非零且正交：其内积由平方分割等于圆周上
\(\int_0^L\varphi(r)\varphi(r-M)dr=0\)。
所以 (15) 是两个正交秩一算子之差，严格非零。
单个参数评价为非零已足以证明形式角点代数中的边界非零。

自然的对称闭链确实存在：
\[
 z_{\rm sym}=u^*\otimes uk-ku^*\otimes u,\qquad bz_{\rm sym}=0.
\]
但结合律强制
\[
 b(u^*\otimes u\otimes k)
 =1\otimes k-u^*\otimes uk+ku^*\otimes u,
 \quad z_{\rm sym}=1\otimes k-b(u^*\otimes u\otimes k).        \tag{16}
\]
故这项角点 Hochschild 类只等于单位测试链，与 \(u\) 无关。
它不能被登记为保留原源主关系的加权 Chern 比较。

实际提升上同一准确公式是
\[
 Z_{\rm sym}=T^*\otimes TK_h-\alpha(K_h)T^*\otimes T
            =(T^*T)\otimes K_h
                     -b_\alpha(T^*\otimes T\otimes K_h).       \tag{17}
\]
所有链都有一个实际迹类腿，群乘法完整平移所有右侧系数。
在角点 \(T^*T=1\)，式 (17) 回到 (16)；
原源依赖留在 \((T^*T-1)\otimes K_h\) 的边界部分。
它还没有被构造为一个独立、非平凡、具有算术归一化的完整相对 Chern 类。
本节只排除这项直接加权及对称闭链修复，不排除更高次数或不同时间传递。

实际 \(p\) 边也给出提升非酉的直接见证。在 \(p=\infty\) 后只剩 \(q\) 径向坐标，
记 \(H=H(k)\)。原 Green 投影 \(e\) 的 \(q\) 标签为零，故 \(eH=He\)；
原 \(v\) 的 \(q\) 标签为 \(+1\)，且 \(v^*v=vv^*=e\)。
因此 \(HvH=vH\)。令 \(E=He,V=HvH\)，则
\[
 V^*V=E,\qquad VV^*=H(k-1)e,
 \qquad T_p=1-E+V.
\]
\(V\) 的初、末投影均在 \(E\) 中，所以与 \(1-E\) 的交叉项消失，给
\[
 T_p^*T_p=1,\qquad T_pT_p^*=1-\mathbf1_{k=0}e.                 \tag{17a}
\]
端点 Green 投影非零。因此角点单位酉 \(u\) 的原提升在完整两边匹配商中不是酉元，
不能把其角点 Chern 循环直接登记成该更大商中的酉源循环。

## 8. 与原全群算子的精确范围

固定 \(N\) 时，原全部外部群和 \(A_N(h)\) 在 \(\mathcal I\) 中绝对收敛，
因此 \(\delta_\gamma,D_\gamma,E_\gamma\) 的边界值均为零。
对上面两个直接相对源链，所有 \(N\) 的同一配对数值严格为零，
不能把这条零序列的普通极限宣布成非零周期项。

作为另一个、已经存在的理想循环，\((A_N(h),0)\) 当然允许非零值。
对 \(\gamma=0\)，准确归一化是
\[
 \frac12\Omega_0(A_N(h),0)=D_Nh(0)
 +L\sum_{a\ne0}\rho_p^{|a|}h(-aL)
 +M\sum_{b\ne0}\rho_q^{|b|}h(-bM).
\]
这里保留原两轴无限群和、\(D_N\) 和原壳层权重；该 \(1/2\) 不能与另一个有限位半迹因子混同。
但从 (9) 自由把这一个理想循环加到直接源边界上，只会按定义产生原周期分布，
没有证明它由源 \(u\) 的主关系强制产生。

本轮得到的有限结论是：一个使用实际匹配边界和原条带的合法 Hochschild 相对链；
完整边界方程强制其直接两因子版本归零；任意连续标量不变扩张的新增障碍；
以及实际加权角点 Chern 链不闭、自然对称闭链源类退化的见证。
下一项若要产生非零算术比较，必须独立构造并核验一个非平凡相对 Chern 类或时间传递，
指出 (9) 中的理想类如何来自原源及实际壳层，而非自由指定。
这些结论没有否定所有高次相对理论，也没有推进到全局 Weil 正性或 RH 结算。
