# 427. 固定正角的实际乘法代数与不可消去的交换子迹余圈

2026-10-04。接续已推送的[426](426-f1-fixed-corner-source-commutators-and-relative-readout-module.md)。
本稿支付此前尚缺的乘法封闭性，但同时证明普通迹扩张不可能在完整新代数上循环。
障碍由同一平滑采样的端点产生；不改变原平方分割，不添加目标周期原子。

## 1. 去除共同酉元后的实际采样

沿用425的完整 \(w_n\) 基和两个正交通道。记
\(\mathcal W=\mathcal W_p\mathcal W_q\)，定义有界采样 \(V:L^2(\mathbb R)\to\mathcal H\)：
\[
 (V\phi)_{p,n}(t)=d_p(t)\phi(t-nL)\quad(n<0),\qquad
 (V\phi)_{q,k}(t)=d_q(t)\phi(t-kM)\quad(k<0).                 \tag{1}
\]
各行的径向向量分别是 \(w_{n,p}\otimes w_{0,q}\) 和
\(w_{0,p}\otimes w_{k,q}\)。425(29)给
\[
 K_\infty=V\mathcal W,\qquad
 A(h)=A_\infty(h)=VU(h)V^*,\quad
 V^*V=M_m,                                                   \tag{2}
\]
\[
 m(x)=\sum_{n<0}d_p(x+nL)^2+\sum_{k<0}d_q(x+kM)^2.           \tag{3}
\]
\(\mathcal W\) 与 \(U(h)\) 交换，故在A中消去。若仍使用原 \(K_\infty\)，
则 \(K_\infty^*K_\infty=\mathcal W^*M_m\mathcal W\)，不能漏掉酉共轭。

原光滑紧支平方分割保证每个局部区间内(3)只有有限项，并且存在 \(a<b\) 使
\[
 m\in C^\infty,\quad 0\le m\le2,\quad
 m(x)=0\ (x\le a),\qquad m(x)=2\ (x\ge b).                  \tag{4}
\]
右端每个分割的全部非零平移都已落在负标签，贡献1；左端两个分割都没有可见负标签。
不要求过渡单调。特别 \(\|V\|=\sqrt2\)。

## 2. 乘法封闭的完整迹类证明

对 \(h,k\in C_c^\infty\)，由(2)
\[
 A(h)A(k)=VU(h)M_mU(k)V^*
         =2A(h*k)+R(h,k),                                   \tag{5}
\]
其中
\[
 R(h,k)=VU(h)M_{m-2}U(k)V^*\in\mathcal S_1.                 \tag{6}
\]
这里 \(m-2\) 在左端是常数，不能直接称其紧支。
实际证明是：\(V=V\mathbf1_{[a,\infty)}\)，\(V^*\) 的输出在 \([a,\infty)\)；
若 \(\operatorname{supp}k\subset[-K,K]\)，则 \(U(k)V^*\) 的输出在 \([a-K,\infty)\)。
选光滑 \(\chi\)，在此区间恒为1、在充分负端为0，令 \(f=\chi(m-2)\)。
由(4)，\(f\) 光滑紧支，且
\(M_{m-2}U(k)V^*=M_fU(k)V^*\)。
\(U(h)M_f\) 的核 \(h(x-y)f(y)\) 光滑且两变量紧支，故Fourier秩一展开给迹类；
再乘有界 \(V,U(k),V^*\) 得(6)。

因此426的
\[
 \mathcal D=A(C_c^\infty(\mathbb R))+\mathcal S_1              \tag{7}
\]
已经是实际非单位化星代数，\(\mathcal S_1\) 是其双侧理想。
乘积交叉项由迹类理想性处理，且 \(A(h)^*=A(h^*)\)。
其迹类商中的测试乘法准确为 \(h\cdot k=2(h*k)\)，不是未带归一化的普通卷积。

## 3. 完整交换子本身迹类

令
\[
 C(h,k)=U(h)M_mU(k)-U(k)M_mU(h).                             \tag{8}
\]
其光滑核为
\[
 C(h,k)(x,y)=\int\big[h(x-z)m(z)k(z-y)
                         -k(x-z)m(z)h(z-y)\big]dz.          \tag{9}
\]
\(x-y\) 被两个测试支集控制；x充分负时各项为0，x充分正时 \(m=2\)，
两卷积相等而抵消。因此该核两变量均紧支，确为迹类。
于是
\[
 [A(h),A(k)]=VC(h,k)V^*\in\mathcal S_1,\quad
 \operatorname{Tr}[A(h),A(k)]=\operatorname{Tr}(M_m C(h,k)).  \tag{10}
\]
最后的循环合法，因为C已迹类，V有界；没有循环两个裸非迹类算子。
全部混合通道已包含在 \(V^*V=M_m\) 中。

## 4. 精确普通迹与平滑端点

