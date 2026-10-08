# 原MT六邻域对角调节与同一实际计数预算

2026-10-08。作者 compression。基线 main
5d508871ac3f087319e49c3b444187eaa66a7d30。
只新增本研究，不修改478、冻结核证书、原解析源或Git。

本稿完整支付一个很小的实际余量：原六邻域试探允许负的常数对角，
而谱对偶只需上界 \(B\preceq I\)。由已经支付的同一全域核界和七点证书，
可得
\[
 p_{\rm dg}=
 \frac{20320312500000C_0-40625024990}{20243124957721}
 =0.6730581102819731\ldots ,
 \quad C_0=\frac32-\frac1{\sqrt2}\cot(1/\sqrt2).
 \tag{1}
\]
它比478的 \(p_6\) 严格增加约 \(1.712296814\times10^{-10}\)；
不同零点比例为 \((1+p_{\rm dg})/2\)。
这里是完整数学推导及精确有理核算，尚需不同作者全文审查后项目准入。
不声称新的零条带、世界纪录、最佳参数或常数级四矩。

## 1. 冻结输入与有限对偶

本稿只引用[478作者源](hybrid-mt-six-neighbor-spectral-dual-and-actual-counting-research-compression.md)
的全实轴核界、全域七点证书及304固定平滑接口。
该源 canonical LF SHA256 为
c69dcf11fe9ed46be77dbd5c2926e6058193cf61808613a73121797aa53656a9。
[478](../../notes/478-original-mt-six-neighbor-dual-and-whole-chain-proportion.md)
canonical LF SHA256 为
6ab8384289cf7470b7ee448e381f5e9afdd268b13852f95322c98c1a62dd5c54。
本稿不重新执行核或七点覆盖，也不改它们的参数与输出。

沿用正偶概率密度 \(f_0\)、实核 \(k_0=\widehat f_0\)，
\[
 j(t)=(t-1)^2-(t-2)_+^2\quad(t\ge0),\qquad J(G)=\operatorname{Tr}j(G).
\]
对任何有限 \(G\succeq0\) 和 Hermitian \(B\preceq I\)，有
\[
 J(G)\ge2\operatorname{Tr}B(G-I)-\operatorname{Tr}B^2. \tag{2}
\]
为直接核实其单侧适用范围，对任何实数 \(b\le1\)：
当 \(0\le t\le2\) 时，\(j(t)-2b(t-1)+b^2=(t-1-b)^2\ge0\)；
当 \(t\ge2\) 时，该差为
\((1-b)(2t-3-b)\ge0\)。
在B本征基对G用凸标量j的Jensen，再逐项应用此式，得到(2)。
既不要求 \(B\succeq-I\)，也不要求与G交换。

## 2. 已付六邻边加一个常数对角

取原 \(d_0=3809/4000\)，对于相邻gap至少 \(d_0\) 的n点列y，
定义 Hermitian K：在 \(1\le|i-j|\le6\) 时
\(K_{ij}=k_0(y_i-y_j)\)，其余含对角为0。
完整 Gram \(G_0\) 仍含全部条目。
原已认证 \(M_r\) 的和为 \(51/100\)，故
\[
 \|K\|\le S=\frac{51}{50},\qquad
 E_6=\operatorname{Tr}K^2=\operatorname{Tr}K(G_0-I).
 \tag{3}
\]
最后一个等号只使用K所保留边与G一致及实对称核。

对 \(e\ge0\)，令
\[
 u=\frac{1+e}{S},\qquad B=-eI+uK,\qquad c=2u-u^2.
\]
由 \(\lambda_{\max}(K)\le S\)，
\(\lambda_{\max}(B)\le-e+uS=1\)，所以(2)合法。
\(\operatorname{Tr}K=0\)、\(G_{0,ii}=1\) 精确给
\[
 J(G_0)\ge cE_6-e^2n. \tag{4}
\]
下方谱可能小于-1，不影响(2)。对角损失 \(e^2n\) 全部保留。

取固定有理参数
\[
 e=\frac1{62500},\quad u=\frac{62501}{63750},\quad
 c=\frac{4062502499}{4064062500}>0.
 \tag{5}
\]
原七点证书在全部连续窗口求和仍是
\(E_6+\operatorname{span}(y)/500\ge\tau(n-6)\)，\(\tau=19/5000\)。
当 \(0\le n\le6\) 时右侧非正，空点列按span=0处理。
所以
\[
 J(G_0)\ge\alpha n-\eta\operatorname{span}(y)-6c\tau,\quad
 \alpha=c\tau-e^2=\frac{77187542279}{20320312500000},\quad
 \eta=\frac c{500}=\frac{4062502499}{2032031250000}. \tag{6}
\]
端项是 \(6c\tau\)，不是 \(6\alpha\)。

## 3. 全部位置和增长一致的实际传递

