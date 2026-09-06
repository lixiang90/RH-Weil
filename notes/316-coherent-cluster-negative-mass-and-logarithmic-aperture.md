# 316. 保留簇内全部负项：可见性只需高度直径o(1/log T)

2026-09-06。VIS-REG第7轮；为突破315的簇宽限制而延长一个数学轮次（GOAL上限8轮）。
状态：[T/R] 明确几何前提下的完整压缩负迹与簇质量估计，已通过[独立内部复核](../reviews/2026-09-06/316-coherent-cluster-review.md)；[C/O] 实际簇选择。
本篇不把簇内其他负列删除：它们提供与正泄漏同尺度的集体负响应。
不作RH、零点比例或世界优先权声明。

## 1. 固定对象与要削减的输入

沿用315的实际深点集合、簇C及外部分离D=T^θ，固定
\[
 0<s<d_0<1/2,\qquad
 k=\max\{s,1/4+\Phi_s(\theta)/2\}<d_0.
\]
簇内所有深度e>s，有一个选定目标z=x+id满足d≥d0；不再要求它是簇内最深点。
簇的高度直径≤rT，簇与所有其他深度>s的点相距至少D。
本篇仅要求
\[
 c_T=A r_T\longrightarrow0,\qquad A=\tfrac12\log T.
 \tag{1}
\]
即rT=o(1/log T)。其余浅非实点和临界线点均允许存在，全部重数保留。

定义簇的负列总质量
\[
 W_C=\sum_{w\in C}2m_wH_w,\qquad H_w=\|h_w\|^2,
 \quad G_w=\|g_w\|^2=1+H_w.
 \tag{2}
\]
WC不是原A的负谱迹；它由节点、窗与原始权重直接计算，也可用正列范数G_w−1计算。
因e>s固定，有H_w→∞一致，故大T时G_w≤2H_w。
目标存在给WC≥2mH_z≥cT^d0/L，L=log T。

## 2. 深度在固定正区间时的统一相关下界

对a,b∈[s,1/2)，记相同中心、无高度相位的形状积分
\[
 J_{a,b}=\int\eta_A^2(u)\sinh(au)\sinh(bu)\,du.
\]
取A≥1+1/s，在u∈[A−1,A]上使用正的MT密度下界及sinh(t)≥c exp(t)，
且a+b≤1，得到Jab≥c exp(A(a+b))/A。
另一方面直接积分给H_a≤C_s exp(2aA)/A，H_b同样成立，因此
\[
 J_{a,b}\ge q_s\sqrt{H_aH_b},\qquad q_s>0. \tag{3}
\]
q_s与A、点数和所选a,b无关。不使用固定深度渐近替换一致估计。
将sinh同时换成cosh，同样得到
\[
 \int\eta_A^2\cosh(au)\cosh(bu)\,du
 \ge q'_s\sqrt{G_aG_b},\qquad q'_s>0. \tag{4}
\]

