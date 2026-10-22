# 源依赖族的局部—全局预算：可实际计算的两类族与容量责任

2026-10-22。独占稿，未修改公共STATE、cadence、合同、Goal或Git。
恢复了README/STATE/check/show、G20261014、C035、最新D20261022A与macro frontier，
实际读了上轮全局截面报告、567全稿、568 §§2–3/5、569预算cocycle相关段落、
405 §§1–5、537原源定理及519/520/553所需旧像/范数原件。
只补查Stacks 30.8（见§4）；没有串新文献来源。

**结论：源依赖metric、主pair和相对评价确实能避开“固定离散群裸加性map只能为零”的窄障碍。
下面给出无需Weil核卷积的实际族、原范数费、真实flat restriction/kernel与局部跳跃计算。
但pole矩驱动的具体族会丢掉537非根；更一般平滑坐标只解决参数化，尚不解决405全部关系。
两类族都没有产生同源平方二次容量或完整Weil身份。**

## 1. 原对象与最强旧对照

物理源固定为r(u)=e^{u/2}f(u)，先在D(I)=Cc∞((-L,L);C)上讨论原du范数和zero-extension
Dlog图范数

    ||r||_D²=(2π)^−1∫ log(2+|ξ|)|rhat(ξ)|²dξ ≥ log2 ||r||²_du。

405主关系p∈P_an及h不在compact源内，相关消去检验在physical S_exp扩张域进行。
全Q的radical包含physical I，405的B只在I内以P_an为radical；两者不能合并。
537固定窗给r0=(∂²−1/4)ψ、ψ非零compact且支撑在原正性窗时Q_W(r0)>0。
不把该正性搬到无界成长窗。

上轮regular L=hZ、非零metric的独立预算为Nλ≤1；tensor log#容量为max(nd,0)+O(1)。
567更强的平方责任是实际signed对应D及同一对象上的RR二次项、乘法和容量，
不是把这个线性预算再展开一次。强旧whole仍542+555→557的4/5 issued上预算，
本稿不改actual core、coupling、Ξ或全源Weil正性。

## 2. 实际源到metric族：pole矩坐标的成功与失败

定义不经过J_W的实际连续坐标

    t_±(r)=M_±(r)=∫ e^{±u/2}r(u)du。

对原I有精确Cauchy–Schwarz费用

    |t_±(r)| ≤ sqrt(2sinh L)||r||_du
             ≤ sqrt(2sinh L/log2)||r||_D。                 (1)

因此这些坐标在每个fixed窗合法；常数随L增长，不能写成成长统一O(1)。
在S_exp上它们亦是连续矩，不借用compact窗费覆盖非compact h/p。

取一个实际regular adelic群L_r=Z、所有有限frame为恒等，arch frame

    τ_r(n)=exp(−Re t_+(r))n，s_r=1∈L_r。                 (2)

这是r到一个“metrized line + distinguished global section”的明确非线性map；
不声称s_r对所有r均在单位小球（当Re t_+≥0时才在）。
tensor识别Z⊗Z≅Z使τ_(r+s)=τ_r⊗τ_s，s_(r+s)=s_r⊗s_s。
有限p消失核仍p^kZ，截面s_r的原有限消失阶为0。
在同一对象上，非零单位小截面满足N位消失的预算精确为

    logN ≤ Re t_+(r)。                                  (3)

原norm按(1)支付arch高度；局部条件在本族不随源变，所以(3)只运输上轮格前端。
degree对源是实线性的，其mixed二阶差为0，不能恢复非零Weil二次型。

405检验是可判的：physical r_p=e^(u/2)p有t_+(r_p)=d(p)=0、t_−(r_p)=c(p)=0。
所以(2)及任何只依(t_+,t_−)的族，对P_an平移不变。
但对537的非根，由两次合法分部积分

    M_±((∂²−1/4)ψ)=((±1/2)²−1/4)M_±(ψ)=0。             (4)

因此r0与0给完全相同的族/截面，非根可见性失败。
这不是一般family no-go，而是**所有仅以两pole矩为参数的族**的精确失败。
405的h给t_±(r_h)=1/4，提示本族仍看得到双degree；这适合degree扩张角色，
不能据此声称它已下降到全Q radical商。

也可取任意fixed smooth φ，令t(r)=∫r barφ；则
|t(r)|≤||φ||₂||r||_du≤||φ||₂/sqrt(log2)||r||_D。
这使同一构造有实际非pole源依赖，也可用φ=r0保证该单一非根可见。
可是一般φ没有消去405全部P_an，不能把“能选一个坐标”登记为关系测试通过。
553更强地已付：physical P_an的平移span在全线L²/Hlog稠密。
所以这个固定φ坐标若消去全部指定关系，便必为零，与r0可见矛盾。
这里只消费旧密度，不重新声称新bounded-readout障碍。
只把坐标换成568 smooth J_W-probe可复用旧关系闭合，仍是旧signed来源的复合。

