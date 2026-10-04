# 425. 原几何壳层的固定正角算子与纯周期有限部比较

2026-10-04。接续[424](424-f1-relative-chain-repair-and-four-component-obstruction.md)，直接回到[412](412-f1-transverse-compression-and-periodic-traces.md)、[414](414-f1-deep-boundary-unitary-and-time-defect.md)的原几何壳层。
本稿构造一个固定有界算子，证明其实际截断迹与原半壳层迹完全相等，并给出自然负端体积扣除后的两有限位周期分布。
这是指定两素数的算子／迹比较；不是主关系消失、完整Weil公式、RR、正性或RH证明。

## 1. 原球向量、真实壳层和固定平移方向

对一位 \(r\in\{p,q\}\)，置 \(D_r=\log r\)、\(\rho_r=r^{-1/2}\)、
\(c_r=\sqrt{1-\rho_r^2}\)。在原径向基 \(e_j\) 上写
\(\lambda_a e_j=e_{j+a}\)。412的 \(V_a\) 等于 \(\lambda_{-a}\)，
414物理群表示中的 \(V_{-a}\) 因而就是本稿 \(\lambda_a\)。
令
\[
 b_N=c_r\sum_{m\ge0}\rho_r^m e_{N+m},\qquad
 R_N=\sum_{j=-N}^{N-1}P_{e_j}+P_{b_N}.                       \tag{1}
\]
这是来自Haar与紧单位平均的原投影，\(\operatorname{rank}R_N=2N+1\)。由
\(b_N=c_re_N+\rho_rb_{N+1}\)，有
\[
 w_N=\rho_re_N-c_rb_{N+1}=\lambda_Nw_0,\quad
 S_N=R_{N+1}-R_N=P_{e_{-N-1}}+P_{w_N}.                       \tag{2}
\]
\(w_N\) 与 \(b_N\) 正交。其零起点系数为
\[
 w_0(0)=\rho_r,\qquad
 w_0(j)=-(1-\rho_r^2)\rho_r^{j-1}\ (j\ge1),\qquad
 w_0(j)=0\ (j<0).                                          \tag{3}
\]
在 \(e_j\leftrightarrow z^j\) 的Fourier识别中，\(w_0\) 对应
\[
                   B_r(z)=\frac{\rho_r-z}{1-\rho_r z}.        \tag{4}
\]
\(|B_r(z)|=1\) 在单位圆上成立，因此 \(w_n=\lambda_nw_0\) 是完整正交基。
这给两个重要恒等式：
\[
 W_r=P_{w_0},\quad
 R_r^-=\sum_{j<0}P_{e_j}+P_{b_0}
       =\sum_{n<0}P_{w_n},\qquad R_r^-W_r=0.                 \tag{5}
\]
后一等式可直接证明：\(w_n\) 的负坐标部分有限，非负尾为 \(b_0\) 的倍数，故 \(n<0\) 时属于左边像；
对 \(n\ge0\)，\(w_n\) 的支集非负且与 \(b_0\) 正交，故属于左边正交补。完整性给(5)。

## 2. 从原秩二壳层提取正角，而非添加目标原子

定义
\[
 R_{K,r}^-=\sum_{j=-K}^{-1}P_{e_j}+P_{b_0},\qquad K\ge0.
\]
直接平移(1)–(2)得
\[
 \lambda_{-N}R_N\lambda_N=R_{2N}^-,\quad
 \lambda_{-N}S_N\lambda_N=P_{e_{-2N-1}}+W_r.                  \tag{6}
\]
取原414的平方分割 \(d_p,d_q\in C_c^\infty(\mathbb R)\)，实值且
\[
 \sum_n d_p(t-nL)^2=\sum_n d_q(t-nM)^2=1,\quad
 \int d_p^2=L,\quad\int d_q^2=M,\quad L=\log p,\ M=\log q.    \tag{7}
\]
原截止是
\(C_N=R_{N_p,p}\otimes S_{N_q,q}\otimes M_{d_p}
       +S_{N_p,p}\otimes R_{N_q,q}\otimes M_{d_q}\)。
用实际乘子酉元
\(Z_N=\lambda_{-N_p}\otimes\lambda_{-N_q}\otimes1\) 重定位，得到四个正交通道。
其中两个正角通道为
\[
 C_N^+=R_{2N_p,p}^-\otimes W_q\otimes M_{d_p}
           +W_p\otimes R_{2N_q,q}^-\otimes M_{d_q}.            \tag{8}
\]
另两个通道把相应 \(W_r\) 换成 \(P_{e_{-2N_r-1}}\)。所有正交性由(5)及负原子的支集给出。
所以(8)是原壳层的实际子通道。原秩二壳层的二分来自(2)，没有从目标分布指定 \(1/2\)。