簇内任意点与目标的高度差Δ满足|Δu|≤cT。
当cT≤1时，cos(Δu)≥cos1>0。由偶性，hh和gg内积只留下cos相位，故
\[
 |\langle h_w,h_z\rangle|^2\ge a_s H_wH_z,\qquad
 |\langle g_w,g_z\rangle|^2\ge b_s G_wG_z, \tag{5}
\]
其中a_s,b_s>0固定，可取(cos1)²q_s²和(cos1)²(q'_s)²。
两个不同目标的行向量不需要彼此正交；本篇只使用一个测试方向。

## 3. 同一簇的正泄漏为相位小量，负响应保持总质量

令PC=Σ_{w∈C}2mw gw⊗gw、UC为全部簇内sqrt(2mw)hw列，h=h_z、H=H_z。
由(5)，
\[
 {\langle U_CU_C^*h,h\rangle\over H}\ge a_s W_C. \tag{6}
\]
相反，gh实型内积含sin(Δu)。用|sin(Δu)|≤cT及Cauchy–Schwarz，
\[
 |\langle g_w,h\rangle|\le c_T\sqrt{G_wH}.
\]
因此
\[
 \alpha_C={\langle P_Ch,h\rangle\over H}\le2c_T^2W_C,
 \qquad \|P_C\|\le\operatorname{tr}P_C\le2W_C.
\]
由PC²≤||PC||PC，
\[
 \boxed{\beta_C={\|P_Ch\|\over\sqrt H}\le2c_TW_C.} \tag{7}
\]
这里不以WC中的每列质量直接冒充负迹；(6)经统一相关下界才给单个测试方向的负响应。
同高度时cT可以取0，所有gh内积为0，式(7)仍成立。

此外，以g_z为测试方向，(5)给
\[
 \|P\|\ge\|P_C\|\ge b_s\sum_{w\in C}2m_wG_w\ge b_sW_C. \tag{8}
\]
这是对整个正背景的下界，不把迹等于范数。

## 4. 全部正负列与显式日程

把全部P分成PR+Ps+Pf+PC：临界线、深度≤s、簇外深点和簇内深点。
所有簇外深点距目标至少D，因此314的实际尾界适用。
其余负列仍属于A_T，在下界中可合法舍去。

记αo=〈(Ps+Pf)h,h〉/H、βo=||(Ps+Pf)h||/sqrt H。
314给
\[
 \alpha_o\ll LT^s+L^3T^{\Phi_s(\theta)},\qquad
 \beta_o\ll LT^s+L^2T^{1/4+\Phi_s(\theta)/2}.
\]
因WC≥cT^d0/L且k<d0，αo/WC→0、CL/WC→0。
完整算子的同一方向满足
\[
 -\langle A_Th,h\rangle/H
 \ge(a_s-2c_T^2)W_C-CL-\alpha_o. \tag{9}
\]
选定
\[
 \boxed{\lambda_T=L^3T^k+\sqrt{c_T}\,W_C.} \tag{10}
\]
不要求从A的负谱读出λ；第二项由有限簇的原始列范数计算。
当cT>0时，βC/λ≤2sqrt(cT)；当cT=0时βC=0，单独处理，不除以0。
又有(CL+βo)/λ=O(1/L)，所以
\[
 1\le\|R^{-1}h\|/\|h\|
 \le1+O(L^{-1}+\sqrt{c_T})=1+o(1).
\]
令v=R^−1h，将完整(9)除以||v||²/H，得到
\[
 \boxed{\operatorname{tr}(R_{T,\lambda_T}A_TR_{T,\lambda_T})_-
        \ge(a_s-o(1))W_C.} \tag{11}
\]
误差常数只依赖固定s、d0、θ和计数常数；o(1)沿指定cT→0日程成立。
例如可用O(sqrt(cT)+L^−1+L²T^(s−d0)+L⁴T^(Φs(θ)−d0)+L²T^−d0)控制相对误差。

最后，由(8)，
\[
 \lambda_T/\|P\|\ll L^4T^{k-d_0}+\sqrt{c_T}\to0. \tag{12}
\]
全局逆范数转移乘数发散，而单方向逆变换代价趋1；保持的是(11)所列簇质量下界，
不声称全部负谱比例趋1，也不把不同簇的(11)直接相加。

## 5. 与315的严格比较及待审边界

仍可取d0=2/5、s=7/20、θ=1/5、k=51/140。
315为兼顾λ/||P||→0要求L³rT→0，并展示rT=L^−4；本篇只需LrT→0。
例如rT=1/(L log L)满足本篇条件，却不满足315所列充分宽度条件。
新日程包含sqrt(cT)WC，以集体负响应吸收正泄漏；该预算与315没有统一大小次序，且λ仍为o(||P||)。
不能声称在更宽簇下维持315单目标的同一λ，也不能把a_s换成1而无新证明。

改进来自保留簇内全部负项及其统一相关下界，而非再造一个计数模型。
这是真实有限算子上、由明确几何条件推出的结果；实际满足该簇条件的目标选择仍开放。
原始输入的使用范围、近远拼接、WC归一化及全部适用量词已通过独立审查；新旧预算比较已按异议修正。
下一有限问题应检查多个彼此分离簇的集体测试Gram和效应范数，
不能用单簇下界直接求和来宣称新的零点密度或RH结论。

## 6. 原始依赖及比较范围

实际计数来源为已归档Bellotti–Wong v2与Chourasiya–Simonič v2，核读范围见314–315审查报告。
本篇不新增零密度定理，只使用314的移动中心正背景尾界。
Lamzouri v1的§2和Lemma3.2证明提供相关有限自伴接口及MT密度背景；
本篇不对sharp窗套用其平滑全谱二阶渐近式。
Tikhonov原文的最小化机制、Birman负谱阈值、Douglas算子支配是前期310–311的经典比较对象，
没有被本篇改写为新的全局正性输入。

独立审查认为本篇超出197§5／312§4抽象条件的重写：由簇几何证明一致相关、以WC计量集体响应并闭合新日程。
这仍是经典框架内的条件性定量实例；既不证明实际簇存在，也不建立组合的世界优先权。
