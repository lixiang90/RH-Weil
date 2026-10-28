# 闭C*理想包含锥：实际有限张量精确边界的强旧核账

2026-10-28；/root/rational_old_admission 独占支持稿。同G20261027、原0c4f；恢复README/STATE、check后show、Goal/C049、D20261028AA及唯一next。STATE已将本审核和另一独占e_eta test记为实际运行，C049已耗尽；本稿不修改STATE/cadence/Git，也不消费另一稿。子代理get_goal返回null，不据此否定STATE所记root同1793085111 active；root结算仍须核其实际运行实例。

**结论：此同一闭C*对象和原projective链域上，所有给定z_r已经是实际边界，未约化同调也为零。** 更强结论由显式C*函数演算因子化及一个有限Hochschild二链恒等式直接给出，原始元费用不超过6||r||_1。不能只消费较弱的边界闭包结论。它是旧闭理想资产上的标准直接应用0，未给新独立算术输入或Goal核心方法类边界。

## 1. 实际输入和原域

绑定的唯一准入原件为
`reviews/2026-10-28/independent-mixed-formation/next-canonical-inclusion-cone-admission.md`，3804 bytes，LF SHA256 `955c019afa19bbe3ccd903bec6d74245bfaf28d4b752911f6fcfcc071b5086d1`。
旧573原件13719 bytes，LF SHA256 `da5ed121715fa71ce3e83c61aef7160825778ce0beeca8df39d4ae55fbb4cd93`；实际依赖为其§1指定扩大域、§6式(10)–(11)及§7式(12)。

固定这些原件中的幺正u、实际表示及

 Abar=C*(A_src)，Jbar=closure(D_src)为Abar的闭双侧C*理想，
 F_r=VU(r(-·))V*，a=u*，B_r=uF_r。

573已付全部complex r∈L1(R)的F_r∈Jbar和||F_r||≤2||r||_1；不是只给compact源，也不是代数J_*=D_src。此处Abar含1；下面的通用引理在非幺正C*代数中也可在单位化内作同样函数演算，不须改变本实际对象。

链域严格为C_n(E)=E完成projective tensor的(n+1)重积，带原算子范数；S_n=C_n(Abar)⊕C_(n−1)(Jbar)，取sum norm，C_-1=0。i_n是包含Jbar→Abar诱导的收缩链映射；无需假设完成projective tensor的包含一定等距或单射。微分为

 D_n(x,y)=(b_n x+i_(n−1)y，−b_(n−1)y)。

b_1(p⊗q)=pq−qp，b_2(p⊗q⊗t)=pq⊗t−p⊗qt+tp⊗q；乘法有界，故这些算子延伸到原完成链域。实际z_r=(a⊗B_r，−[a,B_r])∈S_1闭合，因[a,B_r]=F_r−uF_ru*=δF_r。其原闭性不依赖任何HH/excision认同。

## 2. 闭理想内的精确因子化，含零元素

对任意B∈Jbar，存在C,D∈Jbar，使

 CD=B，||C||||D||=||B||。

B=0取C=D=0。以下设B≠0，令t=|B|=(B*B)^(1/2)，M=||B||，D=t^(1/2)。闭C*理想的连续函数演算给t,D∈Jbar：所用标量函数都在0为0，可用零常数项多项式在[0,M]上一致逼近。

对ε>0定义实际元素

 C_ε=B(t+ε1)^(-1/2)∈Jbar。

右因子是Abar内的有界函数演算元素，故理想性已足；没有引入polar partial isometry，更没有假设它属于Abar、Jbar或某个商。对任意连续q，[0,M]上的函数演算及B*B=t²直接给

 ||Bq(t)||=sup_(λ∈spec(t)) λ|q(λ)|。

标量函数f_ε(λ)=λ/sqrt(λ+ε)一致趋于sqrt(λ)，因为

 0≤sqrt(λ)−f_ε(λ)
   =[sqrt(λ)/sqrt(λ+ε)]·[sqrt(λ+ε)−sqrt(λ)]≤sqrt(ε)。

所以||C_ε−C_δ||≤sqrt(ε)+sqrt(δ)，C_ε在原算子范数中Cauchy；**闭性**给C=lim_(ε↓0)C_ε∈Jbar。又

 C_ε*C_ε=t²/(t+ε)，
 ||t−t²/(t+ε)||≤ε，

故C*C=t，||C||=sqrt(M)=||D||。最后

 ||B−C_εD||
 =sup_(λ∈spec(t)) λ[1−sqrt(λ/(λ+ε))]≤ε，

其中λ=0取0，λ>0时将括号有理化即可；取极限即CD=B，范数乘积等于M。这里确实产生Jbar中的两个实际元素，不只是B∈closure(Jbar²)。未借用未核前件的Cohen–Hewitt、H-unitality或excision。

## 3. 有限张量原始元及全部符号

对任意a∈Abar及任意B∈Jbar，采用上一节的一次分解B=CD，置

 x=−a⊗C⊗D∈C_2(Abar)，
 y=aC⊗D+Da⊗C∈C_1(Jbar)。

