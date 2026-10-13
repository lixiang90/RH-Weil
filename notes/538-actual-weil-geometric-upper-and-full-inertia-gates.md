# 实际 Weil 型的几何上界、全源惯性门与固定尾供给范围

2026-10-14；C010准入轮，起始HEAD35609ba，长期比较基线3a72930。
新增结论分别标为proved、conditional、experiment；实际simple-even消费完整全源桥与新整数门。
同一轮独立原源重组与不同组织逆审见
[geometric-source审查](../reviews/2026-10-14/c010-inertia/geometric-source-audit.md)和
[全源惯性/上界逆审](../reviews/2026-10-14/c010-inertia/full-inertia-audit.md)。
C008止损、不等待附件；C001原12组与所有暂停路线保持。

## 1. 实际对象与完整原来源

固定I=(-17/16,17/16)、Lebesgue L²范数及自然闭型域

    Dlog={f∈L²(I):∫log(2+|t|)|Ff(t)|²dt<∞}。

Q为原完整Weil型：actual Gamma multiplier Reψ(1/4+it/2)−logπ=2θ′，
完整dual pole及primepowers2,3,4,5,7,8。原复杂源、odd负pole及常数规范不删。
[537](537-source-exact-weil-window-positive-tail-admission.md)完整解析、全source误差、
新原FULL_REBUILD和独立全整数门已经给Q≥τI，τ=2^-49162。
本轮重新核所用raw bytes，不由作者PASS或旧收据决定数学。

    source-matrices SHA256 4bce98228442805bc5ae16e9c26c8df88e85c35ab7ec8deffdd808adbf1217ac
    tail-columns SHA256   2a88894c7405e01a37cbdef8671e9d628ddc60ae9cdb335fa2636fe49b6666a2

原有完整比较为Q≥τI+R，R=M+K+U，mI≤M≤bI，
m=9617/10400，b=63183/10400；U是已付rank-two正尾供给。
原head是degree0,…,447，每parity224，并非本轮新增参数。
其全源complement误差n=896·2^-190+2^-440、cross e=1389·2^-95+2^-440、
complement norm h=11696·2^-190+2^-440均沿用已付原预算。

## 2. 新actual even上界：完整Gamma尾的有符号计算

原64阶geometric R压缩只提案一个偶向量，没有ζ零点数据或拟合。
冻结为[64个精确有理Legendre系数](../reviews/2026-10-14/c010-inertia/sonin-even64-rational-source.json)，
f=1_I Σ_(n=0,2,…,126)c_n P_n(u/L)，L=17/16。
Nf=Σ c_n²·17/[8(2n+1)]严格正；原source字节SHA为
4bd25aab1f1574ae156884aedef90829f047a328cd2f897330b3311b6e83ff1c。
试探精度仅影响提案，冻结后所有门为Fraction/integer判断。

actual等式是

    Q(f)=<f,(M+K)f> + π^-1∫_256^∞[A(t)−7/2]|Ff(t)|²dt。

head只用raw A+J0中心，原J0已含L²，不能再乘L²；也不混入U后重复加tail。
归一化head operator费用为2^-204+2·2^-220，包含完整primitive与kernel预算。
全部Gamma尾另对这个确切源直接支付。

endpoint derivatives d_k=L^-k Σ_(n≥k)c_n(n+k)!/[2^k k!(n−k)!]给无remainder的

    Ff(t)=2[sin(Lt)S(t)+cos(Lt)C(t)]，
    S=Σ_j(-1)^j d_(2j)t^(-2j−1)，C=Σ_j(-1)^j d_(2j+1)t^(-2j−2)。

因为degree126，第127导数为0。端点跳跃正由这些boundary项支付。
保守界|Ff|²≤8(S²+C²)保持每个square内部的全部signed cross。
若S²+C²=Σ b_m t^-m，完整积分

    Iq=Σ b_m 256^(1−m−q)/(m+q−1)≥0，q=0,1,2，
    J=Σ b_m 256^(1−m)/(m−1)²≥0

均先用Fraction精确相加，不按项absolute化。
实际Binet上包络为

    A(t)−7/2≤log(t/(2π))−7/2+1/(15t)+25/(8t²)，t≥256。

实际weight与上包络均positive，故

    tail≤(8/π){[log(256/(2π))−7/2]I0+J+I1/15+(25/8)I2}。

Machin160交错上下界与log160 atanh级数完整remainder，再作256bit向外dyadic。
独立逆审改用endpoint成对直接积分，未调用原convolution字典；head三角积分、
constants及最终结果与原精确相等，见full-inertia-audit §7。

最终已支付

\[
\lambda_1(Q_{even})\le u=
\frac{7954159549289785371664718615168914673915149}{2^{256}}
<7\cdot10^{-35}.\tag{1}
\]