## 3. metric曲率和主pair的自由度不能代独立容量

改取λ_r=exp(−κ|t(r)|²)，κ>0，仍得正metric和全局截面1。
degree是κ|t|²，原高度有κ C_φ²||r||_du²的真实上界。
tensor的额外因子为exp(−2κ Re(t(r)overline{t(s)}))，可明确记录为transition cocycle。
所产生的mixed二次型仅κ t(r)overline{t(s)}，秩至多1。
把多个坐标并列可提高rank；但选择其正metric并没有证明等于经典完整Q。
若直接将degree设成Q_W(r)，度量exp(−Q_W(r))在Q不定时也处处正，
因此纤维正metric本身无判别力；再要求其曲率半正正是相应Weil型的PSD条件。
这与569已付matched cocycle相容，没有独立减少正性责任。

另一项完全可算的主pair控制：任取q(r)∈Q_+^×，令

    L_r=q(r)Z，τ_r(x)=x/q(r)，s_r=q(r)，
    a_p(r)=q(r)^−1∈Q_p^×。                              (5)

有限frame a_p把s_r送到1，arch高度也为1；原λ≡1，全局小截面数恒3，
local budget与原对象Z完全相同。q可以取p^floor(Re t(r))，发生真实的代表跳跃，
但主变换后的同一对象预算不跳。
若错误只读v_p(s_r)=floor(Re t(r))而忽略变动的L_r/frame，会得到虚假的local消失增益。
此例说明“源依赖除子”可以只是主规范自由度：必须同时运输frame和arch norm。
本族恒主等价，当然也丢掉537非根。

若每个有限系数n_p(r)为源连通域到离散Z的连续函数，它确实常数。
这只约束**逐系数连续且同一离散标记**的族；不能扩大成代数相对除子、
moving support、参数相关截面、非平凡Picard族或允许跳跃的所有构造均不存在。
局部系数固定也不迫使截面在该位的消失阶固定。

## 4. 真相对P¹族：局部消失可跳，真实flat kernel消除部分假费

这是第二个实际构造，不需要ζ零点或J_W。设S=Spec Z[t]，X=P¹_S，
在仿射坐标x上取D=m∞，m≥1。全局截面为

    H0(X,O(m))=Z[t]{1,x,…,x^m}，rank=m+1。              (6)

