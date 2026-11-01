# ROOT C070 working attempt：相对责任与phase-blind前件的界限

2026-11-01。工作稿，非ROOT结果验收。实际固定Pi_(e^j)、E_(j²)和原三源，不改path/gain/receiver，不引入新候选。两独立稿的joint capture upper已读；主三比值仍OPEN。下述仅是标准Hilbert代数／依赖负控制，不计新定理或数学轮。

## 1. 不需要先把actual remainder假定为零的精确费用

令Phi_j(r)=2^(-1/2)(D_j(r)E_N,D_j(check r)E_N)，其norm²=C_j(r)。由反射平均，even/odd源在这个direct-sum feature中正交。按原a=1/2分解

    u_a=(tau_a g+tau_-a g)/2=g+h_c，
    v_a=(tau_a g-tau_-a g)/2=-a g′+h_s。

这里h_c=u_a-g、h_s=v_a+a g′只是同一平移测试的exact remainder，不是另选sourcefamily。置A=C_j(g)、B=C_j(g′)、S=C_j(tau_a g)、R=C_j(h_c)+C_j(h_s)。在两个orthogonal槽的direct sum中，反三角不等式给

    R >= [sqrt(A+a²B)-sqrt(S)]²。                         (1)

这没有丢掉相干cross，也没有用k的pointwise近似。若共同c_j匹配(q0,q1,q0)，则必须

    liminf c_j R_j >= [sqrt(q0+a²q1)-sqrt(q0)]² >0。       (2)

故想由低频Taylor否定匹配，必须实际支付与anchor相对的remainder，而不是只证明R=o(j)。两个独立稿的capture upper和必要c_j j→∞不能把(2)右侧消掉。

另须注意G=ghat=1−m2 t²/2+O(t⁴)，m2=∫u²g(u)du>0。常数乘子commutator为零，因此D_j(g)自身以G−1的二阶变化为起点；h_c的symbol(cos(at)−1)G也是二阶，不能因它是Taylor remainder就声称比g的能量更小。可定义lambda=a²/m2，使

    R_even(t)=(cos(at)−1)G(t)−lambda(G(t)−1)=O(t⁴)，
    D_j(cos(at)G)=(1+lambda)D_j(G)+D_j(R_even)。

这是exact bounded-multiplier identity及局部Taylor事实，仍没有给finite-right Hermite相对范数。常数I只用于commutator代数，不把delta-source纳入原compact/Dlog域，也不从此推出Weil目标值。没有以这个refinement重选测试。

## 2. 为什么actual对角＋完整HS信息不能单独给锚源lower

以下是逻辑negative control，**不是**对实际Pi的变形提案或另一个数学任务。先固定finite X,N及原compact源r。令W_b=M_(exp(ibt))，只为检查一个推论的前件，记P^(b)=W_b Pi_X W_b*。W_b与所有M_rhat交换，所以

    [P^(b),M_rhat]=W_b[Pi_X,M_rhat]W_b*。

P^(b)的对角k(t,t)、|k(t,v)|²、原夹源正迹和完整HS commutator范数均与Pi_X相同。可是右接同一E_N的有限列能量是

    1/2 Σ_eps ||D_X(eps r) W_b* E_N||HS²。

对每fixed n，W_b*phi_n在L²中随|b|→∞弱趋0：它与任意L²向量的内积是一个L¹函数的Fourier变换。旧560域给D_X(eps r)∈HS，故它是compact，作用这些弱零列后强趋0。有限N和两个eps求和，于是上式趋0；同样可对原三个固定测试同时成立。

因此只用phase-blind对角/完整HS数据不能给finite-E anchor的正下界。这里**没有**说P^(b)仍是同一B_X P G_X^(-1)P B_X*、仍满足固定physical Sonin边界或代表actual Pi_X。恰好相反：actual完整P/B/G结构可能提供额外phase信息，当前尚未支付。该负控制不能判定实际C_j的比值，也不排除未来从确切Gram逆证明它。

## 3. 实际剩余任务

第一腿已给有限列、absolute-Fubini三重kernel、Hermite CD/ladder及translation cross；两腿分别用Mehler和oscillator/Sobolev给同一路径的uniform actual capture o(j)。这些保留了正确receiver/source角色。

要完成C070仍须在actual Pi_(e^j)与E_(j²)下证明非零anchor／相对高阶remainder或另一份校准无关比较。上述(1)/(2)、Taylor refinement及phase negative control都没有支付这一项。不能把条件式或逻辑模型计为实际反例，也不能因upper较容易闭合而把合同目标改成upper。独立anchor切口仍在实际尝试。
