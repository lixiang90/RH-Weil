# 445 全族 continuation 独立审查（twisted_research）

2026-10-07。**限定 PASS。** 本审查独立于 radial_review；直接阅读全文445，核原通用 continuation、late-height、primitive/imprimitive及quadratic-transfer证明，并复核其441–444接口。

审查对象：`notes/445-conditional-strip-improvement-and-family-continuation.md`，canonical LF SHA256（CRLF及单独CR换LF后UTF-8）：

`99ac005976c7c22934b5597c25b0d6fc6d7f3f4d9be604f8cbd53e130eae0f2e`。

结论为：在445列明的原算术/分析通用[R]、原全primitive finite-order Hecke 7/8结论及441–444同源推导的范围内，low/high合同的共同量词和Mellin反证合法，得到稿中严格sigma1=69999/80000边界。未发现实质缺口。PASS不是对整篇原论文外部依赖的重新验收，没有Lean构建、kernel证书或RH证明；AF比例不参与本次改进。

## 1. 固定源及推导链绑定

OpenAI/math源提交 `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，文件
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，canonical LF SHA256：

`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。

本次直接读取以下原来源位置：

| 原条款 | 行号 | 审查用途 |
|---|---:|---|
| 全primitive Hecke beta_*定义、finite factor deletion | 373–398 | 原共同角色族、supremum、poles excluded |
| `lem:continuation-criterion`完整陈述和证明 | 400–502 | sigma0∈(1/2,1)、统一epsilon_*、小Z、Mellin/Fourier与非attainment |
| target-independent T与same S数据 | 3327–3368 | T在eta之前固定，增加S不改变T，所有零延拓保持 |
| principal-data/contract | 5502–5623、6180–6301 | 同一H、c_S、A_T、全高度principal余项与主留数signal |
| fixed-bin及central accounting | 5808–6165 | whole-bin先移、同一累计height预算、固定A/B后选外尾阶数 |
| `lem:late-height-closure` | 6520–6580 | target后选tau,N，公共saving在target前固定 |
| quadratic transfer | 6715–6780 | Euler factor身份、imprimitive、s=1极点例外 |
| 原Part II order | 16191–16453 | 量词顺序和同一physical函数无T1 |

此外，当前441–444版本绑定如下；该表标明445所合并的具体对象，不将哈希视作数学证书。

| Note | canonical LF SHA256 |
|---|---|
| 441 | `dffcaa1899358d581fe3d6438ee87d075588e5e7e8f41ccd8a629fe5c31be0dd` |
| 442 | `87abb4dd86ccae9b8209e030606413ef2b8682631f9c4d9195afdd808ad1b6b7` |
| 443 | `79bfb7f8770eb3865ccdfe0da416388b2182383bd425fd57b39f520b3fd59bc6` |
| 444 | `47686e9b6b28239562e83e9ab5199349458fd19bf9abbe45cca67df8c876957c` |

本代理先前已经独立逐源审441和443，并写same-source central joint/high完整推导；该新推导当前SHA为
`3cd3f9ff46e38e76ae245a5123946992772cee163edcd0ecafe7718612c34c2e`。
本次亦阅读全文444，核其与上述推导一致。442的principal/outer和D2*接口按已保存完整读源报告与原proof交叉核对；本审查不将固定几何旧high theorem作为新接口。

## 2. Low到omega以及共同数据

反证假设sigma1<beta_*，以原全Hecke7/8结论为明确[R] bootstrap，故
`Delta1=beta_*-sigma1∈(0,1/80000]`。这是一个原共同族的全局数，与目标eta无关。441的newlow指数准确为C(sigma1)=14999/80000，C(s)=s−11/16的slope仍为一。

原A_T最终非零、逆有任意subpower，c_S是固定正数。因此可在target前选positive epsilon_low、epsilon_norm，使和不超过Delta1/2，得到

\[
 |J_\eta(Z)|\ll_\eta Z^{C(\sigma_1)+\omega},\qquad
 \omega=\Delta_1/2\in(0,\Delta_1).
\]

固定eta只影响常数/阈值，未影响omega。J仅需于充分大real Z定义，符合原continuation criterion；小Z的控制全部来自f，而非要求J能在小Z延拓。

