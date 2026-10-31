# 限定逆审：native指数lift与ordinary连接像

2026-10-31；`/root/native_k_boundary_fresh`。同G20261027、原0c4f基线。本人只写本稿；未改STATE、Goal、cadence、库或其它原件，未联网／下载／运行新数值或创建合同。

**裁决：限定PASS，按标准强旧0停止这一公式。** Root5802、当前独立终稿14394及读出限定1095已实读。Native指数lift、ordinary K₁→relative K₀连接像精确为0、同一537覆盖失败均成立。独立稿§3“well-defined／逐源读出”单凭措辞不能排任意非保零函数；其过宽读法冻结，仅按另附限定重闭，不影响native证明。没有新独立经典正性或完整方法类边界。

## 1. 对象与前件没有换成任意entire数据

原physical源为r=e^(u/2)f∈S_exp,C，中心Mellin为F_r(s)=∫e^((s−1/2)u)r(u)du=M_f(s)，F_r(0)=μ₋r、F_r(1)=μ₊r。卷积仍是原u线卷积，F_(r*h)=F_rF_h；r的du、全线zero-extension Dlog没有改变。

519给实际闭源像I等于全部真实ζ零点的完整重数jets之核；再交两个degree核才是Pan。乘上其它源保完整jets与两个零值，所以其physical像P_c是闭卷积理想。不能把405 Gaussian源本身的两degree(1/4,1/4)也叫principal而删去。也没有用“只值radical”代替重数jets。

520§3明确未证明native商等于全部无约束jet乘积。Root早期消息的相反待验前提在消费前已撤销，当前两稿均把A_nat=Cδ₀⊕S_exp卷积单位化与额外A_ent=O(C)分开。δ₀仅是形式单位，不是du源、Dlog有限测试或可代入Weil型的函数。所有weighted估计只施于S_exp部分。

## 2. 实际native指数收敛与费用

记q_A(g)=∫e^(A|u|)|g(u)|du。三角不等式给weighted Young：q_A(g*h)≤q_A(g)q_A(h)。全部A≥0和k≥0的q_A(D^kg)与原S_exp上确界半范数等价：反向多取一个指数权；正向用e^(A|u|)g的W^(1,1)估计，例如sup e^(A|u|)|g|≤q_A(g′)+Aq_A(g)。原S_exp的更高指数衰减支付两端极限。

导数可放在一个卷积factor上，故对n≥1，

    q_A(D^k(r^(*n)))≤q_A(D^kr)q_A(r)^(n−1).

因此g_r=Σ_(n≥1)r^(*n)/n!在每个实际半范数收敛，并有root所列q_A(g_r)≤e^(q_A(r))−1及导数比值界。零源比值连续解释正确，没有漏付n阶导数或把高阶费用降成du。独立稿以weighted上确界给出的同一估计也成立。

于是U_r=δ₀+g_r在A_nat中实际存在；绝对收敛的Cauchy乘积与binomial消去给U_r*U_(−r)=δ₀。对每个fixed s，Mellin字符连续，合法换序给F_(g_r)=e^(F_r)−1。故这里是**native实际全局单位lift**，不是从O(C)插值反向假设有源。

先fixed supp r⊂[−L,L]时q_A(r)≤√(2L)e^(AL)||r||du≤√(2L/log2)e^(AL)||r||Dlog，方向正确。高阶仍需q_A(D^kr)／相应强半范数；g_r一般不再compact，不可继承原支撑。这些是指定代表的充分费，不是K零类的必要lower、全线统一du界、成长窗uniform或算术height。

## 3. Ordinary连接方向、Pan与同一537

取q:A_nat→B_nat=A_nat/P_c。当前源公式是r↦∂[q(U_r)]，方向为K₁(B_nat)→K₀(A_nat,P_c)。q(U_r)本来就是上游单位U_r的像，因此ordinary relative exactness给

    ∂[q(U_r)]=0，∀r∈S_exp,C。

