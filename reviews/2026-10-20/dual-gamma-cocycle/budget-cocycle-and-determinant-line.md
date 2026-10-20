# 完整 Weil 预算片的协同变换：实 cocycle、全纯 phase 与 determinant line 的责任边界

2026-10-20；569 的独立数学原稿。只读消费 405、552、562、563、568；不改宏观状态、轮数或 Git。
本文不证明完整经典 Weil 正性。新付的是上一轮留下的 matched cocycle 合法逃逸的明确实现，
以及为什么它不会凭空支付正容量。完整 Γ 的双 conormal 来源比较由另一原稿负责。

## 1. 固定对象、域和双线性约定

令 \(\mathcal A\) 为复局部凸空间，\(b_j\) 为有限个连续 Hermitian 型，约定第一个变量复线性，
\(q_j(r)=b_j(r,r)\in\mathbb R\)。把所有符号吸入 \(b_j\)，例如

\[
 b=b_\infty+b_{\rm pole}-b_{\rm pp},\qquad Q(r)=q_\infty(r)+q_{\rm pole}(r)-q_{\rm pp}(r).
 \tag{1}
\]

也可将最后一片直接记成 \(b_-=-b_{\rm pp}\)。设

\[
 R=\{h\in\mathcal A:b(h,r)=0\ (\forall r\in\mathcal A)\},\qquad V=\mathcal A/R.
 \tag{2}
\]

这是全配对的根空间，不能只假设 \(Q(h)=0\)：不定型的 isotropic 向量未必属于根。
连续型保证 \(R\) 闭。下述代数及 norm 变换在任意这种空间上成立；全纯与曲率论断只需要
限制到有限维复仿射切片，不假设无限维商已经具有某个未构造的复解析结构。

经典应用严格采用 568§5.1 的物理域 \(\mathcal A=\mathcal S_{\exp}(\mathbb R;\mathbb C)\)，
\(r=e^{u/2}f\)，完整 \(\Gamma\)、全部素数幂和双极点按 405/563/568 规范固定。
各片在此域绝对收敛；这个域不能换成紧支域来放入非紧支 Gaussian 关系。
紧支正性目标仍是全部 \(C_c^\infty\) 复源；扩域只是合法测试原有关系。
若将素数片进一步逐 prime 拆分，须先支付该源上全局求和收敛，再交换求和与变换。

## 2. 严格的实 1-cocycle：cross 项不能丢

