# 414. 双零边界的实际酉元与同一表示中的联合周期迹

2026-09-21。[T/O] 来源审查、两份独立数学复核及采纳定向核对均已闭环。
沿用413的同一两有限位径向来源，实零层始终不加入。

## 1. 来源、Green投影与旋转满角

固定不同素数p,q，L=log p、M=log q，θ=M/L无理。
T₀=Z∪{∞}，有限点孤立、∞邻域含一个上尾。
Y=T₀²×R_t，离散Γ=Z²按
(a,b)(j,k,t)=(j+a,k+b,t+aL+bM)作用。
令A=C₀(Y)⋊Γ；B₀=Z²×R为开层，D={(∞,∞)}×R为闭层，
J=C₀(B₀)⋊Γ，I=C₀(Y\D)⋊Γ，A_D=C₀(R)⋊Γ。
413已计算J≅C₀(R_x)⊗K(ℓ²Z²)，x=t−jL−kM；
K₀(I)→K₀(A_p⊕A_q)=Z²单射、像为{(n,−n)}。η表示(1,−1)。

系数约定α_(a,b)f(t)=f(t−aL−bM)。
选实值非负c∈C_c∞(R)，满足

    Σ_n c(t−nL)²=1。                                    (1)

可从正集的L平移覆盖R的紧支光滑φ出发，除以sqrt(Σ_nφ(t−nL)²)。
在B=C₀(R)⋊p^Z中定义

    e=Σ_n c(t)c(t−nL)U_p^n，
    w=Σ_n c(t)c(t−nL−M)U_p^n，   v=wU_q。               (2)

紧支性使这些和只有有限个非零Fourier系数。
Green右Hilbert C(R/LZ)-模的内积为
⟨ξ,ζ⟩([t])=Σ_n overline(ξ(t−nL))ζ(t−nL)；
左B内积为Σ_n ξ(t)overline(ζ(t−nL))U_p^n。
因此e=Θ_(c,c)、w=Θ_(c,c_q)，c_q(t)=c(t−M)。
(1)给

    e²=e=e*，ww*=e，w*w=α_q(e)，v*v=vv*=e。             (3)

eB e=C(R/LZ)e，且⟨c,c⟩=1使e满；e在A_D中仍满。
e属于代数本身，裸U_p、U_q通常只属于乘子代数。
“秩一”指Hilbert C(S¹)-模中的秩一，不是整个Hilbert空间中的有限秩。

令u₀=exp(2πit/L)e，则u₀、v在角单位e下酉，且

    v(f(t)e)v*=f(t−M)e，u₀v=exp(2πiθ)vu₀。             (4)

每个eBα_q^b(e)由Θ_(c,α_q^bc)作为C(R/LZ)-模生成，故eA_De由
C(R/LZ)e和v生成。q次数的规范圆作用与旋转代数满射相容；
零次部分忠实，圆平均条件期望忠实，故此满射单射。
这是实际满角同构，不能用裸eU_qe替代修正后的v。

## 2. 源酉元和实际一般提升

由Y→R及同一Γ作用有非退化表示A_D→M(A)，
系数在j,k方向常值。记(2)的乘子像仍为e,v。
令h(j)=1_(j≥0 or j=∞)，Q(j,k,t)=h(j)h(k)，则

    u=1−e+v∈A_D^~，u*u=uu*=1，
    T=1−Q+QuQ=1−QeQ+QvQ∈A^~。                        (5)

Q在M(A)中；两个Q压缩的系数有紧上尾与紧t支集，故QeQ,QvQ∈A。
在D上Q=1，所以T的商正是u。
这是一般提升，未宣称T酉或可逆；相同表达式1−e+v在M(A)中确是酉提升。
代数单位化与乘子代数的区别不能略去。

## 3. p边的实际核余核

在P={∞}×Z×R取s模L；proper群胚模纤维为ℓ²(Z_a×Z_k)，
t=s+aL+kM。各k块中c_k(a)=c(s+aL+kM)为单位向量。
e是各块的秩一投影，v把c_k送至c_(k+1)，u在正交补恒等。
Q在此只看k≥0，与e交换。因此T在c_k链上是负k处恒等，
与非负k处单边正移位的直和；其他方向恒等。
其核0、余核span(c₀)，并且c₀随s的圆周过渡相容：

    ind_P(T)=−1。                                        (6)

## 4. q边的有限边界通量

在Q层取s模M，纤维ℓ²(Z_j×Z_b)，t=s+jL+bM。
令H=1_(j≥0)，c_b(j)=c(s+jL+bM)，并记

    a_b(s)=⟨c_b,Hc_b⟩=Σ_(j≥0)c(s+jL+bM)²。             (7)