物理时间取 \(\mathsf T_s\phi(t)=\phi(t-s)\)，
\(U(h)=\int h(s)\mathsf T_s\,ds\)，\(h\in C_c^\infty(\mathbb R)\)。固定
\[
 P_{(a,b)}=\lambda_a\otimes\lambda_b\otimes\mathsf T_{aL+bM}.
\]
有限 \(N\) 的正角算子定义为
\[
 A_N^+(h)=\sum_{g\in\mathbb Z^2}C_N^+P_gU(h)C_N^+.           \tag{9}
\]
各有限基由负原子、球向量和波形组成，矩阵元在群位移中有常数乘
\(\rho_p^{|a|}\rho_q^{|b|}\) 的界，常数允许依赖 \(N\)。时间块
\(M_{d_r}\mathsf T_\ell U(h)M_{d_s}\) 的迹范数统一不超过
\(\|\widehat h\|_1\|d_r\|_2\|d_s\|_2/(2\pi)\)。
沿414的有限基／Fourier秩一积分证明，(9)在迹范数中绝对收敛。
这不假定未压缩的 \(\sum_gP_g\) 有界。

## 3. 固定极限的有界采样定义

候选固定截止为
\[
 C_\infty=R_p^-\otimes W_q\otimes M_{d_p}
                 +W_p\otimes R_q^-\otimes M_{d_q}.           \tag{10}
\]
不能把 \(C_\infty\sum_gP_gU(h)C_\infty\) 作为未经证明的定义。
下面直接定义有界采样算子 \(K_\infty:L^2(\mathbb R)\to
\ell^2(\mathbb Z^2)\otimes L^2(\mathbb R)\)。令
\[
 \mathcal W_r=(\rho_r-\mathsf T_{D_r})(1-\rho_r\mathsf T_{D_r})^{-1},
 \quad \mathcal G_r=c_r(1-\rho_r\mathsf T_{D_r})^{-1}.          \tag{11}
\]
Neumann级数在范数中收敛；(4)或直接乘法给 \(\mathcal W_r\) 酉，且
\(\|\mathcal G_r\|^2\le(1+\rho_r)/(1-\rho_r)=:\mathsf B_r\)。定义
\[
\begin{split}
 (K_\infty\phi)(t)={}&d_p(t)\left[
   \sum_{j<0}e_{j,p}\otimes w_{0,q}(\mathcal W_q\phi)(t-jL)
   +b_{0,p}\otimes w_{0,q}(\mathcal G_p\mathcal W_q\phi)(t)\right]\\
 &+d_q(t)\left[
   \sum_{k<0}w_{0,p}\otimes e_{k,q}(\mathcal W_p\phi)(t-kM)
   +w_{0,p}\otimes b_{0,q}(\mathcal G_q\mathcal W_p\phi)(t)\right].
\end{split}                                                        \tag{12}
\]
平方分割给任意 \(\psi\in L^2\)
\[
 \sum_{j<0}\int d_p(t)^2|\psi(t-jL)|^2dt\le\|\psi\|_2^2,     \tag{13}
\]
q同理。两大通道互相正交，各自的负原子部分和球部分也正交。因此(12)在整体Hilbert范数中收敛，且
\[
 \|K_\infty\|^2\le2+\|d_p\|_\infty^2\mathsf B_p
                       +\|d_q\|_\infty^2\mathsf B_q=:C_*.    \tag{14}
\]
现在定义实际固定算子
\[
 A_\infty(h)=K_\infty U(h)K_\infty^*,\quad
                     \|A_\infty(h)\|\le C_*\|h\|_1.          \tag{15}
\]
形式采样 \((\Omega\phi)(j,k,t)=\phi(t-jL-kM)\) 本身通常无界；
(12)只是在压缩后实现 \(C_\infty\Omega\)，没有将 \(\Omega\) 当作有界算子使用。

## 4. 精确截断恒等式和强星极限