原3327–3343直接支持T先于目标、增加S不改T。最终target S包含其conductor、fixed-ray data、共同P0及必要的fixed exclusions；相应xi、b_*和calibration随最终S固定。physical sums、Poisson身份、H_eta、c_S与A_T均用这一个S。不能用一组S证明low再用另一组S证明high，445没有这样做。

same physicalslot windows在target前固定；目标增加的有限S只改变最终threshold及有限删除，不改变rayprime渐近leadingconstant。P0的positive Euler majorant在删去更多素数后仍有效，故H_eta在Re s>sigma1的近1、非零合同保持。所有H_eta由同一个实际u=1校正得来，不另插入一个较易非零的signal。

J和f的定义不含T1；A_T、c_S也不含T1。每个目标随后可以用不同tau估计它们，但不能借此改变这两个函数，445已明确这个关键条件。

## 3. High余量与K/mu选择顺序

newcentral certificate m_ad=307/11016000已相对C(sigma1)。zeta=m_ad/32的上端extension最多耗m_ad/16；central real、multiplicity与inverse-normalizer总预算小于m_ad/4后，剩余仍大于m_ad/2。比较C(beta_*)还减去正Delta1，不重复扣旧7/8到sigma1的变化。

选择先后无循环：先用m_ad的固定份额指定actual count/moment/capacity与rounding losses，并选原uniformplainmesh；然后选finite even K、equal ell_i和disjointwindows。此时才定义

\[
 \mu=\sigma_1\ell_1/(2K),\qquad
 m_w=l_y/20,\quad m_z=h_1/600.
\]

mu严格小于sigma1 minell_i，principal槽localdecay使用new正确指数sigma1，而不是无付款保留旧7/8。K固定后再缩amplitude/prime-bin powers与e，既不反过来改变先前mesh，也不要求在K趋无穷时一致。

principal三项的smallpowers与e低于各margin四分之一，分别仍留至少3/4 m_w、3/4 m_z、3/4 mu。外小行margin172249/2000000另留一半；large-row fixedz_infty可在target前选到至少m_ad saving。newrealboxes和dmax=h1+zeta<1均固定。

故

\[
 m_0=\min\{m_{ad},m_w,m_z,\mu,172249/2000000\}>0,
 \qquad m=m_0/4
\]

在这些步骤之后统一选择合法。central最初预算不必重新缩到m0，因为已剩不少于m0/2；principal和outer也各留不少于m0/2。有限sum及额外任意smallpowers可用这些strict余量吸收。common m依赖已固定slot system和geometry，仍在eta之前固定。

actual central #rows来自443的kappa_eff=3/4调用，未使用signed negativeDelta旧statement或nominalR。mixederror subsets的numerator conductor budget只使用一次；floor没有actualwitness保证，单独用absolutecount；boundednontrivialunits保留在外小行。445的四范围覆盖全部physicaldyads而不是只认证h1。

## 4. Internal orders、late height与外尾

固定target后，允许arithmetic datum、Theta和finiteinternalheight/seminormorders依赖它。A_eta一次支配retained numerator、actualcounts、dyadic/witness、primeprofile及所有内部成本；B_eta由fulltuple all-height/global/absolutebounds给出。提高稍后的externalN只改externaltestseminorm及threshold，不重跑一个N-dependentinternalmoment。

原detector e0只依赖requestedloss与boundedpre-saturationranges，可以在target前选e；profile/seminormheight成本随后固定。一个累计T1/2矩阵预算同时覆盖physical Im z、witness和primefrequencies，不能在后续步骤恢复完整buffer。

对原literal detectorheightconditions，445取
`tau0,eta=d_min epsilon_ht/[20(1+A_ht,eta)]`。
因为U>=Z^{d_min}，最终有`(1+T1)^{A_ht,eta}<=U^{epsilon_ht/10}`；同时tau<=d_min/100给T1<=U^{1/100}。这也控制所列crude detectorerror。小行/大行absolute估计不依赖buffered cutoff。

完整(7)的A_eta、B_eta先固定后，取

\[
 0<\tau_\eta\le\min\{d_{min}/100,\tau_{0,\eta},m/[4(A_\eta+1)]\}.
\]

