# 明确K_g源：原费用付清，连续mixed比较被553覆盖

2026-10-27；同G20261027／runtime1793085111／原0c4f基线。执行STATE唯一明确K_g/P0/Phi_g准入，不恢复C047、不建C048/585。两原稿／fresh与root最终版本见[收据](../../reviews/2026-10-27/corrected-theta-source/root-consumption-scope.json)。

## 1. 实际Gaussian与完整零模

只用独立R_g版本，不解冻原literal K。[Poisson原稿](../../reviews/2026-10-27/corrected-theta-source/polynomial-gaussian-poisson-and-zero-modes.md)及root独立核，在z适配的B-orthonormal坐标、B-selfdual测度下，

\[
 \varphi_z(X)=(4\pi X_3^2-1)e^{-\pi|X|^2},\quad
 \mathcal F_B\varphi_z=-\varphi_z,\quad
 \varphi_z(0)=-1,\quad\int\varphi_z\,dX=1.
\]

令c_L为实际L的selfdual-measure covol，L^#为B-dual，不假设L selfdual。准确的普通Poisson式为

\[
 K_L(v,z)=-c_L^{-1}v^{-3/2}K_{L^\#}(1/v,z).
\]

large-v零模为−1，small-v零模为+c_L^−1v^−3/2，二者均为整个空间的常数。同一P0真杀两主项。有限compact orbifold lifts上的统一正定Gaussian界，给每个固定空间阶k及logv阶j的

\[
 \|D_v^jP_0K_L(v)\|_{C^k}
 \le\begin{cases}C_{k,j}e^{-av},&v\ge1,\\
 C'_{k,j}v^{-3/2}e^{-a'/v},&v\le1.
 \end{cases}
\]

所有常数限于fixed模型/格及固定阶，不报跨level一致。P0只用Ck有界或spectral Hm投影相容，不与任意空间微分算子无声交换。

## 2. 真实smooth源、原范数及实结构

W(t)=e^(3t/4)P0K_L(e^t)是C∞(M)-valued S_exp核。[费用原稿](../../reviews/2026-10-27/corrected-theta-source/original-fees-infinite-pan-and-net.md)实付对全部r∈L²(R,dt)的同一个Bochner积分

\[
 Tr=\Phi^g_r=\int r(t)W(t)dt,\quad
 \|Tr\|_{H^m}\le C_m\|r\|_{du},\quad
 C_m^2=\int\|W(t)\|_{H^m}^2dt<\infty.
\]

每个Hm及Ck费用均有限，取值C∞；空间/时间/均值交换有实际majorant。原r=e^(t/2)f_phys不改，Dlog费用为C_m/√log2，强p_(N,0)费用为C_m/√N，均为充分upper而非sharpnorm/necessary lower。全部noncompact Pan及平移留在域内。

actual Γ换格点给scalar下降；PDF5的period模型λ_z(b)=b(z,1)确认F∞为z↦barz，R_g与K_L在该共轭下对称，real r给real invariant Φ，complex源按实空间复化。因此a(Φ)在已恢复的smooth metric定义范围内可解释，非完整算术theta身份。共轭保positive volume measure，但有向形式c*μ=−μ；当前至多两组件由共轭交换且K相同，所以此实际P0源逐组件均值零，不能泛化为任意global mean-zero函数。

## 3. 扣最强旧：只有闭包同一，mixed仍全退化

553已给405实际p_b的复span在原L²du稠密。同一个L²逼近序列经每个C_m界得到

\[
 \overline{T(P)}^{H^m}=\overline{T(F)}^{H^m}
 =\overline{T(L^2)}^{H^m},
\]

也在C∞ Fréchet拓扑成立。没有证明exact T(P)=T(F)，没有将Pan在原强源拓扑宣称稠密，更没有证明T非零或其像一定无限维。

若固定sesquilinear配对β在该目标拓扑对第一腿连续，且β(Tp,Tr)=0对全部Pan及全部r成立，则上述闭包逼近迫β(Ts,Tr)=0对所有s,r。无需literal Tp=0；非零对象像可以有退化配对。H¹中E=−∫Δφ·barψ dμ及其locally-constant closed base明示，连续性已付；cited metric height为−E/4，不能免费改成正height或承袭作者7.4。任何声称同一完整经典Weil Gram身份的这类拉回，都与537正非根冲突；本轮未构造该身份。

因此当前fixed P0 scalar metric recipe按标准Gaussian/Poisson＋553强旧合成**0数学轮**停止，不再调核/模型/ray/level/weight/阻尼。支付了实际修补smooth源和全原费，但无新classic primitive/整过滤/截面乘法/mixedRR、完整signedgrowth/actualq/core/coupling/Ξ；whole leading4/5仍负惯性UPPER。cadence2／历史48／cycle16不动，Goal门open。

## 4. 唯一下一：保留同一raw K的mean/coupling检验

下一仅[未投影raw mean与bounded leg的联合准入](../../reviews/2026-10-27/corrected-theta-source/next-raw-mean-joint-source-admission.md)。raw K已经是本次实际输入，P0移除了它的空间均值；恢复这一已给数据不改核/参数。其±3/4主项可能需要强源费用，不能直接被当前T的globaldu结论覆盖；也不能冒充classic双pole ±1/2或称已逃逸。

只准核actual p_b的mean腿、与T腿联合闭包及强旧去重；不只看一个scalar非零便判全coupling。natural metric height本已忽略空间常数，不把这一旧事实另计新。该下一未执行，不预合同/轮数，也不续后章或paper。