每个y的槽都在Jbar：C,D∈Jbar且aC,Da∈Jbar。它们是这些闭C*代数上的有限张量，既不需无限tensor和，也不声称C,D属于原未闭A_src/D_src。

直接按原cyclic末项的正号展开：

 b_2x=−aC⊗D+a⊗CD−Da⊗C，
 b_2x+i_1 y=a⊗B，
 b_1y=aCD−DaC+DaC−CDa=aB−Ba。

因此

 **D_2(x,y)=(a⊗B，−[a,B])**。

这是im(D_2)中的等式，不是只取极限得到closure(im(D_2))。原sum-projective norm满足

 ||(x,y)||≤||a||||C||||D||+||aC||||D||+||Da||||C||
          ≤3||a||||B||。

因子化对B可能非线性；此处没有宣称存在某个未构造的bounded linear contracting homotopy。逐B的实际原始元和统一范数界已经足够给所有下述结论。

## 4. 原physical源和全部费用

对原来的每个complex r∈L1(R)，a=u*范数1，B=B_r=uF_r∈Jbar，||B_r||=||F_r||≤2||r||_1。故有实际w_r=(x_r,y_r)∈S_2，满足

 D_2w_r=z_r，||w_r||≤6||r||_1。

r→z_r仍为原复线性源映射；无需把上述非线性原始元选择误称源线性。适用于全L1，因而包含全部原S_exp物理源及405的非compact真实关系与平移，也包含537的非根；没有只核关系而漏非根。

对每个L>0及supp r⊂[−L,L]，若r∈L2，则

 ||w_r||≤6sqrt(2L)||r||_du；

若原zero-extension Dlog费用有限，则进一步

 ||w_r||≤6sqrt(2L/log2)||r||_Dlog。

全线只消费L1尾费，不把它换成global L2/Hlog统一范数，也不删除L依赖。全链使用原operator norm；没有把因子C_r,D_r提升为trace-class或给其trace norm控制。

## 5. 未约化、约化和mixed读出的准确后果

在同一S复形，z_r在H_1(S)=ker D_1/im D_2中已为0，当然在约化同调ker D_1/closure(im D_2)中也为0。故本source族没有“只在闭包为0、在未约化中仍非零”的剩余类。闭性仅在构造Jbar内实际因子时用过；之后是有限张量的准确边界。

任何定义在这个未约化同调上的线性读出，对[z_r]都为0，无需另加连续性。若mixed读出在每条腿对边界不变，则任意两个源z_r,z_s的配对也为0；定义在约化同调上的连续mixed读出是其中一例。**仅有连续性而没有边界不变性**的raw链双线性/半双线性函数不受此零结论，但不能凭此称为该同调类的regulator或mixed型。

不连续或无界一词本身也不能救同一链域上的exact零类：若读出在整个当前链域上定义且对所有D_2边界为0，必仍消这些z_r。较小的强链域、原trace-norm域或原代数域可能不含C_r,D_r及此原始元；那里的边界资格必须重新证明，本文没有排除或授予它们。特别I=S1不在operator norm中闭，不能把第2节的闭C*因子化原样搬回S1；平方根因子也未必trace-class。

不声称整个S复形acyclic，不把包含锥直接认作商HH，不推一般excision或全部higher类为零。573§10的R_n=C_n(Q)⊕C_(n+1)(QJ)、d=(bx,πx−by)方向不同，原−4相对HH1电荷的已付域仍保留；本稿没有回滚它，更没有把−4冒充Hodge primitive。

## 6. 最强旧净值与计轮建议

最短依赖链是：573在指定扩大域识别闭理想Jbar并含ALL L1 raw源、支付原L1/fixed du-Dlog费 → 普通C*函数演算在同一闭理想中给B=CD精确分解 → 通用Hochschild二链展开给有限exact原始元 → 原source类在未约化与约化同调均零。第2–3节把直接应用所需前件和常数完整列出，不以未审定理名代证明。

573原稿没有直接写本次S_2原始元公式；本稿亦不凭有限旧库搜索宣称世界新颖性。不同cone的闭代表是实际新写下的对象，但其存活已被已付闭理想结构和上述一般恒等式直接决定，无新增独立算术/几何输入、非根计算或成长比较。因此建议按**强旧标准应用0**停止此固定pair/原norm/source规则，不以较弱e_eta闭包证再开unreduced续轮，不授C050/587。该建议来自明确公式和同域扣账，不来自正文自贴“标准”标签。

局部上已关闭“这个原source类是否精确存活”的问题；宏观上的同一非零primitive/principal/mixed、577完整signed消失、危险core/cross及Ξ未付，whole542+555→557 leading4/5仍仅负惯性UPPER。未支付完整Γ/contact、proper powers、双pole或Weil正性的新身份。此固定recipe停止不通过Goal的实质核心方法类边界门；另一个实际pair/有费强域未被泛排，也不能仅据未排获得新预算。
