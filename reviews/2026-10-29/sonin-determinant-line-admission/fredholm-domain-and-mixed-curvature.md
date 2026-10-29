# Sonin压缩行列式：ordinary域、Gram metric与mixed二阶式

2026-10-29；限定候选准入核，不建合同、不计轮。恢复README/STATE/check→show、G20261027/C057/D20261029Q/formal19和前沿；读取560全文、591全文及其trace-domain澄清。当前完成门与cadence由root维护，本稿不改STATE/Git/manifest，不新读外部论文/PDF或运行数值。

**结论。** 下述ordinary Fredholm定义在每fixed finite-Euler层、compact smooth或S_exp物理源上合法。标量holomorphic τ与正Gram metric必须分开；后者在原点的mixed Levi式精确为591已付的connected covariance V_R，无额外factor2。没有新增算术principal或独立mixed正号。Strongest-old净值及最终消费由root裁决。

## 1. 实际对象、测度与源域

固定有限prime集F，P=Π_F为560实际正交Sonin投影，含完整G_F逆；不是裸有限Euler乘子。Receiver H=L²(R,dμ)，dμ=dt/(2π)。相对μ的kernel diagonal为κ_P(t,t)=2πρ_F(t)，560给

    T_F(r)=∫|rhat(t)|²ρ_F(t)dt，
    2πρ_F=Γ−2Σ_(p∈F)logp Σ_(n≥1)p^(−n/2)cos(ntlogp)+ε_F，
    ε_F∈C₀，ρ_F≥0且连续，ρ_F(t)≤C_F log(2+|t|)。

Γ为actual2θ′。以下迹积分使用ρ_F dt，**不是**ρ_F dμ；若用dμ则应写κ_P。所有常数先依fixed F，不授cofinal uniform费。

令B_F=L∞(dt)∩L¹(ρ_Fdt)，范数为||f||∞+∫|f|ρ_F。它是乘法Banach代数，fg的weighted L¹由||f||∞∫|g|ρ控制。原physical r的f=rhat，Fourier为∫r(u)e^(−itu)du。若r∈Cc∞或S_exp，则f∈Schwartz⊂B_F；分两段用|f|≤||r||₁及|t²f|≤||r″||₁可得

    ||f||∞≤||r||₁，∫|f|ρ_F≤C′_F(||r||₁+||r″||₁)。       (1)

这付强源/导数费用，**不是**原du或zero-extension Dlog的统一界。仅weighted L²(log)的Dlog条件不自动给weighted L¹(log)，所以本ordinary τ不声称覆盖全部Dlog；其二阶式另可依591在原Dlog上延拓。

## 2. S₁夹源定义，不能复活bare乘积

对bounded φ且∫|φ|ρ_F<∞，取a=|φ|^(1/2)、u=φ/|φ|（零处取0）。RKHS的ONB/Tonelli给

    ||M_aP||HS²=∫|φ|ρ_Fdt。

任意共同0≤R≤P都有R≤I、PR=R，M_aR^(1/2)=M_aP R^(1/2)为HS，且同样的平方范数不超过上式。因此

    A_R(φ):=R^(1/2)M_φR^(1/2)
           =(M_aR^(1/2))* M_u(M_aR^(1/2))∈S₁，
    ||A_R(φ)||₁≤∫|φ|ρ_Fdt。                           (2)

这是普通trace-class的独立付款。没有从PM_f为HS推出PM_fP为S₁，也没有宣告未夹源R M_φ为S₁；C054澄清中冻结的bare记法继续冻结。R可无限秩、非projection、非trace-class。

f∈B_F时φ=e^f−1满足∫|φ|ρ_F≤e^(||f||∞)∫|f|ρ_F，故

    τ_R(f)=det_H[I+A_R(e^f−1)]                         (3)

是ordinary Fredholm行列式。R=P时它等于E=PH上的det_E(Pe^(M_f)P)，其余P⊥块为identity。由幂级数的weighted L¹界，f↦A_R(e^f−1)为B_F→S₁的entire映射，τ亦entire。

有||A_R(e^f−1)||op≤e^(||f||∞)−1。因此||f||∞<log2给共同零自由邻域及logτ_R(0)=0的holomorphic分支；log(I+K)的S₁级数按||K^n||₁≤||K||op^(n−1)||K||₁收敛。该op半径不依F/R，但S₁费和高阶系数仍依ρ_F，不是uniform cofinal C²控制。

## 3. 标量logdet的混合导数

设L_R(f)=logτ_R(f)，局部中心化F_R(f)=L_R(f)−Tr A_R(f)。ordinary trace-class微分给

    DL_R(0)[f]=Tr A_R(f)，DF_R(0)=0，
    D²L_R(0)[f,g]=D²F_R(0)[f,g]
      =Tr[A_R(fg)−A_R(f)A_R(g)]
      =Tr[R^(1/2)M_f(1−R)M_gR^(1/2)]。               (4)

