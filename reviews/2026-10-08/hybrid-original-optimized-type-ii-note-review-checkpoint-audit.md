# 481优化原Type II归约：独立全文数学审查

2026-10-08。审查者：checkpoint_audit。被审笔记作者：root。
仅新增本审查；不修改481、尾项研究源、旧冻结输入、检查器、输出或Git。

**结论：限定PASS。** 481的同一原scalar参数化归约、完整误差
第四矩13/21、conditional complete moment transfer29/42，以及所列
费用族内最小化结论均成立。初稿一般参数遗漏的y>1/2前件已补齐；
本审绑定包含该修正及最终输入清单的版本，没有剩余数学阻断。

## 1. 最终版本与全文阅读范围

canonical UTF-8 LF只统一CRLF/lone CR，不trim或改变EOF。

| 完整输入 | canonical LF SHA256 |
|---|---|
| [481最终笔记](../../notes/481-original-type-ii-squarefull-tail-and-optimized-moment-transfer.md) | 4ce3ea2ac087d734142c8788607c1c54fc6887bcf535c806c88097447afdc63e |
| [477完整Vaughan系数与lower-block证明](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 |
| [479 Weyl、短Λ及maximal prefix证明](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 |
| [原scalar及proper-power准入](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [476 conditional whole5/7](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |
| [480原complete moment transfer](../../notes/480-original-type-ii-single-prime-part-and-whole-moment-transfer.md) | 13a6cbd697ad960cdb97543090861373f21b6970710bc2d247edac59bb08e791 |
| [新平方满尾及Euler留数完整源](hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md) | 66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab |
| [尾项源不同作者root审查](hybrid-original-squarefull-tail-and-euler-review-root.md) | d083729b771a56c9153b134f00ca21764cd22b7fd2acce502c4adcd0a2734279 |
| [最终精确检查器](../../scripts/hybrid_optimized_type_ii_checkpoint.py) | ef8e89e94686036d302d3c817fbbecec80a5ab9f31529dfa814f1aea9273abfc |
| [最终保存有限输出](../../output/hybrid-optimized-type-ii-checkpoint.json) | 8e8ff66d8e8b58cec3fb29cd32dffd3a54a82c01870d46a1ff9b74afe832d500 |

481最终全文239行已读；原477全文324行、479证明524行、
proper-power准入370行、476全文96行、480全文185行及尾项源401行
均实际全文读取，冻结hash逐项核对。没有以已有审查的PASS代替阅读。

审查者是所引用401行尾项源的作者；本审是对不同作者root的481新增
参数重设、完整Vaughan账本、费用优化及whole transfer的独立重推。
本审不能另充尾项源自己的不同作者认证；该源另由root完成独立审查，
本轮全文读取其70行并绑定上述hash。
本审不认证历史上[R7/8]的证明，只保留476引用的原输入合同。

## 2. 参数对象、finite identity及所有边界

同一X=T/(2π)、L=logX、aL≥c_phi>0、J_T=[T/4,4T]和
原sqrtX<p≤X genuine-prime scalar完全保留。
U,V,M,Y仅重设Vaughan有限分区；新的bV和C4仍按新截断重新定义。

原477§4的恒等式可从有限F_U、G_V的generating identity直接逐系数重推，
对每个精确整数U,V及n>U成立，不依原1/8幂。
1−ζG_V的k≤V系数全零、k>V系数为−bV(k)，最后负号和k>V域正确。
故只要Y>U，Y<n≤X的完整Λ高段精确为I2+I3+C4。

一般前件已写为0<v<a、max(1/2,a+v)<y<1。
y>1/2确保低段sqrtX<n≤Y与高段Y<n≤X准确拼成原Λ高多项式；
y>a+v确保展开short-m时Y/M>V，原k>V由乘积下端强制。
因为a>v且a+v<1，另有v<1/2、U<sqrtX<Y；高段n>U前件也满足。
没有从只适用于固定旧cut的结论直接搬运新对象。

主取v=2/21、a=4/21、y=17/21严格满足全部前件。
V=floorX^(2/21)、M=floorX^(4/21)与H=V²都是实际整数；
V²≤X^(4/21)且V²为整数，故H≤M精确成立。
大X时V≥X^(2/21)/2、M≥X^(4/21)/2、H≥X^(4/21)/4；
这些floor只带固定常数，不增加额外endpoint polynomial。

按short-m、large proper powers、large genuine primes/r>H、
large genuine primes/r≤H的顺序分区，Λ支持只在prime powers上，
故四项是完整不交finite partition。所有项保留Y<mk≤X。
s(k)由valuation恰为1的素因子组成，r(k)平方满，与s互素且唯一。
在Ropt内，s=1时1<k=r≤V²，rad(k)≤V，bV(k)=0准确；
所以实际非零项自动s≥2且s rad(r)>V。
m>M≥H≥r与m为prime还推出(m,r)=1；没有添加(m,s)=1。

新M、V、Y均与480不同。本审没有把Ropt视为旧Rsharp的子集；
也没有使用signed多项式对子集的norm单调性。

## 3. 新参数下的完整子项费用

对实际sharp有限多项式平方，再用原时间二矩于长度Y²，
低段给X^eps(1+Y²/X)。系数平方能量由subpower divisor bound支付；
不是将正半素数计数当作signed whole upper。
主y=17/21时显示成本2y−1=13/21。

原479证明§§2–3的对数相位Weyl界对每个实际sharp子区间
及所有1≤长度≤CX统一；部分求和保留两endpoint与j=0,1权。
Type I外系数原g与μ的加权L1≤X^eps sqrt(UV)，
故sup≤X^(1/6+v+eps)，真实长度≤X的二矩≤X^eps，
sup²乘二矩的第四费用为1/3+2v=11/21。

short-m展开原μ divisor后inner区间正是(Y/(md),X/(md)]。
共同下端使k>V自动满足，但不更改该集合。
sup≤X^(1/6)sqrt(MV)log^C，真实n系数由τ3(n)/sqrt n控制，
时间二矩仍为X^eps，因而完整费用1/3+a+v=13/21。
这保留所有U<m≤M的Λprime powers与允许k。

large proper-power m的dyad加权L1≤log²X，对每个固定m以
实际bV数组maximal prefix保留两个移动k端点；
非空块K<X/M，所以第四费用X^eps(1+X/M²)，显示1−2a=13/21。
这个合同的proof对新的M及V统一，不需要旧M=X^(1/4)。

原proper-power migration是同一个原sqrtX<n≤X scalar，
norm差O_phi(X^(-1/12))，与Vaughan截断无关。
FULL READ其平方项base pq时间均值和k≥3直接尾界，合同足够；
没有在未知fourth增长下把这个norm差当成additive o(1)。

## 4. 完整平方满尾与varying c_r

固定r之后n=ms重排保持c_r(n)的全部原prime/squarefree/
(s,r)=1、sr>V与m>M条件，原共同cut正是Y/r<n≤X/r。
没有要求m与s互素，也没有将μ divisor替成任意μ(n)。

对实际n,r≤X，|c_r(n)|≤τ(r)τ3(n)，divisor常数对r,V,M统一。
用于dyadic填零的n≤2X只多一个固定Λ/L常数。
因此原maximal prefix proof可逐个固定r对这个真实数组使用：
其常数只依赖统一subpower bound，允许数组随r变化。
这不是从一个较大signed函数norm推任意子集norm。

squarefull r∈(K,2K]的带权L1=O(1)，由唯一a²b³表示直接计数。
对每个实际r的移动n endpoints作两个prefix之差；
随后对外r与全部K=2^jH使用L4 Minkowski。
非空n-dyad有NK<X，K≥H，故N²/X≤X/H²。
最终尾项第四矩X^eps(1+X/H²)支付所有aspect ratios和边界。
任意固定最终eps先分配更小coefficient/maximal损失，再吸收
O(log²X)个dyads；没有把日志损失当成真正负幂。

H=V²时所有非零squarefull k有r=k>V²，已完整纳入尾项。
显示cost1−4v=13/21；无需第二次单列支付它们。
本审重推的是这个实际尾项upper，其余large-s mixed4仍未付款。

## 5. 合成误差与所列费用族内的最优性

精确PH=Ropt+Eopt中，Eopt先合成low、Type I、short-m、
large proper powers、squarefull tail及proper-power migration。
有限次L4 Minkowski后重新分配固定eps，得到
M_Eopt≪X^(13/21+eps)，norm指数13/84。
两向四矩耦合仅对Ropt与这个完整误差用一次(u+v)^4≤8(u^4+v^4)，
所以8没有因重复triangle被暗中相乘。

独立用有理数重算的五个显示成本为
(13/21,11/21,13/21,13/21,13/21)，另取与0的最大值。
该精确算术复核只是核指数，不能替代上述无限均值证明。

在所列费用、H≤V²的族内，尾项成本至少1−4v。
设这个费用账本的最大指数为c，则
a≥(1−c)/2、v≥(1−c)/4，且c≥1/3+a+v。
故c≥1/3+3(1−c)/4，即c≥13/21。
主取参实现下界，且一般前件可行，所以限定的最小化结论成立。
这个证明不宣称y取值唯一，也不优化未知signed Type II全体、
其他指数对、H>V²的不同剩余或零自由边界。

## 6. conditional complete第四矩传递及留数范围

本节才使用476原[R7/8]合同，取得完整PH fourth≤X^(5/7+eps)。
先由Ropt=PH−Eopt与norm三角推出Ropt的同幂完整upper，
之后对两个完整函数用
|M_F−M_G|≪||F−G||4(||F||4+||G||4)^3。
所以重新分配任意固定eps后得到显示指数
(3*(5/7)+13/21)/4=29/42。

精确差5/7−29/42=1/42；
480指数479/672−29/42=5/224。
最终eps<1/42时，除以X^(5/7)的差趋0；
不需要PH的同阶lower，也没有据此认领相对实际主项的equivalence。
该误差仍增长，不是O(1)四矩预算，也不能用于新比例/κ反馈。

small-r生成函数的ζ/ζ(2z) C−1由完整finite μ展开给出。
在Reρ>1/2，finite C的(1+p^(-z))分母非零，
ζ(2ρ)非零，prime proper-power系列局部一致解析；
因此未作共同上截断的真实signed generating function留数为−mρ。
低端有限系数删除只加减entire多项式，留数不变。
实际finite-height scalar本身是entire有限和；这里的留数指其
Perron所用generating function，不能把两者混同。
边界与full Perron tail尚须按其合同支付，局部留数不代付该步骤。
主新剩余仍包含r=1的balanced prime×prime实际sector；
其存在不是signed whole norm lower，也不是方法不可能性证明。

## 7. 精确检查器、保存输出与独立readonly重放

随后按父线程明确追加任务全文读最终检查器235行、保存JSON104行。
检查器仅使用标准库；逐行核其canonical LF、Fraction、精确整数root
和symbolic prime-log字典实现，再执行其已经读取的readonly分支。

FROZEN中的五个proof输入有明确固定hash，全部吻合。
NOTE和checker本身的实际canonical hash加入保存JSON的files，
因此--check将它们与本轮绑定的输出一并核对，不会默默忽略改动。
JSON的七个files、成本、参数和check_digest与实际build一致；
另列的root尾项审查与480由本数学review绑定，不伪称它们是checker
FROZEN里的两个额外文件。最终输出明确三个proves_*标志都为false。

finite X=4096、6561以整数幂比较计算floor_U,V,M,Y，
high n=floorY+1,...,X准确对应原real lower endpoint。
lam(n)以{p:1}代表Λ(p^j)=logp，log(n/d)以factor(n/d)的exponent字典表示；
g、I2、I3、C4不使用浮点log近似。全部8587个high系数各检查
Vaughan恒等式、四分区及merged-squarefull-tail，共25761项。
其他17项是五源hash、七项有理/域检查、两个floor域和三个finite Euler，
合计25778项。

merged-tail的prime检验factor(m)=={m:1}准确排除proper powers，
不会在m为composite时索引不存在的factor key。
rr为平方满、s squarefree、(s,rr)=1的条件确保唯一原k分解；
m可与rr共享素因子，尾项没有误加(m,rr)=1。
finite Euler三组V=2,3,5、H=V²使用各自有限prime乘积，
完整保留q|rad(t)的μ(q)而没有q^(-z)，以及a的a^(-z)权和局部分母。
这些确切核对finite identity中的减1，不认证无限Euler续拓或真实ζ零点。

本审实际独立运行命令：

    C:\Python312\python.exe -B -X utf8 scripts/hybrid_optimized_type_ii_checkpoint.py --check

退出码0；stdout精确为：

    PASS: 25778 exact checks; infinite conclusions require math reviews.

此分支只调用build读取输入及OUT.read_text比较；仅--write才写OUT。
本审未执行--write，-B避免pycache，未生成新输出或运行旧覆盖。
运行前后note、script、OUT的canonical hashes均保持表中值。

## 8. 最终范围

限定PASS认证的是481新增数学归约及其明确的条件传递。
尾项源的root独审、本文新增数学独审与§7有限重放各有明确范围；
本审不把三个范围合并成无限全链证书，不运行生成输出。
没有重跑旧覆盖或修改任何绑定文件、Git。

有限Fraction核对只支持所列有理成本与差值，
不认证无限解析输入、实际完整near mixed4、RH或新的zero-free strip。
最终whole5/7、既有simple proportion与sigma*没有从本审改动。
