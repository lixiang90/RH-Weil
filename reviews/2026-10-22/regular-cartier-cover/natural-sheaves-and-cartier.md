# 574实际覆盖的连续regular方程、Cartier实现与消失过滤

2026-10-22。独占分支；只写本文件，不改STATE、合同或cadence。先恢复G20261014、STATE、C037/574结算与宏观前沿。
本稿是明确层选择后的直接计算；标准Cartier语言并非新外部定理，新增原件也须经root与独立审查才能消费。

结论有正反两面：**在真实覆盖上，连续结构层已经有非零因子和非平凡的Cartier型线；不能把它概括为“没有Cartier”。然而相应的边界消失理想、整数长度与截面容量均不同于代数曲线，且这一步不修复574的物理源准入。**

## 1. 固定对象与真正的强旧对照

完全固定574、413的对象，不以另一个解析空间替换它：

\[
T=\mathbf Z\cup\{\infty\},\quad
Y=T^2\times\mathbf R_t,\qquad
(a,b)(j,k,t)=(j+a,k+b,t+a\log2+b\log3).
\]

删双∞得O，\(W_p=\{k<\infty\}\)、\(W_q=\{j<\infty\}\)，交B的共同坐标为
\(x=t-j\log2-k\log3\)。P、Q为两个单∞闭边界；B在O中稠密。只在真正不变片上讨论等变下降，整个作用仍非proper。
两side商\(Z_{\log2},Z_{\log3}\)是574的负端螺旋加圆，绝不把全轨道空间自动当成Hausdorff曲线。

强旧输入不能漏掉：

