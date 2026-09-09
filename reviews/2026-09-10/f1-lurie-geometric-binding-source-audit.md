# Lurie 8／19：period ring 到实际几何的来源边界

2026-09-10。只读子代理Singer完整核读两份已归档原件；未重新审查372的级数。
这是内部来源审查，不是对全部Fargues–Fontaine理论的独立认证。

## Lecture 19

[原件](../../literature/f1/lurie-2018-lecture19.pdf)，SHA256
`569edb08218447296501a97f03b69a2bd4115e6a20e89f114700de0185831ee7`。

PDF第1页开篇固定**代数闭**特征p perfectoid域F=C^flat。此假设覆盖全讲。
Construction1、Remark2先构造O(m)及规范映射
B^(φ=p^m)→H^0(X,O(m))，X=Proj(⊕B^(φ=p^n))。
PDF第2页Theorem5(a)才证明该映射对所有整数m是同构。
Theorem3、Lemma4、Theorem5及Corollary6给Pic≅Z、每个闭点度一、
H^0(O)=Q_p、H^1(O)=0及相应高阶上同调消失。
证明具体使用权一因子分解与Lecture10的logarithm求值满射。

372所用F的值群为H_p，因而不是代数闭的：若素数ℓ≠p，u^(1/ℓ)
会要求值1/ℓ∈H_p。不能直接搬用本讲上述定理，也不能据此断言一般F下定理必然失败。
没有从这些结论得到通常代数曲线的有限维公式h^0(O(n))=n+1。

## Lecture 8

[原件](../../literature/f1/lurie-2018-lecture08.pdf)，SHA256
`82b19edd39cdb4356ea83a4ef5c1122563d0a5427c33b613bc8e759764c48eda`。

开篇只要求一般特征p perfectoid F，使用全族Gauss范数完成B。
PDF第1–2页Proposition2、Corollaries3–4参数化的是带
Q_p^cyc→K嵌入的untilt；商Z_p^×和Q_p^×分别处理嵌入及Frobenius轨道。
PDF第3页Remark7才追加代数闭假设，以穷尽全部untilt的相关轨道。
第3–5页Construction8、Propositions11、14为任一特征零untilt构造
完备DVR B_dR^+(y)及从适当环域的映射。此讲尚未完成logarithm零点简单性。
局部DVR的整数阶数与v_F的值群H_p是不同数据。

## 不需代数闭即可完成的一个几何接口

设P为正分次整环，s,t∈P_n，n>0，t≠0。直接由Proj定义，

    s/t ∈ (P[t^-1])_0 = Γ(D_+(t),O_Proj(P)) ⊂ K(Proj(P))。

(0)为齐次素理想且不包含P_+，所以Proj(P)非空且为积分概形。
该比值已是实际开集上的正则函数及实际有理函数；不需要先证明
P_n=H^0(O(n))或O(n)可逆。P嵌入B，局部化与分式域的比较是单射。
同权本身不保证非常数或主除子非零，372使用轮廓另作证明。

这一步不自动给adic模型的亚纯层、闭点重数、全局Weil除子或RR。
尤其不能把权零分式误写成B中的不变全纯元素。

下一来源任务：一般非代数闭F的正则性、线丛、截面和闭点定理；
若经代数闭包证明，须处理值群扩成Q后的下降。
FF除子到C_p的映射及固定ζ接口均不是上述两讲的现成结论。
