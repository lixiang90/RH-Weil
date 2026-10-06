# 原Haar物理截止：源核准入、混合耦合与实际源词有限部障碍

2026-10-06，独立推导。接续425、430–433；并对照434的完整波形核式。
本报告保留原物理时间、两个对数周期、Haar几何尾及原源酉元，不改用波形标签截止或不变坐标截止。
这里证明每个固定物理压缩迹类，并给一个合法分割上的实际源词反例；不声称完整相对Chern、Weil正性或RH。

## 1. 原物理行与右伴随方向

置 \(D_p=L=\log p,D_q=M=\log q\)，\(\rho_r=r^{-1/2}\)，
\(\kappa_r=\sqrt{1-\rho_r^2}\)。仍用
\[
 b_N=\kappa_r\sum_{m\ge0}\rho_r^m e_{N+m},\qquad
 w_N=\rho_r e_N-\kappa_r b_{N+1},\qquad \lambda_a e_j=e_{j+a}.
 \tag{1}
\]
时间作用为 \(\mathsf T_s\phi(t)=\phi(t-s)\)；
\(P_{(a,b)}=\lambda_a\otimes\lambda_b\otimes\mathsf T_{aL+bM}\)。
原合法平方分割记为 \(c=d_p,d=d_q\)，实值光滑紧支，分别以L、M为平方分割周期。
以下
\[
 \mathcal W_r=(\rho_r-\mathsf T_{D_r})(1-\rho_r\mathsf T_{D_r})^{-1},
 \quad \mathcal G_r=\kappa_r(1-\rho_r\mathsf T_{D_r})^{-1},
 \quad K_\infty=V\mathcal W_p\mathcal W_q
 \tag{2}
\]
完全来自425。因 \(\mathcal W_r\) 酉且彼此交换，原物理e行给
\[
\begin{array}{c|c|c}
 &\text{径向向量}&\text{时间行算子}\\ \hline
 p,n<0&e_{n,p}\otimes w_{0,q}&M_c\mathsf T_{nL}\mathcal W_p^*\\
 p,\mathrm{ball}&b_{0,p}\otimes w_{0,q}&M_c\mathcal E_p\\
 q,k<0&w_{0,p}\otimes e_{k,q}&M_d\mathsf T_{kM}\mathcal W_q^*\\
 q,\mathrm{ball}&w_{0,p}\otimes b_{0,q}&M_d\mathcal E_q
\end{array}
\tag{3}
\]
其中 \(\mathcal E_r=\mathcal G_r\mathcal W_r^*\)。这是V的行，非另造采样。
直接代数化简给
\[
\begin{split}
 \mathcal W_r^*&=\rho_r-(1-\rho_r^2)
          \sum_{m\ge1}\rho_r^{m-1}\mathsf T_{-mD_r},\\
 \mathcal E_r&=-\kappa_r\sum_{m\ge1}
                         \rho_r^{m-1}\mathsf T_{-mD_r}.
\end{split}\tag{4}
\]
第二式使用
\(\rho_r-\mathsf T_{-D_r}=-\mathsf T_{-D_r}(1-\rho_r\mathsf T_{D_r})\)。
两个级数的系数都在ell¹中。右伴随因此是正方向 \(\mathsf T_{+mD_r}\)，不能在核中漏去。

实际物理下截止是
\[
 \mathsf P_K=\mathbf1_{j\ge-K_p,\ k\ge-K_q}\otimes1_t,
 \qquad K_p,K_q\ge0.
 \tag{5}
\]
它将(3)的原子行截到 \(-K_p\le n<0,-K_q\le k<0\)，保留两个原球行。
故 \(\mathsf P_K V\) 的径向像有限维，尽管 \(\mathsf P_K\) 本身无限秩。

## 2. 原周期平滑核的统一迹类界

