# 346. 非零Poisson频率的现有总成本与固定频带几何

2026-09-08。周期9第5动作。[T]。
Gibbs只读[独立复核通过](../reviews/2026-09-08/346-independent-review.md)，
采用符号分支量词及上界不能排除其他改进的两处修订。
采用345的固定taper、R=ceil(X³)、实际外层与g_delta，
只评估目前能够证明的逐频率绝对上界，并写清固定xi时的驻点区间。
该上界不能达到目标，不等于实际余项有对应下界，也不排除更精细的算术估计。

## 1. 每个外层的低频与大频率界

记m=rv、lambda=Xm/Y、A_*=Y^-1/2。
在非空shell上w~w0~Y/m，345的函数满足
\[
 \int|g_\delta(w)|dw\ll {A_*\over\lambda}
          \int_{-M}^M|H(t)|dt\ll {A_*L\over\lambda}.               \tag{1}
\]
故|k|<=8lambda的全部整数频率之和满足
\[
 \sum_{0<|k|\le8\lambda}|\widehat g_\delta(k)|\ll A_*L.           \tag{2}
\]
这里lambda趋于无穷（m>=v>V），整数+1也可吸收。
该范围包括没有驻点的部分；没有将它们免费删去。

对|k|>8lambda，将H中的两个符号频带分别写成343的I_sigma形式，
其幅度改为
\[
 B(w)=(mw)^{-1/2}W(w)\chi_\delta(X\log(w/w_0))
                  {\bf1}_{[A/m,B/m]}(w).
\]
这里B(w)中的B/m表示原cell上端；函数B与整数端点常数不要混淆。
幅度的sup及总变差均O(A_*)：chi_delta只有两次单调过渡，
TV为2，不在一阶变差中支付1/delta；W与平方根权有固定数量的光滑片。
硬cell跳跃仍计入总变差。

在支撑上，|sigma xi X/w|<=2Xm/A<3lambda，
所以相位导数与0距离至少|k|-3lambda>|k|/2。
其二阶导数绝对积分O(lambda)，分段分部积分给
\[
 |I_{\sigma,\delta}(k,\xi)|
 \ll {A_*\over |k|}+{A_*\lambda\over k^2}
 \ll {A_*\over |k|},                                             \tag{3}
\]
对1<=xi<=2一致。中心项乘bar K_infty=O(1/M)，其普通Fourier积分同样
由幅度BV给O(A_*/|k|)，故
\[
 |\widehat g_\delta(k)|\ll A_*/|k|\quad(|k|>8\lambda).
\]
这只在远离驻点区间的大频率范围使用，不滥用“无驻点”这一名称。
积分不受未展开的Lambda权影响，因为它们只在固定外层。

由log R=O(L)，(2)(3)合计
\[
 \boxed{\sum_{0<|k|\le R}|\widehat g_\delta(k)|
                      \ll Y^{-1/2}L.}                          \tag{4}
\]
没有主张无穷绝对尾有限，345的对称尾账本仍独立保留。

## 2. 全部外层成本

另三Lambda平方根权质量为O(Y^(3/2))，而
\[
 \sum_{\substack{r\ge1,v>V\\rv\le B}}|\mu(r)|\Lambda(v)
 \ll \sum_{r\le B/V}{B\over r}\ll YL.
\]
所以目前逐频率、逐外层取绝对值的这项完整预算为
\[
 \boxed{\sum_{\rm outer}|c_{\rm outer}|
                 \sum_{0<|k|\le R}|\widehat g_\delta(k)|
                    \ll Y^2L^2=X^{3/2}L^2.}                    \tag{5}
\]
Type I或Type II只取外层子集也有此界；这不是说两通道实际大小相同。
若仅考虑m<=Z<=B，Z>=V，完全相同的账本给
\[
 \text{此部分的现有绝对预算}\ll YZL^2.                          \tag{6}
\]
因此即便限于341可能有长自由纤维的小m角落，
仅这些逐频率界也不能推出该角落对o(L⁴)可忽略，更不能消去其他通道。
这里判断的是明确上界不能给所需结论，不是证明实际绝对和必然大、
所有绝对值方法都失败或剩余有符号响应非小量。

## 3. 固定xi与整个xi积分的频率范围必须区分

343的|k|~lambda是xi遍历[1,2]之后的联合可能范围。
当xi固定，k的驻点区间实际上为
\[
 \sigma k>0,\qquad {\xi X\over u_+}\le |k|\le{\xi X\over u_-},
\]
其长度至多
\[
 \xi X(1/u_--1/u_+)\ll{\lambda M\over X}
                         ={m\over X^{1/4}}.                    \tag{7}
\]
完整shell时此长度可与右侧比较；被cell截断后只有上界。
因此m=o(X^(1/4))时，每个固定(sigma,xi)分支的驻点整数k至多一个，
两符号合计可有一对k,-k。
但随xi移动它会扫描O(lambda)个频率，不能把整个xi积分也换成一个k。
反之Type II固定原自由变量纤维可短于1，却不排除固定xi的双频区间较长。
这没有自动生成具有特定素模数的完整Kloosterman核。

此外，原shell在w中的长约w0/sqrt X，恰与二阶相位的驻点尺度同阶，
不支持不计端点的整条Gaussian主项替换。
以w=w0(1+u/sqrt X)、|u|<=1+O(X^-1/2)为例，准确地
\[
 \sigma\xi X\log(w/w_0)-kw
 =-kw_0+\sqrt X(\sigma\xi-kw_0/X)u
                    -{\sigma\xi\over2}u^2+O(X^{-1/2}).          \tag{8}
\]
余项对xi∈[1,2]一致；-kw项在u里本来就是精确线性。
二次项在整个归一化区间保持O(1)，没有趋于无穷的高斯局部化参数。
可进一步分析带真实端点的有限Fresnel积分，但单个积分中的小Taylor余项
仍须支付全部k与外层系数的总成本，不能直接宣布最终o(L⁴)。

## 4. 对当前路线的含义

341–345给出合法的自由变量变换、零频／点修正及有效尾接口。
本篇没有从它们推出新的非零频率算术相消：
现成逐项预算(5)仍远大于所需量级，固定xi短驻点区间也不能消掉xi积分。
若保留这一变换，k与r,v,b,c,d或xi间的共同相消是一条待验证方向；
上述预算不排除其他可证明的改进。若使用参数分离与分块，须计入相应成本。
另写未证的小相关预算不构成新输入。
这一有限成本审计不是GOAL第十节C的广泛机制边界成果。
