# 有限主部目标、Baire与固定正窗Gram：functional审查

2026-10-27。仅处理STATE指定比较的functional部分，不改Goal／STATE／cadence／合同，不建立C046。本稿消费537的实际fixed窗正性和552的完整Γ高频主项；新写出的Baire／代数秩及finite-rank组合是标准推论，不是新的经典正性输入或whole预算改善。源与目标是否满足本稿假设，须由实际modular输入审查另付。

恢复已读README／STATE、check→show、G20261027、A20261027、D20261027B、MACRO_FRONTIER顶部，以及537、552、553、580必要原件。根Goal是否active由root现场工具核验；子代理不创建运行实例。

## 1. 原对象与准确问题

固定紧区间K，具有非空内部，且K包含于I=(−17/16,17/16)。令

\[
 E=C_K^\infty(\mathbb R;\mathbb C),\qquad
 E^0=\{r\in E:\mu_+(r)=\mu_-(r)=0\},\quad
 \mu_\pm(r)=\int e^{\pm u/2}r(u)du.
\]

E取C∞的固定支持Fréchet拓扑，E^0取闭子空间拓扑。两者均完备、可度量，因此Baire。compact K上的函数及所有导数一致收敛保持支持K，故E确为C∞中的闭子空间；μ±在此连续，E^0也闭。不能把C_c∞的整个LF域直接称为Fréchet，当前论证使用固定K。

目标H是Hausdorff复拓扑向量空间，作为向量空间有递增并

\[
 H=\bigcup_{N\ge0}H_N,\qquad \dim_\mathbb C H_N<\infty,
\]

并且各H_N闭。Hausdorff TVS中的有限维子空间闭是标准事实；也可以把闭性明确列为实际目标需核的前提。本论证不要求H完整、不要求strict LF或特定inductive-limit universal property。把这种更强拓扑当额外必要前件会过度收窄。

所检验的是一个复线性J:E→H或J:E^0→H，以及完整Bζ是否只经J因子化：

\[
 B_\zeta(r,s)=\mathcal G(Jr,Js).
 \tag{1}
\]

G可不定、不连续；以下核障碍不需要目标正性。它不把H的命名自动变成有合法输入的算术源映射。

## 2. Baire结论：连续全域源映射的pole层必须统一有限

若J连续，令E_N=J^−1(H_N)。这些是闭线性子空间，并且E=∪E_N。Baire定理给某个E_N具有非空内部。具有非空内部的线性子空间等于全空间：平移到0得到一个0邻域包含其中，再用标量缩放覆盖任意向量。因此

\[
 J(E)\subset H_N\quad\text{对某个固定N}.
 \tag{2}
\]

相同证明适用于E^0。N可以依赖整个J和K；此处不是一个对所有映射共同的N，也不提供随K／weight／lattice增长的量化上界。结论是每个连续全域J必为有限秩，而不是输入每个r虽各有有限poleorder便可无代价地让N(r)任意成长。

这个结论仅在目标真是上述可数并且J真连续时适用。若只给每个坐标连续但没有实际目标拓扑，先核各preimage是否闭；若仅有整数／有理dense源的map，源未必Baire，不能套(2)。

## 3. exact正Gram的更强障碍：不需要连续性

Baire虽定位了统一有限poleorder，但exact因子化(1)的失败其实已有更简单的代数理由。

取χ∈C_c∞(int K)，在一个非空开区间为正。族

\[
 \{\chi(u)e^{tu}:t\in\mathbb R\}
\]

在复数上不可数线性独立。对任意有限个不同t，除以χ后得到开区间上的指数多项式；在一点取0至m−1阶导数给Vandermonde矩阵，系数全零。故E的Hamel维数不可数，而H=∪H_N的Hamel维数至多可数。任意复线性J:E→H，不论连续与否，都有非零核。

E^0同样不可数维：令P=D²−1/4。P在compact smooth源上单射，因为其齐次方程的非零解不能compact支持；分部积分给P(E)⊂E^0。因此对上述不可数族施P后仍线性独立。

[537](../../../notes/537-source-exact-weil-window-positive-tail-admission.md)已付

\[
 Q_\zeta(r)\ge\tau\|r\|_{du}^2,
 \qquad\tau=2^{-49162}>0,
 \quad r\in E.
 \tag{3}
\]