f的Fourier为O(1/t)，所以f∈Dlog；保even的缩支撑/光滑逼近由原form core使norm/Q收敛。
因此(1)是真正Q的upper，亦可取严格同界的合法smooth源。
与537合并，完整Q底与even底都有[tau,u]包围；奇偶及重数由下文另外的whole lower门认证。
结果归档[exact预算](../reviews/2026-10-14/c010-inertia/sonin-even64-geometric-upper.json)。

## 3. 全源谱计数及阈值运输

同自然closed form有compact resolvent，反射保域。原head complement给真正min–max后果

\[
\lambda_{225}(Q_{even}),\lambda_{225}(Q_{odd})\ge\tau+m-n>9/10,
\qquad N_Q(9/10)\le448.\tag{2}
\]

这里每parity只有224个head方向；这是完整Q的谱数目上界，远非simple-even。
不是有限矩阵通过推成定理，而是原全源complement费用与min–max消费。

令目标s，t=s−τ（也可保守取t=s），m_t=m−t>n。
原全算子压缩满足A_t=A−tI、B_t=B−2tA+t²I，D_t=B_t−A_t²=D=B−A²≥0。
D不为0；B不能替换成A²。保持原εD=εB+(2b+εA)εA，不盲加独立shift费用。
完整Schur/cross完成平方以

    αt=eθ+(1+χ)e²/(m_t−n)，
    βt=(e/θ+n)/m_t²+(1+χ^-1)h²/[m_t²(m_t−n)]

给safe finite lower型

    Pt=H0+Uhat+Wt^-1−(εH+σ+αt+βt εD)I−βt(B0−A0²)，

其中Wt≥E*(M−tI)^-1E>0须真实认证。对0≤t<m，廉价合法选择
Wt=(1−t/m)^-1W0；原W0误差已经付，不重用未知shift trial预算。
正complement和可逆triangular congruence严格给

\[
N_Q(s)=n_-(Q-sI)\le n_-(P_t).\tag{3}
\]

(3)是conditional消费门，有限Pt有负方向不反推Q有负方向。
非正交frame证明必须核codimension/full rank；若仅有近似负误差，另付frame Gram下界。
同一s>u必须同时有N_Qodd(s)=0、N_Qeven(s)≤1，才能由(1)证明真正simple-even。
这些two lower门由§5完整支付；旧τ共同下界、64阶R的odd/second-even排序均不能替代它们。

## 4. 原对象负对照与供给范围

冻结16/32/64每parity、80digits的ordinary R探索，两路独立重组一致；不是interval谱证书。
正确raw规范是Γ_nn=17/[8(2n+1)]、center=(lo+hi)/2^257、
Uraw=(648/17)(r0r0*+r1r1*)，tail raw center=(lo+hi)/2^641。
多乘L²的错误J0对象在paid constant源上严格<-1/8，而正确R同源严格>1/32。
这个negative control只显示尺度错误，不是C009反例。

[全Fraction odd64源](../reviews/2026-10-14/c010-inertia/c010-odd-rational-ceiling.json)
付整个εR=2^-204+2·2^-220+9·2^-512后给λ1(Rodd)<2·10^-31。
这只限制固定lower supplier R，不能给Qodd upper；原未消费余tail为正。
因为(1)低于此ceiling，不能凭64阶结果排除当前门。
本轮随后只检查原已冻结/认证wholehead的224维odd供给，付εR后upper约1.68368·10^-31，
仍高于u及s=10^-34，见[精确预算](../reviews/2026-10-14/c010-inertia/full-head-odd-result.json)。
因此未发现指定固定门的反例，也不据此证明odd lower。
该预注册单次对象检查不是扩大C001或刷新原pilot。随后只做原wholehead的一次移位sign门。

## 5. 一次移位全惯性证书：真正simple-even及严格谱隙

固定t=s=10^-34、原224×2 head、theta=2^-48、chi=1、80digits提案，
没有阈值/N/精度扫描。原W0使用§3的合法scalar上界，不重新导入未知inverse费用。
完整same-congruence推导见
[独立移位审查](../reviews/2026-10-14/c010-inertia/shifted-congruence-audit.md)。
若原正congruence为K0=Lambda Bc*P0Bc，则

    Kt=K0−(t/m)d289CwT0 V
       −d17T0(Δalpha+Δbeta εD)VQd^-1V
       −dT0 Δbeta/S0 V braw V
       +dT0 Δbeta/(17S0²) V araw Qd araw V。