对 \(B\in G_M\)，记核 \(K_B(x,y)\)。430的联合M周期、光滑及有限传播保证
所有核导数在全平面一致有界。若 \(a,b\in\mathbb R\)，\(d_1,d_2\in C_c^\infty\)，则
\[
 M_{d_1}\mathsf T_a B\mathsf T_b^*M_{\overline{d_2}}
 \tag{6}
\]
具有光滑核 \(d_1(t)\overline{d_2(t')}K_B(t-a,t'-b)\)，支集位于固定紧矩形。
在严格更大的紧矩形中作双Fourier秩一展开，两变量各两次分部积分，
得到常数乘 \((1+m^2)^{-1}(1+n^2)^{-1}\) 的绝对可和界。
常数只用有限个全局核导数及 \(d_1,d_2\)，**不依赖a,b**。
因此(6)为迹类且有统一迹范数界。

代入(4)，每个有限径向块 \(X_\alpha B X_\beta^*\) 是迹范数绝对收敛的双几何和。
于是
\[
 \mathsf P_KVBV^*\mathsf P_{K'}\in\mathcal S_1
 \quad(K,K'\text{任意固定非负物理截止}).
 \tag{7}
\]
此证明没有把有界采样或无限径向投影直接当成迹类。

## 3. 全部有限源指数的固定物理压缩

430的真实源为
\[
 u^i=1-e+v_i,\qquad
 e=\sum_a M_{c(t)c(t-aL)}P_{(a,0)},\quad
 v_i=\sum_a M_{c(t)c(t-aL-iM)}P_{(a,i)}.
 \tag{8}
\]
每个固定i的非零a集有限；\(v_0=e\)，负i由实际伴随给出。
把(8)记为有限列表 \(u^i=\sum_{s\in S_i}M_{f_s}P_{g_s}\)，i=0可直接用单位一项。
物理移位准确满足
\[
 \mathsf P_KP_g=P_g\mathsf P_{K+g}.
 \tag{9}
\]
对足够大的K，所有 \(K+g_s\) 非负。由(3)写
\[
 \mathsf P_Ku^iV
   =\sum_{s,\alpha}|r_{i,s,\alpha}\rangle Y_{i,s,\alpha},\quad
 r_{i,s,\alpha}=\lambda_{g_s}r_\alpha^{K+g_s},\quad
 Y_{i,s,\alpha}=M_{f_s}\mathsf T_{\ell_{g_s}}X_\alpha^{K+g_s}.
 \tag{10}
\]
其中 \(\ell_g=g_1L+g_2M\)，且径向求和有限。
所有Y仍是一个光滑紧支乘法、一个时间平移和(4)的ell¹滤波器之积。
故(7)的统一界支付每对左右Y。对小K，先选择足够大的K′，再以
\(\mathsf P_K(\mathsf P_{K'}F\mathsf P_{K'})\mathsf P_K\) 压缩。
结论为
\[
 \boxed{\mathsf P_KF_{i,j}(B)\mathsf P_K\in\mathcal S_1,\qquad
 F_{i,j}(B)=u^iVBV^*u^{-j},\ B\in G_M,\ i,j\in\mathbb Z.}
 \tag{11}
\]
加上430的S₁余项，覆盖全部有限代数 \(D_{\rm src}\)。
这不涵盖纯单位、纯u或任意范数完成元素。

迹类已支付后，完整迹为
\[
 \operatorname{Tr}(\mathsf P_KF_{i,j}(B)\mathsf P_K)
 =\sum_{s,\alpha,t,\beta}
 \langle r_{j,t,\beta},r_{i,s,\alpha}\rangle
 \operatorname{Tr}(Y_{i,s,\alpha}B Y_{j,t,\beta}^*).
 \tag{12}
\]
内积第二变量线性。此式包括左右源、所有原球和全部混合耦合。
若 \(Y_\mu=M_{m_\mu}\mathsf T_{\sigma_\mu}R_\mu\)，
\(R_\mu=\sum_d r_{\mu,d}\mathsf T_{-dD_\mu}\)，则其时间迹准确为
\[
 \sum_{d,e}r_{\mu,d}\overline{r_{\eta,e}}
 \int m_\mu(t)\overline{m_\eta(t)}
 K_B(t-\sigma_\mu+dD_\mu,\ t-\sigma_\eta+eD_\eta)\,dt.
 \tag{13}
\]
当 \(B=U(h)\)，核值是
\(h(\sigma_\eta-\sigma_\mu+dD_\mu-eD_\eta)\)。
这是右伴随平移的核检查；不能将第二个输入也按左侧方向平移。

## 4. i,j属于0、正负1时的实际混合矩阵

以下单坐标重叠全部从(1)直接求和：
\[
\begin{split}
 \langle w_{a'},w_a\rangle&=\delta_{a'a},&
 \langle b_{a'},b_a\rangle&=\rho_r^{|a-a'|},\\
 \langle e_\ell,b_a\rangle&=\kappa_r\rho_r^{\ell-a}
                                   \mathbf1_{\ell\ge a},&
 \langle e_\ell,w_a\rangle&=w_0(\ell-a),\\
 \langle w_{a'},b_a\rangle&=-\kappa_r\rho_r^{a-a'-1}
                                   \mathbf1_{a>a'}.
\end{split}\tag{14}
\]
源移位后的p行是 \(e_{n+a}\otimes w_b\) 或 \(b_a\otimes w_b\)；
q行是 \(w_{a'}\otimes e_{k+b'}\) 或 \(w_{a'}\otimes b_{b'}\)。
p/p内积强制 \(b=b'\)，q/q强制 \(a=a'\)。
p/q非零内积必需
\[
                  a>a',\qquad b'>b.
 \tag{15}
\]
对原子还需 \(n+a\ge a'\)、\(k+b'\ge b\)，因此仅有限个负原子近角参与；
球重叠由(14)给真实Haar权重。

对p的左源i及q的右源j，(8)的q位移只允许
\(b\in\{0,i\},b'\in\{0,j\}\)，i=0或j=0时只保留单位列表。
下表列出满足 \(b'>b\) 的全部候选 \((b,b')\)；仍须(15)的a条件及真实系数，
所以它是完整准入筛选，不把每个候选都宣称为非零最终迹：

| i＼j | 0 | 1 | −1 |
|---|---|---|---|
| 0 | 无 | (0,1) | 无 |
| 1 | 无 | (0,1) | 无 |
| −1 | (−1,0) | (−1,0),(−1,1),(0,1) | (−1,0) |

反向q/p耦合由交换左右及共轭给出。(8)、(12)–(15)因此给
\(i,j\in\{0,\pm1\}\) 的明确完整核算法，不删除源e/v混合项。
它允许核中出现 \(aL+bM\)；一般最终有限部是否保留这些项仍需个案计算。

另可在完整w基直接核准434。令 \(a_p(x)=\sum_{n<0}c(x+nL)^2,f=cd\)，则
\[
 (u^rV\phi)_{j,k}(t)=b_{j,k}^{(r)}(t)\phi(t-jL-kM)
 \tag{16}
\]
的实系数为
\[
\begin{split}
 b_{j,k}^{(r)}(t)={}&c(t)\{\delta_{k0}[\mathbf1_{j<0}-a_p(t-jL)]
                 +\delta_{kr}a_p(t-jL-rM)\}\\
 &+\delta_{j0}\mathbf1_{k<0}d(t)
 +c(t)\{\mathbf1_{k<r}f(t-jL-rM)-\mathbf1_{k<0}f(t-jL)\}.
\end{split}\tag{17}
\]
例如 \(v_rV_q\) 输入标签为 \((0,k-r)\)，时间为 \(t-jL-rM\)，
故输出输入时间仍准确为 \(t-jL-kM\)；这是末行及右平移的独立核验。
r=0恰退化为原V。
原物理Q的w矩阵为
\[
 Q_{K,r}=\sum_{n\ge-K}P_{w_n}
   +P_{\kappa_r\sum_{d\ge1}\rho_r^{d-1}w_{-K-d}}.
 \tag{18}
\]
该球向量等于 \(-b_{-K}\)，只差不影响投影的整体符号。
将(17)与两位(18)代入，对 \(F_{r,s}(B)\) 得到434(10)的
\[
 \sum_{j,k,j',k'}q_{K_p,p}(j',j)q_{K_q,q}(k',k)
 \int b_{j,k}^{(r)}(t)b_{j',k'}^{(s)}(t)
 K_B(t-jL-kM,t-j'L-k'M)\,dt .
 \tag{19}
\]
有限可见行及球ell¹系数保证绝对核收敛。434的有限源条带并非有限秩；
是原物理投影作用之后，其有限可见标签加两个球使径向像有限维。

## 5. F00的一般实际物理迹与逃逸球

在V像上，原物理有效单坐标投影是
\[
 R_{K,r}^-=\sum_{n=-K}^{-1}P_{w_n}+P_{b_{-K}},
 \quad
 \langle b_{-K},w_{-(K+d)}\rangle=-\kappa_r\rho_r^{d-1}\ (d\ge1).
 \tag{20}
\]
记 \(d_p=c,d_q=d\)，\(C_B(x)=K_B(x,x)\)。由正交通道求迹，
\(\operatorname{Tr}(\mathsf P_KVBV^*\mathsf P_K)\) 是p、q两项之和；
每项准确为
\[
\begin{split}
 \mathcal T_{K,r}(B)={}&
 \sum_{n=1}^{K_r}\int d_r(t)^2 C_B(t+nD_r)\,dt\\
 &+(1-\rho_r^2)\sum_{d,e\ge1}\rho_r^{d+e-2}
 \int d_r(t)^2
 K_B(t+(K_r+d)D_r,t+(K_r+e)D_r)\,dt .
\end{split}\tag{21}
\]
双几何级数在迹范数及核导数中均绝对收敛。
**仅对F00**，p/q交叉块迹因正交通道为零。
一般源Fij不能沿用此消失；应采用(12)或(19)。

若B传播半径小于 \(\min(L,M)\)，(21)的球和只留d=e。
即使如此，周期对角 \(C_B\) 也会产生随 \(K_pL\) 漂移的残差；
逃逸球强趋零不使这个迹自动趋零。
原 \(B=U(h)\) 的平移不变核另有其准确纯周期公式425(20)，两者不混同。

## 6. 一个允许的原源词，任何线性体积扣除均无联合有限部

现选实际素数 \(p=2,q=5\)，故 \(M>2L\)。
取合法非负c，其支集在长度D的区间中，\(L<D<M/2\)。
这种平方分割确可构造：取光滑非负紧支η，在一个L基本区间严格正，
支集长度D，再置
\[
 c(t)=\eta(t)\left(\sum_n\eta(t-nL)^2\right)^{-1/2}.
 \tag{22}
\]
取合法非负d的一个平移，使其与c的正区重叠；平方分割性质仍保留。
因此 \(f=cd\ne0\) 且支集长度小于M/2。
430右尾中
\[
 \alpha(x)=\sum_kf(x+kM)^2,\qquad
 \beta_1=0,\qquad \gamma_1=1-\alpha .
 \tag{23}
\]
置 \(\nu=2\pi/M\)。非零正质量 \(f^2\) 支持的相位弧长小于π，
旋转相位使该弧位于严格正实部半平面，便得
\[
 \alpha_1=\frac1M\int f(x)^2e^{-i\nu x}dx\ne0,\qquad
 I_c=\int c(t)^2e^{i\nu t}dt\ne0.
 \tag{24}
\]
这里仅说明允许实例，不把这一性质宣称为每个原分割都成立。

取非零非负实偶 \(h=k\in C_c^\infty\)，支集 \(|s|<\varepsilon\)，
\(2\varepsilon<\min(L,M)\)，并足够小使 \(\cos(\nu s)>0\) 在该支集。
实际周期核
\[
 B=U(h)M_{\gamma_1}U(k)\in G_M,\qquad
 K_B(x,y)=\int h(x-z)\gamma_1(z)k(z-y)dz
 \tag{25}
\]
传播半径至多 \(2\varepsilon\)。其对角
\[
 C(x)=\int h(s)k(-s)\gamma_1(x-s)ds,\qquad
 C_1=-(\alpha_1)\int h(s)^2e^{-i\nu s}ds\ne0 .
 \tag{26}
\]
因h实偶，最后积分为严格正的实数。
定义
\[
 P(\theta)=\int c(t)^2C(t+\theta)dt,\qquad
 \overline C=M^{-1}\int_0^M C(x)dx .
 \tag{27}
\]
P光滑M周期，第一谐波 \(P_1=C_1I_c\ne0\)。
令 \(r=\rho_p^2=1/2\)。由(21)传播筛选，
\[
\begin{split}
 \mathcal T_{K,p}(B)&=\sum_{n=1}^{K_p}P(nL)+H(K_pL),\\
 H(\theta)&=(1-r)\sum_{d\ge1}r^{d-1}P(\theta+dL),\\
 \mathcal T_{K,q}(B)&=(K_q+1)M\overline C .
\end{split}\tag{28}
\]
q式使用M周期C与原d平方分割：
\(\int d(t)^2C(t)dt=\int_0^M C\)；球几何权重之和为1。
于是p连续差为
\[
 \mathcal T_{K+1,p}-\mathcal T_{K,p}
 =P((K+1)L)+H((K+1)L)-H(KL).
 \tag{29}
\]
对P的第m谐波，置 \(z=e^{im\nu L}\)，(29)的Fourier乘子准确是
\[
 z+\frac{(z-1)(1-r)z}{1-rz}
 =\frac{z[r+(1-2r)z]}{1-rz}
 =\frac{z}{2(1-z/2)}\quad(p=2).
 \tag{30}
\]
其在单位圆上不为零，因此(29)是一个具有非零第一谐波的连续非恒定M周期函数
在 \(KL\bmod M\) 上的取值。
\(L/M\) 无理，因为有理等式会给 \(2^a=5^b\)；
无理旋转的正轨道稠密，故这些值不能趋于任何常数。

因此对任意固定标量a,b,c，
\[
 \operatorname{Tr}(\mathsf P_KVBV^*\mathsf P_K)
                         -aK_p-bK_q-c
 \tag{31}
\]
没有所有两坐标共尾的联合极限。
严格反证可沿 \(K_p=K_q=K\)：若该序列收敛，连续差必趋零，
而其连续差是(29)加常数 \(M\overline C-a-b\)，沿稠密相位不可能趋零。
这已排除任意固定线性体积选择；不排除按相位选子列或额外周期反项。
原425几何壳层采用 \(K_r=2N_r\) 也不避开本例：
两步连续差的第一谐波在(30)之外仅多乘 \(1+e^{i\nu L}\ne0\)，
而 \(2NL\bmod M\) 仍稠密。故同样的线性扣除在原偶数截止子族上也无联合有限部。

重要的是，这不是仅选430扩大类中的任意核：
真实原源词为
\[
 X=A(h)uA(k)=VU(h)M_{g_1}U(k)V^*,
 \qquad A(h)=VU(h)V^* .
 \tag{32}
\]
430的半线局部化准确给
\[
 X-VBV^*\in\mathcal S_1 .
 \tag{33}
\]
证明不能称 \(g_1-\gamma_1\) 紧支：V*输出位于固定半线，
U(k)有限传播，故先乘一个在该输出半线恒1的光滑χ；
\(\chi(g_1-\gamma_1)\) 才光滑紧支。
随后两侧U(h)、U(k)的传播使双变量核紧支光滑，故迹类。
真实词X属于 \(C^*(1,u,\mathcal E)\) 中由原 \(\mathcal E\) 生成的最小闭源理想J。
因此(31)的障碍也存在于真正最小源理想，不只解析扩大。

若S为(33)的迹类差，物理 \(\mathsf P_K\to1\) 强收敛给
\(\operatorname{Tr}(\mathsf P_KS\mathsf P_K)\to\operatorname{Tr}S\)。
此性质可先以有限秩逼近S，再用双侧压缩的统一迹范数界证明。
其连续差趋零，不能取消(29)的非恒定周期差。
故对实际X，任何(31)型固定线性体积扣除仍没有联合有限部。

## 7. 已证明范围及后续问题

固定截止迹类(11)对每个原合法分割和全部有限Fij成立；
原源完整混合核由(12)–(19)保留。源词有限部反例则是明确的
p=2,q=5及(22)允许分割，不能升级成每个分割、每个测试或每个源共轭的普遍否定。
也不能由本例推出不存在周期依赖的规范相对修补。

这轮结果区分了三个命题：逐截止可求普通迹；原单个A(h)有425的纯周期有限部；
整个源稳定代数采用固定线性体积扣除却未必有有限部。
后续规范边界传递必须处理真实周期相位及逃逸球，而不能只用强收敛或抽象源商。
原源关系、完整相对Chern、实位及全素数比较、Weil二次型正性和RH均未由此证明。