e为c_b的块投影，v把c_b送至c_(b+1)，T=1−H+HuH。
因c紧支且L,M>0，s在[0,M]中时，b充分负有Hc_b=c_b、a_b=1，
b充分正有Hc_b=0、a_b=0，界可一致选取。
故[H,u]在整个基本带中具有共同有限坐标支集。

对投影H及酉u，在H−u*Hu有限秩的本处情形，有

    ind(HuH:Hℋ→Hℋ)=Tr(H−u*Hu)=−Tr(u*[H,u])。          (8)

公式有直接有限维证明：记P=H、R=u*Hu，用u*识别靶空间，
u*(HuH)=RP:Pℋ→Rℋ。令K=ker(P−R)、F=K^⊥=ran(P−R)。
K是两个投影的共同不变子空间，它们在K上相同，故F也同时不变。
无限维部分准确位于PK=RK，RP在此为恒等；不是在整个K上恒等。
有限维部分RP:PF→RF的指数为dim PF−dim RF=Tr(P−R)，从而核准(8)。

展开u=1−e+v。交叉项改变b，没有对角迹；
b块的剩余迹是a_(b+1)−a_b，且只有一致有限多个非零项。
所以

    Tr(u*[H,u])=Σ_b(a_(b+1)−a_b)=−1，
    ind_Q(T)=+1。                                        (9)

指数沿s圆周恒定，K₀(C(S¹))由秩识别。没有断言实际核维数无跳变。
同一T的两侧指数及413的单射给

    ∂_D[u]=−η。                                          (10)

因此u⊕1_n没有可逆的A单位化提升。乘子酉提升并不与此矛盾。

## 5. 时间缺陷与有限恒等式

真实时间作用为β_s(f(t)U_g)=f(t−s)U_g。
取c_s(t)=c(t−s)，则β_s(u_c)=u_(c_s)、β_s(T_c)=T_(c_s)，且

    β_s(T_c)−T_c=−∫₀ˢβ_r(∂_tT_c)dr。                  (11)

只微分有限个紧支光滑系数即可证明；没有按目标分布定义补偿。
任意两个非负平方分割之间，可对(1−r)c+rd重新归一化得到共同紧支路径，
所以u的K类不依赖截止，不能据此断言所有算子读出也不依赖截止。

    (A_D)^β={0}，(A_D^~)^β=C·1；A同理。                 (12)

对β固定的代数元素，每个Fourier系数是沿t平移不变的C₀函数，
故为0；约化交叉积的Fourier系数唯一性给结论。
这不排除乘子箭头、协变Hilbert模或无界复形。

有限区间上有

    Σ_(b=m)^n w_b(a_(b+1)−a_b)
      =w_(n+1)a_(n+1)−w_ma_m
       −Σ_(b=m)^n(w_(b+1)−w_b)a_(b+1)。                 (13)

有限秩正交投影R、有界X,Y满足

    Tr(R[X,Y]R)
      =Tr(RX(1−R)YR)−Tr(RY(1−R)XR)。                   (14)

(14)在乘积中插入R+(1−R)，由有限维迹循环性得到。
这些只是实际缺陷的有限恒等式，未把任意标量权认成Fourier截止。

## 6. 算术主消失仍未证明

若把(10)的源酉边界自动宣布为主关系，并只用412两个原局部函数式ℒ_p、ℒ_q，
取sharp不变非负测试k，支集靠近±L，避开q的周期、p高次周期及0，并令k(L)>0；
按413第7节式(18)，可得

    −ℒ_p(k)+ℒ_q(k)=−2L k(L)≠0。                       (15)

因此不能同时采用这种主关系规则和只有这两个局部项的读出。
任意支撑在{0}的分布补偿也不能消去此见证，因为k在0邻域恒零。
这不排除非局部transgression、连接、循环或导出几何数据。
下节构造T与联合周期迹的共同表示，但不证明主关系、完整B、固定双矩或RR。

## 7. 共同壳层投影

在真实H_rad,p⊗H_rad,q上用412的递增Fourier／紧单位投影R_(N,p)。
S_(N,p)=R_(N+1,p)−R_(N,p)是秩2投影，412的每N精确迹式给

    Tr(S_(N,p)V_(p,a))=2·1_(a=0)。                      (16)

定义正交和

    Π=E_p+E_q，
    E_p=R_(N_p,p)⊗S_(N_q,q)，
    E_q=S_(N_p,p)⊗R_(N_q,q)。                           (17)

