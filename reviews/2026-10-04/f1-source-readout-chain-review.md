# 426 固定源交换子、线性双模与读出选择的独立审查

2026-10-04。审查对象：[426](../../notes/426-f1-fixed-corner-source-commutators-and-relative-readout-module.md)。
绑定最终正文 SHA256：`e90e74e394c0f8a400cf678d81695e63e63eb5e6712af021ecb9bf8355ddb3bd`。
本审查只读正文及425的明确前提，不修改正文。

**结论：PASS，限于正文声明的Hilbert算子、原物理截止、线性双模及非唯一性范围。**
逐项核验(1)–(20)，没有发现需要阻止采纳的数学错误。它并未建立完整相对循环Chern链、算术主消失、RR或RH；这些仍为实际未完成桥梁。

## 1. 正角压缩及全部混合块

采用425已经明确的球／波形向量、固定采样算子和紧支光滑时间核。由
\(R_r^- = \sum_{j<0}P_{e_j}+P_{b_{0,r}}\)、\(HW_r=W_rH=W_r\)，
以及\(b_{0,r}\perp w_{0,r}\)，426(2)确为两个正交径向秩一角；时间乘法部分没有被错误称为有限秩或迹类。

对\(n\ge1\)，直接用\(w_0\)的非负坐标几何系数得到
\(Hw_{-n,r}=-c_r\rho_r^{n-1}b_{0,r}\)，符号、指数与系数均正确。
同通道左Q块秩至多一且迹范数至多一；交叉p←q的左Q径向迹范数恰为
\(c_p\rho_p^{n-1}\)，反向由q控制。
时间支集把每个a所允许的b限制在长度\(2B/M\)的区间，整数个数至多
\(1+\lfloor2B/M\rfloor\)。故(5)–(6)给全混合和的实际迹范数可求和性。
与425强和的矩阵元一致保证所得算子正是\(QA(h)\)；右Q由伴随得到。
这一证明没有把未经Q压缩的原群和误改为绝对迹范数和。

## 2. 乘子域与零普通迹

\(\mathcal M_Q=\mathbb C1+Q\mathcal B(\mathcal H)Q\)是明确的含单位星代数；
\(T=1+Q(u-1)Q\)及\(T^*\)属于此域。
正文已准确补明：任意\(QJQ\)仅为所构造双模的Hilbert有界乘子，未证明其属于原交叉积C*代数的乘子域。
这一区分是必须保留的范围限定。

\(JA=JQA\)、\(AJ=AQJ\)迹类，故\([R,A]\)迹类。
物理投影\(\mathsf P\)满足\(\mathsf P Q=Q\mathsf P=Q\)，因此与每个\(R\in\mathcal M_Q\)交换，
且\(\mathsf P[R,A]\mathsf P=[R,\mathsf P A\mathsf P]\)。右端为有界算子与迹类算子的交换子，普通迹严格为零。
强趋单位的有界投影双压缩在\(\mathcal S_1\)范数收敛，故完整交换子的普通迹也为零。
这里确实使用了截止相容性，没有使用错误的“一切迹类交换子自动零迹”推论。

令\(T=1+J\)，实际展开是
\[
 [T^*,TA]=J^*A-AJ^*+J^*JA-JAJ^*.
\]
四项皆迹类；\(\mathsf P\)同时与T、T*交换，使其压缩等于
\([T^*,T\mathsf P A\mathsf P]\)，对每个截止的迹已为零。
所以(11)–(12)的完整源加权交换子及普通迹结论成立，不需要T酉或\([T,C_\infty]=0\)。

## 3. 延拓的定义无关性及连续性

设\(\mathcal D=\{A(h)+S:h\in C_c^\infty(\mathbb R),S\in\mathcal S_1\}\)。
若\(A(h)\in\mathcal S_1\)，物理压缩迹有界，(1)的精确体积公式强制\(h(0)=0\)；
迹范数压缩收敛随后给\(\operatorname{Tr}A(h)=\Lambda(h)\)。
这是\(\operatorname{span}A(C_c^\infty)\)与\(\mathcal S_1\)交集所需的全部一致性，
所以(14)不依赖表达式，(15)的联合极限与体积系数也不依赖表达式。

