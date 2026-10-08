# 494. 双素数偏差核心与纯上端零点包

2026-10-08。基线 main da5f0df69864b6ecc8685e658b20d48e0a0b479f。
这是上次复盘后的第4轮，继续[493](493-original-reference-subtraction-and-carrier-near-correlations.md)。
原数域、真实素数函数、原时间权和完整目标不变。

本轮严格支付了两个完整mixed项，将当前素数主频带的未付项
缩到两条腿同时出现素数偏差的signed项。
另证明固定真实系数的八平移覆盖桥，使一个完整近相关上界足以
控制canonical区间；零点侧把低实部两端包与高实部下端包纳入已有误差，
剩下分母实部大于1/20的纯上端Cauchy包。
这些结论缩小并明确了实际核心，没有证明新的完整增长幂、中心常数、
零点比例或无零边界，新纪录论文条件仍未满足。

| 新结论 | 完整证明 | 不同作者全文独审 |
| --- | --- | --- |
| 两mixed腿的完整polylog付款 | [228行源](../reviews/2026-10-08/hybrid-original-mixed-prime-continuous-legs-research-checkpoint-audit.md) | [mixed独审](../reviews/2026-10-08/hybrid-original-mixed-prime-continuous-legs-review-high-product.md) |
| 固定系数的八平移覆盖 | [覆盖源](../reviews/2026-10-08/hybrid-original-squarefree-near-finite-cover-research-root.md) | [覆盖独审](../reviews/2026-10-08/hybrid-original-squarefree-near-finite-cover-review-perron.md) |
| 低实部与Y端付款后的Cauchy主项 | [上端包源](../reviews/2026-10-08/hybrid-original-squarefree-upper-cauchy-packet-research-perron.md) | [上端包独审](../reviews/2026-10-08/hybrid-original-squarefree-upper-cauchy-packet-review-checkpoint-audit.md) |

## 1. mixed项全部付款，实际余项只留双偏差

原实际内prime测度删除s原子后记为 \(\mu_{\mathrm{pr},s}\)，
连续参考仍是 \(d\mu_0(p)=dp/(N_L\sqrt p)\)，
\(\Delta\mu_s=\mu_{\mathrm{pr},s}-\mu_0\)，\(N_L=a_L\log X\)。
所有下式使用同一q/s、同u、sharp q-prefix、产品窗和准确频率mask。
按双线性测度身份，
\[
 K_{\mathrm{pr}}
 =K_{0,0}+K_{\Delta,0}+K_{0,\Delta}+K_{\Delta,\Delta}.
\]
493已付双连续 \(K_{0,0}=O(\log^{-3}X)\)。
本轮证明两个raw mixed值 \(K_{0,\mathrm{pr}}\)、\(K_{\mathrm{pr},0}\)
均为 \(O(\log^C X)\)，包含实际s删除的直接正修正。
因而准确得到
\[
 \boxed{K_{\mathrm{pr}}=K_{\Delta,\Delta}+O_{\phi,\chi}(\log^C X).}
\]
这作用于原完整χ-carrier signed主频带，不使用无零前件。
旧nn、graph、chirp及physical桥的完整误差合同仍保持原范围。

关键是先在恢复的空间profile上对连续腿分部积分一次，再保留外F的相消。
所有dyadic、q-clipped端点和bulk均参与，不能只付p=q的特殊alias。
固定连续p后，真实整数r<q的圆频率 \(pr/q^2\) 间距至少 \(p/q^2\)；
几何和与Schur给完整a平方能量。
未求导的r/s profile才作原C²的L1参数分离，求导后的空间因子
直接作为固定p下F的bounded s系数。每个q/p的Parseval之后再积分，
不用未付的空间Fourier加权矩。

原时间权除以n准确分离为 \(V_1(y)=V(y)/y\)，\(y=sn/(qX)>0\)。
其外n相位模长1；逐j的residue Cauchy包括两个端周期和原unit mask。
对每个实际dyadic box，完整费用为
\[
 \ll\frac{Q}{N_L^2X}(1+S/X)\log^C X\ll\log^C X.
\]
再对全部boxes、原同u积分及四种最大标签位置求和仍是polylog。
这是带F的signed预算；不能由此宣称固定参数的centered
\(E_H\)、\(E_G\)正能量已有新的省幂，也不能声称旧JSC一侧协方差合同已付。
双偏差的完整signed算术预算尚未证明。