在径向子空间，另一素数的缩放是紧单位作用，因而恒等；
实际Γ作用的局部径向表示确为W_(a,b)=V_(p,a)⊗V_(q,b)。
张量迹分解给

    (1/2)Tr(ΠW_(a,b)Π)
      =0                           a≠0,b≠0；
      =p^(−|a|/2)                  a≠0,b=0；
      =q^(−|b|/2)                  a=0,b≠0；
      =2(N_p+N_q+1)                a=b=0。               (18)

1/2来自真实壳层秩2；Π是投影，Π/2则只是正算子。
N_p,N_q分别趋于无穷时S_N及Π强趋于0，虽然轴向迹保持非零。
不能交换该强极限与迹。实长度aL+bM稠密，不能假定一个共同紧基本区间。

### 7.1 同一来源的协变表示和时间平滑

取H=H_rad,p⊗H_rad,q⊗L²(R_t)。
C₀(Y)在e_j⊗e_k分量上按f(j,k,t)相乘；定义

    π(U_p^aU_q^b)=V_(p,−a)⊗V_(q,−b)⊗U_(aL+bM)，
    U_sψ(t)=ψ(t−s)。                                    (19)

横向负指数使valuation增加；直接代换验证原α的协变性。
额外实时间1⊗1⊗U_s实现β并与全部π(U_g)交换。
换x=t−jL−kM后，J的表示为C₀(R_x)⊗K(ℓ²Z²)的忠实表示。
Γ=Z²可和，所以full=reduced并可用Fourier系数唯一性。
J为本质理想：若某元素消灭J，各Fourier系数在稠密开层B₀上为0，
再由连续性及系数唯一性为0。所以π也忠实，T及其乘子酉代表都在同一H上。

另取d_q∈C_c∞(R)、d_q≥0、Σ_n d_q(t−nM)²=1；令d_p=c。
此d_q不同于§1的c_q(t)=c(t−M)，后者仍是L长度的平方分割。
在各自基本区间积分平移平方和，得到

    ∫d_p²dt=L，∫d_q²dt=M。                              (20)

长度由实际Green归一化导出。定义有界正算子

    C_N=E_p⊗M_(d_p)+E_q⊗M_(d_q)，
    A_N(h)=Σ_(a,b∈Z) C_N π(U_p^aU_q^b) U(h) C_N，
    U(h)=∫h(s)(1⊗1⊗U_s)ds，h∈C_c∞(R)。                 (21)

整个级数在下面用迹范数定义；没有假定未压缩的Σπ(U_g)有界，
也没有把它称为已经存在的Γ不变投影。

### 7.2 迹范数收敛

对固定K，有常数C_(K,p)<∞使

    ‖R_(K,p)V_(p,a)R_(K,p)‖₁≤C_(K,p)ρ_p^|a|。          (22)

在412的基e_(−K),…,e_(K−1),b_K中，
环带—环带系数只在有限a范围非零；
⟨e_i,V_ab_K⟩在i+a≥K时为sqrt(1−ρ²)ρ^(i+a−K)，否则0；
另一方向由伴随得到，球—球系数为ρ^|a|。
各矩阵元有常数乘ρ^|a|的界，有限秩一矩阵展开给(22)。
E_p,E_q均位于R_(N_p+1,p)⊗R_(N_q+1,q)之内，故
‖E_r(V_(p,−a)⊗V_(q,−b))E_s‖₁≤C_Nρ_p^|a|ρ_q^|b|。
此常数可依赖N_p,N_q，不宣称对N一致。

时间算子M_(d_r)U_ℓU(h)M_(d_s)的核是
d_r(t)h(t−t'−ℓ)d_s(t')。
在严格包含两个截止支集的固定紧区间上，核向周期圆光滑延拓；
分别在t、t'两次分部积分，Fourier矩阵元一致被
C/((1+m²)(1+n²))控制，C不依赖ℓ。
秩一展开证明其迹范数有不依赖ℓ的上界。
还可直接用Fourier秩一积分给显式一致界：约定hat h(ξ)=∫h(s)e^(−iξs)ds，
时间核等于(1/(2π))∫hat h(ξ)e^(−iξℓ)
  |d_r e^(iξ·)⟩⟨d_s e^(iξ·)| dξ。
因为hat h∈L¹，该积分在迹范数中收敛，其范数至多
  ‖hat h‖₁‖d_r‖₂‖d_s‖₂/(2π)，对ℓ一致。
四个(r,s)块与双几何级数给(21)绝对迹范数收敛。
因此可逐(a,b)求迹；没有遗漏稠密的混合长度，也没有交换N极限。

