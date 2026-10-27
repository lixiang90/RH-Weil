# 实际inner-action锥：高阶同伦、两种分裂与普通迹regulator

2026-10-28；/root/unit_modularity独占稿。执行STATE唯一[action-cone准入](../unitary-premise/next-action-cone-hh0-admission.md)，先消费432/573准确范围。同G20261027／原0c4f；不改STATE/cadence/Git，不预C048/585。以下是实际代数上的有限链计算，出稿不代root/fresh总消费；实际HH0是否消失由独占分支另付，本文不从范数闭包推断代数边界。

## 1. 精确域与约定

取A_c=C*(A_src)⊂B(H)、I_c=A_c∩S1、Q=A_c/I_c，q为代数商映射。I_c是双侧代数ideal，但不假定operator-norm闭；Q不是Calkin或Hausdorff C*商。沿原实际酉u∈A_c，记v=q(u)，α=Ad_v，并在Hochschild链每条腿同时施α。

链C_n=Q^(⊗(n+1))取未完成代数tensor；C_−1=0。写(a_0,…,a_n)表示纯tensor，采用

\[
 b_n(a_0,\ldots,a_n)=\sum_{i=0}^{n-1}(-1)^i
 (a_0,\ldots,a_i a_{i+1},\ldots,a_n)
 +(-1)^n(a_na_0,a_1,\ldots,a_{n-1}).
\]

b_0=0，D_n=1−α_n为链映射。冻结锥

\[
 M_n=C_n\oplus C_{n-1},\qquad
 d_n(x,y)=(b_nx-D_{n-1}y,-b_{n-1}y).
\]

全部complex physical r∈S_exp给原F_r=VU(r(−·))V*∈A_c，||F_r||≤2||r||1；f_r=q(F_r)，c_r=(v^−1,vf_r)。实际b_1c_r=D_0f_r，所以J_r=(c_r,f_r)是锥一循环；这只付闭性，不先声明HH类/primitive可见性。

## 2. 一个逐阶明确的inner-action同伦

先选H_n:C_n→C_(n+1)，令H_−1=0，并置

\[
 H_n(a_0,\ldots,a_n)
 =\sum_{j=0}^{n}(-1)^j
 (a_0v^{-1},\alpha a_1,\ldots,\alpha a_j,
 v,a_{j+1},\ldots,a_n).
 \tag{1}
\]

j=0时α-prefix为空。特别H_0(a)=(av^−1,v)。直接展开给

\[
                  b_{n+1}H_n+H_{n-1}b_n=D_n.
 \tag{2}
\]

符号可逐face核：插入位置两侧的内部face由α保持乘法及α(a)v=va配对消去；同一原face的其余项与H_(n−1)b_n带相反号。j=0的首face留下(a_0,…,a_n)，j=n的末cyclic face的总号为(−1)^n(−1)^(n+1)=−，留下−(αa_0,…,αa_n)。因此没有把cyclic末项当普通bar边界省去。

n=1的完整检查是

\[
 H_1(a,b)=(av^{-1},v,b)-(av^{-1},\alpha b,v),
\]
\[
 b_2H_1(a,b)
 =(a,b)-(\alpha a,\alpha b)
 +(ba-ab)v^{-1}\otimes v
 =D_1(a,b)-H_0b_1(a,b).
\]

定义Φ_H:M_n→C_n⊕C_(n−1)为

\[
 \Phi_H(x,y)=(x-H_{n-1}y,y),
\]

右侧direct sum的微分为d_0(x',y)=(bx',−by)。由(2)，Φ_H d=d_0Φ_H，逆为(x',y)↦(x'+H y,y)。故在这个明确选择下

\[
                  H_n(M)\simeq HH_n(Q)\oplus HH_{n-1}(Q).
 \tag{3}
\]

这是代数chain isomorphism，既不套nonunital excision，也不以topological HH替换原链。

## 3. Weighted H0选择、Connes-B与第二个高阶同伦

weighted一链的degree0读法是K_0(a)=(v^−1,va)，它与H_0有同一b边界，但差不是可以直接删掉的tensor：

\[
 K_0(a)-H_0(a)
 =(1,a)-b_2(v^{-1},v,a).
 \tag{4}
\]