来源只补查了[Stacks 30.8, Lemma30.8.1](https://stacks.math.columbia.edu/tag/01XS)，
实际读了单项式描述和Cech证明（HTML26–98行）；(6)亦可直接由两个仿射图的无极点条件核验。
给任意前述有原norm费的源坐标t(r)，其complex specialization给实际相对fiber及截面。
若t=M_+，仍按§2通过P_an而失败r0；若用一般φ，关系测试未付。

令E_t由x(x−t)=0定义。它是有限flat长度2的relative Cartier divisor，即使t=0也保留双点jet。
同一global对象有实际restriction

    H0(O(m)) → A=Z[t,x]/(x(x−t))，
    kernel=H0(O(m−2))，                                (7)

kernel同构通过乘以x(x−t)给出；m=1时右边为0。
在A的固定基{1,x}中，r_m(x)=x^m的余式为t^(m−1)x，故选取两列{1,x^m}的minor为

    det E_m(t)=t^(m−1)。                               (8)

直接把两个点0,t当成始终disjoint，裸点评价矩阵的det=t^m；多出来的t是collision/frame因子。
正确flat length2对象恢复一阶jet，消去这一个假费。
尤其m=1时(8)恒1，完整限制始终满射；m>1的(8)在t=0退化只是这个选列失败。
完整H0(O(m))一直包含好列{1,x}，其minor为1。因此这不是所有评价载体必须付出的det损失。

complex源族中t(r)→0而||r||_du,||r||_D→0时，坏minor的
−log|det E_m|=(m−1)log(1/|t|)无界（m>1）。
所以若候选固定使用这个minor及对数范数，就不能声称该项由原norm平方统一支付。
选择好列、divided differences、不同frame或带零因子的determinant-line延拓均是合法修复；
需要说明具体修复后计量的是哪一个det，不可把此无界值冒充实际源的必要费用。

局部消失与global degree确已在同一对象上比较：x^m在0有order m，
而它作为O(m)截面的零除子总degree m；global H0容量rank m+1正好承担该增长。
这是真实“可变截面消失＋固定/变化degree费用”，不是n_p locally constant所能排除的。
但它只是曲线线性容量。m是构造的外加整数，不受||r||_D决定；
给任意m的sup|x^m|≤1（|x|≤1）没有消除degree m，更不生成signed对应的平方RR。

若只在complex fiber令t=ℓ(r)，t一般不是有理数或代数整数，
不能无来源地定义每个有限p的v_p(t)。Spec Z[t]保有整系数relative对象，
不表示每个任意complex源fiber都带同一套有限位评价。
以后若用parameter-divisor消失代替finite-prime powers，必须给独立的全位specialization/trace身份。

## 5. 连续正反例与函数域的规则检验

在已付连续族d=±1/16中，取旧ODE所给实际坐标

    A_d(r)=∫r C_d，B_d(r)=∫r S_d，
    Q_d(r)=2|A_d(r)|²+2d|B_d(r)|²。                    (9)

只消费568既有身份，不重新求根或重算H。任一fixed I上这两个坐标都有普通L²核范数费，
±两段共享相同的粗指数上界。以t=B_d(r)拉回(2)/(6)的族，在正负两段都完全合法；
同一flat E_t、kernel和degree容量不依d的符号。
因此这些真实family设施的存在不独立鉴别(9)的正号。
若选正插值metric就得到2|A|²+2|d||B|²，负段已改变目标；
若保持signed 2d并要求所有源预算非负，仍是Weil正性的等价重述。
阈值d=0时B方向属最小Weil根，B驱动族甚至不下降该最小商；不能据局部jet维数强制它可见。

真函数域不要求每个复源本身必须是一个整数Cartier divisor。
567的独立几何先对C×C上的整数signed对应给RR/Hodge，随后线性扩张交数，
对源r通过

    E_r(y)=Σ_j r(y+jlogq) E_(j+j0)，0≤y<logq，          (10)

得到其全complex源Gram。每个源支撑只用有限多个实际对应。
这里(10)的系数可复，所得元素在实际对应的复线性span；Hodge正性已经在几何整数格上独立支付，
所以无需先为每个任意复组合构造一个literal小截面。
“有限divisor系数在连通族常数”不能反驳这一真正正例。

真正区分函数域真例与290/568反模型的是同一个square上的有效性、可乘截面、
RR二次项与交数身份，567给了signed D²>0时注入固定H0(2K)的明确矛盾。
P¹上(6)–(8)的线性容量在正反连续段都存在，也无法自行充当这个平方比较。
若转向Poincaré bundle/relative determinant of cohomology，必须实际给相对对象、pushforward、
极化与源坐标的比较；仅命名“Jacobian/Poincaré”不支付它们。

## 6. 完整Γ、素数幂和pole没有被这些族恢复

目标仍是568(14)的完整Q，保pole双矩、指定Γ0 contact、
w(v)=2e^(−v/2)/(1−e^(−2v))及每个p^k的logp/p^(k/2)权。
§2真实读取了pole矩，但既未生成其双曲mixed配对，也没有Γ或prime-power身份。
§4给真正的relative局部order/degree预算，却没有从参数t的zero或degree m
导出全部logp/p^(k/2)加权轨道迹、arch finite-part/contact或双pole度数配对。
这些缺口是同一对象上的trace/预算比较责任，不是可以删项处理的误差。

若以519/520既有Mellin像构造C上的解析除子，例如由完成函数乘pole多项式得到的H，
然后把源的entire变换限制到O_C/(H)，那是保multiplicity的真实解析section/quotient包装；
它可能比pole-only族更正确地保关系与非根，但继承原Mellin/jet输入而不是新算术容量。
C上length(O/(H,z−z0))或高阶jet消失是complex analytic length；
不能直接当成v_p(nonzero integer determinant)或其logp预算。
以后如需把该解析相对族与有限prime位、无穷位高度放在同一det上，
须另给integral model/specialization及全部coupling；“同样是divisor length”不是这条箭头。

569已付的cocycle能在选定预算后协调代表变换；它没有从这些族独立推出Weil正号。
保留正metric、局部jet和detline的全部上述合法修复，也仍须给：

1. 非旧J复合、对全部405关系与537非根角色正确的实际源map；
2. 原du/Dlog费用，含成长量词、parameter degeneration、有限位specialization与frame变换；
3. 同一个global对象的signed局部消失/乘法及独立平方容量；
4. 同一scale预算差到完整Γ/pp/pole Q_W的all-complex身份及全部误差。

本稿新增的可消费信息是两类实际族的精确能力/失败位置，特别是pole-only丢非根、
主pair假增益，以及flat collision与坏minor损失的区别。
它们是初等构造和准入测试，不是新的经典独立容量或全源正性定理；
单靠本稿不能开一个未知RR合同、宣称瓶颈消除或消费新whole后果。
