# 432. 真实相对循环电荷与源不变截止的读出差异

2026-10-04。使用[430](430-f1-source-stable-periodic-smoothing-algebra.md)、
[431](431-f1-source-orbit-essential-symbol-and-boundary-injectivity.md)的实际源域及其有限词商。
本稿给不依赖自由有限部选择的Hochschild一循环电荷，并计算一个对真正u不变的实际截止。
后者仍不能选择原球截止的周期读出，所以源准入及源相容性尚不足以完成算术比较。

## 1. 普通迹的规范相对一循环电荷

取原Hilbert表示中的实际有界星代数
\[
 A_{\rm src}=\operatorname{alg}(1,u,u^*,D_{\rm src}),\qquad
 Q_{\rm src}=A_{\rm src}/\mathcal S_1.                      \tag{1}
\]
430的双侧稳定性使D_src是A_src的双侧理想；S₁仍是双侧理想。
不要求纯u或单位落在D_src，也不假定它们的任何截止压缩迹类。
记商映射q。对代数一链c=sum_r a_r tensor b_r，采用
\[
 b_1c=\sum_r(a_rb_r-b_ra_r).                               \tag{2}
\]
若c是Q_src上的一循环，即b_1c=0，选其原有界提升A_r、B_r，则
\[
 T_c=\sum_r[A_r,B_r]\in\mathcal S_1,
 \qquad \Omega(c)=\operatorname{Tr}T_c.                    \tag{3}
\]
这里单个[A_r,B_r]不必迹类；准入由全部和的商边界零保证。
用S₁改变提升，差的每项为有界算子与迹类算子的交换子，普通迹零。
更一般，q tensor q的核为S₁ tensor A_src加A_src tensor S₁，
这些核张量的b_1迹也为零。因此(3)与提升及链的张量分解无关，是规范线性数据。

对任意二链，选择实际提升并用
\[
 b_2(A\otimes B\otimes C)
       =AB\otimes C-A\otimes BC+CA\otimes B,
\]
\[
 [AB,C]-[A,BC]+[CA,B]=0,                                 \tag{4}
\]
得到Omega(b_2d)=0。所以
\[
             \Omega:HH_1(Q_{\rm src})\longrightarrow\mathbb C
                                                                    \tag{5}
\]
是实际普通迹导出的相对一循环电荷。对称一链a tensor b+b tensor a的电荷为零，
源内共轭亦保留电荷，因为Tr(u T_c u*)=Tr(T_c)。
这些身份已支付，不把它们单独冒称完整周期循环Chern角色或几何主关系。

旧角点的q(A(h)) tensor q(A(k))是一循环，427的迹公式给
\[
 \Omega(q(A(h))\otimes q(A(k)))
       =-4\int s h(s)k(-s)ds.                              \tag{6}
\]
因此本电荷确实携带旧omega；它不是把期望原子塞进标量有限部的自由扩张。
也没有给任意非闭一链定义同样的电荷。

## 2. 真源加权式仍不是商上一循环

对F in D_src，真实加权一链的边界为
\[
 b_1(q(u^*)\otimes q(uF))=q(F-uFu^*).                      \tag{7}
\]
431给F不在S₁时右边非零、其实际提升非紧。所以此链不能直接送入(3)。
有限个原共轭加权式也不能互相修补为S₁：对有限族h_m，
\[
 \sum_m u^m\{A(h_m)-uA(h_m)u^*\}u^{-m}\in\mathbb K
                          \Longrightarrow h_m=0\text{全部}. \tag{8}
\]
差分矩阵或实际深p行都能核准此式。完整有限行推导见
[相对数据报告](../reviews/2026-10-04/f1-source-relative-cocycle-derivation.md)。
仍允许含其他新边的修补、其他相对理想或具有单独收敛证明的无限转移；(8)只收束有限轨道修补。

## 3. 原不变坐标给真正源保持的截止

沿用430的完整w基标签和忠实坐标G。定义原Hilbert空间上的正交投影
\[
 \mathsf P_R=G^*M_{\mathbf1_{(-\infty,R]}}G.                 \tag{9}
\]
源箭头保持x，故[P_R,u]=0；R趋于正无穷时P_R强趋于单位。
它不是有限秩投影，但对每个F in D_src有
\[
                       P_R F P_R\in\mathcal S_1.         \tag{10}
\]
证明只需F_(i,j)(B)：V在x<a为零；在紧x区间[a,R]上，u(x)^i z(x)及
u(x)^j z(x)只有共同有限的径向坐标，其系数光滑。
选光滑chi覆盖[a,R]，将B核夹于chi后得到有限矩阵的光滑紧支核，确为迹类；
再左右乘(9)的有界示性函数得到(10)。S₁余项当然保持迹类。
这不把纯u、单位或任意A_src元素列入(10)。

普通迹由实际核给
\[
 \operatorname{Tr}(P_R F_{i,j}(B)P_R)
       =\int_a^R g_{i-j}(x)K_B(x,x)dx.                    \tag{11}
\]
该式包含所有源混合行，不只p、q轴的独立迹。
由于P_R与u交换及(10)，每个R都准确有
\[
       \operatorname{Tr}\{P_R(F-uFu^*)P_R\}=0.             \tag{12}
\]
431的非紧边界与(12)相容：这里没有迹范数收敛，不能由有限截止迹零推出商边界为零，
更不能据此给非闭链(7)指派Omega。

## 4. 源不变截止仍未选择原物理周期

对原A(h)=VU(h)V*，(11)直接成为
\[
                   \operatorname{Tr}(P_R A(h)P_R)
                         =h(0)\int_a^R m(x)dx.            \tag{13}
\]
m在充分右端为2，所以大R时仅有线性单位项与固定常数乘h(0)。
特别，对支集隔离在非零原周期-L附近、h(-L)=1的合法测试，h(0)=0，
(13)对每个R恒零；而425–428的原球截止读出为
\[
                         \Lambda(h)=L\rho_p\ne0.          \tag{14}
\]
可以取足够小支集避开其他p、q周期，因为L/M无理。
因此即使在已支付真源准入的域中，实际强趋单位、对u精确不变且各压缩迹类的截止，
仍不能由这些条件自动恢复原物理周期。这里比较两个实际来源，而非给新读出预设原子。

对一般B，(11)的被积式在充分右端是周期函数，扣掉平均线性项后仍可能周期振荡；
没有自动定义对全部D_src的R趋无穷有限部或断言其存在。
已有结论是每个R的真实准入、源相容性以及原A测试的明确不匹配。

## 5. 下一相对比较必须支付的内容

当前已有实际源域、有限商范数、非紧边界及规范HH₁电荷，
但原加权链尚不闭，源不变截止也尚未选择球截止的周期数据。
后续应明确更大的相对理想／链，把两种截止的实际传递与新边耦合一起计算，
并证明原Lambda的规范选择，不能只增加“源循环”公理或重用(12)。
本稿不证明完整相对Chern比较、算术主关系、Weil正性、实位／全素数比较、RR或RH。