若(1)成立，对任意0≠r∈kerJ有Qζ(r)=G(0,0)=0，与(3)矛盾。甚至只要求对角Qζ(r)=q(Jr)，exact在r=0处已迫q(0)=0，核中非零源仍给矛盾。G或q的独立正性均不需要。

因此，不能把“给全E的continuous linear map落单pole层”当作exactGram不可能的首个或必要阻碍。Baire的附加信息是拓扑迫uniform有限pole层；exact全源coverage已被代数维数排除。

若从实源出发，也有相应实维数结论，但真正算术整源、复化、continuous family和完成化需各自核角色，不能因此一起排除。

## 4. 误差量词：仅du下界不支付uniform Hlog障碍

只从(3)与每个J的非零核，可对该J选r并得到

\[
 \sup_{h\ne0}\frac{|Q_\zeta(h)-q(Jh)|}{\|h\|_{H_{\log}}^2}
 \ge \tau\frac{\|r\|_{du}^2}{\|r\|_{H_{\log}}^2}>0.
\]

右边依赖J和选源，不能据此说所有finite-rank J有共同正下界。du与Hlog不等价；允许rank增长时该ratio可能趋零。

一个仅用于检验逻辑强度的标准序列控制是：源取rapid sequences，du²=Σ|x_n|²，Hlog²=Σ(1+log(2+n))|x_n|²，Q=cΣ|x_n|²。它满足du-coercivity，而前N坐标的finite-rankQ截断具有Hlog相对误差c/[1+log(3+N)]→0。该例不是本项目Wζ，仅说明不能从coercivity单独得到uniform Hlog lower。

## 5. 消费552的实际Γ高频后，finite-rank误差下界为1

本项目另有足够强的旧输入：[552 §5](../../../notes/552-radial-adelic-green-principal-and-comparison-gate.md)由完整显式公式核固定compact profile的

\[
 Q_\zeta(\psi e^{itu})=(\log|t|)\|\psi\|_2^2+O(1).
 \tag{4}
\]

采用[553](../../../notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md)的原Hlog规范

\[
 \|r\|_{H_{\log}}^2=(2\pi)^{-1}\int
 [1+\log(2+|\xi|)]|\widehat r(\xi)|^2d\xi,
 \qquad\widehat r(\xi)=\int r(u)e^{-i\xi u}du,
\]

同一Fourier平移给Hlog²=(log|t|)||ψ||²+O(1)。以下将(4)在一个固定有限维profile空间上统一消费，并把J核条件精确保持。

设J:E→V的rank为d<∞；这一节不需要J连续。选d+1个在int K中支撑互不相交的φ_j∈C_c∞，各du norm为1。对大实t，令

\[
 a_{j,t}=-t^{-2}P(e^{itu}\phi_j),\quad
 h_{j,t}=a_{j,t}/\|a_{j,t}\|_2.
\]

P的分部积分使μ±(h_{j,t})=0。支撑仍不交，故h_j,t正交且norm1；又

\[
 a_{j,t}=e^{itu}\bigl[\phi_j-2it^{-1}\phi'_j
 -t^{-2}\phi''_j+\tfrac14t^{-2}\phi_j\bigr],
 \quad\|a_{j,t}\|_2\to1.
\]

对每个t，d+1个J(h_j,t)在rank d空间中线性相关。取系数向量x(t)的Euclidean norm为1，使Σx_j(t)J(h_j,t)=0，并置r_t=Σx_j(t)h_j,t。于是

\[
 Jr_t=0,\quad\mu_\pm(r_t)=0,\quad\|r_t\|_2=1,
 \tag{5}
\]

而r_t仍为频率t乘以一个固定有限profile空间内、系数一致有界的函数。无需x(t)有可测性／连续性，因为这里只逐t选源、取序列t→∞，不对t积分。

Γ渐近与Fourier profile的Schwartz尾给

\[
 Q_\zeta(r_t)=\log|t|+O_J(1),\qquad
 \|r_t\|_{H_{\log}}^2=\log|t|+O_J(1).
 \tag{6}
\]

统一性不是未付假设：这些profiles都在由有限个φ_j、φ'_j、φ''_j张成的空间，单位系数集的Schwartz半范数一致有界。在|ξ|≤|t|/2用Γ(ξ+t)−log|t|的有界性，补集由任意多项式阶Fourier尾控制，即得arch式。全部prime-shift在fixed K仅有限个并由du norm有界，包含actual properpowers；pole按(5)实际为零而非从定义删去。因此误差O_J(1)可依赖d、profiles和K，不依赖t。

