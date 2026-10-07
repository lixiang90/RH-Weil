# 440. 主信号 Euler 校正向 2/3 的解析扩域

2026-10-07。外部算术恒等式为 [R]；由它导出的局部简化、正常收敛和非消失扩域为 [T/R]。
这是改变 7/8 探测器几何的一项实际准备，不是新的 L 函数无零定理。

## 1. 固定来源和要支付的接口

只读来源为 OpenAI/math 的提交
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`，
[September-30 paper.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)。
原文 `lem:local-euler`、`eq:local-parameters`、`old-eq:5.13a`、
`eq:local-H-definition` 与 `eq:local-H-defect` 给完整局部因子；
`eq:shared-principal-data` 定义

\[
 H_\eta(s)=\mathcal H_{\eta,1}(s,1,1/6).
\]

原文只在 Re s>7/8 声明这个信号校正正常收敛并接近 1。
这里直接保留完整局部恒等式，证明更大的解析域。
有限阶目标角色及固定算术相位都仍为单位模，原排除集 S 和非单位处的零延拓不变。
没有用 RH、7/8 无零定理或者待证明的新边界来推收敛。

## 2. 主行的准确闭式

固定 p 不在 S，令 Q=Np，取物理主行 u=1，因此 j=0、rho=1。
在 w=1、z=1/6 处记

\[
 v=Q^{-1},\quad D=\eta(p)Q^{-s},\quad
 r=a_p^2Q^{3-6s},\qquad |a_p|=1.
 \tag{1}
\]

这时原 V=W=W_loc=v。原 j=0 的完整公式准确给

\[
 P_p^*=\frac{(1+v)(r-D)}{1-r},\qquad
 P_p=\frac{1+v}{1-v}+P_p^*.
 \tag{2}
\]

例如原分子中的负项除以 1−V 后是
−D(Q−1)v²/(1−v)=−Dv；与 J_0=−D+vr 合并才得到 (2)。
不先删除高次项，也不把零延拓改成别的角色。
代入 H_p=P_p(1−V)(1−W)/(1−D)，得

\[
 \boxed{\quad
 H_p(s,1,1/6)=\frac{1-v^2}{1-r}
       \left(1+\frac{v(D-r)}{1-D}\right).
 \quad} \tag{3}
\]

这个恒等式对任意单位模目标相位成立，不要求目标为平凡角色。

## 3. 正常收敛和统一非消失

固定 sigma_0>2/3。在 Re s>=sigma_0 上，
|r|<=2^{3−6sigma_0}<1、|D|<=2^{−sigma_0}<1，故两个分母都一致离零。
由 (3) 得

\[
 H_p-1\ll_{\sigma_0}
 Q^{3-6\Re s}+Q^{-1-\Re s}+Q^{-2}
 \ll_{\sigma_0}Q^{-1-c},\qquad
 c=\min\{6\sigma_0-4,\sigma_0,1\}>0.
 \tag{4}
\]

整数理想计数 O_F(x) 给 sum_{Np>P_0}(Np)^{−1−c}=O_F,c(P_0^{−c})。
因此乘积在 Re s>2/3 正常收敛，定义全纯函数；估计对虚部和目标的单位相位一致。
把所有 Np<=P_0 的素数加入固定 S 后，

\[
 \sup_{\Re s\ge\sigma_0}|H_\eta(s)-1|
   \le \exp(C_{\sigma_0}P_0^{-c})-1\le1/2
 \tag{5}
\]

可由足够大的 P_0 保证。P_0 在选目标之前确定；目标导子的其他素数仍可随后进入 S。
删去更多因子只缩小同一个乘积误差上界。
原文的系数级校准允许这样的固定排除集扩大，ray group T 不变 [R]。
所以对每个固定 sigma_0>2/3，校正在整个闭半平面非消失，且 |H_eta|>=1/2。
这里没有给 sigma_0 向 2/3 逼近时的统一常数，也没有包括 Re s=2/3。

## 4. 主留数周围的矩形也能向左扩

原主行轮廓还使用 w_r>=19/20、z_r>=33/200。
固定 x_r>=sigma_0>401/600。原准确 defect 恒等式为

\[
 H_p-1=\frac{D(V+W-VW)-VW+(1-V)(1-W)\mathcal E_p}{1-D},
 \quad \mathcal E_p=P_p^*+D.
 \tag{6}
\]

对 p 不整除 u，原 j=0 公式直接给

\[
 |\mathcal E_p|\ll
 Q^{4-6x_r-6z_r}+Q^{1-x_r-w_r-6z_r}.
\]

|1−V|、|1−W| 一致有界；另外 DW、DV 和 VW 都是可和项。
因此

\[
 H_p-1\ll Q^{-1-c_{\rm box}},\quad
 c_{\rm box}=\min\{6\sigma_0-401/100,\sigma_0-3/50,47/50\}>0.
 \tag{7}
\]

这里最紧项是 Q^{301/100−6sigma_0}。
分母 1−R、1−V、1−D 一致离零；这也证明一个邻域内全纯，
不是仅在实轮廓上作形式求和。

对 p 整除 u，必须保留 D=W=0，此时 (6) 为 (1−V)P_p^*。
逐个检查原 j=1,...,5 表格，最紧的未完成项为
Q^{1−x_r−w_r} 与 Q^{3/2−3x_r}，其余项不更大。因此

\[
 H_p-1\ll Q^{-c_{\rm ram}},\quad
 c_{\rm ram}=\min\{\sigma_0-1/20,3\sigma_0-3/2\}>0.
 \tag{8}
\]

ramified 因子只有有限多个；对任意 epsilon>0，充分大的 Q 满足
1+C Q^{−c_ram}<=Q^epsilon，有限小 Q 的乘积并入常数。
故完整校正满足 H_{eta,u}<<epsilon (Nu)^epsilon，常数依赖固定 sigma_0、epsilon，
对全部虚部、单位相位及六次方自由行 u 一致。
式 (7) 仍支付 good-prime 无限乘积。

## 5. 对混合研究的实际含义

[439](439-prime-slot-geometry-and-a-conditional-strip-improvement.md)的候选边界
sigma_new=7/8−1/80000 远大于 401/600；所以主校正的解析与非消失不是该候选的循环障碍。
这项本地扩域已经由准确原因子支付，无需改动 math 仓库或调用它的 Lean 编译。

仍须在同一个实际补偿探测器中证明可变几何 low bound、全部 high 行及递归 detector capacity，
并重新支付共享轮廓的完整误差与统一量词。正常收敛的 H 不能把 1/L 的极点消掉；
也不能用 H 的解析域冒称 L 在 Re s>2/3 无零。
本稿证明的是主信号校正的扩域，完整新零区仍为 [O]。

独立审查和精确代数模型见本轮 reviews 与
`scripts/hybrid_strip_endpoint_exact_audit.py`；有限检查不替代上述无限乘积证明。