### 7.3 一个实际算子中的两个完整有限位项

E_pE_q=0，故交叉块横向迹为0。两对角块时间对角积分为
Lh(−aL−bM)、Mh(−aL−bM)。
(16)给每个N_p,N_q的精确式

    (1/2)Tr A_N(h)
      =[(2N_p+1)L+(2N_q+1)M]h(0)
       +LΣ_(a≠0)ρ_p^|a|h(−aL)
       +MΣ_(b≠0)ρ_q^|b|h(−bM)。                        (23)

混合项在完整共同Γ求和中为0，不是计算前删除。
令h(s)=exp(−s/2)k(−s)，则h(−aL)=exp(aL/2)k(aL)；
按412来源指定的两个Fourier单位扣项，得到

    (1/2)Tr A_N(h)
      −[(2N_p+1)L+(2N_q+1)M]k(0)
      =ℒ_p(k)+ℒ_q(k)。                                  (24)

ℒ_r是412式(13c)，对sharp测试写ℒ_r(k)=2𝒩_r(k)，𝒩_r为有限位半迹，
不同于整数截断N_r。若D_N=(2N_p+1)L+(2N_q+1)M，则
𝒩_p(k)+𝒩_q(k)=(1/4)Tr A_N(h)−(1/2)D_Nk(0)。
本稿壳层1/2不得与有限位半迹所需的另一个1/2混同。
截止形状不影响(23)，因为只用(20)，但实际算子可以不同。
这在原A的同一协变表示中放置了T、共同截断和联合周期迹。
仍未证明该迹下降到相对K类，或T的边界被它消去；
后续应计算T与(21)的实际相对传递／有限压缩交换子及其极限。

## 8. 形式化和来源范围

[BoundaryUnitary.lean](../formal/F1/Analysis/BoundaryUnitary.lean)的六项结果在4.32.2通过，无sorryAx：
positiveTail_leftInverse、positiveTail_rankOneDefect、positiveTail_injective、
finiteFlux、finiteFlux_one_to_zero、weightedFiniteFlux。
只形式化序列移位和有限通量，不认证Hilbert有界性、C*、Fredholm、共同迹或几何存在性。
[原始内核报告](../formal/checks/boundary-unitary-verification.json)、
[源码审计](../formal/checks/boundary-unitary-source-audit.json)保留23份项目源码、十处旧admission，
八包806份vendor源码已核准；原历史报告保持，未重建完整F1。

[Williams作者预备稿v3.1](../literature/f1/williams-crossed-products-draft31-2006.pdf)
（2006-09-06）Corollary4.11/Remark4.12，印刷126/PDF138，(4.43)–(4.44)给Green内积输入。
具体v、满角及两侧指数仍在本文推导，不从裸Morita等价省略修正q箭头及生成性。
[Blackadar作者原件](../literature/f1/blackadar-k-theory-author-book6.pdf)
3.4.1–3.4.5(PDF32–33)、8.1.1/8.1.5(PDF73/75)、8.3.1–8.3.2(PDF76–77)
给单位化和指数边界；21.1.1–21.1.2(PDF231–232)给连接自然性。
一般T不能直接用[1−T*T]−[1−TT*]作为投影差；本文通过实际Fredholm层和相容扩张计算。
[完整独立来源报告](../reviews/2026-09-21/f1-boundary-unitary-source-review.md)限定核读范围，未认证全书。

[核心1–6节复核](../reviews/2026-09-21/f1-boundary-unitary-core-review.md)和
[联合迹复核](../reviews/2026-09-21/f1-boundary-unitary-joint-trace-review.md)完整保存。
工作盘短暂I/O故障后，核心稿保留原字节快照；两份新审查在精确基线的临时副本进行，
随后与原工作区对账，未依赖失联审查者未返回的全审报告。
当前证明状态不由磁盘恢复或Git保存决定；主除子、固定双矩、完整B与RR仍开放。

## 9. 最终保存范围

[核心采纳复核](../reviews/2026-09-21/f1-boundary-unitary-core-followup.md)及
[联合迹采纳复核](../reviews/2026-09-21/f1-boundary-unitary-joint-trace-followup.md)核对正文SHA256
`5da8d6eba880c082d28c49980624a525ebf6b8c136eae2d0276313611dd71f9d`。
最终仅更新开头状态并添加本节；第1–8节数学内容未改。
下一项为[实际缺陷投影与非局部传递](../reviews/2026-09-21/f1-defect-projection-joint-trace-next-proof-plan.md)。
本轮结算源对象及联合迹，完整相对主消失继续，Goal保持active。