第一项最多花m/4的height power；再选fixedintegerN_eta满足
`B_eta-N_eta tau_eta<C(beta_*)-m/2`，最后增大threshold。于是highsaving sigma_hi=m/2对所有targets同一，tau、N和constants允许target-dependent。这完全落在原6520–6580的通用late-height范围内；该lemma本身允许任意sigma0∈(1/2,1)，无新的7/8下界。

## 5. Mellin反证与非attainment

令epsilon_*=min(Delta1−omega,sigma_hi)>0。由于omega=Delta1/2，epsilon_*<=Delta1/2<Delta1，故
`beta_*−epsilon_*>sigma1`。统一epsilon_*在target之前固定是此反证的核心，不能只为每个eta分别获得趋零saving。

low/high的triangle inequality给f在大Z的幂界。小Z时，H_eta在Re s>sigma1有界；Re s>=2的reciprocal Euler product有界，Gaussian在固定strip上有e^{-t²}衰减。将f的原line2仅向右移至任意fixed B>2，不跨zero或pole，得到O_{eta,B}(Z^{B−11/16})。中间compact Z区间由同一Gaussianintegral的连续性控制。因此Mellin积分在Re s>beta_*−epsilon_*局部一致收敛、全纯。

Z=e^u后，原line2signal恰为`e^{-(2-11/16)u}f_eta(e^u)`的Fourierinversion。verticalarithmeticfunction连续且可积，两端幂界使u函数亦可积，故ordinaryFourierinversion识别F_eta(2+it)；再用identity theorem于Re s>1。

H_eta在更大新域内处处满足|H_eta|>=1/2，所以
`G_eta=e^{-(s−5/6)^2}F_eta/H_eta`在Re s>beta_*−epsilon_*全纯，并于Re s>1等于1/L_F^S。meromorphiccontinuation uniqueness使其成为原reciprocal的全纯延拓；亦可在避开principalpole的domain用G_eta L_F^S=1验证。principal s=1的pole使reciprocal有zero，不造成额外residue，也不能抵消一个实际L-zero的reciprocalpole。

原beta_*是 `{1/2}∪全部primitive finite-order Hecke zeros的实部` 的supremum，poles不在集合内。由于beta_*−epsilon_*>sigma1>1/2，supremum定义必给某个eta和actualzero rho满足Re rho>beta_*−epsilon_*，不要求beta_*被任何eta达到。finite deletedfactors在Re s>0非零，故该rho仍使1/L_F^S有pole，矛盾。这个target在统一epsilon_*确定之后选择，符合全族量词。

原continuation criterion 400–432明定sigma0∈(1/2,1)，所以此最终应用并没有静默扩展一条仅声明sigma0>=7/8的continuation theorem。需要重放的较窄范围是先前fixed-bin/principal解析引理，442已经逐前件处理。

## 6. Quadratic transfer与条件结论

finiteEulerfactors在Re s>0非零，primitiveHecke结论延至imprimitive。对任意primitiveDirichletchi，normcomposition给finite-orderHeckecharacter；删除3q之上的primes后，splitp的Hecke因子为 `(1−chi(p)p^{-s})^{-2}`，inertp为 `(1−chi(p)^2p^{-2s})^{-1}`。它们正好等于chi与chi chi_{-3}的两个Dirichlet因子，先在Re s>1相等再meromorphiccontinuation。

在0<Re s<1两Dirichletfactors全纯，一个zero不能由另一个pole抵消；s=1+it、t!=0同样无pole。s=1唯一可能pole-zerocancellation要求一个primitiveinducingcharacter为principal，另一个是chi_{-3}；后者的L(1)=pi/(3sqrt3)>0。因此全部Dirichlet，包括zeta，得到同一**strict**边界；principalpole允许。未对boundaryline作无零声明。

445的结果是所列原generic[R]与原7/8bootstrap成立时的新的引用推导。[R]仍包含完整coefficientwiseprobe/Poisson/calibration、localtables、fixed-familyL bounds/functional equation、witness、marked/plain/recursive moments、amplification、rayprimeasymptotics。此review不替代这些外部证明，也不把finitehash/staticclosure/Fractionaudit当作Leankernel或Comparator证书。

在所绑定范围内，445的同源low/high闭合、lateheight及全族Mellin反证为PASS。没有将AF67.25%固定函数比例用作Hecke坏行幂节省，没有由比例推出RH；来源整体独立正确性与本次新改进的形式化仍是另外的任务。