- [384](../../../notes/384-f1-finite-level-cartier-regularity.md)、[387](../../../notes/387-f1-analytic-continuation-and-cartier-regularity.md)已经在**指定perfectoid环域**上证明有限层乃至全部非零全局函数的局部非零因子性；不是只有形式Cartier名词。
- [396](../../../notes/396-f1-flat-line-enhancement-and-cartier-pullback.md)有实际解析拉回、主分式及线丛增强；丛值测度和指定比较映射不能被忘掉。
- [401](../../../notes/401-f1-dual-cartier-ideal-and-reflexive-collapse.md)有真正下降的非闭理想层，但逐茎rank1不等于局部可逆；其非有限生成、双对偶回O是已付的限定边界。
- CC的[scaling site](https://arxiv.org/abs/1603.03191)另有integral-slope半环结构、单周期Cartier及连续维数RR。这是实际额外结构，不能一概否认；但其半环／topos、单周期RR并未自动等同574的复连续结构层或算术平方mixed容量。旧[来源审计](../../2026-10-20/grh-literature-roadmap/connes-f1-facility-audit.md)已定位§5.4、Thm5.17。

上述空间与O之间目前没有本稿证明的ringed比较态射，更没有把物理405全关系及原范数运输过去的映射。因此它们是保留的真实设施，不能拿来直接替换下文的层。

## 2. 最少附加选择：连续复结构层确有regular方程

先取O上的复连续函数层\(\mathcal C\)，带原Γ拉回作用。所有局部论证在Hausdorff atlas O上进行，等变函数／模由实际群胚下降；不将其冒称scheme。
“regular方程”只指乘该局部函数在结构层上单射。
“Cartier型有效数据”明确指局部由这种方程生成、交上比为结构层unit的可逆理想层；并不引用scheme的维数、Noetherian或有限长度结论。
[Stacks对ringed spaces的regular sequence定义](https://stacks.math.columbia.edu/tag/067M)允许这一纯层论检验；[effective Cartier的scheme定义](https://stacks.math.columbia.edu/tag/01WQ)只作命名参照。

在B置

\[
\rho=e^x=e^t2^{-j}3^{-k},
\quad \rho|_{P\sqcup Q}=0.                                      \tag{1}
\]

此函数真实连续且Γ不变：固定边界点时另一有限坐标和t可取有界局部范围，趋∞的估值使(1)趋0；Γ不变性由x公式逐项抵消。
它在B上严格正，而B在每个O开集中稠密。若\(\rho a=0\)，连续a在稠密B上为0，故在全开集为0。这个证明亦逐茎成立。因此\(I=(\rho)\subset\mathcal C\)真实可逆，乘ρ给\(\mathcal C\simeq I\)。
它的关联线是自由线，作为理想嵌入却不是单位理想；不能把“自由可逆模”与“零除子数据为空”混同。

完全同理，对每个实\(\alpha>0\)，\(\rho^\alpha\)延0给非零因子，记\(I_\alpha=(\rho^\alpha)\)。

\[
I_\alpha I_\beta=I_{\alpha+\beta},\qquad
I_\alpha=I_\beta\text{ 在边界邻域作为理想}
\Longleftrightarrow\alpha=\beta.                                \tag{2}
\]

最后一步因两生成元之比\(\rho^{\alpha-\beta}\)不可能在边界延为非零unit。故连续层中的正则除子参数并不自动量子化为整数。
原估值j、k确为整数；但取紧单位商、再与实t耦合得到的ρ已是正实坐标。保有j、k的原整数性不等于给ρ的连续茎添上DVR。

## 3. 新直接计算：574全部指数子族有连续Cartier型实现

给任意\(z\in\mathbf C\)，选实\(A>\max(0,-\Re z)\)。在两side分别置

\[
h_p(x)=e^{(A+z)x},\qquad h_q(x)=e^{Ax},                          \tag{3}
\]

各自在其单∞边界延0。正实部保证延拓连续，且二者在bulk无零，因此仍由稠密性证明局部非零因子。
交上精确有

\[
h_p/h_q=e^{zx}=g_z.                                             \tag{4}
\]

于是\((h_p)\)、\((h_q)\)通过真实交上的unit生成同一个等变可逆理想层\(\mathcal I_{z,A}\subset\mathcal C\)。
约定局部生成frame满足\(e_p=g_ze_q\)，理想可逆模\(\mathcal I_{z,A}\)就是574的\(\mathscr L_z\)。若按代数几何通常符号记有效数据为D，则\(\mathcal O(-D)=\mathcal I_{z,A}=\mathscr L_z\)、\(\mathcal O(D)=\mathscr L_z^\vee\)；其canonical正则截面在后者。因为z跑遍C，这仍覆盖整个指定子族，但后续源比较不得混用此正负号。
特别\(z=i\pi/\log2\)给非平凡absolute线的真实Cartier型代表，而非给一个自由模另加名称。
各side在边界的frame是\(h_p,h_q\)作为**理想模生成元**的frame；不能把它在\(\mathcal C\)中的点值0当成模纤维frame为0。

对参数z局部取同一个A、并使两实部有统一正下界，(3)在O乘参数空间上联合连续且bulk稠密，故确有参数族、普通continuous base change和同样的regular性。
张量由\(\mathcal I_{z,A}\otimes\mathcal I_{w,B}\simeq\mathcal I_{z+w,A+B}\)逐项实现。
改变A相当于增加共同的principal连续除子；A未由物理源、原范数或独立容量规范化。

这是非空的正结果：不应把574的Cartier准入描述为完全做不到。
但所有(3)的底层零集同为\(P\sqcup Q\)，不是函数域的可移动点支集；变化存在于连续理想的厚度／相位。
此外**全部z均有有效代表**，而纯虚z均有574的不变正fiber metric。这里的“有效＋正metric”本身不能强迫一个未构造的Weil容量符号。

## 4. 两种“局部消失”不能互换

令J为连续函数在\(P\sqcup Q\)上消失的理想层。则

\[
(\rho)\subsetneq J,
\qquad J^2=J.                                                   \tag{5}
\]

严格性：\(\sqrt\rho\in J\)，但\(\sqrt\rho/\rho=\rho^{-1/2}\)在任何边界邻域无连续延拓。
幂等性：给任意\(f\in J\)，置\(a=\sqrt{|f|}\)，在f≠0处置\(b=f/\sqrt{|f|}\)，零处置0。a、b连续、都在J，且f=ab。这也保持Γ不变性及局部限制。
所以从**底层边界的全连续消失**提取J-adic filtration时，各正层均相同，\(J/J^2=0\)。这不是曲线点的\(\mathfrak m/\mathfrak m^2\)一维情况。

相反，任意指定的\(I=(\rho)\)确有严格整数幂链，且

\[
I^n/I^{n+1}\simeq\mathcal C/(\rho) \quad(n\ge0),                \tag{6}
\]

通过乘\(\rho^n\)直接证明；regular性支付消去，不需Noetherian。
但\(\mathcal C/(\rho)\)不是边界连续结构层：\(\rho^{1/m}\bmod\rho\)有nilpotence阶m，m可任意大。
此外\(J/(\rho)\)还可含并非有限幂nilpotent的慢消失元素，如负端充分小ρ时\(1/|\log\rho|\)，局部延0并用连续cutoff补全。
因此(6)并未得到普通曲线的有限长度jets、离散valuation或同一对象的局部整除成本。
形式／导出增厚可以保留这些数据；只是其长度、拓扑完成和RR接口须另付，不能由一项regular方程自动验收。

边界处连续local ring也不可能是DVR：ρ为非零非单位，却有每个正整数次方根；DVR中若v(ρ)=N>0，则存在所有m次根会迫N被所有m整除，矛盾。
此反测限定连续层，不排旧perfectoid、tropical或其他结构层。

## 5. 另一真实自然层：Bruhat型局部常值层过于刚性

在原\(\mathbf Q_2\times\mathbf Q_3\times\mathbf R_+\)上取“有限位局部常值、实位光滑”的复值局部函数层，再取紧单位不变部分与Γ作用。
准确的层选择是局部由有限和\(\phi_2(a_2)\phi_3(a_3)\phi_\infty(t)\)生成，有限位\(\phi_v\)局部常值、实位\(\phi_\infty\)光滑；因此局部有限位level在一个实位小区间上统一，不采用较弱的逐t常值条件。
这是通常Bruhat test对象的局部版本，不能把它与全连续层等同；标准有限位定义可见[一手讲义§5.2](https://yelmaazouz.org/content/documents/p_adicHarmonicAnalysis.pdf)。不把紧支撑的全局test空间误当有单位结构层。

该层中的函数若在一个单∞边界片上恒为0，则在每个边界点附近，由有限位的局部常值性，它在一个实际开邻域上已恒为0。
所以这种方程在边界点的germ是0，不能作为regular局部方程刻出该整个边界。ρ及\(\rho^\alpha\)正因在趋p-adic零点时仍不断变化而不属于此层。
这里只排“把整个单∞边界用该层的regular方程刻出”，不排该层所有real-leaf零集或所有线丛。
共同bulk没有p-adic零点，\(g_z=e^{zx}\)仍是有限位局部常值、实位光滑的unit；因此574的clutch线仍可在此层拼接。
相应side-unit的负尾严格周期，而连续子层分类已给必要kernel；周期gauges又属于本层，故本指定指数子族的absolute kernel仍是574的iΛ，relative kernel仍零。新层并没有自动从存在的线恢复边界Cartier。

若改用p-adic locally analytic结构，须写明其系数域与比较。
不存在连续unital ring map\(\mathbf Q_p\to\mathbf C\)：它固定整数，而\(p^n\to0\)在\(\mathbf Q_p\)中、在\(\mathbf C\)中却无界。
所以不能把p-adic坐标本身免费写成复值analytic局部参数。
以\(\mathbf Q_p\)或\(\mathbf C_p\)系数构造真实analytic层是合法新输入，但它到574复连续线、实位、另一有限位与物理源的比较必须另证。

## 6. Smooth加强保留的合法逃逸

本节补充按root已准入C038的明确smooth候选，并与§3的连续幂例区分。额外选择螺旋在\([0,\infty)\times S^1\)中的ambient smooth层，意指每个side上局部为ambient smooth函数的限制；其Γ等变拉回在实际O上使用。这是一个具体较强结构，不声称由裸拓扑唯一确定。
某些非整数\(\rho^\alpha\)确不再smooth；但不能因此宣布574任意相位都无Cartier代表。
共同flat因子

\[
F(\rho)=e^{-1/\rho^2},\quad F(0)=0
\]

使\(F(\rho)\rho^z\)对任意复z均smooth延0。在两side分别以ambient函数

\[
F_{p,z}(\rho,\vartheta)=e^{-1/\rho^2}e^{z\log\rho},\qquad
F_q(\rho,\vartheta)=e^{-1/\rho^2}                                \tag{9}
\]

限制到实际螺旋，0处均置0；函数不依赖ambient角\(\vartheta\)。对每个k，(9)的k阶ρ导数是有限项
\(e^{-1/\rho^2}\rho^{z-N}P(z)\)之和，N为非负整数、P为多项式。
在z的任意紧集上，模均由\(C e^{-1/\rho^2}\rho^{-N'}\)控制，故趋0；参数z的实／虚导数只增加有限个\(|\log\rho|\)幂，仍趋0。
因此(9)连同任意参数z的mixed derivatives均在0光滑延拓，所有normal Taylor jets为0。它给联合smooth参数family，而不只逐z选择一个不可比较方程。
两side的交比仍为\(\rho^z=g_z\)，bulk非零与稠密性仍证明局部regular性，故得到真实smooth Cartier型理想。
它与§3不同：不需要A+Re z>0的参数域限制，但牺牲了全部有限normal order；不把flat共同因子当成正单位。

所以“所有Taylor jets零”不等于“截面为零”；flat对象若不从层中排掉，就必须保其实际过滤与费用。
特别(9)在选定normal-jet filtration中落入所有\((\rho)^N\)，因\(e^{-1/\rho^2}\rho^{z-N}\)仍smooth。因此该过滤在所选smooth层中不分离。

有一个准确的有限阶子门，不能误称全部Cartier分类。若候选**已独立具有**

\[
f_p=\rho^m u_p,\qquad f_q=\rho^n u_q,\qquad m,n\in\mathbf Z_{\ge0},
\]

其中u是各side边界非零的连续unit，且\(f_p/f_q=g_z\)，则574立刻给

\[
z-(m-n)\in i\Lambda.                                          \tag{10}
\]

若Re z=0，必m=n，进而z∈iΛ，该absolute指数线平凡。此处只排**指定ρ整数幂乘side unit**的regular代表，不排(9)、其他非单式首项、不同normal对象、相对frames或singular metric。
保两boundary frames时还需独立固定unit的边界限制；absolute的(10)不能免费给relative平凡。
这是574精确kernel的直接旧推论，不单独报一项新全局后果。

本稿不重复root正在核查的analytic／formal修补。加强到quasianalytic或真正analytic层、引入额外normal方向、导出／log／tropical结构均是合法路线，不能由continuous或Bruhat反测全部排除。

## 7. 物理源映射的实际门仍在

以上没有用完整Q或任何零点坐标，但只构造了**参数到Cartier线**，尚未构造全主关系保持的物理源到参数。
最自然的衰减recipe实际更弱：取固定\(\kappa\in C_c^\infty\)，对物理\(r=e^{u/2}f\in\mathcal S_{\exp,\mathbf C}\)置

\[
h_p(r)=\rho^A\exp((\kappa*r)(x)),\qquad h_q(r)=\rho^A.          \tag{7}
\]

本式在连续层中可取任意A>0；若同时作为S∞方程消费，须取整数A≥0，或把共同ρ^A改为§6的flat因子F。不能把前文任意实幂默认当smooth。
指数因子在负端趋1，故是side的真实unit。于是(7)不只给相对平凡clutch，**各side生成的Cartier理想本身与r无关**；保留的是mark/frame。537非根也被全部忘掉。
代表费用为

\[
\|\kappa*r\|_\infty\le\|\kappa\|_2\|r\|_{du}
\le\|\kappa\|_2(\log2)^{-1/2}\|r\|_{D\log}.                    \tag{8}
\]

这只是选定代表的充分原费用，不是容量lower。r的支撑窗与覆盖ρ截断不是同一个参数。

若改(3)参数为mean\(z(r)=\int r\)，则保537非根，却仍由405的全主关系
\(P=(D^2-1/4)H, H>0\)给\(z(P)=-\frac14\int H<0\)，送入非平凡574线；添上Cartier理想不会改变其失败。
纯相位mean在实源上有正metric，但全\(P_c\)的任意实缩放同样破坏关系消去。
degree-only标签消关系却杀537双矩零r₀。连续线性标签如要消全部\(P_c\)，仍须先精确消关系，再核553原du／Dlog稠密性；fixed-window或强拓扑逃逸仍保留。

通过旧源商不等于逻辑循环；任何关系保持映射本来就需因式分解。停止的范围是：本稿的Cartier化没有新增独立源桥／过滤／容量，因此不得把旧商的任意scalar读出重新报成算术移动机制。
用完整Q作标签在574已明确合法但被用户排除；本稿没有以它作为构造。

## 8. 连续正反与函数域控制

沿562的\(Z_c(s)=1+c/[s(s-1)]\)、\(d=c-1/4=\pm1/16\)真实连续positive g系统，取相同奇源
\(r=(D^2-1/4)(u\phi(u))\)，φ非零偶非负、紧支撑(-1,1)。其双pole矩和mean全为0，完整\(Q_c(r)\)在两模型严格异号。
(7)在两者都给相同Cartier理想，mean参数也在两者给同一平凡类。因此连续Cartier化既不识别这个正primitive方向，也不区分完整Weil正反。
这是设施充分性反测；没有给一般continuous模型虚构经典adelic覆盖。

真光滑proper曲线的点P有DVR参数t，\((t)^n/(t)^{n+1}\simeq k(P)\)，有限长度为n；正整数阶与有限残余度数由同一整模型确定。
degree-zero线有效则平凡的结论依赖proper代数曲线，不能搬到这里全部z均有有效连续Cartier代表的情形。
574所用\(\mathbf F_5\)真genus2控制的twist确使有效化后h⁰从2变1；其proper族、DVR和RR是额外已知正设施，而非连续fiber metric的推论。

本覆盖上反有无限截面：任意\(\mathscr L_z\)在bulk平凡，任选固定有限x窗内无限多个线性无关连续紧支撑bump，乘bulk frame再在两边界延0，便得全局Γ不变截面。
即使先固定bulk窗，仍有无限维这类截面。它们的存在不证明任何所需算术容量无限，但证明不能直接套通常有限维h⁰或把一个regular除子的形式次数当成有限RR预算。
若引入bandlimit、格、正则性或高度球，必须写其乘法、主关系、紧性及原源费用；不可凭“有截面”免费取得这些条件。

## 9. 本分支的消费范围与独立缺口

可消费的新直接数据是：(1)实际ρ非零因子；(2)任意实幂规则；(3)–(4)把574整个指定指数子族实现为连续Cartier型可逆理想；(5)–(6)精确区分边界消失与指定principal过滤。
不把它们称新外部定理，也不重复计旧384/387/396的Cartier成果。root可将它们作为一个统一研究轮的局部原件，不由分支文件数加轮。

仍欠独立输入为：

1. 在指定真实层／同一整对象内，物理r到Cartier／相对线family的实际全\(P_c\)同构，同时保537非根；非Q、非零点坐标标签还须给原du／Dlog运输。
2. 区别于任意ρ实幂／flat thickening的规范局部消失规则及可消费截面、格或valuative长度；若用连续维数也须证明其准确接口。
3. 同一对象上与该局部规则比较的独立primitive／mixed容量，含局部整除和全局费用；非“定义容量=完整Q”。
4. 容量预算与574(7)完整经典目标的同源identity：完整\(\Gamma=2\theta'\)及contact、每个\(p^k\)、双pole、allcomplex mixed全部保留。本固定2,3覆盖不覆盖全部finite places，也没有恢复arch规范。

因此(7)的自然recipe按用户停止条件到此止；mean和任意旧商scalar包装亦不重启。连续Cartier正结果保留为真实新局部设施，强拓扑、formal／derived、非标量源family和旧perfectoid／scaling-site设施的**实际有费比较**仍是合法未排路线。
本稿没有改变最强旧542＋555→557 whole leading4/5上预算、成长core／coupling／Ξ，也未提供完整Weil正性或Goal完成证据。