连续性所用拓扑应按正文原义理解为商拓扑：取
\[
 \pi:C_c^\infty(\mathbb R)\oplus\mathcal S_1\longrightarrow\mathcal D,
 \qquad\pi(h,S)=A(h)+S,
\]
测试函数空间使用通常LF拓扑，迹类空间使用迹范数。
425(27)保证\(h\mapsto\Lambda(h)\)连续；普通迹为迹范数连续。
\(\Lambda(h)+\operatorname{Tr}S\)在\(\ker\pi\)上为零，因此下降为商拓扑连续泛函。
这不声称算子范数或强算子拓扑上的连续迹，也不暗中完成一个乘法代数。

## 4. 受限循环相容性的准确范围

若\(R=c1+J\)，则
\(RA(h)=cA(h)+JA(h)\)、\(A(h)R=cA(h)+A(h)J\)，后项迹类。
加上有界乘子保持\(\mathcal S_1\)，\(\mathcal D\)确为\(\mathcal M_Q\)双模。
对\(F=A(h)+S\)，
\[
 \widetilde\Lambda(RF)-\widetilde\Lambda(FR)
   =\operatorname{Tr}[J,A(h)]+\operatorname{Tr}[R,S]=0.
\]
故(16)及由\(TA(h)\in\mathcal D\)导出的(17)成立。
它只给一腿在\(\mathcal M_Q\)、另一腿在\(\mathcal D\)的循环相容性，
没有证明\(\mathcal D\)乘法封闭，也没有证明对一般径向群移位不变。
正文没有把这个零交换子擅自识别为完整相对Chern边界或算术主关系，范围准确。

## 5. 指定截止的最小Q约化包络

426(18)是有限波形空间的准确径向线性代数事实。
当K≥1时，\(H\operatorname{span}\{w_{-K},\ldots,w_{-1}\}\)恰为\(\mathbb Cb_0\)；
加入b0后，球／波形三角递推给
\[
 \operatorname{span}\{w_{-K},\ldots,w_{-1},b_0\}
  =\operatorname{span}\{e_{-K},\ldots,e_{-1},b_0\}.
\]
因此\(F+QF\)正是包含指定F的最小Q不变空间；Q自伴使其为约化空间。
两个径向通道仍正交。
这只解释该指定波形族缺失的球方向；正文已排除任意截止唯一性及“有限包络自动与T交换”的过强结论。

## 6. 新增第二读出的严格非唯一性

独立核验425(30)–(31)：\(F_K\to E_\infty\)强收敛、\(A=E_\infty A E_\infty\)，
且\(\operatorname{Tr}(F_KA(h)F_K)=(K_pL+K_qM)h(0)\)。
若A迹类，上一节已给h(0)=0；以有限秩逼近A证明
\(F_KAF_K\to E_\infty A E_\infty=A\)迹范数收敛，故
\[
 A(h)\in\mathcal S_1\quad\Longrightarrow\quad
 \operatorname{Tr}A(h)=\Lambda(h)=0.
\]
426(19)比(13)更强，且确由另一个真实截止推出，没有人为扣除周期原子。

于是\(\Psi_0(A(h)+S)=\operatorname{Tr}S\)定义无关：两种表达式之差的A部分迹类且普通迹为零。
同样的商拓扑论证给其连续性；它匹配普通迹，并由
\(\operatorname{Tr}[R,A]=\operatorname{Tr}[R,S]=0\)满足同一\(\mathcal M_Q\)循环条件。
取h支集只靠近−L、避开0及其他轴周期、h(−L)=1，则
\(\widetilde\Lambda(A(h))=L\rho_p\ne0\)，而\(\Psi_0(A(h))=0\)。
所以普通迹匹配、受限源循环及自然源交换子消失，确实不足以唯一选定原纯周期读出。

## 7. 采纳后仍须保留的未完成事项

没有实质错误需返修；有限范围PASS绑定上述最终SHA。后续不得删去以下限定：

- \(\mathcal D\)只是明确的线性双模，乘法封闭与全循环复形未建立。
- \(\mathcal M_Q\)的任意Hilbert有界角乘子准入不等于原C*交叉积乘子准入。
- (17)的零值尚未识别为原边／角相对Chern链的算术主消失。
- (20)给出真实读出选择障碍；必须补充具有原几何来源的规范性或链层比较才能选定\(\widetilde\Lambda\)。
- 两有限位周期比较尚未接上实位、全体素数及Weil二次型，未证明RR或RH。

本审查的PASS只采纳已有算子与双模结论及其明确非唯一性，不替代这些后续桥梁。