所以在H分裂下，J_r的第一腿为闭链

\[
 z_r=c_r-H_0f_r=(1,f_r)-b_2(v^{-1},v,f_r).
 \tag{5}
\]

为明确Connes-B约定，置signed cyclic rotation

\[
 \tau_n(a_0,\ldots,a_n)=(-1)^n(a_n,a_0,\ldots,a_{n-1}),
 \quad N_n=1+\tau_n+\cdots+\tau_n^n,
 \quad s_n(c)=(1,c),
\]
\[
                 B_n=(1-\tau_{n+1})s_nN_n.
 \tag{6}
\]

在这个未正规化约定B_0(a)=(1,a)+(a,1)。用去掉cyclic末face的b′，有b(1−τ)=(1−τ)b′、b′N=Nb及b′s+sb′=1，直接给bB+Bb=0。又(a,1)=b_2(a,1,1)，故[B_0a]=[(1,a)]于HH1。这里不能在未正规化复形中把(a,1)直接设为零，但它确为明确边界。

因此H分裂的实际source坐标为

\[
            [J_r]\longmapsto (B[f_r],[f_r]).
 \tag{7}
\]

要使首腿在链级恰为weighted K_0，可构造完整高阶K，而非只指定degree0后宣称存在。令degree2算子S只有

\[
 S_0(a)=(v^{-1},v,a)+(a,1,1),\qquad S_n=0\ (n>0),
\]

并置

\[
                 K=H+B-bS+Sb.
 \tag{8}
\]

bB+Bb=0及b²=0给bK+Kb=D。直接核bS_0后，(8)确有K_0(a)=(v^−1,va)；K_1=H_1+B_1+S_0b_1，n≥2时K_n=H_n+B_n。于是第二个分裂Φ_K(x,y)=(x−K y,y)满足

\[
                       [J_r]\longmapsto (0,[f_r]).
 \tag{9}
\]

两坐标相差Connes-B shear；没有矛盾，也不能把(7)的B[f]或(9)的零首腿单独命名为新primitive。分裂依赖同伦选择，不是一个无需选择的HH1/HH0双标签。

## 4. 普通迹给出实际锥regulator，非形式指定

432的Ω在此扩大域仍有直接定义。对Q中的一循环x=Σa_i⊗b_i，选实际有界提升A_i,B_i∈A_c；Σ[A_i,B_i]∈I_c，故Ω(x)=Tr Σ[A_i,B_i]。原提升独立和b_2消去证明逐项仍适用：I_c腿给bounded/traceclass交换子，普通迹为零；不需要每个[A_i,B_i]单独迹类，也不需要Ω在operator-norm tensor完成中连续。

更直接地，对锥一循环(x,y)，取x的有限tensor提升及y=q(Y)，定义

\[
 T_{x,y}:=\sum_i[A_i,B_i]-Y+uYu^*,\qquad
              \widehat\Omega(x,y):=\operatorname{Tr}T_{x,y}.
 \tag{10}
\]

锥循环条件bx=Dy精确保证**整个T_(x,y)**∈I_c。这里没有分别对无穷trace的Y或各交换子取迹。

改变x的tensor提升只增加有界/traceclass交换子的有限和，迹零；Y变成Y+R、R∈I_c时增加−R+uRu*，普通迹亦零。因此(10)是实际Z1(M)上的规范线性数据。对锥边界d(X_2,Y_1)，令W=b_1(\widetilde Y_1)为原有界提升的有限交换子和，不假设W迹类。由b_1b_2=0，(10)在该边界的提升整体恰为

\[
          -(W-uWu^*)+W-uWu^*=0.
\]

故(10)降到H1(M)。它是固定实际extension A_c→Q、lifted action Ad_u与普通迹数据选出的延拓，不只是“inner action标准分裂”所赋的名字。

在H分裂下(10)=Ω(x−H_0y)，因为H_0Y=(Yu*,u)的交换子就是Y−uYu*。在K分裂下也有同值：由(4)，K_0y−H_0y为1⊗y减明确边界，Ω在其上的值为零。两种自然选择因而给同一实际regulator；不由此声称任意高阶同伦选择都会保一个未经指定的regulator。