Qd=diag8(2degree+1)，S0=2^257，Cw=29·2^769，T0=17·29·607630911·2^1282，
d=9617[9617·2^435−325(896·2^250+1)]。
所有corrections为精确有理数，原d只清t=0，不能将新的scalar直接截int。
四分母positive LCM D有824bits；Kint=D Kt保持真正惯性。
自主编译器[scripts/c010_shifted_inertia_certificate.py](../scripts/c010_shifted_inertia_certificate.py)
保留非交换顺序，用Y=VQd^-1及F=araw Qd araw−17S0 braw组织完整整数乘法。
实际全部source/V/K0输入重新绑定原fresh SHA，未执行作者新增代码或导入作者排序声明。

两个sector各自B=maxentry bitlength=4177。全224²个对称条目作真正floor：

    T_ij=floor(2^512 Kint_ij/2^B)−224 delta_ij，
    T/2^512 <= Kint/2^B = (D/2^B) Kt。

每entry floor误差<2^-512，全部row norm<224·2^-512，扣224I确付Loewner lower。
positive比例只运输惯性，不用它冒充原L² Rayleigh尺度。
本轮早期metadata曾把D/2^B文字写反，数学Kint/T实现正确；独立审查发现后，
保留原执行receipt并另存正确解释，不为文字纠错重跑编译。

odd取T本身；even只加一个正rank-one：rho=2^-105，
ordinary inverse iteration仅提案w=wi/2^192，实际512grid update为2^23 wi wj。
这个精确向量无须是真eigenvector；正rank≤1与finite惯性运输才是证明前件。
因子由80digits Cholesky提案，向下固定256bit，证明不取决于浮点Cholesky的sign。
固定guard g=2^372在512grid上对应2^-140。

本仓[独立全整数核验](../scripts/c010_verify_inertia_gram.py)重新读取两个全target/factor，
逐个Gram uppertriangle共50400个单元并累计全部448个row；
对T(odd)或T+2^23ww*(even)，实际

    target=F F*+gI+E，maxrowΣ|Eij|<g。

两个sector residual max仅263bits，严格小于g，另两个wrong-diagonal sign控制都失败于同一门。
完整[结果](../reviews/2026-10-14/c010-inertia/independent-shifted-gram-result.json)
绑定5个原input SHA及两个新target/factor/compile receipt SHA。
独立[source映射审查](../reviews/2026-10-14/c010-inertia/shifted-source-mapping-audit.md)、
[源/整数门审查](../reviews/2026-10-14/c010-inertia/shifted-inertia-source-audit.md)及
[whole-inertia逆审§6–8](../reviews/2026-10-14/c010-inertia/shifted-congruence-audit.md)
分别核对象/非交换编译、算术验收及完整负指数运输，没有余下的conditional消费项。
这给odd T严格正，even T加正rank-one后严格正，所以n_-(Teven)≤1。
经下向舍入、positive congruence及(3)完整运输，得到

\[
\lambda_1(Q_{odd})\ge10^{-34},\qquad
\lambda_2(Q_{even})\ge10^{-34}.\tag{4}
\]

结合(1)，完整Q只有一个eigenvalue在s下；自然compact resolvent确保底 attained，
奇块全在s上，而第二even也在s上，故真正ground**单重且为偶**，并且

\[
2^{-49162}\le\lambda_1(Q)\le u<7\cdot10^{-35},\qquad
\lambda_2(Q)-\lambda_1(Q)\ge10^{-34}-u>3\cdot10^{-35}.\tag{5}
\]

这是同一完整复杂源固定窗的严格谱排序，不是R的有限谱排序或coercivity改名。
源码映射与全form/rank-one运输各有不同组织审查；没有原Γ尾、primitive/whole补空间预算、
正inverse/congruence及实际新全Gram门的任何一项，就不能单独从finite PSD推出(4)–(5)。

## 6. 宏观影响与仍未付前件

新增真正几何even上界(1)、全惯性(4)支付了同固定窗排序前件；(5)给实际simple-even与谱隙。
(2)给完整低谱计数；ordinary pilot仅提案/负对照，没有升级成证书。
局部最低态排序瓶颈现在改变；全域成长/ζ识别/RH未付，C001 log13/2窗不覆盖。
这是真正新forcing，原Goal宏观完成仍须原全三择一要求与总体审计。
完整Goal原三择一另由[fresh方法类审计](../goals/reviews/2026-10-14-active-goal-fresh-completion-audit.md)
重新核535实际全p/λ/finite-repair边界；原对象/trace/依赖与旧第十节分别审核，
不凭旧receipt、合同、有限计算或推送判定。没有世界优先权、外部人类复现或形式化声明。

本轮只消费原cadence一次；C010固定窗合同在完整逆审后结算，不复活C008或刷新C001。
下一问题是growing窗的新同对象正尾/排序费用与ζ识别，而非重演这个已认证固定门。
重准入须新的actual来源和统一费用；不由固定L的(5)推成长L、RH或所有ζ零点简单。