## 2. 近相关到canonical四矩的有限覆盖

保持490的同一真实 \(R(t)=\sum_{Y<n\le X}r_n n^{it}\)，
八个辅助平移都不改变X、Y、U、V、r或平方系数g。
取 \(h_m=(-1+m/2)T\)、\(0\le m\le7\)，并令
\[
 W_T(t)=\frac18\sum_{m=0}^7\nu_T(t-h_m).
\]
原ν在 \([6T/5,9T/5]\) 的一致正下界给
\[
 W_T\ge\frac1{16T}\mathbf1_{[T/4,4T]},\qquad
 \frac1T\int_{T/4}^{4T}|R|^4\le16\int W_T|R|^4.
\]
这是辅助正majorant，不是把单个原ν上界倒用。
其准确核为
\[
 \Psi_{\mathrm{cov}}(u)=
 \Gamma(s_Tu)\left(\frac1d\sum_{k<d}e^{ik\eta u}\right)
              \left(\frac18\sum_{m=0}^7e^{imTu/2}\right).
\]
原阈值 \(\Delta=1024\log^{5/2}X/X\) 外的全部真实系数相关
仍付 \(X^{2-\sqrt{8\pi}}\log^4X\)，对角仍仅已付polylog。
因此一个完整combined近和的一侧上界
\(C_{\mathrm{cov,near}}\ll X^{B+\epsilon}\)、固定 \(B\ge0\)，
足以给canonical \(R\) 的同幂上界；不必八份near分别小。
尚未证明 \(B<5/7\)。

在原全高度 \([R_\theta]\) 和完整准入合同下，
先得到canonical \(R\) 的界，才在J消费490的完整误差
\(c_\theta=1-1/(2\theta)\)。令 \(b=\max(B,c_\theta)\)，
原完整函数的增长为b，完整矩差费用为 \((3b+c_\theta)/4\)。
名义7/8时，真正的 \(B<5/7\) 会改善此增长；覆盖本身不改善它。
W的支撑伸出J，不能把453的固定零点包或旧J误差免费搬到全部W上。

## 3. 零点侧剩余是纯上端的正实部Cauchy包

只在名义 \([R_{7/8}]\)、\(Y=X^{5/7}\) 配置中，
保留453固定负高度零点集合及全部重数，取 \(\eta_0=1/20\)。
对 \(a_\rho=\beta-1/2\le\eta_0\) 的整个低包保留两端entire核，
包括负a及a=0；局部零点计数的直接正包络给四矩费用1/5。
对 \(a_\rho>\eta_0\) 的整个Y端，用weighted Hölder和既有三段密度，
费用函数为 \(4(5/7)(\sigma-1/2)-1+n(\sigma)\)；
全区间supremum是11/35，出现在 \(\sigma=3/4\) 的费用包络。
这不声称有实际零点或密度饱和该包络。

令 \(x=\lfloor X\rfloor+1/2\)，剩余准确主项是
\[
 C_X(t)=-\frac{e^{it\log x}}{N_L}
 \sum_{\substack{\rho=\beta-i\gamma\in\mathcal Z_T\\a_\rho>1/20}}
 \frac{m_\rho x^{a_\rho}e^{-i\gamma\log x}}{a_\rho+i(t-\gamma)}.
\]
完整函数身份为 \(R=C_X+E_C\)，同一J及原ν下
\[
 M_4(E_C)\ll X^{3/7+\epsilon},\qquad
 \max(3/7,1/5,11/35)=3/7.
\]
任何 \(B\ge3/7\) 的R与C_X上界可双向运输，但只运输完整函数差。
分母实部现在一致大于1/20，全部留数、上端相位及原固定集合仍保留。
完整四零点相关尚未付；其既有密度费用仍为5/7，
已有增长合同下的矩差仍为9/14。
该结构分解不扩大到上一节W的支撑。

下一轮聚焦两条真实偏差的带F联合和，或固定上端Cauchy包的
完整四零点相位；系数路线则直接估计覆盖核下的完整近相关。
这些是不同观察量的充分接口，不能彼此替换成已付的正能量。
原比例接口仍须支付实际中心四阶常数及其计数桥。
复盘计数推进至4，默认第6轮俯瞰复盘，最迟第8轮。