对任何只经J读取且在零数据为0的q，令s_t=r_t/||r_t||Hlog，得到

\[
 Js_t=0,\qquad Q_\zeta(s_t)\to1.
\]

从而

\[
 \sup_{r\ne0}\frac{|Q_\zeta(r)-q(Jr)|}{\|r\|_{H_{\log}}^2}\ge1.
 \tag{7}
\]

这适用于每个finite-rank J，不要求rank统一。因此fixed-K上的finite-rank因子化族也不能有趋零的**uniform two-sided Hlog误差**。Baire一旦把某个honest全域modular map化成finite rank，即可套(7)。式(7)是旧Γ~log高频机制与有限核的直接合成，不能不扣552/580而报新whole后果。

## 6. 系数方向：禁止把(7)扩成单边正性方法总体失败

(7)排除exact identity、绝对／two-sided小误差，或上侧

\[
 Q_\zeta(r)\le q(Jr)+\delta\|r\|_{H_{\log}}^2
 \quad\text{with }\delta<1.
\]

它**不排除**正性证明可能使用的下侧

\[
 Q_\zeta(r)\ge q(Jr)-\varepsilon\|r\|_{H_{\log}}^2,
 \qquad q\ge0.
\]

在kerJ上，下式只要求Qζ(r)≥−ε||r||²，与(3)/(6)完全相容。这样的证明仍须独立支付残差的下界／正性；kernel障碍不能代付或否定该笔signed责任。G=0也能形式写下相同目标，故没有实际残差估计时仍只是正性责任重述。

只读J的非线性后处理、有限个J组合或fixed relative quotient，若仍零数据给0，同样受核论证；**非线性源map本身**不在此线性/Baire结论里。不能将二者混同。

## 7. 逃逸与正控制

* **先整／有理源再完成。** 可在可数维dense源代数上把每个有限组合送进honest输入，再完成配对；它不要求J从整个Fréchet E连续地取值于honest H，不能套(2)或不可数维论证。
* **完成化／广义输入。** H的真正无限系数完成空间可有不可数Hamel维数，且不再是union有限pole层；须另证theta／Green／principal公式在该域的延拓与原费。
* **cutoff族／逐测试逼近。** 每层finite rank不阻止逐固定r收敛；在ℓ²中||P_Nx||²→||x||²而uniform误差恒1是标准控制。把actualB的finite projection拿来近似只能验证逻辑相容性，若其正性来自待证Q，不能当classic新正来源。
* **真函数域的连续family。** 旧567实际给Q=L∫_0^L||Σ_jr(y+jL)E_{j+j0}||²dy。每个y只有有限divisor组合，但whole target是y-family／L²完成，不是一个honest可数维输入H。故真FF正源机制已提供本门的合法绕过；不得按“每fiber有限”套成whole目标有限rank。
* **移动目标／非线性。** lattice、weight、载体随源／cutoff变化、真正不同的relative配对及非线性源map均须另核，不因上述命题自动失败。若声称把它们统一成一个countable union、Hausdorff TVS并保连续线性，则要对实际whole target重新核假设。

## 8. 与最强旧结果比较和建议消费

537提供固定窗严格正定。580已给任意finite通道的精确双polezero非根核，以及无限合法Hilbert塔可以保compact可见性却离开原Schwartz输入域。552提供实际Γ高频log主项；553提供全线Hlog中Pan稠密、全域bounded消关系读出必零及cofinal费用。本稿没有改善这些signed费用或得到新classic正号。

相对580“先固定有限通道”，本轮Baire说明：对**单个**从全部fixed-K Fréchet源连续取值于honest可数有限pole层的linear map，企图让poleorder依r无界，仍落单层；但exactcoverage甚至已被纯代数维数排除。这个类型定位有决策价值，不是新增独立算术输入。原norm uniform误差门(7)又是552/580的直接组装。

因此建议root将本稿按标准functional比较／旧推论范围消费，0数学轮；不借此开C046或宣布Borcherds／Weil几何总体边界。真正下一输入应落在尚未排除的连续family／完成化／整源后配对路线，或独立的signed下侧估计，而非再次优化poleN或重做Baire。

完整剩余责任不变：actualr到同一非零primitive载体、405全关系／537与全源coverage、原du/Dlog及全部height尾、完整mixedWeil身份、独立容量和成长core/coupling/Ξ。strongoldwhole4/5仍仅负惯性UPPER。