也可用两个free A模及商同构q(U_r)的relative triple，经实际A模自同构U_r改为identity triple。此论证不需nonunital naive HH excision，也不是从连续指数路径推algebraic K₁类本身为0；消失的只有当前connecting image。

P∈P_c使q(P)=0，商中指数故满足q(U_(r+P))=q(U_r)，完整noncompact Pan及平移均消去。但同一规则也给537真实r₀=(D²−1/4)ψ的连接类0，尽管该fixed17/16、双矩零源已有完整Qζ(r₀)>0。这里杀掉的是进入连接类后的coverage，不是520谱商或全部relative K₀为空。

## 4. 读出语义有限重闭

独立原稿14394保持不改，其§3把“well-defined”与“逐源选择”并用的无条件读法不消费。Root另文1095正确限定：biadditive mixed配对，或每stage仍保零的配对，在零类上为0；同一个只经类的全源函数若还原Q，则F(0)=Q(0)=0，同时又需F(0)=Q(r₀)>0，矛盾。此处无需连续性或有界gain。

任意未归一化的source-adapted F_r却可人为指定F_r(0)=Q(r)；类为0本身没有排除这种携带额外源数据的规则。它没有独立产生正号。有限重闭只支持保零mixed／共同class-only规则，保留raw frame、secondary、metric、extra-data等其它消费责任，不以字面well-defined代替归一化。

## 5. 额外ambient与最强旧范围

独立稿另取H=s(s−1)ξ/2、A_ent=O(C)、B_ent=A_ent/(H)，保全部非平凡重数及0、1各一阶。它采用标准离散Hermite整插值为外部背景：任意finite-N可逆jet矩阵逐node有局部holomorphic matrix log，entrywise插值log后取exp给全局可逆矩阵lift。因此在这个**unrestricted ambient**内普通连接像也为0，逐stage有限rank可增长。

这段标准代数方向成立；它没有给插值增长／源范数，也不能证明native B_nat任意单位可lift。无限product的Spec不被叫作只含离散node的曲线。本次首检根本不用此附属命题，故不能把其更强ambient结论拼回原源拓扑、hermitian／metric或全部relative K₀。

519／520实际源商＋标准卷积指数／relative exactness已经决定本规则；574／575又已有global／side unit导致coboundary并杀537的准确旧角色。那些旧覆盖与本次代数不是同一个对象，不搬其全部Pic分类或链norm；当前零像由显式lift独立核出。这是标准强旧0，不是新算术估计或新核心方法类反例。

完整Γ/contact、全部p^k、双pole和allcomplex源未删；principal／sections／mixed、危险corecross、成长Ξ及whole leading4/5负惯性UPPER没有新后果。保留native非指数／不可lift数据、不同允许gauge、非free／higher／derived／hermitian、metric／secondary与实际signed修复，但这些未构造的条件不自动授后继预算。

## 6. 实读与版本

已恢复README／STATE、check→show、Goal、C065、AU、macro21及前沿入口；旧证据只核519§§1–3、520§§1–3特别非product限定、574§§4–6、575§§5–6与旧537全源正性statement。没有重审旧nested数值或作者全证明。当前独立终稿在其agent确认路径／bytes／hash后才读；初稿存在不代完成。Parent runtime观察是运行状态依据，本child未创建／改变Goal。

原cadence6813bytes/SHA0bd41adf…保持0/history66/latest602/formal21；manifest221943bytes/SHA8d0e293f…仍142项。没有新paper、下载、作者章节、数学轮或宏观重置；Goal三门仍open，PASS待root消费，不是完成Goal。

绑定当前raw版本：root5802／SHA `9619514c7283858af4e05cbdb4f0e5f8eb155f1955acc7e3cedbfa4d71c52719`；独立14394／SHA `38ce273ad35691632d91857c561ec081aa3dea3e59d81fb5c2f3d0c733893243`；读出限定1095／SHA `46bfcce0253bff68e083957ac6d1ab24a6ce661b56eb8a44fe1461984e639041`。Hash只认版本，不认证数学或root结算。