一般把HH0上的任意泛函加到一个分裂读出，会得到另一延拓；那是额外自由数据，不是(10)的普通迹来源。即使给定一个同伦分裂，形式上允许这种自由加项也不能提供算术比较或canonical物理charge。

## 5. 两个实际值：旧−4保留，全部物理J严格为零

取573的旧闭循环ζ=q(T)⊗q(T*)，实际[T,T*]有限秩且Tr=−4。它仍是Q上的闭循环，扩大到A_c不会使这个Ω值失效。因此

\[
          (\zeta,0)\in Z_1(M),\qquad
                    \widehat\Omega(\zeta,0)=-4.
 \tag{11}
\]

若(ζ,0)是锥边界，(10)应给零，与(11)矛盾；故旧类的保留是真实的。这不意味着它等于物理J_r。

对全部complex r∈S_exp，包括全部noncompact405/Pan和537非根，J_r有固定实际提升

\[
             x=u^*\otimes uF_r,\qquad y=F_r.
\]

(10)的整体提升为

\[
 [u^*,uF_r]-F_r+uF_ru^*
 =(F_r-uF_ru^*)-F_r+uF_ru^*=0.
\]

因此

\[
                        \widehat\Omega(J_r)=0
           \quad\text{对全部原complex }S_{\exp}\text{ 源}.
 \tag{12}
\]

这个全源结论不需要HH0[f_r]为零，不需要crop，也不需要把Σ1或Ω的域从标量积分形式外推。它正对应573§8的最强旧：真实对称闭修补的普通迹为零，非零电荷若有，须来自另一个独立闭循环。此锥可以保旧(ζ,0)而仍对物理拉回全零。

## 6. 若HH0有有限代数证书，物理J的显式边界

本节**conditional消费**：只有另一分支在当前准确Q域给出有限一链y=Σ(a_i,b_i)且b_1y=f，才适用；norm-closed commutator span或topological HH零不够。

置T=(v^−1,v,f)，并令

\[
 Z=-\sum_i\bigl((1,a_i,b_i)-(1,b_i,a_i)\bigr)-T.
\]

因为b_2((1,a,b)−(1,b,a))=−(1,[a,b])，由(5)有b_2Z=c−H_0f。利用(2)，直接得到

\[
                  d_2(Z-H_1y,-y)=(c,f)=J.
 \tag{13}
\]

所以在**有限代数HH0证书已另付**时，J不仅regulator值零，而且是原未完成锥的明确代数边界。本文没有证明所有f_r都有该证书，也没有因A_c为C*完成就把它当已给。

## 7. bounded lifts、源费用和未付的拓扑／经典责任

所有H_n项是有限个原代数tensor，α由实际unitary conjugation提升。用有界提升的operator projective tensor代表费，H_n的充分上界为(n+1)倍原代表费；B_n为2(n+1)倍。S_0代表费≤2||A||，K_0实际简式代表费≤||A||，K_1可取10倍二tensor代表费，n≥2可取3(n+1)倍。这里只为每个fixed n付款，不宣称跨n完成化或Ω连续性。

原F_r费用保留：||F_r||≤2||r||1；对support⊂[−L,L]为2√(2L)||r||du，原zero-extensionDlog可再除√log2；对strong p_(N,0)为4p_(N,0)/N。两腿J_r的operator/projective代表和≤2||F_r||。它们足以在A_c的准确扩大域给全部S_exp/Pan的有限锥链，不把此L1/strong费称为globaldu统一费，也不付trace-norm或Chow/height费。

本次实际所得为标准inner-action同伦、split/Connes-B角色和实际普通迹锥延拓；(12)的physical全零是573§8的强旧直接机制。建议本分支0数学轮，不预新classic whole/core/primitive或585。若HH0分支出现新的全源有限证书／必要费用等完整信息，其净分类须由root按实际新内容另审，本文不替它预判。

没有从(10)／(13)得到同一整模型的过滤、截面乘法、mixedRR或完整Γ/contact/properpowers/双pole身份，whole leading4/5仍负惯性UPPER；Goal完成门不因这个合法相对对象关闭。原较小代数、不同relative/non-scalar边、强拓扑及独立signed/D′未被泛排。无新外部来源或下载，所有推导只用当前实际代数与432/573原件。