把(9)在对角上第二项作 \(s\mapsto-s\) 换元，得
\[
 \operatorname{Tr}[A(h),A(k)]
   =\int h(s)k(-s)I(s)ds,
 \quad I(s)=\int m(x)[m(x-s)-m(x+s)]dx.                      \tag{11}
\]
对s在紧区间，x积分一致紧支，所以换元、微分和积分合法。
\(I(0)=0\)，且
\[
\begin{split}
 I'(s)&=-\int m(x)[m'(x-s)+m'(x+s)]dx\\
      &=-\int \frac{d}{dx}\big[m(x+s)m(x)\big]dx=-4.
\end{split}                                                 \tag{12}
\]
最后只用 \(m(-\infty)=0,m(+\infty)=2\)。因此
\[
 \boxed{\operatorname{Tr}[A(h),A(k)]
                         =-4\int s\,h(s)k(-s)\,ds.}         \tag{13}
\]
这是原平滑分割的精确恒等式，不是近锐极限或数值外推。
取非零偶函数 \(g\in C_c^\infty\) 实值，令 \(h(s)=sg(s),k(s)=g(s)\)，则
\[
             \operatorname{Tr}[A(h),A(k)]=-4\int s^2g(s)^2ds<0. \tag{14}
\]
两因子均非迹类；只有它们的交换子迹类，故不与普通迹循环性矛盾。

## 5. 全代数标量迹扩张被严格排除

任意线性泛函 \(\Phi:\mathcal D\to\mathbb C\)，若在 \(\mathcal S_1\) 上等于普通迹，
则由(13)
\[
 \Phi(A(h)A(k)-A(k)A(h))=-4\int s h(s)k(-s)ds.               \tag{15}
\]
用(14)立即否定 \(\Phi\) 在整个 \(\mathcal D\) 上循环；不需要连续性假设。
426的物理读出 \(\widetilde\Lambda\)、零周期读出 \(\Psi_0\) 及所有其他普通迹扩张
在这些交换子上具有完全相同的非零缺陷，不能改一个分布或起点把它消去。
原 \(\mathcal M_Q\) 双模循环仍成立，因为它是另一个明确限定的乘子条件；
本稿没有把历史局部结论撤销，而是证明它不能推广到全部新乘法。

## 6. 必须保留的商余圈

商的单射性已可在本稿内证明：若 \(A(h)\) 迹类，普通迹循环及(13)使其右边对所有k为零。
取 \(k(t)=t\overline{h(-t)}\)，得到 \(4\int s^2|h(s)|^2ds=0\)，由光滑性推出 \(h=0\)。
因此商准确由测试卷积代数给出，可用 \(a(\xi)=2\widehat h(\xi)\) 识别，
\(\widehat h(\xi)=\int h(s)e^{-i\xi s}ds\)；[428](428-f1-corner-essential-symbol-and-complete-readout-freedom.md)再给更强的非紧性与范数结论。
在这个实际符号代数上，(13)写为
\[
 \omega(a,b)=\frac1{2\pi i}\int a'(\xi)b(\xi)d\xi.           \tag{16}
\]
Schwartz衰减使积分和分部积分合法；Fourier换元给(13)中的负号和因子4。
它满足 \(\omega(a,b)=-\omega(b,a)\)，并且标准Hochschild边界
\[
 (b\omega)(a,b,c)=\omega(ab,c)-\omega(a,bc)+\omega(ca,b)=0,  \tag{17}
\]
因为被积式恰为 \((abc)'\)。所以 \(\omega\) 是具体的代数循环1余圈。
它在商上不是标量0余链的Hochschild边界：商交换，而任意 \(b\ell(a,b)=\ell(ab-ba)=0\)，
但(14)证明 \(\omega\ne0\)。

若给A(h)或A(k)加迹类余项，其交换子迹不变；新交叉交换子都是有界乘子与迹类算子的交换子，迹零。
因此该余圈真正降至商，不是特定提升的假象。
它只看两个采样端点形成的跳变，在本稿中未携带 \(\rho_p,\rho_q\) 的纯周期权重。
用这一异常余圈本身尚不能选出426不同的周期读出。

## 7. 实际相对边通量与范围

对物理下截止 \(P=\mathsf P_{K_p,K_q}\)，\(PA(h)P\) 与 \(PA(k)P\) 迹类，
插入 \(1=P+(1-P)\) 得
\[
\begin{split}
 \operatorname{Tr}(P[A(h),A(k)]P)
   ={}&\operatorname{Tr}(PA(h)(1-P)A(k)P)\\
      &-\operatorname{Tr}(PA(k)(1-P)A(h)P).                  \tag{18}
\end{split}
\]
这两个边通量项各自迹类：按 \(A(h)A(k)=2A(h*k)+R(h,k)\)，
\(PA(h)A(k)P\) 是迹类；再减 \((PA(h)P)(PA(k)P)\) 得各项准入。
由(10)，左边压缩在迹范数中趋向完整交换子，所以(18)极限准确为(13)。
有限压缩交换子的普通迹为零，并不消去这个外部边通量。
它给真实来源的相对异常，但尚不是主关系的循环Chern比较。

经典背景可参见[Helton–Howe原论文](https://mathweb.ucsd.edu/~helton/BILLSPAPERSscanned/HHo75.pdf)导言及其符号迹理论。
这里的具体端点、归一化和迹类准入由上式独立证明，不宣称这一一般现象为文献首创。
完整原酉元u是否保持本代数，见[429](429-f1-original-unitary-crosses-the-fixed-corner-domain.md)。
下一步需要携带 \(\omega\) 的真实相对链及扩大的源边域；全代数标量循环扩张这一候选已经收束。
本稿未证明算术主关系、完整Weil比较、RR、正性或RH。