给 \(K_p,K_q\ge0\)，取实际下截止
\[
 \mathsf P_{K_p,K_q}=\mathbf1_{j\ge-K_p,\ k\ge-K_q}\otimes1.
\]
它没有上截止，也不是整个Hilbert空间的有限秩投影。球、波形支撑均在非负坐标，故
\[
 \mathsf P_{K_p,K_q}C_\infty=C_\infty\mathsf P_{K_p,K_q}
 =R_{K_p,p}^-\otimes W_q\otimes M_{d_p}
                      +W_p\otimes R_{K_q,q}^-\otimes M_{d_q}. \tag{16}
\]
将(12)负原子和截到 \(j\ge-K_p,k\ge-K_q\) 得有界 \(K_{K_p,K_q}=\mathsf P_{K_p,K_q}K_\infty\)。
其核可直接比较：形式 \(\Omega U(h)\Omega^*\) 的径向矩阵元 \((m,n)\) 是
\(h(t-t'-\ell_{m-n})\)，恰对应唯一群标签 \(g=m-n\)。
压缩基的几何尾和时间紧支允许此核比较；第2节的绝对迹范数证明使有限压缩完全等于(9)。因此
\[
 A_N^+(h)=\mathsf P_{2N_p,2N_q}A_\infty(h)\mathsf P_{2N_p,2N_q}. \tag{17}
\]
两坐标各自趋于无穷时 \(\mathsf P\to1\) 强收敛；由有界因子分解，(17)强星收敛到(15)，
不要求 \(N_p/N_q\) 有界，也没有交换未压缩的群和与迹。
这里证明的是选出的正角通道；不以 \(C_N\) 的裸强极限推论原算子的迹。

## 5. 完整混合算子保留，域却不再是422的快速绝对和

在(5)的 \(w_n\) 基中，设
\(E_p^\infty=R_p^-\otimes W_q\)、\(E_q^\infty=W_p\otimes R_q^-\)。
同通道 \(E_p^\infty(\lambda_a\otimes\lambda_b)E_p^\infty\) 只在 \(b=0\) 非零，q同通道只在 \(a=0\) 非零。
交叉p←q块只在 \(a<0,b>0\) 非零，此时是范数一的矩阵单位
\[
                        |w_a\otimes w_0\rangle
                        \langle w_0\otimes w_{-b}|.           \tag{18}
\]
反向块在 \(a>0,b<0\)。时间块非零要求 \(aL+bM\) 属于一个由 \(h,d_p,d_q\) 决定的固定有界区间 \(J\)。
对固定a，许可b数有统一上界；对固定b，许可a数亦如此。时间块范数统一有界，
算子值Schur估计给任意有限交叉和的共同范数界；在有限 \(w\) 基输入上求和最终稳定。
因此完整群和强星收敛，其矩阵元与(15)一致。混合块一般非零，不能从实际算子中删除。

这一和一般不绝对收敛。例如若
\(M_{d_p}U(h)M_{d_q}\ne0\)，可用 \(L/M\) 无理选择
\(a_n<0,b_n>0,a_nL+b_nM\to0\)；(18)范数恒一，时间块范数趋于正数。
对这种允许的测试，群项甚至不趋零。
允许重叠分割并取 \(h(0)\int d_pd_q\ne0\) 就给实际例子；不宣称每个测试都发生该现象。

此外 \(R^-\) 的负端常值不属于422的 \(E_1\)。本稿定义域是明确的采样／Schur强和及其有限压缩，
不把 \(A_\infty\) 未经准入写成旧 \(\mathcal A\) 元素，亦不直接套用旧 \(\tau\) 或423的标量循环公式。

## 6. 每个实际截断都是迹类，混合对角绝对消失

固定 \(K_p,K_q\)，(16)的径向像有限维。球与波形的几何系数仍给群项迹范数绝对收敛，
时间平滑界同第2节。因此
\(\mathsf P A_\infty(h)\mathsf P\) 是实际迹类算子。
\(R_K^-\) 与 \(W\) 正交，且
\[
 \operatorname{Tr}(R_K^-\lambda_aR_K^-)
       =K\mathbf1_{a=0}+\rho_r^{|a|},\quad
 \operatorname{Tr}(W\lambda_bW)=\mathbf1_{b=0}.               \tag{19}
\]
所有有限截断的交叉块迹为零；这是完整求和后的迹，不是先删除混合群标签。
于是精确公式为
\[
\begin{split}
 \operatorname{Tr}(\mathsf P_{K_p,K_q}A_\infty(h)\mathsf P_{K_p,K_q})
 ={}&[(K_p+1)L+(K_q+1)M]h(0)\\
 &+L\sum_{a\ne0}\rho_p^{|a|}h(-aL)
   +M\sum_{b\ne0}\rho_q^{|b|}h(-bM).                         \tag{20}
\end{split}
\]
物理 \(e\) 基的对角还给独立绝对控制：
\[
 (R^-\lambda_aR^-)_{jj}
 =\mathbf1_{j<0}\mathbf1_{a=0}+|b_0(j)|^2\rho_r^{|a|},
 \quad (W\lambda_bW)_{kk}=|w_0(k)|^2\mathbf1_{b=0}.           \tag{21}
\]
对 \(n>0\)，
\[
 \sum_j|w_{-n}(j)\overline{w_0(j)}|=2(1-\rho_r^2)\rho_r^n,
 \qquad \sum_j w_{-n}(j)\overline{w_0(j)}=0.                  \tag{22}
\]
两位交叉对角绝对和因而至多
\(4(1-\rho_p^2)(1-\rho_q^2)\rho_p^{|a|}\rho_q^{|b|}\)。
时间光滑核对角为 \(d_p(t)h(-\ell_g)d_q(t)\)，其绝对积分至多
\(\|h\|_\infty\int|d_pd_q|\)，反向同理；与上述双几何界合用，
给完整混合对角的绝对可求和与零值。这里用明确光滑核的对角，没有从抽象S₁算子推出逐点对角界。
这个对角证明与第5节完整算子强和的证明各自必要，不能互相替代。

## 7. 原源半迹比较及自然负端有限部

原414的 \(A_N(h)\) 与本稿 \(A_N^+(h)\) 有准确关系
\[
                    \operatorname{Tr}A_N^+(h)
                             =\tfrac12\operatorname{Tr}A_N(h). \tag{23}
\]
证明如下：重定位不改迹；四通道交叉迹为零；
壳层的负原子 \(e_{-2N-1}\) 和正波形 \(w_0\) 的全部位移自相关都等于
\(\mathbf1_{a=0}\)，因此左右两角的完整迹相等。(23)包括单位项，非只比较非零群标签。
代入(17)、(20)也可逐项复核原414(23)。

固定原赋值起点0，对任意两坐标共尾定义
\[
 \Lambda(h)=\lim_{K_p,K_q\to\infty}
 \left[\operatorname{Tr}(\mathsf P A_\infty(h)\mathsf P)
                    -(K_pL+K_qM)h(0)\right].                 \tag{24}
\]
由(20)，方括号对每个截止已相同，所以联合极限没有路径依赖，且
\[
 \boxed{\Lambda(h)=(L+M)h(0)
   +L\sum_{a\ne0}p^{-|a|/2}h(-a\log p)
   +M\sum_{b\ne0}q^{-|b|/2}h(-b\log q).}                    \tag{25}
\]
这是真实迹类压缩及明确体积扣除产生的有限部，没有按目标原子添加权重。
负原子的数目是 \(K_r\)，留下的单位常数 \(L+M\) 来自原球向量 \(b_0\)；
改扣 \((K_p+1)L+(K_q+1)M\) 会另改单位项，本文没有为消除目标而调起点。
从原源还得到每个有限 \(N\) 的比较式
\[
 \Lambda(h)=\tfrac12\operatorname{Tr}A_N(h)
                         -(2N_pL+2N_qM)h(0).                 \tag{26}
\]
\(\Lambda\) 不依赖平方分割形状，尽管 \(A_\infty\) 本身依赖它们。
它是有限Radon测度在光滑紧支测试上的限制，并满足
\[
 |\Lambda(h)|\le
 \left[L+M+\frac{2L\rho_p}{1-\rho_p}
              +\frac{2M\rho_q}{1-\rho_q}\right]\|h\|_\infty. \tag{27}
\]
这是时间测试的连续性，不能误写成在整个强算子拓扑上的连续迹。

若按原源设 \(h(s)=e^{-s/2}k(-s)\)，则 \(h(0)=k(0)\)，
原414的两个Fourier单位扣项给
\[
             \Lambda(h)-(L+M)k(0)=\mathcal L_p(k)+\mathcal L_q(k). \tag{28}
\]
它比较的是两个完整有限位项；对sharp测试，原 \(\mathcal L_r=2\mathcal N_r\)，
Weil有限位半迹仍须再除2，不把(23)的壳层二分与这个归一化混同。

## 8. 同一固定算子仍有真实的截止歧义

不能把(24)升级成“任意强截止减同一体积都给同一有限部”。
在完整 \(w\) 基中，\(K_\infty\) 的p通道第 \(n<0\) 行及q通道第 \(k<0\) 行分别是
\[
 d_p(t)(\mathcal W_p\mathcal W_q\phi)(t-nL),\qquad
 d_q(t)(\mathcal W_p\mathcal W_q\phi)(t-kM).                  \tag{29}
\]
共同酉元 \(\mathcal W_p\mathcal W_q\) 与 \(U(h)\) 交换，在 \(K_\infty U(h)K_\infty^*\) 中抵消。
这也直接复核第5节的Schur矩阵元。定义另一实际有限径向投影
\[
 F_{K_p,K_q}=\sum_{n=-K_p}^{-1}P_{w_{n,p}\otimes w_{0,q}}
                +\sum_{k=-K_q}^{-1}P_{w_{0,p}\otimes w_{k,q}}. \tag{30}
\]
两通道仍正交。\(F\) 强收敛到
\(E_\infty=R_p^-\otimes W_q+W_p\otimes R_q^-\)，而
\(E_\infty A_\infty E_\infty=A_\infty\)。若要求截止强趋于整个单位，
用 \(1-E_\infty+F\) 即可，其压缩 \(A_\infty\) 与 \(F\) 相同。

这一次压缩涉及有限 \(w\) 基，许可群标签也只有有限个，故由光滑时间核给实际迹类算子。
\(\langle w_n,\lambda_a w_n\rangle=\mathbf1_{a=0}\)，混合交叉迹仍为零。因此
\[
 \operatorname{Tr}(F_{K_p,K_q}A_\infty(h)F_{K_p,K_q})
                     =(K_pL+K_qM)h(0).                      \tag{31}
\]
扣除与(24)相同的体积项，其有限部恒为零，而物理截止给(25)。
两列压缩具有同一个强星算子极限；强收敛和体积扣除本身并不选定周期分布。
选 \(h\) 支集仅靠近 \(-L\)，避开0及其他两个轴的周期，\(h(-L)=1\)，
则物理有限部为 \(L\rho_p\ne0\)，波形截止有限部为零。
差别发生在非零时间，不能靠改一个单位时间常数消除。

歧义有准确的原球来源，而非抽象更换截止。球／波形递推给
\[
 R_{K,r}^-=\sum_{n=-K}^{-1}P_{w_{n,r}}+P_{b_{-K,r}},\qquad
 b_{-K,r}=\lambda_{-K}b_{0,r}.                               \tag{32}
\]
两有效径向截止的差因此是两个正交逃逸球通道
\(G_K=P_{b_{-K_p,p}}\otimes W_q+W_p\otimes P_{b_{-K_q,q}}\)。
\(G_K\to0\) 强收敛，但其普通压缩迹对每个K都等于
\(\operatorname{Tr}(G_KA_\infty(h)G_K)=\Lambda(h)\)，
因为球位移自相关仍为 \(\rho_r^{|a|}\)，波形自相关仍为 \(\mathbf1_{b=0}\)。
波形截止F与逃逸球通道G之间的交叉迹为零，物理截止和波形截止的两迹之差恰由这两个实际通道承担。

(23)–(28)仍是原物理壳层来源的准确比较，不受这个反例否定。
它排除的是只依赖固定算子及任意强截止的无来源有限部；
后续必须证明原几何为何强制采用物理截止，或者构造不同截止间的规范边界传递。

## 9. 进展范围与下一条需要证明的桥

本稿完成原几何源→固定采样算子→实际截断迹→两有限位周期分布的比较。
此前423中固定 \(N\) 的交换异常为零，在此仍为零；(25)并非那些零标量的非零极限，
而是另一明确极限域中的截断迹有限部。

当前尚缺的是原 \(u,T\) 在这个负端极限域中的规范相对Chern／主关系比较。
还没有证明 \(\Lambda\) 在该域循环，或它对源边界为零；两有限位和也尚未与实位及全体素数的Weil二次型比较。
下一步应从(12)的实际采样入手，计算 \(T\) 的压缩与边／角异常，
保留完整混合算子、原时间测试及第8节截止差别，检验是否可形成规范相对链，而非预置扣除项。
具体准入见[下一有限任务](../reviews/2026-10-04/f1-fixed-corner-source-comparison-next-proof-plan.md)。
[426](426-f1-fixed-corner-source-commutators-and-relative-readout-module.md)继续证明原源在这个极限域中的迹类交换子和受限读出相容性；它仍不替代完整相对Chern比较。

完整独立推导见[截止极限报告](../reviews/2026-10-04/f1-cutoff-boundary-limit-derivation.md)。
这里的Hilbert分析由显式证明与独立审查承担；有限有理模型审计不替代无限维证明，亦不宣称Lean已经形式化本稿。
