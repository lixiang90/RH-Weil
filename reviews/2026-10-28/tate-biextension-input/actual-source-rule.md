# 固定 Tate 曲线上的双源 Cartier／双扩张候选

2026-10-28；G20261027／runtime1793085111／原0c4f。按STATE唯一下一动作实际写出一份源公式，再以最便宜的全关系和非根门决定准入。它与已停互素加法规则无依赖，不改那份规则的权或补偿；本稿不预建C050／587，不预计数学轮。

## 一次冻结的对象与规则

使用旧[371](../../../notes/371-f1-tate-curve-frobenius-weight.md)已经给出的实际紧复椭圆曲线
\[
 E=\mathbb C/\Lambda,\quad\Lambda=(\log2)\mathbb Z+2\pi i\mathbb Z,
 \qquad O=[0].
\]
它也等于\(\mathbb C^\times/2^{\mathbb Z}\)。这是复曲线，不是本次新构造的整算术模型，也不把几何乘2平移冒作算术Frobenius。

对完整复物理源 \(r=e^{u/2}f\in\mathcal S_{\exp,\mathbb C}\)，固定唯一标签与实际除子
\[
 \ell(r)=\int_{\mathbb R}e^u r(u)\,du,\qquad P_r=[\ell(r)]\in E,
 \quad D_r=[P_r]-[O],\quad J_r=\mathcal O_E(D_r).                 \tag{1}
\]
系数是整数\(+1,-1\)；当\(P_r=O\)时原除子为0。它不是将复权函数直接称为整除子。

两个独立复源的混合对象先取\(E\times E\)上的实际线
\[
 \mathcal P=\mathcal O_{E\times E}
  (\Delta-E\times\{O\}-\{O\}\times E),\qquad
 \mathcal B(r,s)=(P_r,P_{\bar s})^*\mathcal P.                    \tag{2}
\]
可用覆盖坐标的\(dw\)给两轴的常数一维线选择相容刚性化。这里的pullback是随\((r,s)\)变化的**线值族**；单个纤维是一维复向量空间，不能仅由其抽象同构类读出高度。第二腿共轭也没有把它自动变为Hermitian数值型。Poincaré型双扩张结构／metric、截面及其与完整Weil型的身份均未由(2)支付；首门失败即不继续展开这些设施。

## 三句准入与原费用

1. 独立给定的是实际曲线、Cartier线和两源线族；曲线及RR为旧371资产，(1)仅是旧574已知Mellin标签的一次固定代入。尚无新经典signed／primitive输入。
2. 首检\(p\in P_{\rm phys}\)是否使\(D_p\)为实际主除子，同时保537正窗非根；成功才轮到同对象mixed身份和成长容量。
3. 若首检通过且提供不被旧标签／有限通道结果决定的混合数据，才可能改变源→principal箭头。实际未通过则按强旧前置0止本规则，不能因线族非平凡而准入证明合同。

标签在\(\mathcal S_{\exp}\)上有明确强界
\[
 |\ell(r)|\le\frac43p_{2,0}(r),\qquad
 p_{2,0}(r)=\sup_u e^{2|u|}|r(u)|.
\]
先固定支撑\([-A,A]\)时，原du上的精确dual norm为
\[
 \|\ell\|_{L^2([-A,A])^*}=\sqrt{\sinh(2A)},\qquad
 |\ell(r)|\le\sqrt{\sinh(2A)/\log2}\,\|r\|_{D\log}.             \tag{3}
\]
后一式只为Dlog上界。全线平移\(T_a r(u)=r(u-a)\)保每个固定有限Sobolev范数，却令\(\ell(T_a r)=e^a\ell(r)\)，因此标签不具global有限Sobolev界。不能直接给它套553的全局连续标签结论；首门另用实际Pan值。

\(u,A\)是物理坐标／支撑，\(w,\Lambda\)是曲线覆盖坐标／周期；这里没有用\(A\)替换算术height或源依赖carrier。式(3)不支付双扩张metric的任何高度界。