作用群胚 \(\mathcal A//R\) 的箭头 \((r,h)\) 从 \(r\) 到 \(r+h\)。定义

\[
 c_j(r,h)=q_j(r+h)-q_j(r)=2\Re b_j(r,h)+q_j(h).
 \tag{3}
\]

直接相减得到

\[
 c_j(r,h+k)=c_j(r,h)+c_j(r+h,k),\qquad \sum_jc_j(r,h)=0.
 \tag{4}
\]

第二式用的是 \(h\in R\)，因此 \(b(r,h)=Q(h)=0\)。第一式是 additive 1-cocycle 恒等式，
而且 \(c_j=\delta q_j\) 是显式 coboundary。只保留 \(q_j(h)\) 会漏掉代表 \(r\) 的 mixed 项，
一般不再满足 (4)。这个修复对所有复源、所有关系和任意平移步长都是精确式，误差为零。

这已能构造真正的 equivariant Hermitian line，尽管它还不是上同调行列式线。
取平凡复线 \(L_j=\mathcal A\times\mathbb C\)，赋予**纤维正**的范数

\[
 \|z\|_{j,r}^2=e^{-q_j(r)}|z|^2,
 \qquad T_{j,(r,h)}z=e^{c_j(r,h)/2}z.
 \tag{5}
\]

(3) 保证 transport 是 isometry，(4) 保证严格复合。总 tensor line 上
\(\prod_jT_j=1\)，其范数为 \(e^{-Q(r)}|z|^2\)，故在 \(V\) 上代表无关。
单片 line 的作用商也可显式平凡化：
\([r,z]\mapsto([r],e^{-q_j(r)/2}z)\)。这里是 topological/Hermitian 下降；
transport 中实部一般使它**不是全纯的**。

关键边界：\(e^{-q_j(r)}>0\) 对任意实数 \(q_j(r)\) 都成立。
因此 (5) 对正型、不定型甚至负型同样存在。把它叫作“正线”若只指纤维范数为正，
不包含 \(q_j\ge0\) 或 \(Q\ge0\) 的信息，也没有给出截面容量、局部整除或 RR 不等式。

## 3. 全纯 isometry 会产生可计算的 2-cocycle

为区分全纯 determinant/transition 需求和上一节的实下降，固定 \(h\in R\)，改用

\[
 g_{j,h}(r)=\exp\{b_j(r,h)+\tfrac12q_j(h)\}.
 \tag{6}
\]

这是 \(r\) 的全纯函数，在每个有限维切片上成立；它仍给 (5) 的 metric-isometry，
因为 \(\log|g_{j,h}(r)|^2=c_j(r,h)\)。但复合精确为

\[
 g_{j,k}(r+h)g_{j,h}(r)
 =\sigma_j(h,k)g_{j,h+k}(r),\qquad
 \sigma_j(h,k)=\exp\{i\Im b_j(h,k)\}.
 \tag{7}
\]

\(\Im b_j\) 对底层实向量空间双线性，故 \(\sigma_j\) 满足 2-cocycle 恒等式。
这是 Heisenberg 型的 projective 作用；可通过相应中心扩张严格化。
不应将它误写成每个单片已经获得 \(\mathcal A//R\) 的严格全纯下降。
总 tensor 中

\[
 \prod_j\sigma_j(h,k)=1,\quad \prod_jg_{j,h}(r)=1,
 \tag{8}
\]

因为 \(b(r,h)=b(h,k)=0\)。所以完整 budget 的模和 phase 都协同抵消。
这个 cancellation 仅使用同一个完整 \(b\) 及其根空间，不预读零点位置。
但它也不是新的正性来源：不定 \(b\) 具有完全相同的机制。

在有限维复商切片上，总线的固定 frame metric \(e^{-Q}\) 的 Chern 曲率由
\(i\partial\bar\partial Q\) 给出。沿任意直线 \(r=tv\)，其系数是 \(Q(v)\)。
因此“这个特定总线的曲率半正”恰为 \(Q\ge0\)，是 Weil 正性的重述。
若不固定 frame/section，而只观察 (5) 的抽象实线商，它已经平凡且 norm 恒等于标准 norm，
更不能从这种平凡性读出 \(Q\) 的符号。

## 4. 经典 Gaussian 关系的完整 cross/phase 检验

405 的 \(h=E\eta\in I\) 满足 \(c(h)=d(h)=1/4\)。设 \(r_h=e^{u/2}h\)，
则 \(r_h\in R\subset\mathcal S_{\exp}\)，两个物理 pole moment 为
\(M_+(r_h)=M_-(r_h)=1/4\)。极点型固定为

\[
 b_P(r,s)=M_+(r)\overline{M_-(s)}+M_-(r)\overline{M_+(s)},
 \quad q_P(r)=2\Re(M_+(r)\overline{M_-(r)}).
 \tag{9}
\]

对任意复 \(t\) 及任意物理源 \(r\)，

\[
 c_P(r,tr_h)=\tfrac12\Re\{\bar t[M_+(r)+M_-(r)]\}+\frac{|t|^2}{8},
 \quad c_{\infty-\rm pp}(r,tr_h)=-c_P(r,tr_h).
 \tag{10}
\]

在 \(r=0\) 时恢复旧 \(\pm|t|^2/8\)；\(t\) 实时才可写 \(\pm t^2/8\)。
只重复 diagonal 的 \(1/8\) 不足以核对一般代表变换；(10) 明确付 mixed 项。
沿关系复直线 \(r=sr_h\)，有

\[
 q_P(sr_h)=|s|^2/8,\qquad
 \sigma_P(tr_h,ur_h)=\exp\{i\Im(t\bar u)/8\},
 \tag{11}
\]

arch-minus-prime 片的 phase 正好是倒数。例如 \(t=1,u=i\) 给 pole phase \(e^{-i/8}\)。
所以最直接的单片全纯 transport 确实可能只 projective，不能省略 phase 后称作 determinant transition。
完整 tensor 的作用仍严格且平凡；这给 568 所保留的 matched cocycle 一种实际实现。

这没有把 \(I\) 宣称为全部 \(R\)，也没有把 \(I\) 宣称为旧 \(B\) 的根。
405 精确结论是 \(I\cap\operatorname{rad}B=P_{\rm an}=I\cap\ker c\cap\ker d\)，
且 \(\mathcal S_{\exp}/P_{\rm an}\simeq\mathbb C^2\times(\mathcal S_{\exp}/I)\)
（405 实空间定理的复化）。两个次数方向保留 \(B\) 的双曲型，不能一并丢掉。
这个扩张是合法的代数与拓扑容器，但没有把这些向量升级为 global sections 或 principal divisors。

## 5. 连续正反族中同样存在真实 compact 的 cocycle 测试

对 562/563 的真实正 primitive/g-integer 族
\(Z_c=1+c/[s(s-1)]\)，\(0<c\le1/2\)，写 \(d=c-1/4\in(-1/4,1/4]\)。
完整源 \(W_d=2C_d\)，\(C_d''=-dC_d\)、\(C_d(0)=1\)、\(C_d'(0)=0\)，
\(S_d''=-dS_d\)、\(S_d(0)=0\)、\(S_d'(0)=1\)。其完整型为

\[
 Q_d(r)=2|A_r|^2+2d|B_r|^2,
 \quad A_r=\int rC_d,\quad B_r=\int rS_d.
 \tag{12}
\]

两端极点全部保留，模型 Γ=0；不是把经典 Γ 改成零。
取任意非空有限开窗 \(U\)。四个实解析函数
\(C_d,S_d,e^{u/2},e^{-u/2}\) 在 \(U\) 线性独立：若两组解空间有公共函数，
同时满足 \(F''=-dF\) 与 \(F''=F/4\)，由 \(d>-1/4\) 得 \(F=0\)，各组内部亦独立。
取 \(\chi\in C_c^\infty(U)\)、\(\chi\ge0\)，在一个子窗上严格正，记四函数为 \(\phi_i\)。
其矩阵 \(G_{ij}=\int\chi\phi_i\phi_j\) 严格正定：非零线性组合解析且不恒零。
令 \(\alpha=G^{-1}(0,0,1/4,1/4)^T\)、\(h_d=\chi\sum\alpha_i\phi_i\)，则

\[
 A_{h_d}=B_{h_d}=0,\quad M_+(h_d)=M_-(h_d)=1/4.
 \tag{13}
\]

因此 \(h_d\) 是**真实 compact** 源，并属于完整型根空间（包括 \(d=0\) 阈值）；
\(q_P(h_d)=1/8\)，全部 Π 的带符号预算为 \(-1/8\)。式 (3)–(11) 的对应 cocycle/phase
测试在正段 \(d>0\)、反段 \(d<0\) 及阈值上同时通过。
这不只是形式增加一个 \(\mathbb C\) 方向来模拟关系。

式 (12) 的正负判定归 563/568 旧资产；新增检验是同一个实际源族的预算协同构造。
它说明 matched metric/cocycle 是正确相容设施，但本身筛不掉负段。
在一个含负方向 \(v\) 的有限维商切片上，\(e^{-Q_d}\) 仍是正纤维 metric，
而曲率在该方向为负；要求半正曲率恰重新要求 (12) 非负。

## 6. 真正的有限评价 determinant line 需要额外什么

给定一个已经独立存在的有限维评价映射 \(E:S\to J\)，可构造两项复形
\([S\xrightarrow E J]\) 于次数 \(-1,0\)，及真正的 determinant line

\[
 \lambda(E)=\det J\otimes(\det S)^{-1}
 \simeq\det\operatorname{coker}E\otimes(\det\ker E)^{-1}.
 \tag{14}
\]

这来自 kernel/image/cokernel 的短正合列；与任意二次型取指数不同。
若维数相同，有规范截面 \(\det E\)，它非零当且仅当 \(E\) 可逆。
line 本身始终存在，不代表其规范截面非零；存在非零评价 minor 也不代表 Weil Gram 为正。
有限 projective 模的短正合列相容性及两项 perfect complex 的此构造，已核
[Stacks 0FJ9](https://stacks.math.columbia.edu/tag/0FJ9)、
[0FJI](https://stacks.math.columbia.edu/tag/0FJI)；本节只消费这些有限级事实。
不从其名称引入未构造的经典层、proper family 或无界 Fredholm 截面。

若 \(S,J\) 上另有独立正 Hermitian Gram \(H_S,H_J\)，平衡维数时

这里用列坐标 \(x\) 按 \(q_S(sx)=x^*H_Sx\) 定义矩阵，即在本文第一变量线性的约定下
\((H_S)_{ij}=b_S(s_j,s_i)\)，target 同理；不能把它与 \(b_S(s_i,s_j)\) 的矩阵混同。

\[
 \|\det E\|^2=|\det[E]|^2\frac{\det H_J}{\det H_S}.
 \tag{15}
\]

换基 \(s'=sA,j'=jB\) 时，\([E]'=B^{-1}[E]A\)，两个 Gram 按 \(A^*H_SA\)、\(B^*H_JB\)
变化，(15) 精确不变。这里有真实的 source、target、kernel 和相容 norm。
若 \(H_J\) 直接取未知 Weil Gram，正 Hermitian metric 的前提已偷带目标。
取 \(|\det H_J|\) 则删了符号；正 determinant 也不足以保证 Gram 半正（两个负本征值的 determinant 为正）。
要求全部相应 Gram 主子式非负在全 coverage 下仍是原 Weil 正性的等价组织。

要将 LS 的“非零 D＋有限位整除＋无穷位上界”运输到此接口，还须独立给：

1. 同一个 \(S\) 的可乘 global sections/函数源，以及真实目标 jets、消失过滤、\(\ker E\) 的意义；
2. 算术格或所有 places 的相容结构，使同一个非零 determinant 截面承受局部 order 条件；
3. 独立 RR/height/volume 容量上界，且换基、principal 变化由同一局部映射控制；
4. 它的全位预算差除以固定 scale，精确趋于**完整** Weil 型，含 Γ、全部 powers、极点、mixed 和 uniform 误差。

有限位 lower 与无穷位 upper 只有在同一个截面上才比较。对一个数域标量非零 \(D\)，product formula
给 \(\sum_v n_v\log|D|_v=0\)；它把这些局部费用连起来，但单纯的 g-integer 测度没有
自动提供 \(D\)、局部 DVR、格或所有 norm。把 (5) 的 tensor metric 命名为这个 determinant metric，
没有支付上述四点。

## 7. 函数域检验：局部 line/cocycle 与全局容量分开

对真实光滑 proper 曲线 \(X/\mathbb F_q\)、线丛 \(L=\mathcal O(D)\) 及有效有限 jet 除子 \(E\)，
实际 sheaf 正合列

\[
 0\to L(-E)\to L\to L|_E\to0
 \tag{16}
\]

给真实评价 \(H^0(L)\to H^0(L|_E)\)，其 kernel 是 \(H^0(L(-E))\)，并在 cohomology determinant 中
协同连接 kernel、jets 和 \(H^1\)。若 \(\deg E>\deg D\)，kernel 为零；RR 给 \(H^0(L)\) 容量。
这些是几何提供的独立设施，而不是由式 (3) 定义出来的。

主变化 \(D'=D+\operatorname{div}\varphi\) 时，\(f\mapsto f/\varphi\) 给 \(\mathcal O(D)\simeq\mathcal O(D')\)，
同时运输 (16) 的 source、target 和 kernel；局部平凡化的 order/norm 变化相容，总次数为零。
因此真正的 determinant line 允许各片非零、协同变换，并不要求每个 Green/order 分量分别消失。
但此处真实的 \(\varphi\) 及 global function field 是关键输入。

568 的 \(q=5\) 真曲线和 290 反模型都具有正整数闭点数、perfect local jets、正 raw-Frobenius 载体。
每个有限 map 一旦给出，也都具有 (14) 的形式 determinant line 与换基 law；所以这些局部性质
不能单独排掉 primitive Gram 失正。反模型未被给出同一个真实曲线的 (16)、RR 与交数几何；
不能从相同局部设施倒推其存在，也不能把 trace subtraction 的正号当作已付。
函数域完整 Weil 正性仍依赖平方上的有效性/交数与容量比较（567），不是 determinant functor 本身的定理。

## 8. 对 finite-part/Γ 规范的直接含义

若只在 arch 片增加 \(a\|r\|_2^2\)，其 cocycle 增量为
\(a(2\Re\langle r,h\rangle+\|h\|_2^2)\)。为了维持同一个完整 \(Q\)，必须由另一片精确负补偿。
这种重新记账有合法 cocycle，却不识别目标 Γ；任意抵消的 contact 重新分配都能做到。
如果全余项固定而真正改了完整源，则 568 的非零零关系立即检测到 \(a\ne0\)；
这仍只校准该 contact 自由度，不排一般 Mellin \(B(s)\) kernel gauge。

所以 dual conormal/finite-part 方向必须先从其固定字符、测度、双侧权、cutoff 定义独立得到
同一个完整 arch 分布及接触常数。若仅事后选 \(a\delta_0\)、手调半轴权或人为指定匹配 cocycle，
上述相容下降没有把它升级为经典 Γ 的独立恢复。

## 9. 根消费边界与真实增量

已付：完整 Hermitian 分片下的全源 real 1-cocycle，保留 mixed 项；全纯 transport 的精确 Heisenberg
2-cocycle 与完整 tensor phase cancellation；经典 \(1/8\) 的全 complex cross 检验；
连续正反族内真实 compact 关系的同样协同检验；实际有限评价 determinant 的正合列/norm 责任。

未付：这些 line 与某个独立 global evaluation/perfect complex 的自然识别；真实 principal/gluing；
共同截面上的局部 order 下界、全局 RR/height 容量及完整源预算身份和增长误差；经典独立正极化。
纤维 metric 总为正、cocycle 消失、determinant line 存在均不包含这项正性。

旧资产归属：405 的关系、双次数和精确 \(1/8\)，552 的 radial Green 非下降/频率费用，
563/568 的连续正负号及 finite jets 反例都不重计。这里新增的是合法协同修复的显式实现及其精确强度，
没有改善 strongest-old 542+555→557 whole leading \(4/5\)，也未改变 560 成长 \(K\)/sign/core/coupling/通常 \(\Xi\) 责任。
是否构成主稿一轮由 root 统一结算，不在子稿计轮；不是宏观 Goal 完成。

来源阅读：本轮实际打开 Stacks tags 0FJ9、0FJI、0FJW、0B5B；只消费 0FJ9/0FJI 的有限 projective/两项复形构造。
未引用一条尚未核对的 Deligne–RR/Quillen anomaly 定理来支付经典 Γ；本文 cocycle/phase 公式均由给出的二次型直接计算。