每项已由(2)或HS相乘付S₁；Tr A_R(f)A_R(g)的交换使用已合法的trace cyclicity，所以(4)为对称complex双线性式。R=P时确为Tr_E(PM_fgP−PM_fPM_gP)，并等于Tr(PM_f(1−P)M_gP)。

对physical r,s，令f=rhat、g=overline(shat)。由合法循环，(4)恰为

    V_R(r,s)=〈(1−R)^(1/2)M_fR^(1/2),
                (1−R)^(1/2)M_shat R^(1/2)〉HS，     (5)

第一槽linear。特别D²L_R(0)[f,bar f]=V_R(r,r)≥0；没有factor2。一般R的1−R与R不互补projection，不能省掉591 jump表达式中的killing项。

## 4. 真正的Gram metric与holomorphic标量的区别

holomorphic τ_R(zf)自身的log|τ_R(zf)|²在非零处pluriharmonic，不能把(4)直接叫作这个标量的Chern curvature。实际正metric候选应明确为

    G_R(z,w)=τ_R(zf+barw barf)，h_R(z)=G_R(z,z)>0。     (6)

其对角operator为I−R+R^(1/2)e^(2Re(zM_f))R^(1/2)，至少为min(1,e^(−2|z|||f||∞))I，因此普通det严格正。R=P时这是e^(zM_f)E中frame的压缩Gram。一般R可用isometry J_R:x↦(R^(1/2)x,(1−R)^(1/2)x)，并令D_z=diag(e^(zM_f),I)：

    J_R*D_w*D_zJ_R=I+A_R(e^(zf+barw barf)−1)。

在H中取有限ONB截断，每个det是这些frame向量外积的Gram kernel，故positive definite；S₁有限截断的locally uniform determinant极限给(6)的PD性质。不存在未付的ambient finite trace假设。

混合Levi在0的精确值是

    ∂z∂barz logh_R(z)|₀
      =Tr A_R(|f|²)−Tr A_R(f)A_R(bar f)
      =V_R(r,r)。                                    (7)

以logG_R(z,z)−logG_R(z,0)−logG_R(0,z)作holomorphic-frame归一化不改(7)。将正Levi形式称为某条Hermitian line的曲率时，必须固定line/dual及Chern号约定；此处只消费明写的正Levi。它不是由标量τ的zero divisor独自生成的正曲率，更不是global arithmetic principal-pair、整截面或mixed RR的构造。

## 5. 高阶项、非线性源与极限顺序

每fixed F/R局部有F_R(tf+sg)=二次式(4)/2+O_(F,R,f,g)((|t|+|s|)³)。若候选要求同一finite层的精确quadratic Weil身份，二阶式必先匹配V_R；高阶不能修错的二阶系数。若使用同一holomorphic源重参数Φ，Φ(0)=0且DΦ(0)r=rhat，pullback的mixed Levi仍由(7)决定。中心化DF_R(0)=0也使C²重参数的二阶项只读其一阶tangent；若改一阶tangent则需要新source-map与原norm费用，已不是本固定候选。

不能仅据fixed-layer Taylor式否定任意cofinal nonlinear scalar/height极限。ρ_F费用、三阶余项及derivative可能不uniform；交换F→primes与t,s→0至少另付相应locally uniform analytic或C²控制。单有点态functional收敛不自动给其二阶导数收敛。本稿没有补这些前件，亦不把共同op零自由半径冒成uniform高阶费。

同样，加入真实新的nonholomorphic metric项、signed relative quotient、多载体抵消或不同tangent可改变curvature；必须单独给实际式和完整费用，本稿不排除它们。仅holomorphic frame改变或减linear counterterm不改变(7)。

## 6. 对本候选能消费的最强结论

当目标就是上述共同determinant Gram metric在原点的curvature族，所有0≤R_X≤Π_X允许任意rank、合法无限维、非局部及整组三测试适应，但同层使用同R。由(7)，其三源值**逐层精确**等于591的V_R。因此591统一gap已直接阻止它们在g、τ_(1/2)g、g′三个完整目标上同时匹配；无需新cofinal derivative交换。正tensor powers/共同正混合在curvature上给positive gain/总权，其必要费用只按591原superpolynomial下界消费，非本稿新增或充分条件。成长gain、任意pointwise nonlinear metric极限和signed quotient仍未排。

此处没有删完整Γ/contact、properpowers或双pole来重命名目标；只是实际curvature尚不等于Q_W。旧560已给T−K+pole，591给V_R与完整目标的缺陷责任；行列式/Gram的合法性不支付同一非零算术primitive、principal/Green边、整过滤/截面乘法或mixed RR。Whole4/5负惯性UPPER、危险core/cross/Ξ及原Goal完成门均未因本核验改变。

依赖：[560](../../../notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md) §1/§4，[591](../../../notes/591-connected-occupation-covariance-three-fixed-test-barrier.md)及其[trace-domain澄清](../connected-variance-three-test-proof/trace-domain-clarification.md)。本稿自含定义/计算，未对既存Segal–Wilson/Simon原PDF新增阅读或把其一般line术语当新算术输入；无新math预算、来源、数值或后继variant队列。