## 最便宜的精确全关系检查

沿[405](../../../notes/405-f1-adelic-restriction-moments-and-radical.md)和[574 §4–5](../../../notes/574-actual-adelic-cover-relative-picard-and-source-transport.md)，令\(h=E\eta_h\)，\(H(u)=e^{u/2}h(u)\)，真实physical关系
\[
 P=(D^2-\tfrac14)H\in P_{\rm phys},\qquad
 \ell_z(P)=\tfrac12(z^2-\tfrac14)\xi(\tfrac12+z).
\]
该式用405全整数Gaussian/Mellin归一化和强衰减，无边界项；本稿不裁成compact关系。代入本次固定\(z=1\)得
\[
 \ell(P)=\tfrac38\xi(\tfrac32)>0.                               \tag{4}
\]
正号只用Re\(s>1\)的正实Gamma／Euler数据，不用RH或未知根。
取\(a=(\log2)/(2\ell(P))\)。全复关系空间对标量闭合，故\(aP\in P_{\rm phys}\)，但
\[
 P_{aP}=[\tfrac12\log2]\ne O.
\]
若\([P_{aP}]-[O]\)为主除子，就有非恒定亚纯函数只在\(O\)有至多一阶极点，冲突旧371属一RR给出的\(h^0(E,\mathcal O_E([O]))=1\)。故\(J_{aP}\)确实非平凡，**真实Weil零关系没有成为该曲线上的主除子**。

更准确地，非零复线性值(4)使\(P_{\rm phys}\)的点像已经扫满\(E\)。这不把Pan等同于全源空间；只是这个标签忘记了原商所需的区分。先截断Pan或只检compact交集都不能修复本门。

## 全源完整读出的另一旧责任

若某个完整双源读出只依赖\((P_r,P_{\bar s})\)的固定刚性化点数据，并在\((O,O)\)与零源给相同值，则它看不见\(\ker\ell\)。在537的fixed17/16正窗内取两个不交支撑非零smooth bump \(v_1,v_2\)且\(\ell(v_2)\ne0\)，则
\[
 r=v_1-\ell(v_1)\ell(v_2)^{-1}v_2\ne0,\quad \ell(r)=0,
 \qquad Q_\zeta(r)>0.
\]
因此仅点数据的完整Weil身份失败；这正是旧568／575的有限通道覆盖责任，不是新核心方法类边界。若另带完整原源、路径、非固定frame或额外无界腿，则不属于这个判定；那些额外数据必须给实际公式，不能失败后自动加入。

目标仍是同一完整经典\(Q_\zeta\)，包含全部\(\Gamma=2\theta'\)、FP-contact、每个\(p^k\)的\(\log p\)及双pole。式(1)–(2)没有将其任何部分识别为高度或mixed pairing；不报告局部正metric为经典正性。该候选亦可作为其他系统的一个组件，但本次没有那份总型／coupling输入。

## 分类与停止范围

首门的最强后果已由405／574的实际Mellin公式、371的真实RR与537／568／575有限通道责任直接蕴含。这里不产生新全关系定理／高度费／核心边界，按前置强旧0，不以简单程度或RH收益决定计轮。停止这一固定\(E_2,\ell_1,D_r,\mathcal B\)源规则；不更换evaluation点、曲线周期或增加Green拟合来续预算。

不是所有Tate／Poincaré／非标量／relative／源适应方法均失败；尤其line值族不能凭一个未定义数值高度被否定。实际关键primitive/mixed、净signed/corecross与Ξ仍未付，whole4/5仅UPPER、latest586及cadence0/history50/cycle17不变。当前等待两份独占支持和独立fresh核查；本稿发出不等于root消费。

## 原发稿后的消费状态

三当前稿经独立fresh限定PASS，root已按[首门结算](../../../goals/reviews/2026-10-28-tate-biextension-source-gate-stop.md)消费，强旧前置0止；上文“等待”是原发稿观察。仅追加状态／链接，固定公式和数学范围不变。