按原 \(d_0\) 将任意简单点列分成短簇及全部单点簇S。
S合为一个分离主块，\(\operatorname{span}(S)\le\operatorname{span}(x)\)。
每个大小 \(m\ge2\) 的短簇用互不交的相邻pair；
原核下界 \(|k_0(g)|>1/10\) 给其总J至少
\(2\lfloor m/2\rfloor/100\ge m/150>\alpha m\)。
完整Gram一次pinch成S、pairs与剩余单点，得
\[
 J(G_0(x))\ge\alpha s-\eta\operatorname{span}(x)-6c\tau. \tag{7}
\]
没有每簇端项，也没有重叠累加同一谱余项。

先固定原实偶光滑单位profile \(f_\delta\)，
\(\epsilon_\delta=\|f_\delta-f_0\|_1\)，
全轴 \(|k_\delta-k_0|\le\epsilon_\delta\)。
仍使用以k0造的同一B，故可行性不随增长维数改变。
真实Gram对角精确为1，故负对角项与核差的迹精确为0。
其余保留边给
\[
 2\operatorname{Tr}B(G_\delta-G_0)
 \ge-2uS\,n_s\epsilon_\delta=-2(1+e)n_s\epsilon_\delta. \tag{8}
\]
实际短簇每节点费用
\(\beta_\delta=(2/3)(1/10-\epsilon_\delta)^2\)。
令 \(\alpha_\delta=\alpha-2(1+e)\epsilon_\delta\)。
对所有 \(0\le\epsilon_\delta\le1/10000\)，有
\[
 0<\alpha_\delta\le\alpha<
 \frac23(1/10-1/10000)^2\le\beta_\delta.
 \tag{9}
\]
最后一步是epsilon单调性；具体两项精确余量见第4节。
因此同样的全部点数账本给
\(J_\delta\ge\alpha_\delta s-\eta X_T-6c\tau\)。

原全部复零点自伴算子A仍保留全部离线正负块，
\(\operatorname{Tr}A=N\)、
\(\|A\|_{\rm HS}^2=(R_\delta+o_\delta(1))N\)，
\(R_\delta\to2-C_0\)，\(X_T/N\to1\)。
原完整重数/惯性预算仍为
\[
 s\ge2N-\|A\|_{\rm HS}^2+J_\delta,\qquad
 2D\ge3N-\|A\|_{\rm HS}^2+J_\delta. \tag{10}
\]
先固定profile令T趋无穷，再让profile趋原MT，
即得 \(\liminf s/N\ge(C_0-\eta)/(1-\alpha)=p_{\rm dg}\)。
用同一第二式及 \(\alpha_\delta>0\) 得不同点下界
\(\liminf D/N\ge(1+p_{\rm dg})/2\)。
没有免费使用 \(D\ge(N+s)/2\)，没有让profile随T移动。

## 4. 可复算的精确比较

使用[477有理输出](../../output/hybrid-multipoint-cap-exact-algebra.json)
中C0的严格区间，canonical LF SHA256
d84077ab71b47d1ea253cad9675fa8c25f9aa4dade775ad73ff53033167625c3。
将两端代入(1)，严格下端为
\[
 \frac{144883718717093990038447236655639983274406783850455}
 {215261827327800757567083368853099932747578493370368}.
\]
严格上端为
\[
 \frac{72441859358546995019223618327819991669906394854915}
 {107630913663900378783541684426549966373789246685184}.
\]
新下端减去478的旧上端精确为
\[
 \frac{38202658750375724709585783275561655495674769405}
 {223107690410244439578888423481057719096362234296731172864}>0. \tag{11}
\]
因此提升不依赖浮点最后位。以epsilon最大值核(9)，
\[
 \alpha-2(1+e)/10000=\frac{36561707377}{10160156250000}>0,
\quad \frac23(1/10-1/10000)^2-\alpha
 =\frac{232041622759}{81281250000000}>0.
\]

还可不展开巨整数地复算改进符号。令
\(u_0=1/S,c_0=2u_0-u_0^2,D_0=1-\tau c_0,h=1/500\)，
\(\Delta c=c-c_0=2u_0(1-u_0)e-u_0^2e^2\)。
新旧p之差的分子精确是
\[
 \Delta c(\tau C_0-h)-(C_0-hc_0)e^2, \tag{12}
\]
分母为两个正的计数分母之积。
冻结C0区间即可独立核其严格为正。本稿未宣称选定e全局最优。

## 5. 原[R7/8]的准确位置

这一步作用于原算子A内的同一简单列P；并未替换离线Q、HS输入或源character。
因此与现有原7/8条带相容，但比例推导并不需要该条带。
原 \(\kappa\) 是positive-slot解析条件
\(\beta_*\le(1+\kappa)/2\) 的参数；(1)是全零点简单比例。
它们不是同一个量，不能把p代入kappa。
条带对离线特征深度的限制也没有在本稿提供额外J或完整A谱尾的正下界。
如要从新比例改进无零边界，仍需对同一原探测器/有限算子支付新的联合算术桥。
本稿支付的是对角调节的实际极小比例余量，未重开旧失败subaction。
